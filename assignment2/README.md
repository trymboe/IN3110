# README.md Assignment2 

## Task 2.1

### Prerequisites

You will need to have bash installed on your computer


### Functionality

The script can move all or some type of files from one folder to another


### Missing Functionality

The script has all the functionality presented in the assignemnt.

### Usage

First of all, run this command in the folder where move.sh is:
$ chmod a+x move.sh

The program takes 3 arguments, source folder, destination folder and file type.
To move all files from one the folder "A" to folder "B", do this:

$ ./move.sh A B all 

or if you want to use full path:

$ ./move.sh ~/documents/myFolder/A documents/myOtherFolder/B all
If you use full path, be cautious of paths with spaces in them.

To move only one type of file, like only the .txt-files, do this:

$ ./move.sh A B .txt


## Task 2.2 and 2.3

### Prerequisites

You will need to have bash installed on your computer and have directory
~/.local/share on your computer. And you have to use a ifi workstation or similar.

In your terminal, type:
$ cd ~
$ vi .bash_profile

in the .bash_profile-file, type:
source [full path to track.sh file]

Restart your terminal


### Functionality

This script can time different tasks you do by manually telling it
when you start and when you end a certain task.
It can also display how long time you've used on different tasks


### Missing Functionality

I do not use a permanent environment, I only save everything in the timer_logfile.

Not a missing functionality, but the code is not segmented into multiple functions because
when the file is sourced all functions are callable from the terminal. That could led to
errors

I do not search for the timer_logfile file use grep, but create it if it does not exist
whenever the user run the program.

### Usage

When you have sourced the file you can use it like this
To start a task, do this:

$ track start 'taskName'

To stop a task, do this:

$ track stop

To check status, do this:

$ track status

To view log of all tasks, do this:

$ track log
