# coding=utf8
import sublime_plugin, sublime, re

def clipboard():
	return sublime.get_clipboard()

# to transfer cleaned data to sublime text
def clean_paste(data):
	# step 1. make smart ticks dumb
	data = unicode(data)
	data = data.replace(u'”', '"').replace(u'“', '"').replace(u'’', "'")
	# step 2. replace hr's with new lines
	data = data.replace('________________________________________', '\n')
	# step 3. clean new lines
	data = data.replace('\n', ' ')
	# step 4. watch for multiple spaces
	data = data.replace('    ', ' ') # 4 spaces
	data = data.replace('   ', ' ') # 3 spaces
	data = data.replace('  ', ' ') # 2 spaces
	# step 5. clean previously hyphenated words
	#         this may need a regex to clean scenario
	#         where the text is in form ' - ' & ensure
	#         we are within a few characters of a previous
	#         end line. Table that for now.
	data = data.replace('- ', '') 
	return data;

# Paste PDF Function

class PastePdf(sublime_plugin.TextCommand):
	def run(self, edit):
		copy(clean_paste(clipboard()))
		self.view.run_command('paste')