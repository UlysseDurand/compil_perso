# compil_perso
Projet pour compiler d'un language perso vers du latex/html

## Objectif :
On aimerait faire notre propre markdown, qui s'adapterait très bien à comprendre du JSON et à écrire en LaTeX ou HTML.

## Idée / Structure :
On aurait un fichier principal ```main.mdinv``` décomposé en deux parties séparées par une ligne de ```?```.
- La première partie serait une partie d'"initialisation", c'est à dire qu'elle permettrait de pouvoir initialiser des variables qui seront utiles par la suite, et d'éxécuter des commandes de début.
- La deuxième partie sera le corps, c'est ce qui sera affiché par LaTeX ou HTML, des commandes pouront être utilisées grâce au symbole % afin de substituer du texte modulable, plus complexe, généré par le code.

### Variables
Les variables seront d'un type OCaml 
```
type var = S of str | J of str | L of str | H of str
```
S désigne une chaîne de caractères,
J désigne une arborescence (en fait un arbre où les noeux sont des chaînes de caractères, ce qu'on a avec un fichier JSON),
L désigne le contenu d'un fichier en languinv (on en reparlera par la suite),
et H désigne une chaîne de caractère importante, qui sera utile dans les métadonnées (auteur, date, titre, etc...).

### Commandes
Les commandes seront là pour insérer un type particulier de contenu.
Dans la partie initialisation, une ligne correspond à une commande de comprise.
Dans la partie de corps, une commande sera interprétée si elle est entourée à gauche par %_ et à droite par %.
Il y a plusieurs commandes :

Les commandes de définition de variable : 
- [a] = "[b]" -> interprété en OCaml par ```let a = S("[b]")```
- [a] = [b].json -> interprété en OCaml par ```let a = parse_json("[b].json")```
- [a] = [b].languinv -> interprété en OCaml par ```let a = read_text("[b].languinv")```
- [a] : [b] -> interprété en OCaml par ```header.("a") <- "b"```

Les commandes d'écriture :
De base il ne devrait y en avoir qu'une seule : 
- affiche([a],[b]) avec [a] = L(codelanguinv), [b] = X(arb_json) -> affiche ce que dicte le code en languinv, en prenant en paramètre l'arbre JSON.
Mais d'autres un peu trop basiques étaient nécessaire, nous verrons par la suite qu'elles sont dérivées de la commande affiche() :
- a([a]) affiche [a] (potentiellement une variable).
- b([a]) affiche [a] en gras
- i([a]) affiche [a] en italique
- u([a]) affiche [a] souligné
- ln([a],[b]) fait un lien cliquable, le lien est [b] et c'est [a] qui est le lien, et [b] le texte affiché.

### LanguInv
Pour languinv, il y a la même histoire de partie d'initialisation et de partie de corps.
Le corps est séparé en blocs commençant par un en-tête ?????[a] où [a] désigne un language vers lequel on pourrait compiler.
Dans le bloc, on fait une fonction qui à partir de notre entrée JSON, ressort une chaîne de caractères (correspondant à ce que l'on veut sortir).
Les %[a]% seront replacés par le résultat du parcours [a] dans l'arborescence JSON. Ce résultat se doit d'être une feuille
Les %?[a}?% seront remplacés par l'execution du code OCaml [a].
Dans ce dernier, on a accès à l'arborescence JSON par la variable input : JSON.
Le parcours se fat via la commande parse_json(input,[b]) où b désigne un parcours dans l'aborescence.

### un petit exmeple de la commande affiche()

On pourait utiliser la fonction affiche pour écrire du texte en gras, comme dans l'exemple de codelanguinv suivant :
```
?????html
<b>"%0%"</b>
?????LaTeX
\textbf{%0%}
```
Alors, %_b("du texte")% est équivalent à %_affiche(gras.languinv,"du texte")%.



## Un exemple complet :
On aimerait pouvoir compiler un CV (ligne par ligne) qui s'apparente à du Markdown, accompagné de fichiers JSON :

```
var_age = "20"
var_fichier = infos_CV.json

var_affichages = affichages.languinv

auteur : Ulysse DURAND
titre : CV d'infomatique

?????

Bonjour,
Je m'appelle Ulysse et j'ai %_aff(var_age)% ans.

je cherche actuellement à être admis à une école normale supérieure dans le département d'informatique.

# Mon parcours :
%_affiche(var_affichages?liste-date-entree,var_fichier?parcours)%

# Mes projets persos : 
%_affiche(var_affichages?projets,var_fichiers?projets)%

# Formations complémentaires et concours :
%_affiche(var_affichages?liste-date-entree,var_fichier?concours)%

#Compétences :
%_affiche(var_affichages?skills,var_fichier?skills)%

#Divers : 
%_affichage(var_affichages?liste-date-entree,var_fichier?miscl)%
```

Avec comme début de fichier infos_CV.json :
```
<parcours>
	<> <f>2019-2021</f><f>MPSI, MP*, Lycée Blaise Pascal, Clermont-Ferrand, option informatique.</f> </>
	<> <f>2019</f><f>Baccalauréat, S-SI option mathématiques, mention très bien.</f>
</parcours>
```
Et comme début de fichier affichages.languinv :

```
let concaten_ar_str ls = 
	Array.of_list (
		List.fold_right
			(fun a b -> a^b)
			""
			ls
	)
-----
<liste-date-entree>

?????LaTeX
fun input -> concaten_ar_str (List.map (fun (a,b) -> "\cvitem{"^a^"}{"^b^"} ") input)
?????HTML
fun input -> "<table>"^concaten_ar_str (List.map (fun (a,b) -> "<tr><td>"^a^"</td><td>"^b^"</td></tr>") input)^"</table>"

<liste-date-entree/>
```

## Possibles amélioration futures :
- Ajouter une commande de définition Alias telle qu'en appelant au début ```gras = gras.languinv``` puis ```Alias gras [a] avec a du regex 
