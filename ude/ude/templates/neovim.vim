call plug#begin()
Plug 'christoomey/vim-tmux-navigator'  " ctrl+hjkl tmux integration
Plug 'tpope/vim-sleuth'                " Fix tabs
Plug 'plasticboy/vim-markdown'         " Markdown support
Plug 'godlygeek/tabular'               " Required for markdown table formatting
Plug 'tpope/vim-fugitive'              " GIT plugin
Plug 'glench/vim-jinja2-syntax'

" Coc Language Server Protocol support
Plug 'neoclide/coc.nvim', {'do': { -> coc#util#install()}} " LSP support
Plug 'neoclide/coc-json', {'do': 'yarn install --frozen-lockfile'}
Plug 'neoclide/coc-html', {'do': 'yarn install --frozen-lockfile'}
Plug 'neoclide/coc-css', {'do': 'yarn install --frozen-lockfile'}
Plug 'neoclide/coc-highlight', {'do': 'yarn install --frozen-lockfile'}
Plug 'neoclide/coc-yaml', {'do': 'yarn install --frozen-lockfile'}

" Eye candy
Plug 'crusoexia/vim-monokai'
Plug 'kaicataldo/material.vim'
Plug 'vim-airline/vim-airline'

{% if "fzf" in enabled_features %}Plug 'junegunn/fzf'
Plug 'junegunn/fzf.vim'
{% endif %}

{% if "typescript" in enabled_features %}
Plug 'neoclide/coc-tsserver', {'do': 'yarn install --frozen-lockfile'}
Plug 'leafgarland/typescript-vim'
Plug 'ianks/vim-tsx'
{% endif %}

{% if "python" in enabled_features %}
Plug 'neoclide/coc-python', {'do': 'yarn install --frozen-lockfile'}
{% endif %}
call plug#end()

" ---------------
"  Basic Config
" ---------------
colorscheme material
set termguicolors 
set nobackup       "no backup files
set nowritebackup  "only in case you don't want a backup file while editing
set noswapfile     "no swap files
set clipboard+=unnamedplus " Yank / paste from clipboard
set noundofile
set number
set relativenumber
set hidden
set cmdheight=2    " Better display for messages
set expandtab      " Default to spaces
set shiftwidth=2   " Default to 2 spaces for indentation
let g:vim_markdown_folding_disabled = 1  " Disable markdown folding because of bug


{% if "fzf" in enabled_features %}
" ---------------
"  FZF
" ---------------
nnoremap <silent> <space>p :FZF<cr>
nnoremap <silent> <space>P :FZF ~<cr>
nnoremap <silent> <space>b :Buffers<cr>
{% endif %}

" ----------------
"  COC
"  ---------------
" Typescript detection
" au BufNewFile,BufRead *.ts set filetype=typescript
"au BufNewFile,BufRead *.tsx set filetype=typescriptreact

" coc airline integration
let g:airline_section_error = '%{airline#util#wrap(airline#extensions#coc#get_error(),0)}'
let g:airline_section_warning = '%{airline#util#wrap(airline#extensions#coc#get_warning(),0)}'
let g:airline#extensions#branch#enabled = 1

" Smaller updatetime for CursorHold & CursorHoldI
set updatetime=300

" Use <c-space> for trigger completion.
inoremap <silent><expr> <c-space> coc#refresh()

" Use <cr> for confirm completion, `<C-g>u` means break undo chain at current position.
" Coc only does snippet and additional edit on confirm.
inoremap <expr> <cr> pumvisible() ? "\<C-y>" : "\<C-g>u\<CR>"

" Use `[c` and `]c` for navigate diagnostics
nmap <silent> [c <Plug>(coc-diagnostic-prev)
nmap <silent> ]c <Plug>(coc-diagnostic-next)

" Remap keys for gotos
nmap <silent> gd <Plug>(coc-definition)
nmap <silent> gy <Plug>(coc-type-definition)
nmap <silent> gi <Plug>(coc-implementation)
nmap <silent> gr <Plug>(coc-references)

" Use K for show documentation in preview window
nnoremap <silent> K :call <SID>show_documentation()<CR>

function! s:show_documentation()
  if &filetype == 'vim'
    execute 'h '.expand('<cword>')
  else
    call CocAction('doHover')
  endif
endfunction

" Highlight symbol under cursor on CursorHold
autocmd CursorHold * silent call CocActionAsync('highlight')

" Remap for rename current word
nmap <space>rn <Plug>(coc-rename)

" Remap for format selected region
vmap <space>fs  <Plug>(coc-format-selected)
nmap <space>fs  <Plug>(coc-format-selected)

" Remap for do codeAction of selected region, ex: `<leader>aap` for current paragraph
vmap <space>a  <Plug>(coc-codeaction-selected)
nmap <space>a  <Plug>(coc-codeaction-selected)

" Remap for do codeAction of current line
nmap <space>lc  <Plug>(coc-codeaction)
" Fix autofix problem of current line
nmap <space>qf  <Plug>(coc-fix-current)

" Use `:Format` for format current buffer
command! -nargs=0 Format :call CocAction('format')

" Use `:Fold` for fold current buffer
command! -nargs=? Fold :call     CocAction('fold', <f-args>)

" Using CocList
" Show all diagnostics
nnoremap <silent> <space>e  :<C-u>CocList diagnostics<cr>
" Manage extensions
" nnoremap <silent> <space>e  :<C-u>CocList extensions<cr>
" Show commands
nnoremap <silent> <space>c  :<C-u>CocList commands<cr>
" Find symbol of current document
nnoremap <silent> <space>yf  :<C-u>CocList outline<cr> 
" Search workspace symbols
nnoremap <silent> <space>yp  :<C-u>CocList -I symbols<cr>
" Do default action for next item.
nnoremap <silent> <space>j  :<C-u>CocNext<CR>
" Do default action for previous item.
nnoremap <silent> <space>k  :<C-u>CocPrev<CR>
" Resume latest coc list
" nnoremap <silent> <space>p  :<C-u>CocListResume<CR>

" Remap for listing buffers
vmap <space>b  :<C-u>Buffers<cr>
nmap <space>b  :<C-u>Buffers<cr>

" Open on new vertical split
nmap <space>vp  <C-w>v<C-l><space>p 
nmap <space>vP  <C-w>v<C-l><space>P 
nmap <space>vb  <C-w>v<C-l><space>b

" Finds text in files
nmap <space>sp  :<C-u>Ag<cr>

" Open file explorer
nmap <space>o  :<C-u>Explore<cr>

" Open file explorer in vertical split
nmap <space>vo  <C-w>v<C-l>:<C-u>Explore<cr>
