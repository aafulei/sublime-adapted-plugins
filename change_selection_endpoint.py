# ===== Change Selection Endpoint =============================================
# Adapted from a post on Sublime Forum by Terence Martin (OdatNurd)
# https://forum.sublimetext.com/t/move-caret-to-beginning-or-end-of-selection-without-losing-selection/29329/2
# =============================================================================

import sublime
import sublime_plugin


class ChangeSelectionEndpointCommand(sublime_plugin.TextCommand):
    """
    Change the selection endpoint.

    -----
    order
    -----
     0   swap                   e.g. SELECTION| ---> |SELECTION
     1   change to (begin, end) e.g. SELECTION|
    -1   change to (end, begin) e.g. |SELECTION
    """
    def run(self, edit, order=0):
        new_sel = []
        for x in self.view.sel():
            if order == 1:
                new_sel.append(sublime.Region(x.begin(), x.end()))
            elif order == -1:
                new_sel.append(sublime.Region(x.end(), x.begin()))
            else:
                new_sel.append(sublime.Region(x.b, x.a))
        self.view.sel().clear()
        self.view.sel().add_all(new_sel)
