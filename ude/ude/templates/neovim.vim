call plug#begin()
Plug 'christoomey/vim-tmux-navigator' " ctrl+hjkl tmux integration
Plug 'neoclide/coc.nvim', {'do': { -> coc#util#install()}} " LSP support
Plug 'tpope/vim-sleuth' " Fix tabs
Plug 'plasticboy/vim-markdown'
Plug 'godlygeek/tabular' " Required for markdown table formatting

" Eye candy
Plug 'crusoexia/vim-monokai'
Plug 'kaicataldo/material.vim'
Plug 'vim-airline/vim-airline'

{% if "fzf" in enabled_features %}Plug 'junegunn/fzf'
Plug 'junegunn/fzf.vim'
{% endif %}

{% if "typescript" in enabled_features %}
Plug 'leafgarland/typescript-vim'
Plug 'ianks/vim-tsx'
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
set hidden
set cmdheight=2    " Better display for messages

{% if "fzf" in enabled_features %}
" ---------------
"  FZF
" ---------------
nnoremap <silent> <leader>p :FZF<cr>
nnoremap <silent> <leader>P :FZF ~<cr>
nnoremap <silent> <leader>b :Buffers<cr>
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
nmap <leader>rn <Plug>(coc-rename)

" Remap for format selected region
vmap <leader>f  <Plug>(coc-format-selected)
nmap <leader>f  <Plug>(coc-format-selected)

" Remap for do codeAction of selected region, ex: `<leader>aap` for current paragraph
vmap <leader>a  <Plug>(coc-codeaction-selected)
nmap <leader>a  <Plug>(coc-codeaction-selected)

" Remap for do codeAction of current line
nmap <leader>ac  <Plug>(coc-codeaction)
" Fix autofix problem of current line
nmap <leader>qf  <Plug>(coc-fix-current)

" Use `:Format` for format current buffer
command! -nargs=0 Format :call CocAction('format')

" Use `:Fold` for fold current buffer
command! -nargs=? Fold :call     CocAction('fold', <f-args>)

" Using CocList
" Show all diagnostics
nnoremap <silent> <space>a  :<C-u>CocList diagnostics<cr>
" Manage extensions
nnoremap <silent> <space>e  :<C-u>CocList extensions<cr>
" Show commands
nnoremap <silent> <space>c  :<C-u>CocList commands<cr>
" Find symbol of current document
nnoremap <silent> <space>o  :<C-u>CocList outline<cr>
" Search workspace symbols
nnoremap <silent> <space>s  :<C-u>CocList -I symbols<cr>
" Do default action for next item.
nnoremap <silent> <space>j  :<C-u>CocNext<CR>
" Do default action for previous item.
nnoremap <silent> <space>k  :<C-u>CocPrev<CR>
" Resume latest coc list
nnoremap <silent> <space>p  :<C-u>CocListResume<CR>

" Remap for listing buffers
vmap <leader>b  :<C-u>Buffers<cr>
nmap <leader>b  :<C-u>Buffers<cr>
