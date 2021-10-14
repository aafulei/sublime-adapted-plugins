# ===== Recenter ==============================================================
# Adapted from Recenter​Top​Bottom by Matt Burrows
# https://github.com/mburrows/RecenterTopBottom
# =============================================================================

import sublime
import sublime_plugin


def cycle(seq):
    while True:
        for elem in seq:
            yield elem


g_recenter_pos = ["top", "center"]
g_next_pos_gen = cycle(g_recenter_pos)


class RecenterResetter(sublime_plugin.EventListener):
    """Reset the next position to go to the first in the list.

    In theory, recenter is a per-view behavior. To keep things simple, we
    implement it with a global resetter.
    """
    def on_selection_modified_async(self, view):
        global g_next_pos_gen
        g_next_pos_gen = cycle(g_recenter_pos)


class RecenterCommand(sublime_plugin.TextCommand):
    def run(self, edit, margin=2):
        # margin should be > 0
        view = self.view
        pos = next(g_next_pos_gen)
        if pos == "center":
            view.run_command("show_at_center")
        else:
            # --- WRONG --------
            # if not view.sel():
            # ------------------
            # view.sel() evaluates to True even if there are no selections
            if len(view.sel()) == 0:
                return
            cursor_row = view.rowcol(view.sel()[0].begin())[0] + 1
            visual_reg = view.visible_region()
            if pos == "top":
                target_row = view.rowcol(visual_reg.begin())[0] + 1
            else:
                target_row = view.rowcol(visual_reg.end())[0] + 1
            # amount > 0 for scroll up, amount < 0 for scroll down
            amount = target_row - cursor_row
            if amount > 0:
                amount = max(amount - margin, 0)
            else:
                amount = min(amount + margin, 0)
            view.run_command("scroll_lines", {"amount": amount})
