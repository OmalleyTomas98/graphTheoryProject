
<p align="center"> 
<h1 align="center">Graph Theory NFA Builder </h1>
  
  <a href="https://github.com/github_username/repo">
    <img src="graphTheoryImages/googleCloud.jpg" alt="" width="1000" height="500">
  </a>
  
## Description
 <p align="left">
You must write a program in the Python programming language [2] that can
build a non-deterministic finite automaton (NFA) from a regular expression,
and can use the NFA to check if the regular expression matches any given
string of text. You must write the program from scratch and cannot use the
re package from the Python standard library nor any other external library.
<br />
</p>

| Header | Description |
| --- | --- |
| `Author` | Tomas O'Malley (G00361128)@gmit.ie |
| `Course` | Software Development GA_KSOAG_H08 Y3  |
| `Module` | Graph Theory  |
| `Program` | NFA Graph Theory Project|
| `Langauge` | Python 3|
| `Weighting` | 100% |
| `Year of Study` | 3 |


## Documentation
- A .pdf version of the document you are currently reading is currently avaiable in this Repo for offline use.
 
## Installation
 
- Download [git](https://git-scm.com/downloads) to your machine if not already installed.
- Download [python](https://www.python.org/downloads/) to your machine if not already installed.
_______________________________________________________________________________________________
- Open your systems CLI **Windows Command line** / **MAC OSX Terminal or Linux Terminal**
- Type the follow commands
- git clone  https://github.com/OmalleyTomas98/graphTheoryProject.git
- cd graphTheoryProject
- python3  menu.py


## Features

- Command line interface menu 
- Build a NFA to check a Regular Expression 
- Output whether a match or a mismatch


## Development
  | Header | Description |
| --- | --- |
| `Langauge` | Python 3  |
| `Editor` | Vi |
| `Enviroment` | Google Cloud Linux Debian CLI |



## Research
- **Python**
  - Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together. Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance. Python supports modules and packages
  
<p align="center"> 
 <a href="https://github.com/github_username/repo">
        <img src="graphTheoryImages/python.png" alt="" width="750" height="250">
  </a>
</p> 


    
- **Regular Expression**
  - A regular expression, regex or regexp is a sequence of characters that define a search pattern. Usually such patterns are used by string searching algorithms for "find" or "find and replace" operations on strings, or for input validation.There are are a large number of regex operators but I will just cover the operators used in my program.
  
   - The integrated common regular expressions in my program :
      
      
            -    Kleene Star   : *
            -    Or            : |
            -    Concatinate.  : .
            -    Example regular in match function of NFA program:
            ___________________________________________________________________
            -    print(match("a.b|b*", "bbbb")) = A and b or Many B's is = "bbb"
            -    Returns True in output
        
  
 
      
## Testing  
  - I conducted a series of short matching tests at the end of the development to determine if the Regular expression operators were working correctly. 
  
  - Here are the examples I tested in the Regex.py File
    ```py 
         tests = [
                         ["a.b|b*" , "bbbb" , True],
                         ["a.b|b*" , "bbxxb" , False],
                         ["a.b" , "ab" , True]

                 ]
      ``` 
  - All the test cases resulted in a pass clause after compiling the class and I was ready to finish the programs Development 
 
## Program Code  Structure
  - There a mulitple files included in this repository which came from adjusting to the python langauge and the google cloud VM enviroment. 
      - Menu.py : In the Menu file is where the program is executed from.It holds the menu system for the user to input a regular expresson + string and outputs the match/mismatch from the Regex.py file on fly as an import.
           ```py 
          import Regex
          
          UserRegex= input("Please enter a regular expression: e.g  (a.b|b*) : ")
          print("**********************************************************")
          s= input("Please enter a single string of text: e.g bbbb :")

          print("Match Result = " , Regex.match(UserRegex,s))
          ```

     

## Program Running
  - Underneath is a screenshot of the program running on my local machine 
<p align="center"> 
        <img src="graphTheoryImages/RunningProgram.png" alt="" width="750" height="250">
  </a>
</p> 


## Resources 

- The code Implemented/Tweaked was sourced from online vidoes delivered by Dr. Ian Mcloughlin which shaped the foundation to this project.


