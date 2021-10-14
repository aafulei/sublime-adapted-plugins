# ===== Go to Last Edit =======================================================
# Adapted from GotoLastEditEnhanced by Leonid Shagabutdinov
# https://github.com/shagabutdinov/sublime-goto-last-edit-enhanced
# =============================================================================

import sublime
import sublime_plugin


VIEW_HISTORY_CAP = 5000


class ViewHistory():
    """A queue of continuous numbers (front, back] that record edit regions."""
    def __init__(self, cap):
        # dummy front
        self.front = 0
        self.back = 0
        self.index = 0
        self.cap = cap

    def push(self):
        self.back += 1
        self.index = self.back
        if self.back - self.front <= self.cap:
            # within capacity, nothing to pop
            return 0
        old = self.front
        self.front += 1
        return old


class ViewHistoryCenter():
    def __init__(self):
        self.views = {}

    def get(self, view):
        return self.views.setdefault(view.id(), ViewHistory(VIEW_HISTORY_CAP))


g_view_history_center = ViewHistoryCenter()


def same_regions(R, S):
    return len(R) == len(S) and all(R[i].a == S[i].a for i in range(len(R)))


class GotoLastEditCommand(sublime_plugin.TextCommand):
    def run(self, edit, reverse=False):
        view = self.view
        hist = g_view_history_center.get(view)
        if not reverse:
            if hist.index == hist.front + 1:
                # reach beginning of history
                return
            index_to_go = hist.index - 1
        else:
            if hist.index == hist.back:
                # reach end of history
                return
            index_to_go = hist.index + 1
        regions = view.get_regions("goto_last_edit_{}".format(index_to_go))
        if not regions:
            return
        view.sel().clear()
        view.sel().add_all(regions)
        view.show(regions[0])
        hist.index = index_to_go


class GotoLastEditUpdater(sublime_plugin.EventListener):
    def on_modified_async(self, view):
        hist = g_view_history_center.get(view)
        last_regions = view.get_regions("goto_last_edit_{}".format(hist.index))
        # sublime text seems to update regions with linear moves of cursors
        if same_regions(last_regions, view.sel()):
            return
        popped = hist.push()
        if popped:
            view.erase_regions("goto_last_edit_{}".format(popped))
        view.add_regions("goto_last_edit_{}".format(hist.index), view.sel())
