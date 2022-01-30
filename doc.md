# Documentation

## Command syntax
Here is how to compile :
```
python3 [path to compile.py] [path to lgi file] [path to mdx file] [output language] [option1] [option2] ...
```
option1, option2, ... are optional.

## The options
option1, option2, ... make the option list.
You can start any line of your mdx or lgi file by |option| and the line will read by the program only if option is in the option list.

This is usefull for compiling in multiple languages, for example, if you have the following lines :
```
|fr| # Bonjour à tous
|en| # Hello everybody
```
with only fr as option, the program will read 
```
# Bonjour à tous
```
(Why not using it for optional indications after an exercice, or for an optional non family friendly contents within your text)

## .lgi file format

It has a XML structure following the following XML Schema (xsd) :
```xsd
<xs:schema>
    <xs:element name="lgi">
        <xs:complexType>
            <xs:element name="header">
                <xs:complexType>
                    <xs:element name="commoncode" type="string"<!--python code--> />
                </xs:complexType]>
            </xs:element>
            <xs:element name="block" maxOccurs="unbounded">
                <xs:complexType>
                    <xs:attribute name="lang"/>
                    <xs:attribute name="fileout"/>
                    <xs:element name="aliases" type="string"<!--aliases code--> />
                    <xs:element name="code" type="string"<!--python code--> />
                    <xs:element name="beforemdx" type="string" />
                    <xs:element name="aftermdx" type="string" />
                </xs:complexType]>
            </xs:element>
        </xs:complexType>
    </xs:element>
</xs:schema>
```

## Compilation

The program executes the following tasks :
* executes commoncode from header
* takes the block with lang corresponding to the language argument in the command
* execute the block's code
* prints content of *beforemdx* from the block
* prints the compiled content of your mdx file according to aliases from the block
* prints content of *aftermdx* from the block

### content of beforemdx, aftermdx and the mdx file compiled

It prints the string while executing the python code between '%'s. So ```The calculus gives %print(3**7,end='')%, that's huge !``` will print ```The calculus gives 2187, that's huge !```.
With this you could, for example, within the commoncode, fetch and parse a json file, so in your mdx file you can have ```%print(data["title"])%```, which will print what is whithin the title key from the data dict. (Why not making HTML requests to an API or read the temperature through a sensor).

Then, it changes the grammar of the mdx file according to aliases, here is how it works :

### aliases code

Let's use an example to illustrate (from maths.lgi).
```
3'^# (.*?)~n~' -> '\section{%1}~n~'
3'^---(.*)~n~---' -> '\begin{itemize}%1~n~\end{itemize}'
3'^#### (.*?)~n~' -> '\item %1~n~'
```

Each line in an aliases code is an alias, it takes the form of an integer (0,1,2 or 3) followed by a regex expression within single quotes ```'``` and then there is an arrow``` -> ```with a string within single quotes.

The program uses the regex substitute function, taking a pattern, a subtitute, and optional flags as arguments.
the flags combinations corresponding to the integers are the following :
- 0 : none
- 1 : multiline
- 2 : dotall
- 3 : multiline + dotall
It subtitutes your regex pattern with the right string, and replaces the %i by the content of the group number i from your regex pattern.

```~n~``` is a line break.
```~a~``` is a &.
```~p~``` is a %.

so you can imagine that with this aliases code, the following text1 will compile into text2 :

text1
```
# Few facts
---
#### I wanted to put a joke in here but I had no imagination

#### If you do have some imagination contact me at uldr@pm.me
---
```

text2
```
\section{Few facts}
\begin{itemize}
\item I wanted to put a joke in here but I had no imagination
\item If you do have some imagination contact me at uldr@pm.me
\end{itemize}
```
And text1 is a lot clearer than text2 !
