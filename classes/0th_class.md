# Programming Concepts & Logic.

In this course you will learn how to program computers with the programming 
language called _[Python](https://www.python.org/)_ (will be easy to pick up 
how to programming with it).

> Formally you will learn the _structured_ programming paradigm.

# Installation of Python programming language.

The course will be taught on the Python 3.8, but I recommend that you install 
the newest stable version, because — most probably — is better and also it
will can be compatible with this version: `python3.8`

## MacOS and Linux (UNIX based operating systems).
Probably has the Python installed. </br>

### Linux
- Use, in your terminal ─ `python --version` ─ to know wich is your Python 
version and, hence, if it is installed.

If it is not installed — please — perform this:

#### **On Debian and Debian based operating systems**

- Perform this commands on your terminal:
    - Replace the \<version> to the version number, _e.g._: `python3.8`

    ```bash
    $ sudo apt update
    $ sudo apt install python<version>
    ```

#### **On RedHat, CentOS...**

```bash
$ sudo yum install python
```

### On MacOS

Use, on a terminal, the command: `which python` if you receive a message like
`/usr/bin/python` means that you has the python installed.

Firtly install the [xCode](https://apps.apple.com/br/app/xcode/id497799835)
then install the _command line tools_ on a terminal.

```bash
$ xcode-select --install
```

Second the [pip](https://pypi.org/) ─ Python Package Index, a pack manager.
```bash
$ sudo easy_install pip
```
And update it.
```bash
$ sudo pip install --upgrade pip
```

And lastly the _brew_.
```bash
$ ruby -e "$(curl -fsSL https://raw.github.com/mxcl/homebrew/go)"
```
then the python itself.

```bash
$ brew install python3
```

## Windows.

1. Access the site of the Python programming language: https://www.python.org/
2. Download the executable (`.exe`) installer.
3. Install it.

# Basics

You will need a text processor such as [gedit](https://wiki.gnome.org/Apps/Gedit)
(Linux, MacOS, Windows), 
[TextEdit](https://support.apple.com/guide/textedit/welcome-txted6a660ee/mac) 
(MacOS) or 
[Notepad](https://www.microsoft.com/en-us/p/windows-notepad/9msmlrh6lzf3?activetab&activetab) 
(Windows).

On _Win_ you may use IDLE, it is installed with the programming 
language installer. Press the super key or click on the _Win_ icon on the 
taskbar and type "IDLE", then initialize it (it will open an interactive 
Python shell): in the menu bar choose `file > new file` to create and edit 
(write the code in) a file; to run the code go to `Run > Run Module` or 
press `F5` key (the shotcut).


## I will, and recommend to, use a _code_ editor such as [Brackets](http://brackets.io/) or [Codium](https://vscodium.com/)...

So, create a file and put in it the extension (means, after the dot):  _py_ </br>
_E.g._, `file_name.py`

# Observation

> Please note that, in this course, _you will learn how to program_, you 
> won't learn the aspects and advantages of Python programming language.

# To invoke the Python interpreter

Simply type `python` on the terminal.

# The Zen (philosophy) of Python...

```Python
import this     # Type this code, on Python shell, then you will get this text.
```

The Zen of Python, by Tim Peters.

Beautiful is better than ugly. </br>
Explicit is better than implicit. </br>
Simple is better than complex. </br>
Complex is better than complicated. </br>
Flat is better than nested. </br>
Sparse is better than dense. </br>
Readability counts. </br>
Special cases aren't special enough to break the rules. </br>
Although practicality beats purity. </br>
Errors should never pass silently. </br>
Unless explicitly silenced. </br>
In the face of ambiguity, refuse the temptation to guess. </br>
There should be one ─ and preferably only one ─ obvious way to do it. </br>
Although that way may not be obvious at first unless you're Dutch. </br>
Now is better than never. </br>
Although never is often better than *right* now. </br>
If the implementation is hard to explain, it's a bad idea. </br>
If the implementation is easy to explain, it may be a good idea. </br>
Namespaces are one honking great idea ─ let's do more of those!

# About me

I am Matheus Miranda an undergraduate student bachelor's in Computer Science.

That's my GitHub profile: [Jhynn](https://github.com/jhynn).
