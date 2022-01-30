import json
import re
import sys, os
import xml.etree.ElementTree as ET

lgifile = sys.argv[1]
mdxfile = sys.argv[2]

args = sys.argv[3:]

root = ET.parse(lgifile).getroot()
leslangs = []
outfiles = []

for e in root:
    if e.tag=="block" and ("lang" in e.attrib):
        leslangs.append(e.attrib["lang"])
    if e.tag=="block" and ("fileout" in e.attrib):
        outfiles.append(e.attrib["fileout"])

arguments = {}
for i in range(len(args)):
    if args[i][0] == '-' and i<len(args)-1:
        arguments[args[i][1:]] = args[i+1]

lang = leslangs[0]
outfile = outfiles[0]

if "l" in arguments:
    lang = arguments["l"]

if "o" in arguments:
    outfile = arguments["o"]

if "lgi" in arguments:
    lgifile = arguments["lgi"]

tmp = ""
lflgs = re.MULTILINE|re.DOTALL

def chercharbre(t,s,l):
    for e in t:
        if e.tag==s:
            val = True
            for a,b in l:
                if a in e.attrib and e.attrib[a] != b:
                    val = False
            if val:
                return e

def lesoptions(s):
    for e in args:
        s = re.sub("^\|"+e+"\|","",s,flags=lflgs)
    s = re.sub(r"^\|[^\|]*\|.*?\n","",s,flags=lflgs)
    s = re.sub("~a~","&",s)
    return s

def lescape(s):
    toescape = [(r'\\',r'\\\\'),("'",r"\\'"),('"',r'\\"'),('\n',r'\\n'),('\r',r'\\r'),('\t',r'\\t'),('\b',r'\\b'),('\f',r'\\f')]
    for carac in toescape:
        s = re.sub(carac[0],carac[1],s)
    return s

def stringtocodeprint(s):
    return "\nprint(\""+lescape(s)+"\",end=\'\')\n"

def parse(s):
    res = ""
    splitted = s.split("%")
    for i in range(len(splitted)):
        if i%2==0:
            res+=stringtocodeprint(splitted[i])
        else:
            res+=splitted[i]
    return res

def aliased(al,s):
    lines = al.split("\n")
    for line in lines:
        reg = re.search("(.)'(.*)' -> '(.*)'",line)
        if reg: 
            n,e1,e2 = reg.groups()
            e1 = re.sub("~n~","\n",e1)
            e2 = re.sub("~n~","\n",e2)
            n = int(n)
            fl = 0
            if n==1:
                fl = re.MULTILINE
            elif n==2:
                fl = re.DOTALL
            elif n==3:
                fl = re.MULTILINE|re.DOTALL
            e2 = lescape(e2)
            trucs = ["\\0","\\1","\\2","\\3","\\4","\\5","\\6","\\7","\\8","\\9"]
            for i in range(10):
                e2 = e2.replace("%"+str(i),trucs[i])
            s = re.sub(e1,e2,s,flags=fl)
    return s

def pourcent(s):
    return re.sub("~p~","%",s)

##### PARSING THE LGI FILE
lgistring = open(lgifile).read()

header = chercharbre(root,"header",[])
commoncode = chercharbre(header,"commoncode",[]).text
block = chercharbre(root,"block",[("lang",lang)])
aliases = chercharbre(block,"aliases",[]).text
code = chercharbre(block,"code",[]).text
beforemdx = chercharbre(block,"beforemdx",[]).text
aftermdx = chercharbre(block,"aftermdx",[]).text

tmp+=lesoptions(commoncode)

tmp+=lesoptions(code)

tmp+=pourcent(parse(lesoptions(beforemdx)))

tmp+=pourcent(parse(aliased( lesoptions(aliases), lesoptions(open(mdxfile).read()) )))

tmp+=pourcent(parse(lesoptions(aftermdx)))


##### COMPILING EVERYTHING

open("tmp.py","w+").write(tmp)
os.system("python3 tmp.py "+" ".join(args)+" > "+outfile)
os.system("rm tmp.py")