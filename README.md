# Personnal Compiler
The program helps you to make a compiler from a custom language defined by yourself to some other language (like LaTeX or HTML), in the way you want it to be done.

## Recommendations
In order to help yourself, please consider making your custom language easy to read (something that looks like Markdown).

Also, there is a standard .lgi library, why not using it, either as an example, either as the base of your own *custom.lgi* file

## Requirements
You need to have Python3 installed.

## How to use it
* Express in the *custom.lgi* file how you want to compile your custom language according to the wiki. Note that in this file you can specify the way to compile toward multiple output languages (for example, LaTeX and HTML).
To make the *custom.lgi* file, make sure to follow the [documentation](https://github.com/UlysseDurand/compil_perso/blob/main/doc.md)
* Write your *document.mdx* file in your custom language.
* just run the following command :
```
./compilecustom [your .lgi file] [your .mdx file] [your output language]
```
### Example

Filetree :
```
+-- README.md
+-- doc.md
+-- bin :
|   +-- compile
+-- example :
|   |document.mdx
+-- data :
|   +-- compile.py
|   +-- lgifiles :
|   |   +-- CV.lgi
|   |   +-- maths.lgi
```

then, run ```python3 data/compile.py data/lgifiles/maths.lgi example/document.mdx latex en```

(or ```./bin/compile maths example/document.mdx latex en```)

and the *maths-doc.tex* file will be generated.

### A friendly configuration
You can add bin to your PATH environment variable, so you can compile your own languages anywhere.

And add your own lgi files to the data/lgifiles folder.

## An example for the show
Here is an example of what it can do, 
with *maths.lgi* and the following mdx file :
```
|fr|# THEORIE GENERALE
|en|# GENERAL THEORY

|fr|## DETERMINANT DANS UNE BASE
|en|## DETERMINANT IN SOME BASIS

|fr|### Notion de forme p-lineaire sur E.
|en|### p-linear form on E.

|fr|L'application $\varphi:E^p \rightarrow \mathbb{K}$ est {\it p-lineaire}
|en|The $\varphi:E^p \rightarrow \mathbb{K}$ application is said to be {\it p-linear}
|fr|si chacune des applications partielles est lineaire.
|en|if and only if each of its partial functions is linear.

|fr|### Forme alternée, antisymétrique.
|en|### Alternated, antisymetric form

|fr|On suppose que $\varphi$ est une forme p-linéaire sur E.
|en|We will suppose that $\varphi$ is a p-linear form on E.
---
|fr|#### Définitions
|en|#### Definitions

|fr|$\varphi$ est !balternée! si $\varphi$ s’annule sur tout système de p vecteurs contenant au moins
|fr|deux vecteurs égaux. On dit qu’elle est !bantisymétrique! si, à chaque fois que le système S'
|fr|est déduit du système S par permutation de deux vecteurs, on a : $\varphi(S')=-\varphi(S)$.

|en|$\varphi$ is !balternated! if $\varphi$ is null on any system of p vectors which contains at least
|en|two equal vectors. It is said to be !bantisymetric! if, when the S' system is the S system but
|en|with two permutated vectors we have : $\varphi(S')=-\varphi(S)$.

|fr|#### Propriétés
|en|#### Properties

~~~
|fr|#### $\varphi$ alternée $\implies \varphi$ antisymétrique. Réciproque vraie si car $\mathbb{K}\neq 2$
|en|#### $\varphi$ alternated $\implies \varphi$ antisymetric. true reciprocal if car $\mathbb{K}\neq 2$

#### $\varphi$ 
|fr|antisymétrique
|en|antisymetric
$\iff \forall \sigma \in S_p$, $\forall (x_1,\hdots,x_p) 
\in E^p, \varphi(x_{\sigma(1)},\hdots,x_{\sigma(p)})=\epsilon (\sigma).\varphi(x_1,\hdots,x_p)$.

#### $\varphi$ 
|fr|alternée
|en|alternated
$\iff \forall (x_1,\hdots,x_p)\in E^p, ((x_1,\hdots,x_p)$
|fr|liée
|en|linearly dependant
$\implies \varphi (x_1,\hdots,x_p) = 0)$.
~~~
---

### !t!
|fr|Soit E de dimension n, et B une base de E. Il existe une unique forme n-
|fr|linéaire alternée $\varphi$ sur E valant 1 sur la base B. Par déﬁnition, $\varphi$ = det B . On a de plus la
|fr|formule :
|en|let E be a vector space of dimension n, and B be a basis of E. There exists a unique n-linear alternated form
|en|$\varphi$ on E which evaluates to 1 on the B basis. By definition, $\varphi$ = det B.
|en|Moreover, we deduce the following formula.
!equ!\forall x \in E, det_B(x_1,\hdots,x_n)=\sum_{\sigma \in \mathcal{S}} 
\epsilon (\sigma).\varphi_{\sigma(1)}(x_1)\hdots \varphi_{\sigma(n)}(x_n).!equ!
|fr|où $(\varphi_1,\hdots,\varphi_n)$ est la base duale de $(e_1,\hdots,e_n)$.
|en|where $(\varphi_1,\hdots,\varphi_n)$ is the dual basis of $(e_1,\hdots,e_n)$.
```
with the "fr" option, it produces the .tex file of this pdf : https://github.com/ulyssedurand/compil_perso/blob/master/example/maths-doc.pdf.
