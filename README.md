# Write-to-iTerm

Because the other [Sublime Text 2](http://www.sublimetext.com/2) plugins for sending text to iTerm weren't cutting it.

The default shortcut is the three keys immediately to the left of your space bar (`control` + `alt` + `command`) and `enter`. If nothing is selected, this sends the current line to iTerm, and advances the cursor to the next line. If something is selected, it sends that, and doesn't change the selection. If multiple things are selected, it will send each one as a different command (as if you had selected each individually and sent them in turn).

This shortcut is intended to be a quick demo only. Please add the following snippet to your "Key Bindings - User" preferences file (you can quickly access that file from within Sublime Text 2 with the shortcut `⌘+shift+p "key user"`):

    {
      "keys": ["shift+enter"],
      "command": "write_selection_to_iterm"
    }


## Installation

This is not yet in [`Package Control`](https://sublime.wbond.net/), so installation must be done manually:

    cd ~/"Library/Application Support/Sublime Text 2/Packages"
    git clone https://github.com/chbrown/Write-to-iTerm.git "Write to iTerm"

Or for development, clone it elsewhere and symlink it in:

    cd ~/github
    git clone https://github.com/chbrown/Write-to-iTerm.git
    cd ~/"Library/Application Support/Sublime Text 2/Packages"
    ln -sf ~/github/Write-to-iTerm "Write to iTerm"


## Issues

Currently, iTerm (technically, iTerm2.app) is weird and adds a newline to all input sent to it via `osascript`, _unless_ that input ends with a space (" "). However, I get the feeling that the iTerm developer (@gnachman) doesn't really give a damn about the applescript interface, so that might get fixed in the future.

If you are getting a tab-completion prompt in iTerm2.app when sending it text, or it's not calling the text you sent it, ensure that your `~/.inputrc` config file does not contain the line, `Control-j: menu-complete`.

See this diff for an example fix: chbrown/dotfiles@d0b0f3227b3a07127f13104f02b654751b592752


## TODO: Publish to Package Control

* [Instructions](https://sublime.wbond.net/docs/developers)
* [My channel fork](https://github.com/chbrown/package_control_channel)


## License

Copyright © 2013 Christopher Brown. [MIT Licensed](LICENSE).
