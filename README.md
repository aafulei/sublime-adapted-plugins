# My Adapted Plugins for Sublime Text 3

Sublime Text 3 plugins that I adapt for own use.

1. [Change Selection Endpoint](#change-selection-endpoint) [`.py`](./change_selection_endpoint.py)
2. [Copy Filename](#copy-filename) [`.py`](./copy_filename.py)
3. [Default Folder for New File](#default-folder-for-new-file) [`.py`](./default_folder_for_new_file.py)
4. [Git Blame Status Bar](#git-blame-status-bar) [`.py`](./git_blame_status_bar.py)
5. [Goto Last Edit](#goto-last-edit) [`.py`](./goto_last_edit.py)
6. [Recenter](#recenter) [`.py`](./recenter.py)

## Install

### Command Palette

```
1. Package Control: Add Repository

    https://github.com/aafulei/sublime-adapted-plugins

2. Package Control: Install Package

    sublime-adapted-plugins
```

## Adapted Plugins

### Change Selection Endpoint

```
Adapted from a post on Sublime Forum by Terence Martin (OdatNurd)
https://forum.sublimetext.com/t/move-caret-to-beginning-or-end-of-selection-without-losing-selection/29329/2
```

Change beginning and ending points of selections.

#### Arguments

| `order`  | Action                   |
| -------- | ------------------------ |
|       0  | swap                     |
|       1  | change to `(begin, end)` |
|      -1  | change to `(end, begin)` |

#### Recommended Key Bindings

```json
{ "keys": ["alt+s"], "command": "change_selection_endpoint" },
```

### Copy Filename

```
Adapted from a post on Sublime Forum by IGRACH
https://forum.sublimetext.com/t/file-name-and-full-path-to-clipboard/4833/10
```

Copy current filename to clipboard.

#### Recommended Key Bindings

```json
{ "keys": ["primary+k", "primary+i", "primary+n"], "command": "copy_filename" },
```

By the way, there is a built-in Sublime Text command to copy the file path to the clipboard.

```json
{ "keys": ["primary+k", "primary+i", "primary+p"], "command": "copy_path" },
```

### Default Folder for New File

```
Adapted from a post on Sublime Forum and a gist by finscn
https://forum.sublimetext.com/t/default-folder-to-save-new-files
https://gist.github.com/finscn/8bc573bb3a970b1c214d
```

Set default folder to save a new file. Try

1. the same as that of last active file
2. the first opened folder

### Git Blame Status Bar

```
Adapted from a gist by Rodrigo Berm??dez Schettino
https://gist.github.com/rodrigobdz/dbcdcaac6c5af7276c63ec920ba894b0
```

![](img/git-blame-status-bar.png)

### Goto Last Edit

```
Adapted from GotoLastEditEnhanced by Leonid Shagabutdinov
https://github.com/shagabutdinov/sublime-goto-last-edit-enhanced
```

Jump back to previous edits.

#### Recommended Key Bindings

```json
{ "keys": ["alt+u"], "command": "goto_last_edit" },
{ "keys": ["alt+o"], "command": "goto_last_edit", "args": { "reverse": true } },
```

### Recenter

```
Adapted from Recenter???Top???Bottom by Matt Burrows
https://github.com/mburrows/RecenterTopBottom
```

Alternate between `Show at Top` and `Show at Center`.

#### Recommended Key Bindings

```json
{ "keys": ["primary+k", "primary+k"], "command": "recenter" },
```

## License

Major credits go to the original authors. `Goto Last Edit` is under MIT. All my
adaptations are under MIT.
