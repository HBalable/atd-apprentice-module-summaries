Unit 11: LINUX
=============

<!--
Introduction to the Linux OS.
Topic 1:The Linux Community and a Career in Open Source
1.1 Linux Evolution and Popular Operating Systems
1.2 Major Open Source Applications
1.3 Understanding Open Source Software and Licensing
1.4 ICT Skills and Working in Linux
Topic 2: Finding Your Way on a Linux System
2.1 Command Line Basics
2.2 Using the Command Line to Get Help
2.3 Using Directories and Listing Files
2.4 Creating, Moving and Deleting Files
Topic 3: The Power of the Command Line (weight: 10)
3.1 Archiving Files on the Command Line
3.2 Searching and Extracting Data from Files
3.3 Turning Commands into a Script
Topic 4: The Linux Operating System (weight: 8)
4.1 Choosing an Operating System
4.2 Understanding Computer Hardware
4.3 Where Data is Stored
4.4 Your Computer on the Network
Topic 5: Security and File Permissions (weight: 7)
5.1 Basic Security and Identifying User Types
5.2 Creating Users and Groups
5.3 Managing File Permissions and Ownership
5.4 Special Directories and Files
-->


Linux is an open source, UNIX-like operating system kernel designed to work on many different platforms. It has an active community developing it, so many distros (Linux distributions) are constantly evolving. It is impossible to count the available distos to try out, as people are free to modify existing source code and compile their own, thoug a quick search for "Linux distros" on *DistroWatch\**, a popular database of open source distros, returns over 800 results.

The most common distros are a particular flavour of Linux, called GNU/Linux, which is a combination of the Linux kernel and an assortment software from the GNU project, a collaborative development project with the goal to give people the freedom and encourage them to modify and share software. Richard Stallman, the founder of this project, wrote the first GNU General Public License (GPL) which enforces the aims of the the project by requiring that any adaptations and redistributions are bound by the same license. Licenses with this ruling are given the name *Copyleft*, as they impose restrictions which are protected by copyright law, but still allow for the modification and sharing of the work, something that is normally prohibited outside of "fair-use" for most copyrighted material.

### Open Source

Open source is a term used to describe software that has publicly available source code, meaning that developers/enthusiastasts can modify and compile the package themselves. Software licensed under an open source license can usually be modified and redistributed by anyone who has acquired a copy of the software.

Here is the definition currently on the OSI's (Open Source Initiative) website:

>Generally, open source software is software that can be freely accessed, used, changed, and shared (in modified or unmodified form) by anyone. Open source software is made by many people, and distributed under licenses that comply with the The Open Source Definition.

Though Linux is not OSI licensed, it is licensed under GPL v2, a license written by the Free Software Foundation (FSF), an organisation also founded by Richard Stallman.

Using Linux
----------

Linux is praised for having the ability to be incredibly lightweight, in the way that you can find fully-usable distributions that only use a minimal amount of space (*Damn Small Linux (DSL) is a distro of only 50MB*) and in the sense that it doesn't have to consume a lot of computer resources. Some Linux distros don't even include a GUI (Graphical user interface), and are completely CLI-based (Command-line interface), which means that they are controlled entirely by typing text-based commands and writing scripts. Even for distros with a user-friendly graphical interface, in many cases people find it easier to do certain tasks using commands, so terminal emulators exist in virtually every GUI-based distro so that you can still use the command-line interface.

### Useful commands

Here I wont explain everything that these commands can do as there is already enough documentation out there available to read. But I will cover the basic commands I use on a daily basis to get around Linux.

#### cd
Changes the Current Working Directory (CWD) to the given path.

#### ls
Lists files in the given path (or ./ by default). Using the -a argument also shows hidden files and the -l arguement shows files in a list format.

For example:

```
~ >>> cd Downloads/
~/Downloads >>> ls                                              
file1.txt  file2.mp4  my_book.epub 
~/Downloads >>> ls -a                                             
.  ..  .hidden_file  file1.txt  file2.mp4  my_book.epub
~/Downloads >>> ls -l                                           
total 0                                                                         
-rw-rw-r-- 1 sysadmin sysadmin 0 Mar  1 20:00 file1.txt                         
-rw-rw-r-- 1 sysadmin sysadmin 0 Mar  1 20:00 file2.mp4                         
-rw-rw-r-- 1 sysadmin sysadmin 0 Mar  1 20:00 my_book.epub   
```

*Note: on Linux, '~' means your home directory, '.'' is the current directory, and '..' refers to the parent directory*


#### touch
Creates a new file with the given name.

```
~/Downloads >>> touch new_file.md                               
~/Downloads >>> ls                                              
file1.txt  file2.mp4  my_book.epub  new_file.md  
```

#### mkdir
Creates a directory, given a name and a desired path.

```
~/Downloads >>> cd ..
~ >>> ls                                                     
Desktop  Downloads
~ >>> mkdir ./my_folder                                         
~ >>> ls                                                        
Desktop  Downloads  my_folder
```

#### cp
Copies a given file to the given destination. If you are copying a directory, you can use the -r flag to recusively copy the contents too.

```
~ >>> cp ./Downloads/new_file.md ./copied_file.md 
~ >>> ls
Desktop  Downloads  my_folder  copied_file.md
```

#### mv
The same as cp but deletes the original file. You can technically use it to rename a file too.

```
~ >>> mv copied_file.md my_folder/moved_file.md
~ >>> ls
Desktop  Downloads  my_folder
~ >>> ls my_folder
moved_file.md
```

#### rm
Removes (deletes) a given file. The -r (recursive) flag can be used to remove directories.

```
~ >>> rm -r my_folder
~ >>> ls
Desktop  Downloads
```

#### alias
Assigns a given command/script to a given alias.

```
~ >>> alias m mkdir
~ >>> m my_new_folder
~ >>> ls
Desktop  Downloads  my_new_folder
```

#### tree
This script looks recursively through child folders and draws an easy to read folder structure diagram.

```
~ >>> tree .
.                                                                               
|-- Desktop                                                                     
|-- Downloads                                                                   
|   |-- file1.txt                                                               
|   |-- file2.mp4                                                               
|   `-- my_book.epub                                                            
`-- my_new_folder                                                               
                                                                                
3 directories, 3 files   
```

#### find
Searches recursively from the given directory for list of files that satisfy a given query, and can execute them all, given the -exec flag. One useful way to find files is by name. So by using the -name flag, you can pass the script a pattern to look for in the names of files. You can also find files by date, size, owner and many other attributes.

```
~ >>> find . -name "*book*"                                       
./Downloads/my_book.epub
~ >>> find . -name "*b*"                                          
./.bash_logout                                                                  
./.bashrc                                                                       
./Downloads/my_book.epub   
```

#### cat
"cat", short for concatenate, displays the contents of text files.

```
~ >>> cat Downloads/file1.txt
one two                                                                         
three four                                                                      
five six                                                                        
seven eight                                                                     
dog can                                                                         
six elephants                                                                 
lamp keyboard                                                                   
```

#### grep
Returns a list of lines, given an input, that match a given pattern. It searches for lines inside given files, so in combination with find, you can easily search recursively for files containing specific strings, which can be very useful.

```
~ >>> cat Downloads/file1.txt | grep six
five six                                                                        
six elephants
~ >>> grep six Downloads/file1.txt
five six                                                                        
six elephants
```

*Note: The '|' character in the example above passes the output of the first command (cat) to the grep command*

#### man
Opens up a documentation page for a given command. These pages are generally not  _info_ is a similar command included in the GNU project, which was intended to encourage a more long-form type of documentation. It has support for hyperlinks for referencing different chapters or files from within the docs.






\* https://distrowatch.com

