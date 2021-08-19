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
+-- CV.mdx
+-- data :
|   +-- compile.py
|   +-- CV.lgi
|   +-- maths.lgi
```

then, run ```python3 data/compile.py data/CV.lgi CV.mdx latex en```

and a *document.tex* file will be generated.

## Showtime
Here is an example of what it can do :
with *maths.lgi* and the following mdx file :
```
# THEORIE GENERALE

## DETERMINANT DANS UNE BASE

### Notion de forme p-lineaire sur E.

L'application $\varphi:E^p \rightarrow \mathbb{K}$
 est {\it p-lineaire} si chacune des applications partielles
 est lineaire.

### Forme alternée, antisymétrique.

On suppose que $\varphi$ est une forme p-linéaire sur E.

---
#### Définitions

$\varphi$ est !balternée! si $\varphi$ s’annule sur tout système de p vecteurs contenant au moins
deux vecteurs égaux. On dit qu’elle est !bantisymétrique! si, à chaque fois que le système S'
est déduit du système S par permutation de deux vecteurs, on a : $\varphi(S')=-\varphi(S)$.

#### Propriétés

~~~
#### $\varphi$ alternée $\implies \varphi$ antisymétrique. Réciproque vraie si car $\mathbb{K}\neq 2$

#### $\varphi$ antisymétrique $\iff \forall \sigma \in S_p$, $\forall (x_1,\hdots,x_p) 
\in E^p, \varphi(x_{\sigma(1)},\hdots,x_{\sigma(p)})=\epsilon (\sigma).\varphi(x_1,\hdots,x_p)$.

#### $\varphi$ alternée $\iff \forall (x_1,\hdots,x_p)\in E^p, ((x_1,\hdots,x_p)$ 
lié $\implies \varphi (x_1,\hdots,x_p) = 0)$.
~~~
---

### !t!
Soit E de dimension n, et B une base de E. Il existe une unique forme n-
linéaire alternée $\varphi$ sur E valant 1 sur la base B. Par déﬁnition, $\varphi$ = det B . On a de plus la
formule :
!equ!\forall x \in E, det_B(x_1,\hdots,x_n)=\sum_{\sigma \in \mathcal{S}} 
\epsilon (\sigma).\varphi_{\sigma(1)}(x_1)\hdots \varphi_{\sigma(n)}(x_n).!equ!
où $(\varphi_1,\hdots,\varphi_n)$ est la pase duale de $(e_1,\hdots,e_n)$.
```
it produces the .tex file of this pdf : [https://github.com/ulyssedurand/compil_perso/blob/master/example/maths-doc.pdf].