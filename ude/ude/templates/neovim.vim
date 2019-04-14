call plug#begin()
Plug 'christoomey/vim-tmux-navigator' " ctrl+hjkl tmux integration
Plug 'neoclide/coc.nvim', {'do': { -> coc#util#install()}} " LSP support

" Eye candy
Plug 'crusoexia/vim-monokai'
Plug 'kaicataldo/material.vim'
Plug 'vim-airline/vim-airline'

{% if "fzf" in enabled_features %}Plug 'junegunn/fzf'
Plug 'junegunn/fzf.vim'
{% endif %}
call plug#end()

colorscheme material
set termguicolors
set nobackup       "no backup files
set nowritebackup  "only in case you don't want a backup file while editing
set noswapfile     "no swap files
set noundofile
set number
set relativenumber

" coc airline integration
let g:airline_section_error = '%{airline#util#wrap(airline#extensions#coc#get_error(),0)}'
let g:airline_section_warning = '%{airline#util#wrap(airline#extensions#coc#get_warning(),0)}'

{% if "fzf" in enabled_features %}" Fzf key bindings
nnoremap <silent> <leader>f :FZF<cr>
nnoremap <silent> <leader>F :FZF ~<cr>
nnoremap <silent> <leader>b :Buffers<cr>
{% endif %}
