# Lab 1 Part 1 <br> Introduction to File/Directory Structure and Bash Command Line Interface

## Logging On

You should do this lab on the machines in your classroom using the generic ``pcse_user`` account.

**NOTE:** *pcse* is an abbreviation for the *Physics, Computer Science and Engineering* department.

On the Windows laptops in front of you,
you should see a  screen that says "Press CTRL + ALT + DELETE to log on".
If you do not see this screen because your laptop is already logged in, then first log out.

> NOTE: Reboot the machine when you first enter the lab!
> Ocassionally the machines have trouble connecting to the GitLab server ("remote not accessible"), and the fix is to REBOOT.  So, just reboot now!

Now log on  by pressing CTRL + ALT + DELETE to bring up a login screen,
then typing "pcse_user" and no password (the character between the e and u is an underscore,
  the shift key to the right of the 0).


You may bring your laptop to class, and use that if you would like for subsequent labs.
If you choose not to, you will use the pcse_user account on these machines, as you will for all exams.

**Warning:** The files in the pcse_user account are removed each time you log out, so please make sure all files that you work on are saved (e.g. to GitLab) before logging out.
Be sure to log out before leaving your computer;
you are responsible if someone accesses your files.

## Files and Directories

Computers use *files* to store data, and *directories* to organize files.  
Some files contain simple human readable text, some *binary* computer readable data, and yet others contain executable *application* code.  
Directories can hold files as well as other directories.

Your files, directories,
and programs are in a hierarchical *file system*.

For example, to see what files are on your Desktop in Windows, `press the Windows key`, then type `File Explorer` and press ``ENTER``.  

** Do this now.**

This `File Explorer` is an *interface* that lets users interact with their computers.
Most people who use computers use Graphical User Interfaces (GUIs) to navigate their computer as we will with the *File Explorer* in Windows.

File Explorer is the GUI that lets you view where a file is.
You can open any of the files in File Explorer by moving your mouse to them, and double clicking on them (press and release left mouse button quickly two times for double click).
Most novice users interface with their computer using GUIs such as File Explorer.

**Now click on `Desktop` in the browser tree to the left.**

You should see a list of the files that you see on your Desktop.

**NOTE:** As you go along, please initial the appropriate line on the provided form to keep track of your progress.


**Note:** You will likely see more icons on the Desktop than in the File Explorer Window. That is because Windows tries to make it easier to access some standard files/programs by displaying icons on the Desktop that actually reside elsewhere in the file structure.

Now go to the top level directory
in File Explorer by choosing "This PC" then "C:" in the File Explorer.

**Go to the top level directory now.**
Make note of your progress on the provided form.

 You should see several graphical *folder* icons, analogous to a folder in a file cabinet; in everyday usage, people use the term *folder* and *directory* interchangeably.

 For example, you should see:
*  Windows \[this folder is for programs for the Windows Operating System, and you should not change anything in this directory],
* Program Files \[this folder holds most of the programs you run],
* Program Files (x86) [this folder holds legacy programs], and
* Users [this has a folder for each user on the system].

Each of these folders may have several other folders.

**Now select the `Users` folder by
double clicking on it in File Explorer.**
It should have at least one sub-folder in it, 'pcse_user'.
This ``Users\pcse_user`` is the *home* directory for the default user. Select the `pcse_user` folder.

 > NOTE: In the current lab setup, a temporary user ID is set up, and so the
 > actual folder may be named "pcse_user.PCS.000.001.002" or similar.
 > There may be multiple such folders if you have not recently rebooted.
 > If you select the wrong folder it will give you an "access denied" error.


The proper folder for current user should have several sub-folders.
 Select `Desktop`.
 You should be back at the `Desktop` folder we originally opened.

The file structure hierarchy  that you just navigated looks something like this *tree*:

![picture of a file hierarchy][folderstructure]

**NOTE:** In computer science, a *tree* structure has its *root* node at the top, and *leaf* nodes at the bottom.

## Graphical User Interfaces (GUIs) vs. Command Line Interfaces (CLIs)

In contrast to the GUI, we will use a Command Line Interface (CLI), also called a *shell* much of the semester.
CLIs are available on all operating systems including
Windows, MAC OS, and Linux,
and are often available when GUIs are not an option.  
For example, many servers or embedded systems do not have monitors attached, and the only access is via a network interface to a CLI.

Different operating systems use different commands for their CLI.  
To avoid this, we will make use of the ``GitBash`` CLI on Windows.  
This CLI uses *Bash* commands, which are standard on MAC OS and Linux.  
If you are curious, see https://en.wikipedia.org/wiki/Bash_(Unix_shell) for more information (Optional reading - not required!).

Later we will install GitBash on your personal Windows machine,
but for now use the lab machines where GitBash is already installed.

Some terms to know moving forward are:

* **Working directory** - This term refers to the directory that our commands are relevant to.  If one does not specify a directory for a command to use, generally the current *working directory* is assumed. You can visualize this term as when you open your file explorer, and click into the Desktop icon. It will list the folders and files currently contained in the Desktop folder, so the current working directory is now the Desktop folder.

* **ANY OTHER USEFUL TERMS TO KNOW**

To start, press the Windows key, and type "Git Bash" in the search prompt,
and choose Git Bash Shell.
It should look like this:

![picture of git-bash shell][bashpic]

The git-bash command brings up a window that is called a Bash shell (a shell is a Command Line Interface).
You can create the same type of window on a Mac by choosing Terminal from Spotlight Search (press command-space then type "Terminal" then press the enter key).
Terminal in Mac is a Bash shell.  
The default terminal in Linux is also a Bash shell.

We will go over the most common commands that you will use in this shell,
but you can always *google* these bash commands because bash shells are common.

Here is a summary of the 4 fundamental bash commands you will use in this course:

* `pwd` - Stands for *print working directory*. This command prints out the **full path** to your current working directory.

* `ls` - This command lists all of the current files and directories contained in your working directory.

* `cd` - Stands for change directory. This command allows the user to navigate the file system tree. You can change directories by typing in the prompt `cd <directory>` or for a real example `cd Desktop`.

* `mkdir` - Stands for make directory. This is similar to clicking new folder in the file explorer gui. This command will make a new directory given a name in the current working directory. For example, `mkdir cpsc250l` will make a new folder in the current working directory called 'cpsc250l'.

Verify that the prompt shows ``~`` as one first line of the image.  
If not (e.g. ``/bin``), type ``cd ~`` and ENTER key
to *change directory* to the user home directory indicated by the ``~`` (tilde) character.  
The ``~`` is used as a short cut to indicate the users defined *home* directory;
you may use ``~`` to indicate the full path to the home directory in any bash shell.
> NOTE: If you `pwd` from the `~`, you will see the true temporary user ID assigned to you.


**NOTE:** The term *folder* and *directory* are often used interchangeably. We will follow the technical distinction and use *directory*.  See https://en.wikipedia.org/wiki/Directory_(computing) for more information.

From the `~` (current user) folder, type the commands that are in the above image of the shell:
* `cd Desktop` and then ENTER key
  * **NOTE:** You **must** include at least one space between cd and Desktop
* `ls` and ENTER key.

You should see the same files  that you saw listed in the File Explorer Window.

**Note:** You will see some files on the Desktop GUI that do not appear when you type `ls`.
That is because those files are not really stored on the Desktop,
but Windows displays them there to make it easier for the user.

Now use the command `ls -altr` to list all files (including hidden ones) in a detailed (long) form in order of modified date.  

Use the command `pwd` to *print working directory* to show the full path of the Desktop directory.  
Under MAC OS/Linux/Bash terminals, directory names are delimited with a forward slash `/`;
 under Windows, directory names are delimited with a back slash `\`.
For the curious, see [this article](https://www.howtogeek.com/181774/why-windows-uses-backslashes-and-everything-else-uses-forward-slashes/) .

Starting a the ``root`` or top level directory `/`,
we can `cd` into each directory in turn.  
Try it by first `cd`ing into the root folder by typing `cd /` and ENTER, then type `pwd`.  
You should be in the root folder denoted by `/`.  
From here, change into each sub-directory in turn according to the original path given by the first `pwd` command we used above.

 > NOTE: You will first have to change into the `c` folder (hard drive),
 > so your first change from root is `cd /c`.
 >  


Enter one directory name at a time `cd <directory name>`, then `pwd` to see the directory, and `ls -altr` to see the contents.  

**NOTE:** The convention `<directory name>` above indicates an optional or replacement name.  In this case, to change into the `users` sub-folder, you would enter `cd users`+ENTER.

If you `pwd` at this point, you should see `/c/users`.

> NOTE: After getting to `/c/users` you can jump to the current user folder using `cd ~` to avoid typing a long user name.


Do this `cd <directory name>` step by step until you return to the `Desktop` directory.

You can back up one directory by using `cd ..`.  Try it, `pwd`, and then return to the `Desktop` directory using `cd`.

You should have navigated the file structure via command line just as you did before using the File Explorer GUI.


**NOTE:** Although Windows does not care if you type "PCSE_user" or "pcse_user"
to log on, or "desktop" or "DEsKToP" for the Desktop folder,
most operating systems (including Mac) and most programming languages (including Python) will care.
They are **case-sensitive** meaning that UPPERCASE letters and lowercase letters are completely different.
In case sensitive operating systems,  you could have two files, one named a.txt, and other named A.txt,
and they could store completely different information,
and they would be unrelated to each other.
Windows ignores case in file and directory names,
but you should get used to paying attention to
whether a letter is UPPERCASE or lowercase.

#### Shortcuts
Wow! That is a lot of typing. There are two shortcuts that you should use a great deal in the bash shell:

First, bash shells allow you to use the tab key for file completion. Try this:
* Use git-bash shell to go to the pcse_user home directory.
  * Hint: The quick way is given above!
* Type `cd`, then a SPACE, the letters `D`, `e`, and finally the *TAB* key. The shell should automatically complete the file name to be Desktop if there are no other files that start with De in the the pcse_user directory.

**NOTE:** If there other `De` files or directories, then hitting TAB again will show a list of the possible options.  Just continue typing letters to *disambiguate* the name, then hit TAB to complete.

Second, bash shell remembers your previous commands. Type the UP arrow to see what your previous command was. Tap the enter key, and git-bash will execute your command again. Or, type the UP arrow key twice to see the two commands before.
Type the DOWN arrow to go to back.  
Using UP and DOWN arrays can help you quickly retrieve prior commands that you want to repeat.

**Make frequent use of the TAB File completion and UP/DOWN arrow command recall whenever you are in the bash shell.  It will save you much time!**.


## Questions to answer (on form)

1. What is another name for the CLI?
2. What is the full path to the `Desktop` directory? (as given in GitBash terminal)
3. What command do you use to back up one directory?
4. What is the full path to the directory above `Desktop`?

## Creating New directories

To create a directory, use the `mkdir` command in bash.

 You should have a folder for every class that you are taking, especially every Computer Science class.  
 You may choose to place the directories wherever you like (e.g. ``Documents`` or ``~``),
 but for today we will place a `cpsc250L` directory in the Desktop.

* Type `pwd` to make sure you are in the Desktop directory.
  * If not, go there using your `cd` commands.
* Type `mkdir cpsc250L`.
  * You should see a new folder icon appear on your desktop.
    * **NOTE:** Lab machines are special, and automatically delete any user created files or directories when you log out, so you won't see this folder the next time you log in.  
  * You should create a `cpsc250L` directory on your laptop to store all of your projects for labs, and a `cpsc250` directory for lecture.


## Optional Reading

The following is not part of the lab, but if provided to give you pointers for advanced learning.  This is material you should eventually master as part of your CS skill set before your graduate.

[Optional Reading](optional_bash.md)


**Use your browser back button to return to the main README.**
---------

[bashpic]: ../img/git_pic.png
[folderstructure]: ../img/folder_structure.png
