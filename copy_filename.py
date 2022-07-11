# ===== CopyFilename ==========================================================
# Adapted from a post on Sublime Forum
# =============================================================================

# standard
import os

# sublime
import sublime
import sublime_plugin


class CopyFilenameCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sublime.set_clipboard(os.path.basename(self.view.file_name()))
