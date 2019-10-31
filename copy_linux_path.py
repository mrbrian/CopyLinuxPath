import os
import sublime
import re
import subprocess
import sublime_plugin

class CopyLinuxPath(sublime_plugin.TextCommand):

    def run(self, edit, **kwargs):
        full_file_path = sublime.active_window().active_view().file_name()
        no_backslash = full_file_path.replace('\\', "/")
        no_drive_letter = re.sub('.*:', "/home/byee", no_backslash)
        no_filename = re.match('(.*/)', no_drive_letter).group(1)
        sublime.set_clipboard(no_filename)

class AddIncludeAtTop(sublime_plugin.TextCommand):

    def run(self, edit, **kwargs):
        INCLUDE_STR = "#include"
        active_view = sublime.active_window().active_view()
        orig_selection = [x for x in active_view.sel()]
        selection = active_view.sel()
        include_block_start_pos = active_view.find(INCLUDE_STR, 0).a
        for region in selection:
            selected_text = active_view.substr(region)
            include_statement = "{} <{}.h>\n".format(INCLUDE_STR, selected_text)
            active_view.insert(edit, include_block_start_pos, include_statement)
        selection.clear()
        all_includes = active_view.find_all(INCLUDE_STR)
        include_block_end_pos = all_includes[-1].b
        selection.add(sublime.Region(include_block_start_pos, include_block_end_pos))
        active_view.run_command("sort_lines")
        selection.clear()
        active_view.sel().add_all(orig_selection)

class RunRemoteTmuxCommand(sublime_plugin.TextCommand):

    def run(self, edit, **kwargs):
        cmd_a = ["ssh", "localhost", "tmux send-keys", "echo\ hello Enter"]
        wd = "C:\\Windows\\System32\\OpenSSH"
        p = subprocess.Popen(cmd_a, cwd=wd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
        if p.stdout is not None:
            msg = p.stdout.readlines()
        print(msg)