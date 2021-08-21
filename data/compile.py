import json
import re
import sys, os
import xml.etree.ElementTree as ET

lgifile = sys.argv[1]
mdxfile = sys.argv[2]
lang = sys.argv[3]
args = sys.argv[4:]

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
    s = re.sub("!a!","&",s)
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
            res+="\nprint("+splitted[i]+",end=\'\')\n"
    return res

def aliased(al,s):
    lines = al.split("\n")
    for line in lines:
        reg = re.search("(.)'(.*)' -> '(.*)'",line)
        if reg: 
            n,e1,e2 = reg.groups()
            e1 = re.sub("!n!","\n",e1)
            e2 = re.sub("!n!","\n",e2)
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

##### PARSING THE LGI FILE
lgistring = open(lgifile).read()
root = ET.parse(lgifile).getroot()

header = chercharbre(root,"header",[])
commoncode = chercharbre(header,"commoncode",[]).text
block = chercharbre(root,"block",[("lang",lang)])
aliases = chercharbre(block,"aliases",[]).text
fileout = block.attrib["fileout"]
code = chercharbre(block,"code",[]).text
beforemdx = chercharbre(block,"beforemdx",[]).text
aftermdx = chercharbre(block,"aftermdx",[]).text

tmp+=lesoptions(commoncode)

tmp+=lesoptions(code)

tmp+=stringtocodeprint(lesoptions(beforemdx))

tmp+=parse(aliased( lesoptions(aliases), lesoptions(open(mdxfile).read()) ))

tmp+=stringtocodeprint(lesoptions(aftermdx))


##### COMPILING EVERYTHING

open("tmp.py","w+").write(tmp)
os.system("python3 tmp.py "+" ".join(args)+" > "+fileout)
# os.system("rm tmp.py")