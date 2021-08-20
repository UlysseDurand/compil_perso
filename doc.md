# Command syntax
Here is how to compile :
```
python3 [path to compile.py] [path to lgi file] [path to mdx file] [output language] [option1] [option2] ...
```
option1, option2, ... are optional.

# The options
option1, option2, ... make the option list.
You can start any line of your mdx or lgi file by |option| and the line will read by the program only if option is in the option list.

This is usefull for compiling in multiple languages, for example, if you have the following lines :
```
|fr| # Bonjour à tous
|en| # Hello everybody
```
with only fr as option, then the program will read 
```
# Bonjour à tous
```
(Why not using it for optional indications after an exercice, or for an optional non family friendly contents within your text)

# .lgi file format

It has a XML structure following the following XML Schema (xsd) :
```xsd
<xs:schema>
    <xs:element name="lgi">
        <xs:complexType>
            <xs:element name="header">
                <xs:complexType>
                    <xs:element name="aliases" type="string"<!--aliases code--> />
                    <xs:element name="commoncode" type="string"<!--python code--> />
                </xs:complexType]>
            </xs:element>
            <xs:element name="block" maxOccurs="unbounded">
                <xs:complexType>
                    <xs:attribute name="lang"/>
                    <xs:attribute name="fileout"/>
                    <xs:element name="code" type="string"<!--python code--> />
                    <xs:element name="beforemdx" type="string" />
                    <xs:element name="aftermdx" type="string" />
                </xs:complexType]>
            </xs:element>
        </xs:complexType>
    </xs:element>
</xs:schema>
```

# Compilation

The program executes the following tasks :
* executes commoncode from header
* takes the block with lang corresponding to the language argument in the command
* execute the block's code
* prints content of *beforemdx* from the block
* prints the compiled content of your mdx file according to aliases from header
* prints content of *aftermdx* from the block

## content of mdx file compiled

First, it prints the string returned by the python code between %.
With this you could, for example, within the commoncode, fetch and parse a json file, so in your mdx file you can have ```%data["title"]%```, which will print what is whithin the title key from the data dict. (Why not making HTML requests to an API or print the temperature).

Then, it changes the grammar of the mdx file according to aliases, here is how it works :

## aliases code

Let's use an example to illustrate (from maths.lgi).
```
3'^# (.*?)!n!' -> '\section{%1}!n!'
3'^---(.*)!n!---' -> '\begin{itemize}%1!n!\end{itemize}'
3'^#### (.*?)!n!' -> '\item %1!n!'
```

Each line in an aliases code is an alias, it takes the form of a number (0,1,2 or 3) followed by a regex expression within single quotes ```'``` and then there is an arrow``` -> ```with a string within single quotes.

The program uses the regex substitute function, taking a pattern, a subtitute, and optional flags as arguments.
It subtitutes your regex pattern with the right string, and replaces the %i by the content of the group number i from your regex pattern.

```!n!``` is a line break.

so you can imagine that with this aliases code, the following text1 will compile into text2 :

text1
```
# Definitions
---
#### A shovel is a stick with an iron part
#### An axe is a stick with an iron part
#### A sword is a stick with an iron part
---
```
<!-- Therefore, A shovel, an axe and a sword are the same. -->

text2
```
\section{Definitions}
\begin{itemize}
\item A shovel is a stick with an iron part
\item An axe shovel is a stick with an iron part
\item A sword is a stick with an iron part
\end{itemize}
```
And oh my, text1 is a lot clearer than text2 !