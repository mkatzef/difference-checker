# difference-checker

A tool for comparing two pieces of text. Written in Python, with a Tkinter GUI.

## Getting Started

This project consists of a single module.
* `DifferenceChecker.py` - The difference checking methods and the GUI class to use them.

### Prerequisites

To run difference-checker, the host machine must have the following installed:
* `Python3` - The programming language in which difference-checker was written. Available [here](https://www.python.org/).
* `Tkinter` - The Python library required for the difference-checker user interface.\*

\*Included with the standard Python3 installation on Windows and MacOS, requires separate installation on Linux. For Debian-based systems, this is achieved through the following command:
`apt-get install python3-tk`

### Running

The tool may be started by running the script as follows:
`python3 DifferenceChecker.py` 

### Use

Enter a passsage of text in each of the two text boxes before clicking on the "Check" button. The two pieces of text are checked for equality line-by-line (ignoring whitespace).

The result window shows the percentage of matched lines, and a line-by-line breakdown.

## Authors

* **Marc Katzef** - [mkatzef](https://github.com/mkatzef)
