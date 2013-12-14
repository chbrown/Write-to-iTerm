import sublime
import sublime_plugin
from subprocess import Popen, PIPE


iterm_osascript_template = '''
tell application "iTerm"
  tell current session of current terminal to write text "%s"
end tell
'''.strip()


class SendSelectionToTermCommand(sublime_plugin.TextCommand):
    '''
    command name: "send_selection_to_term"
    '''
    # def __init__(self, *args, **kwargs):
        # # but we don't, because we can just as easily re-read
        #   our config whenever we're called
        # settings = sublime.load_settings('Term.sublime-settings')
        # return super(SendSelectionToTermCommand, self).__init__(*args, **kwargs)

    def send_text(self, content):
        content = content.rstrip('\n')
        # escape slashes first so that we don't doubly-escape any of the intentional double-quote escapes
        content = content.replace('\\', '\\\\')
        # double quotes are the only thing we really need to escape
        content = content.replace('"', '\\"')

        osascript_text = iterm_osascript_template % content

        proc = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        stdout, stderr = proc.communicate(osascript_text)

    def run(self, edit):
        view = self.view
        # view.sel() is a list of 2-tuples which are cursor positions within the file.
        # for a single cursor point the left and right tuple items will be equal,
        #   in which case selection.empty() will be True
        settings = sublime.load_settings('Term.sublime-settings')
        for selection in list(view.sel()):
            content = view.substr(selection)
            if not content:
                # if the selection is empty, expand to the whole line
                line_selection = view.line(selection)
                content = view.substr(line_selection)
                if settings.get('term_cursor_advance') is True:
                    # view.rowcol converts from a cursor index to row and column indices
                    row, col = view.rowcol(selection.begin())
                    # view.text_point is the inverse of rowcol:
                    #   it converts from (row, col) to a cursor indx
                    next_line = min(view.text_point(row + 1, col),
                        # but we want to end, maximally, at the end of the subsequent line
                        max(view.text_point(row + 2, 0) - 1,
                            # but if there is nothing two lines down,
                            #   min out at the end of the current line
                            view.text_point(row + 1, 0)))
                    view.sel().subtract(selection)
                    view.sel().add(sublime.Region(next_line, next_line))

            self.send_text(content)
