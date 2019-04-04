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

Plug 'tpope/vim-sleuth'               " Makes sure tabs / spaces are consistent
Plug 'tpope/vim-fugitive'             " For Git
Plug 'chiel92/vim-autoformat'         " Autoformatter for several languages
Plug 'scrooloose/syntastic'           " Syntax checker. Displays errors
Plug 'christoomey/vim-tmux-navigator' " ctrl+hjkl tmux integration
Plug 'ctrlpvim/ctrlp.vim'             " Find files fast

" Eye candy
Plug 'crusoexia/vim-monokai'
Plug 'kaicataldo/material.vim'
Plug 'vim-airline/vim-airline'

" Syntax highlighting
Plug 'rust-lang/rust.vim'
Plug 'leafgarland/typescript-vim'

" Autocompletion
Plug 'autozimu/LanguageClient-neovim', {
    \ 'branch': 'next',
    \ 'do': 'bash install.sh',
    \ }
Plug 'junegunn/fzf'
Plug 'Shougo/deoplete.nvim'
Plug 'roxma/nvim-yarp' " needed for deoplete
Plug 'roxma/vim-hug-neovim-rpc' " needed for deoplete

" Stuff that i've used before and might use again
"Plug 'easymotion/vim-easymotion'
"Plug 'davidhalter/jedi-vim'

call plug#end()

" Custom parameters 
set hidden
set nocompatible
colorscheme material
syntax on
set termguicolors
set fillchars+=vert:│
set nobackup
"let g:tsuquyomi_completion_detail = 1
"autocmd FileType typescript nmap <buffer> <Leader>t : <C-u>echo tsuquyomi#hint()<CR>
set incsearch
let g:syntastic_python_checkers = ['pylint', 'mypy']
autocmd BufEnter * silent! lcd %:p:h " automatically change the current directory to the opened buffer
set nobackup       "no backup files
set nowritebackup  "only in case you don't want a backup file while editing
set noswapfile     "no swap files
set noundofile
set number
set relativenumber

" Plugin settings
let g:deoplete#enable_at_startup = 1
let g:LanguageClient_autoStart = 1
let g:LanguageClient_serverCommands = {
  \ 'typescript': [$LANGSERVER_TS, '--logfile', '/tmp/tsserver.log']
  \ }

nnoremap <silent> K :call LanguageClient#textDocument_hover()<CR>
nnoremap <silent> gd :call LanguageClient#textDocument_definition()<CR>
nnoremap <silent> <F2> :call LanguageClient#textDocument_rename()<CR>

