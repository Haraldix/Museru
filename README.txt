git clone https://github.com/Haraldix/Museru.git
c:/Repos/Museru
push spell:
git push -v  https://github.com/Haraldix/Museru Museru_master
kysyy aluksi salasanaa - aina väärin
salasana kahdesti: githubiin ja pushiin!

pdb debug:
goto:https://www.digitalocean.com/community/tutorials/how-to-use-the-python-debugger#working-interactively-with-the-python-debugger

args	a	Print the argument list of the current function
break	b	Creates a breakpoint (requires parameters) in the program execution
continue	c or cont	Continues program execution
help	h	Provides list of commands or help for a specified command
jump	j	Set the next line to be executed
list	l	Print the source code around the current line
next	n	Continue execution until the next line in the current function is reached or returns
step	s	Execute the current line, stopping at first possible occasion
pp	pp	Pretty-prints the value of the expression
quit or exit	q	Aborts the program
return	r

python -m pdb Etyde001.py

variable watch:
(Pdb) commands 1 
“1=breakpoint"
(com) print self.fw_dh_ui_autotest_path
(com) print fw_dh_ui_autotest_path
(com) end