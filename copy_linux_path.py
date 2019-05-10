import os
import sublime
import sublime_plugin
import re

class CopyLinuxPath(sublime_plugin.TextCommand):

    def run(self, edit, **kwargs):
        full_file_path = sublime.active_window().active_view().file_name()
        no_backslash = full_file_path.replace('\\', "/")
        no_drive_letter = re.sub('.*:', "/home/byee", no_backslash)
        no_filename = re.match('(.*/)', no_drive_letter).group(1)
        sublime.set_clipboard(no_filename)