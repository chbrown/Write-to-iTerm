# Term

Because the other [Sublime Text 2](http://www.sublimetext.com/2) plugins for sending text to iTerm weren't cutting it.

The default shortcut is the three keys immediately to the left of your space bar (`control` + `alt` + `command`) and `enter`. If nothing is selection, this sends the current line to iTerm, and advances the cursor to the next line. If something is selected, it sends that, and doesn't change the selection. If multiple things are selected, it will send each one as a different command (as if you had selected each individually and sent them in turn).

Currently, iTerm is weird and adds a newline to all input sent to it via `osascript`, _unless_ that input ends with a space (" "). However, I get the feeling that the iTerm developer (@gnachman) doesn't really give a damn about the applescript interface, so that might get fixed in the future.


## Installation issues

If you are getting a tab-completion prompt from iTerm2.app when sending it text, or it's not calling the text you sent it, ensure that your `~/.inputrc` config file does not contain the line, `Control-j: menu-complete`.


## License

Copyright © 2013 Christopher Brown. [MIT Licensed](LICENSE).
