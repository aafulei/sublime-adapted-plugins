# ===== CopyFilename ==========================================================
# Adapted from a post on Sublime Forum by IGRACH
# https://forum.sublimetext.com/t/file-name-and-full-path-to-clipboard/4833/10
# =============================================================================

# standard
import os

# sublime
import sublime
import sublime_plugin


class CopyFilenameCommand(sublime_plugin.TextCommand):
    """Copy current filename to clipboard."""
    def run(self, edit):
        try:
            sublime.set_clipboard(os.path.basename(self.view.file_name()))
        except AttributeError:
            pass
