# Leo's UNIX Dev Environment

nvim + tmux + bash setup for my own personal needs. Supports, out of the box:

* typescript
* javascript
* rust
* python
* go
* html / css / less
* markdown
* tmux / nvim integration
* language server protocol
* code review helpers

Tested on OSX. Requires Python 3.7.

## Installation

```
git clone https://github.com/leolimasa/unix-dev-env 
unix-dev-env/install.sh
```

## Basic Usage

* Run a tmux session by doing `tmux`
* Run `tmux-newwindow [folder]` to open a new project at the folder

## Features

* Put desired features into `UDE_FEATURES` if you wish to limit what gets installed
  * Ex.: `UDE_FEATURES=python,rust install.sh`
* Put features that you want excluded into `UDE_EXCLUDE_FEATURES` if you want to install all but a few
  * Ex.: `UDE_EXCLUDE_FEATURES=go install.sh`
* See the `ude/features` folder for all available features. Each file is a feature name.

## Key Maps

### Navigation

| Key                | Action                                     |
|--------------------|--------------------------------------------|
| ctrl+b w           | Select tmux pane / project                 |
| ctrl+hjkl          | Move between windows                       |
| ctrl+b z           | Zoom in / out of a window                  |
| ctrl+b alt+[arrow] | Increase / decrease size of pane           |
| ctrl+b {           | Move pane left                             |
| ctr+b }            | Move pane right                            |
| ctrl+b &           | Close current project / window             |
| <space> b          | Open buffer                                |
| <space> p          | Open file in project                       |
| <space> P          | Open file from home dir                    |
| <space> o          | Open file explorer                         |
| <space> vp         | Open project file in a new vertical split  |
| <space> vP         | Open home dir file in a new vertical split |
| <space> vb         | Open buffer in a vertical split            |
| <space> vo         | Open file explorer in a vertical split     |


### Code

| Key         | Action                           |
|-------------|----------------------------------|
| gd          | Go to definition                 |
| gy          | Go to type definition            |
| gi          | Go to implementation             |
| gr          | References                       |
| K           | Show docs                        |
| <space> rn  | Rename                           |
| <space> fs  | Format selected                  |
| <space> a   | Code actions for cursor position |
| <space> qf  | Quick fix                        |
| <space> e   | Show errors / diagnostics        |
| <space> c   | Show commands                    |
| <space> yf  | Find symbol in file              |
| <space> yp) | Find symbol in project           |
| <space> sp  | Search all files in project      |
| :Format     | Formats entire buffer            |

### Markdown

| Key          | Action                             |
|--------------|------------------------------------|
| zR           | Opens all folds                    |
| zr           | Reduce fold level                  |
| zm           | Increase fold level                |
| zM           | Folds everything                   |
| gx           | Open URL under cursor              |
| :TableFormat | Formats the table under the cursor |
| :Toc         | Opens up the TOC for the markdown


## Binaries

All these commands will be installed in your path.

| Name           | Description                                                                                                            |
|----------------|------------------------------------------------------------------------------------------------------------------------|
| autonumber     | Adds numbers to indented text coming from STDIN. Useful for adding number bullet points to markdown through vim pipes. |
| gitdiff        | Checks out two git branches and creates a diff between them                                                            |
| history-find   | Fuzzy searches your command history                                                                                    |
| tmux-newwindow | Creates a new tmux tab for a folder. E.g: `tmux-newwindow some/project/dir`. Needs to be ran inside tmux               |
| filter.py      | Outputs everything from stdin to stdout. Useful for things like running psql through a pipe.


## Tips

* `tmux-newwindow` sets the env variable `PR` (project root) to the folder pass as the argument.
  * That allows you to use $PR to refer to the project root anywhere. Ex.: `nvim $PR/src/test.ts`

