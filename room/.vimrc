version 6.0
if &cp | set nocp | endif
let s:cpo_save=&cpo
set cpo&vim
inoremap <silent> <Plug>NERDCommenterInsert  <BS>:call NERDComment('i', "insert")
nnoremap <silent>  :CtrlP
xmap S <Plug>VSurround
nmap cs <Plug>Csurround
nmap ds <Plug>Dsurround
nmap gx <Plug>NetrwBrowseX
xmap gS <Plug>VgSurround
nmap mca <Plug>NERDCommenterAltDelims
xmap mcu <Plug>NERDCommenterUncomment
nmap mcu <Plug>NERDCommenterUncomment
xmap mcb <Plug>NERDCommenterAlignBoth
nmap mcb <Plug>NERDCommenterAlignBoth
xmap mcl <Plug>NERDCommenterAlignLeft
nmap mcl <Plug>NERDCommenterAlignLeft
nmap mcA <Plug>NERDCommenterAppend
xmap mcy <Plug>NERDCommenterYank
nmap mcy <Plug>NERDCommenterYank
xmap mcs <Plug>NERDCommenterSexy
nmap mcs <Plug>NERDCommenterSexy
xmap mci <Plug>NERDCommenterInvert
nmap mci <Plug>NERDCommenterInvert
nmap mc$ <Plug>NERDCommenterToEOL
xmap mcn <Plug>NERDCommenterNested
xmap mcm <Plug>NERDCommenterMinimal
nmap mcm <Plug>NERDCommenterMinimal
xmap mc  <Plug>NERDCommenterToggle
nmap mc  <Plug>NERDCommenterToggle
xmap mcc <Plug>NERDCommenterComment
nmap mcc <Plug>NERDCommenterComment
nnoremap mgt :SignifyToggle
nnoremap mgh :SignifyToggleHighlight
nnoremap mgk :exe v:count .'SignifyJumpToPrevHunk'
nnoremap mgj :exe v:count .'SignifyJumpToNextHunk'
nnoremap <silent> mcgv :ColorVList Value
nnoremap <silent> mcg5 :ColorVList Five-Tone
nnoremap <silent> mcg4 :ColorVList Tetradic
nnoremap <silent> mcgs :ColorVList Saturation
nnoremap <silent> mcg2 :ColorVList Complementary
nnoremap <silent> mcgq :ColorVList Square
nnoremap <silent> mcgp :ColorVList Split-Complementary
nnoremap <silent> mcgn :ColorVList Neutral
nnoremap <silent> mcgm :ColorVList Monochromatic
nnoremap <silent> mcgl :ColorVList luma
nnoremap <silent> mcgh :ColorVList Hue
nnoremap <silent> mcgc :ColorVList Clash
nnoremap <silent> mcga :ColorVList Analogous
nnoremap <silent> mcg6 :ColorVList Six-Tone
nnoremap <silent> mcg3 :ColorVList Triadic
nnoremap <silent> mcim :ColorVInsert CMYK
nnoremap <silent> mc2m :ColorVEditTo CMYK
nnoremap <silent> mcin :ColorVInsert NAME
nnoremap <silent> mc2n :ColorVEditTo NAME
nnoremap <silent> mcipr :ColorVInsert RGBP
nnoremap <silent> mc2pr :ColorVEditTo RGBP
nnoremap <silent> mcil :ColorVInsert HSL
nnoremap <silent> mc2l :ColorVEditTo HSL
nnoremap <silent> mcial :ColorVInsert HSLA
nnoremap <silent> mc2al :ColorVEditTo HSLA
nnoremap <silent> mciar :ColorVInsert RGBA
nnoremap <silent> mc2ar :ColorVEditTo RGBA
nnoremap <silent> mcih :ColorVInsert HSV
nnoremap <silent> mc2h :ColorVEditTo HSV
nnoremap <silent> mcipa :ColorVInsert RGBAP
nnoremap <silent> mc2pa :ColorVEditTo RGBAP
nnoremap <silent> mcir :ColorVInsert RGB
nnoremap <silent> mc2r :ColorVEditTo RGB
nnoremap <silent> mci0 :ColorVInsert HEX0
nnoremap <silent> mc20 :ColorVEditTo HEX0
nnoremap <silent> mcis :ColorVInsert HEX#
nnoremap <silent> mc2s :ColorVEditTo HEX#
nnoremap <silent> mcgg :ColorVTurn2
nnoremap <silent> mcii :ColorVInsert
nnoremap <silent> mc22 :ColorVEditTo HEX
nnoremap <silent> mcpc :ColorVClear
nnoremap <silent> mcpa :ColorVPreviewArea
nnoremap <silent> mcpl :ColorVPreviewLine
nnoremap <silent> mcan :ColorVNoAutoPreview
nnoremap <silent> mcap :ColorVAutoPreview
nnoremap <silent> mcpp :ColorVPreview
nnoremap <silent> mcq :ColorVQuit
nmap mcn <Plug>NERDCommenterNested
nnoremap <silent> mcd :ColorVPicker
nnoremap <silent> mcE :ColorVEditAll
nnoremap <silent> mce :ColorVEdit
nnoremap <silent> mcw :ColorVView
nnoremap <silent> mcmx :ColorVMax
nnoremap <silent> mc3 :ColorVMax
nnoremap <silent> mcmd :ColorVMid
nnoremap <silent> mcmn :ColorVMin
nnoremap <silent> mc1 :ColorVMin
nnoremap <silent> mcsn :ColorVSchemeNew
nnoremap <silent> mcsf :ColorVSchemeFav
nnoremap <silent> mcss :ColorVScheme
nnoremap <silent> mcv :ColorV
nmap <silent> mig <Plug>IndentGuidesToggle
nmap ySS <Plug>YSsurround
nmap ySs <Plug>YSsurround
nmap yss <Plug>Yssurround
nmap yS <Plug>YSurround
nmap ys <Plug>Ysurround
nnoremap <silent> <Plug>NetrwBrowseX :call netrw#NetrwBrowseX(expand("<cWORD>"),0)
nnoremap <silent> <Plug>SurroundRepeat .
xnoremap <silent> <Plug>NERDCommenterUncomment :call NERDComment("x", "Uncomment")
nnoremap <silent> <Plug>NERDCommenterUncomment :call NERDComment("n", "Uncomment")
xnoremap <silent> <Plug>NERDCommenterAlignBoth :call NERDComment("x", "AlignBoth")
nnoremap <silent> <Plug>NERDCommenterAlignBoth :call NERDComment("n", "AlignBoth")
xnoremap <silent> <Plug>NERDCommenterAlignLeft :call NERDComment("x", "AlignLeft")
nnoremap <silent> <Plug>NERDCommenterAlignLeft :call NERDComment("n", "AlignLeft")
nnoremap <silent> <Plug>NERDCommenterAppend :call NERDComment("n", "Append")
xnoremap <silent> <Plug>NERDCommenterYank :call NERDComment("x", "Yank")
nnoremap <silent> <Plug>NERDCommenterYank :call NERDComment("n", "Yank")
xnoremap <silent> <Plug>NERDCommenterSexy :call NERDComment("x", "Sexy")
nnoremap <silent> <Plug>NERDCommenterSexy :call NERDComment("n", "Sexy")
xnoremap <silent> <Plug>NERDCommenterInvert :call NERDComment("x", "Invert")
nnoremap <silent> <Plug>NERDCommenterInvert :call NERDComment("n", "Invert")
nnoremap <silent> <Plug>NERDCommenterToEOL :call NERDComment("n", "ToEOL")
xnoremap <silent> <Plug>NERDCommenterNested :call NERDComment("x", "Nested")
nnoremap <silent> <Plug>NERDCommenterNested :call NERDComment("n", "Nested")
xnoremap <silent> <Plug>NERDCommenterMinimal :call NERDComment("x", "Minimal")
nnoremap <silent> <Plug>NERDCommenterMinimal :call NERDComment("n", "Minimal")
xnoremap <silent> <Plug>NERDCommenterToggle :call NERDComment("x", "Toggle")
nnoremap <silent> <Plug>NERDCommenterToggle :call NERDComment("n", "Toggle")
xnoremap <silent> <Plug>NERDCommenterComment :call NERDComment("x", "Comment")
nnoremap <silent> <Plug>NERDCommenterComment :call NERDComment("n", "Comment")
imap S <Plug>ISurround
imap s <Plug>Isurround
imap  <Plug>Isurround
let &cpo=s:cpo_save
unlet s:cpo_save
set paste
set autochdir
set autoindent
set backspace=indent,eol,start
set expandtab
set fileencodings=ucs-bom,utf-8,default,latin1
set helplang=en
set mouse=a
set printoptions=paper:letter
set runtimepath=~/.vim/bundle/vundle,~/.vim/bundle/vim-powerline,~/.vim/bundle/nerdtree,~/.vim/bundle/vim-nerdtree-tabs,~/.vim/bundle/vim-indent-guides,~/.vim/bundle/colorv.vim,~/.vim/bundle/vim-signify,~/.vim/bundle/nerdcommenter,~/.vim/bundle/ctrlp.vim,~/.vim/bundle/vim-surround,~/.vim/bundle/vim-fugitive,~/.vim/bundle/tabular,~/.vim/bundle/vim-stylus,~/.vim/bundle/jellybeans.vim,~/.vim/bundle/vim-colors-solarized,~/.vim,/var/lib/vim/addons,/usr/share/vim/vimfiles,/usr/share/vim/vim73,/usr/share/vim/vimfiles/after,/var/lib/vim/addons/after,~/.vim/after,~/.vim/bundle/vundle/,~/.vim/bundle/vundle/after,~/.vim/bundle/vim-powerline/after,~/.vim/bundle/nerdtree/after,~/.vim/bundle/vim-nerdtree-tabs/after,~/.vim/bundle/vim-indent-guides/after,~/.vim/bundle/colorv.vim/after,~/.vim/bundle/vim-signify/after,~/.vim/bundle/nerdcommenter/after,~/.vim/bundle/ctrlp.vim/after,~/.vim/bundle/vim-surround/after,~/.vim/bundle/vim-fugitive/after,~/.vim/bundle/tabular/after,~/.vim/bundle/vim-stylus/after,~/.vim/bundle/jellybeans.vim/after,~/.vim/bundle/vim-colors-solarized/after
set shiftwidth=2
set smarttab
set suffixes=.bak,~,.swp,.o,.info,.aux,.log,.dvi,.bbl,.blg,.brf,.cb,.ind,.idx,.ilg,.inx,.out,.toc
set tabstop=2
set wildignore=*.pyc
" vim: set ft=vim :
