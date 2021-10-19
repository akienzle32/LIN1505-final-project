# LIN1505-final-project

This was my final project for a computational linguistics class (LIN1505) that I took in Fall 2019 at the University of Toronto, taught by Barend Beekhuizen. Put very simply, the program, written in Python and employing the spaCy dependency parser, extracts sentences featuring verbs of particular lexical classes in a syntactic context of interest from the Corpus of Contemporary American English and writes them out to a .txt file. For the project, I was interested in the syntactic alternation seen in (1)-(2). 

(1) Henry cleared all the dishes from the table.  
(2) Henry cleared the table of all the dishes.

For two distinct sets of verbs, the program extracts all such sentences and produces a file that tallies and records every hit of type (1) and (2). Ensuring that the program only extracted sentences with the right syntax was the main hurdle to overcome in writing this script. Considering that this was the first program of more than 20 or so lines that I had written from scratch, it's possible that the script could be made more elegant (and conform more to coding conventions). But in the end the program worked nicely, and because of time constraints my main goal was functionality. If you'd like to read a more detailed description of the motivation behind the project, please see the abstract included in this repository. 
