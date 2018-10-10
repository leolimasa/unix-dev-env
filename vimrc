"  VIM Configuration file
"
"  Needs Plug: https://github.com/junegunn/vim-plug
"  Also needs to compile YouCompleteMe support after installing plugins by
"  running install.py in ~/.vim/pluggged/youcompleteme
"
"  Source it from ~/.vimrc by doing:
" 
"  so /path/to/git/vimrc
"
"

" When started as "evim", evim.vim will already have done these settings.
if v:progname =~? "evim"
  finish
endif

" Get the defaults that most users want.
source $VIMRUNTIME/defaults.vim

if has("vms")
  set nobackup		" do not keep a backup file, use versions instead
else
  set backup		" keep a backup file (restore to previous version)
  if has('persistent_undo')
    set undofile	" keep an undo file (undo changes after closing)
  endif
endif

if &t_Co > 2 || has("gui_running")
  " Switch on highlighting the last used search pattern.
  set hlsearch
endif

" Only do this part when compiled with support for autocommands.
if has("autocmd")

  " Put these in an autocmd group, so that we can delete them easily.
  augroup vimrcEx
  au!

  " For all text files set 'textwidth' to 78 characters.
  autocmd FileType text setlocal textwidth=78

  augroup END

else

  set autoindent		" always set autoindenting on

endif " has("autocmd")

" Add optional packages.
"
" The matchit plugin makes the % command work better, but it is not backwards
" compatible.
" The ! means the package won't be loaded right away but when plugins are
" loaded during initialization.
if has('syntax') && has('eval')
  packadd! matchit
endif


" Plugins
call plug#begin('~/.vim/plugged')

Plug 'leafgarland/typescript-vim'
Plug 'quramy/tsuquyomi'
Plug 'crusoexia/vim-monokai'
Plug 'tpope/vim-sleuth'
Plug 'easymotion/vim-easymotion'
Plug 'ctrlpvim/ctrlp.vim'
Plug 'valloric/youcompleteme'
Plug 'chiel92/vim-autoformat'
"Plug 'davidhalter/jedi-vim'
Plug 'tpope/vim-fugitive'
Plug 'scrooloose/syntastic'

call plug#end()

" Custom parameters 
set nocompatible
let g:tsuquyomi_completion_detail = 1
colorscheme monokai
syntax on
set termguicolors
set fillchars+=vert:│
set nobackup
set nonumber
autocmd FileType typescript nmap <buffer> <Leader>t : <C-u>echo tsuquyomi#hint()<CR>
set incsearch
let g:syntastic_python_checkers = ['pylint', 'mypy']
autocmd BufEnter * silent! lcd %:p:h " automatically change the current directory to the opened buffer
set nobackup       "no backup files
set nowritebackup  "only in case you don't want a backup file while editing
set noswapfile     "no swap files
