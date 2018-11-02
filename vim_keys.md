* Switch terminal to normal mode
    * ctr-w N
* Swap windows
    * Ctr-w r
* Format
    * :Autoformat
* Search
    * :grep -r --include=whateverpattern 'regex' [directory]
    * do :copen to actually list the results in quickfix
* Explore
    * d = create directory
    * % = create file
* Blank buffer
    * :enew
* Center screen at cursor
    * zz
* Show complete file info
    * Ctrl g
* Open / Close folds
    * zo and zc
* File explorer
    * :Explorer
* Switch ctrlp mode
    * Ctrl p then Ctrl f
* Ctrl P navigation
    * Use Ctrl j and Ctrl k to go up down the list
* Completion options (omnicomplete)
    * Ctrl x Ctrl o
* Go to definition
    * Ctrl ]
* Come back from definition
    * Ctrl t
* Copy to clipboard
    * " * y
* Paste from clipboard
    * " * p
* Revert file
    * :u1|u
* Next tab
    * :tabn
    * gt
* Previous tab
    * tabp
    * gT
* Split window horizontaly
    * Ctrl ws
* Split window vertically
    * Ctrl wv
* Quit window
    * Ctrl wq
* Max out window height
    * Ctrl w _
* Max out winkow width
    * Ctrl w |
* All about windows: https://robots.thoughtbot.com/vim-splits-move-faster-and-more-naturally
* QuickFix window
    :copen " Open the quickfix window
    :ccl   " Close it
    :cw    " Open it if there are "errors", close it otherwise (some people prefer this)
    :cn    " Go to the next error in the window
    :cnf   " Go to the first error in the next file
* Fix panel sizes
    * Ctrl w +
    * Ctrl w -
    * Ctr w |
    * Ctrl w =
* Scroll per line
    * Ctrl Y or Ctrl E
* Scroll per page
    * Ctrl U or Ctrl D
* Go back to previous buffer
    * Ctrl 6
* Go back to previous jump
    * Ctrl o
* Go to next jump
    * Ctrl i
* List buffers
    * :ls
* Open buffer
    * :b
* Paste stuff in vim's command line
    * Ctrl r "
* New directory
    * d
* Remove / delete buffer entirely
    * bd
* Move window to tab
    * Ctrl w T
