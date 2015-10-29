# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

1. pushd [directory path] - saves the current directory and takes you to the new one in the argument. Without arguments it will take you to the last pushd'ed directory
2. popd - takes you to the previously saved directory
3. cp [file1] [file2] - copies file1 to file2
4. mv [file1] [file2] - renames file1 to file2
5. less [file] - opens file in a new window
6. more [file] - opens file in window
7. cat [file] - streams file in window without paging
8. $ | $ - takes output of command on left and "pipes" it to the right
9. man [command] - look up commands in the manual
10. grep -i [word or words] *.txt - search for the words or words in all text files in current directory

---


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

1. ls : lists contents in current directory
2. ls -a : "Include directory entries whose names begin with a dot (.)." [From manual]
3. ls -l : "List in long format. If the output is to a terminal, a total sum for all the file sizes is output on a line before the long listing." [From manual]
4. ls -lh : "When used with the -l option, use unit suffixes: Byte, Kilobyte, Megabyte, Gigabyte, Terabyte and Petabyte in order to reduce the number of digits to three or less using base 2 for sizes." [From -h in manual]

Any combination of those flags are meaningful. For example, combining to form "ls -a -lh" pulls up the sizes of the files as well as the directories beginning with a dot (.).

---


---

What does `xargs` do? Give an example of how to use it.

From the manual: construct argument list(s) and execute utility. Often combined with "|" to pipe something(s) to the xargs command.

Example: find . -name "*.txt" | xargs grep -i cowabunga
  this will pipe each text file to the end of the xargs command so that grep can be used to search for "cowabunga" in each file.


---

