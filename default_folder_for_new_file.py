# ===== Default Folder for New File ===========================================
# Adapted from a post on Sublime Forum and a gist by finscn
# https://forum.sublimetext.com/t/default-folder-to-save-new-files
# https://gist.github.com/finscn/8bc573bb3a970b1c214d
# =============================================================================

# standard
import os

# sublime
import sublime
import sublime_plugin


class DefaultFolderForNewFile(sublime_plugin.EventListener):
    """Set default folder to save a new file."""
    def on_new_async(self, view):
        try:
            # set new file's default folder same as that of last active file
            active_view = view.window().active_view()
            active_index = view.window().views().index(active_view)
            last_view = view.window().views()[active_index-1]
            file = last_view.file_name()
            dir_path = os.path.dirname(file)
            active_view.settings().set("default_dir", dir_path)
        except Exception as e:
            try:
                #  set new file's default folder the first opened folder
                view.settings().set("default_dir", view.window().folders()[0])
            except Exception as e:
                pass
