# ===== Change Selection Endpoint =============================================
# Adapted from a post on Sublime Forum and a gist by Terence Martin (OdatNurd)
# https://forum.sublimetext.com/t/move-caret-to-beginning-or-end-of-selection-without-losing-selection/29329/2
# =============================================================================

import sublime
import sublime_plugin


class ChangeSelectionEndpointCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        new_sel = []
        for x in self.view.sel():
            new_sel.append(sublime.Region(x.b, x.a))
        self.view.sel().clear()
        self.view.sel().add_all(new_sel)
