# Personnal Compiler
The program helps you to make a compiler from a custom language defined by yourself to some other language (like LaTeX or HTML), in the way you want it to be done.

## Recommendations
In order to help yourself, please consider making your custom language easy to read (something that looks like Markdown).

Also, there is a standard .lgi library, why not using it, either as an example, either as the base of your own *custom.lgi* file

## Requirements
You need to have Python3 installed.

## How to use it
* Express in the *custom.lgi* file how you want to compile your custom language according to the wiki. Note that in this file you can specify the way to compile toward multiple output languages (for example, LaTeX and HTML).
* Write your *document.mdx* file in your custom language.
* just run the following command :
```
./compilecustom [your .lgi file] [your .mdx file] [your output language]
```

### A friendly configuration
You can use your PATH environment variable, so you can compile your own langage anywhere.

And why not making the following file

*mdxtotex* :
```
./compilecustom custom.lgi $1 latex 
```

So in any folder you can run ```mdxtotex [a .mdx file]```, and it will compile your mdx file in latex according to your own custom language definition.

## Example
Here is an example of how to use this personnal compiler :

Filetree :
```
+-- README.md
+-- compilecustom
+-- custom.lgi
+-- document.mdx
+-- data :
|   + main.py
|   + std.lgi
```
[//]: # (TODO : FAIRE UN VRAI EXEMPLE)
