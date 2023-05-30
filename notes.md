# Thoughts on VSCode and Python

## Disclaimer


__Note: I've been programming for a long time, and until vsCode came along, there have been no IDEs that have been customizable enough and easy enough to use to warrant exploration. Because of this, I'm extremely used to programming using just a text editor, and this may introduce bias into these notes.

My concern is that trying to learn vsCode as well as Python may be more trouble than it is worth. Sighted people don't really need to learn a code editor; it's all laid out visually for them. Screen reader users, however, need to learn how to minimize distractions, convince the editor to help without causing undue distraction or confusion, etc.  To this end, there is a fair amount of configuration that needs to happen to make this more comfortable for screen reader users. My advice would be to read these notes, and decide whether it is worth it. Most sighted people will be using an IDE of some kind, probably idol, the one built into Python, which is 100% inaccessible. However, I think it might be better to at least consider using a text editor like notepad, and the command line rather than possibly fighting with vsCode.  Again, however, this position might be biased, so the decission must be yours.__


## Version

I'd recommend downloading and installing the vsCode insiders build. It tends to have better accessibility support. Download from:

- https://code.visualstudio.com/insiders/#

I'm currently using:

>Version: 1.79.0-insider (user setup)
Date: 2023-05-20T01:18:53.811Z



## Concepts

There are two basic elements to vsCode's interface: editors, and views. Editors are where you edit program source, document source, and vsCode settings. Views are display components which contain things like a file explorer (similar to windows explorer), a terminal, debugger, etc.

You can have many editors and views on screen at once, but as I discuss later, as a screen reader user I highly suggest paring things down as much as possible to focus on at most one editor, and perhaps one view. The editor may contain more than one file, for example it's nice to be able to edit source code and unit tests together. 

## Keys you should know

- alt+f1 gets you accessibility info for the view your currently in!
- control+tab and control+shift+tab moves forwards / backwards among editors in current group
- tab
   + in editor indents (especially useful in python editors and markdown editors)   
   + in non-editor views moves among controls
- f6 and shift+f6 moves forward / backwards among "parts" of the interface
   + part is usually an editor, or open view such as a terminal or debugger
- control+f4 closes a view or editor
- alt+f4 closes vsCode
- f1 opens command pallet
    + an exhaustive list of command where up / down navigate
    + type to filter, then up / down to see filtered results
    + key bindings are included at the end of the command name


A quick overview of all accessibility features (worth a read) is at:

- https://code.visualstudio.com/docs/editor/accessibility

## Initial setup

vsCode is extremely powerful, and customizable. It allows many different styles of use and is almost infinitely configurable. What follows are just my suggestions as a screen reader user, so you may find that these do not meet your needs. If so, then you have many options, but you must explore to find what works best for you and your way of working.

### Focus

When using a screen reader, especially when using spoken output, it is, in my opinion, very helpful to focus on one task at a time, and switching contexts should be easy, and well defined. For me, this means, among other things:

- having only one editor on screen at a time
- having only one terminal, or debugger on screen at any one time
- having as few other vsCode views open as necessary

My suggestion, therefore, is to explore the view menu ( press alt+v ) and turn off everything except a terminal, and one editor.

- go into the view menu
- open the "appearance" submenu
   + turn off all the sidebar stuff
    + turn off full screen
    + turn off status bar and activity bar
    + be sure "zen mode" is not enabled
    + minimap and breadcrumbs should be unchecked
    + "panel" should be checked ( this is where your terminal will appear )
    + whitespace should be checked
- go into the "editor layout" submenu
    + press enter on "single"
- press enter on "terminal" in the main view menu

Now you have two working areas: the editor (which may contain more than one file), and the terminal.

- press f6 to move among workspaces (i.e. between terminal and editor in this configuration)
- press control+tab to move among files in the editor
- when in termian, press shift+tab to move into the output buffer and use arrows to explore it
   + press tab again to get back to your terminal command line




## Editor

There are some good things about using vsCode, but there are many pitfalls and annoyances, especially for screen reader users.

### Errors

VSCode will signal an error with an audible signal. However, because it is continually checking the code on each keystroke, you may hear error signals as you are typing due to the fact that you haven't actually finished what your typing yet! This can be annoying and confusing.

If you do hear an error signal and have finished and need to know what the error complaint is, 

- move to the beginning of the line where the error signal sounds
- press f8

To get a list of all audible cues and their meanings:

- press f1 to get into command pallet
- type audio and press enter


## Indentation

Python requires proper indentation. For me, who is used to free-formatted languages like javascript, lisp, and C, this insistance on indentation is a real annoyance. It will also be the cause of many errors, especially as you learn the language and the code editor.

You need to setup your screen reader to report line indentations. Both Jaws and NVDA can do this.

Using NVDA, do:

- NVDAKey+control+d to enter document formatting settings
- tab to "line indentation" and change setting with arrows

You can set a keyboard shortcut to change this setting:

- press nvdaKey+n to enter settings menu
- arrow to preferences and press right arrow to open submenu
- arrow to "input jestures" and press enter
- press the letter "d" to find the "document formatting" settings and right arrow to open submenu
- find "line indentation" and press tab
- press enter on "add" and then press a shortcut (including modifiers); I use control+i
- arrow to choose scope (either all keyboards, or desktop only, or laptop only) and press enter

Explore these input jestures; there is lots of customization to be had there.

## Tools recommended by 6.010

- [Installation and intructions for 6.010 tools](https://py.mit.edu/spring23/info/infrastructure)
- [Introduction to linux command line (needed for submiting labs in 6.010)](  https://py.mit.edu/spring23/readings/command_line)

## Project to play with

This project comes from the 6.010 programming self diagnostic page:

-    https://py.mit.edu/spring23/diagnostic

THis page is not very accessible, and I've already reported that issue, so hopefully they will fix it before the summer is over. However, I have written my own version of the program along with unit tests and was able to successfully submit it and got a passing grade, which means it passes all of their tests. 




## Testing

Unit testing will be an important aspect of the course. VSCode makes it fairly easy to test python code, but you need to get setup first.

### Configuring plugin

- be sure pytest is installed in your python interpreter
- type f1 to enter command pallet
- type "settings ui" and press enter
- type "pytest enable" in the search and press downArrow
- arrow around to find "pytest enabled" and press tab
- check it with spacebar
- arrow till you find "unittest enabled"
- press tab and be sure this is unchecked
- control+f4 to close

