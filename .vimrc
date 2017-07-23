" .vimrc

set tabstop=4          " number of visual spaces per TAB
set softtabstop=4      " number of spaces in tab when editing
set expandtab          " tabs are spaces
set number 			   " number the raws
set ruler			   " Always show current position
set visualbell         " Blink cursor on error instea of beeping
set wrap 	       " Always wrap long lines
set cmdheight=2        " Height of the command bar
set hlsearch           " Highlight search results

" Last line
set showmode
set showcmd

set showmatch          " Show matching brackets when text indicator is over them
set mat=2              " How many tenths of a second to blink when matching brackets

syntax enable          " Enable syntax highlighting



""""""""""""""""""""""""""""""
" => Python section
""""""""""""""""""""""""""""""
let python_highlight_all = 1
au FileType python syn keyword pythonDecorator True None False self

au BufNewFile,BufRead *.jinja set syntax=htmljinja
au BufNewFile,BufRead *.mako set ft=mako

au FileType python map <buffer> F :set foldmethod=indent<cr>

au FileType python inoremap <buffer> $r return 
au FileType python inoremap <buffer> $i import 
au FileType python inoremap <buffer> $p print 
au FileType python inoremap <buffer> $f #--- <esc>a
au FileType python map <buffer> <leader>1 /class 
au FileType python map <buffer> <leader>2 /def 
au FileType python map <buffer> <leader>C ?class 
au FileType python map <buffer> <leader>D ?def 
au FileType python set cindent
au FileType python set cinkeys-=0#
au FileType python set indentkeys-=0#


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => Syntastic (syntax checker)
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

" Python
let g:syntastic_python_checkers=['pyflakes']
