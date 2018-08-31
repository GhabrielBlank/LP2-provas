
# coding: utf-8

# In[245]:

tc = 29
QE = 12684
votos_partido={}
partidos= []
candidatos= {}
with open("eleicao.csv", encoding="utf-8") as f:
    f.readline()
    for line in f:
        line= line.split(";")
        partidos.append (line[2])
        candidatos [line[1]]= line[3]


# In[246]:

partido_candidatos = partidos
set (partidos)


# In[247]:

for i in partidos:
    votos_partido[i] = 0


# In[248]:

pegar_valor = 0
with open("eleicao.csv", encoding="utf-8") as f:
    f.readline()
    for line in f:
        line= line.split(";")
        pegar_valor= votos_partido.get(line[2]) + int(line[3])
        votos_partido [line[2]] = pegar_valor
        


# In[249]:

print (votos_partido)


# In[250]:

QP= {}
for i in votos_partido:
    QP [i]= votos_partido.get(i)/ QE


# In[251]:

print (QP)


# In[252]:

Media_partido= {}
for i in votos_partido:
    Media_partido [i] =  votos_partido.get(i)/ (QP.get(i)+1)


# In[253]:

vaga_partido={}
for i in partidos:
    vaga_partido[i] = 0


# In[254]:

import operator
dono_cadeira=""
dono_cadeira = max(Media_partido.items(), key=operator.itemgetter(1))[0]


# In[255]:

vaga_partido


# In[256]:

cadeiras=[""] *29
cont= 0
for a in cadeiras:
    dono_cadeira =max(Media_partido.items(), key=operator.itemgetter(1))[0]
    vaga_partido[dono_cadeira] = vaga_partido.get(dono_cadeira)+1
    Media_partido [dono_cadeira] = Media_partido.get(dono_cadeira)/ (QP.get(dono_cadeira)+vaga_partido.get(dono_cadeira)+1)
    vaga_partido[dono_cadeira] = vaga_partido.get(dono_cadeira)


# In[257]:

vaga_partido


# In[258]:

teste = ""
funfa = {}
for a in vaga_partido:
    if vaga_partido.get(a) !=0:
        funfa[a] = vaga_partido.get(a)


# In[259]:

funfa


# In[260]:

import pandas as pd
from collections import OrderedDict
from datetime import date


# In[261]:

labels = ["num", "nome", "colig", "votos"]
teste = pd.DataFrame()


# In[262]:

teste


# In[263]:

sera=[]
vai=[]
da=[]
certo=[]
with open("eleicao.csv", encoding="utf-8") as f:
    f.readline()
    for line in f:
        line= line.split(";")
        for key in funfa:
            if line[2]==key:
                sera.append(line[0])
                vai.append(line[1])
                da.append(line[2])
                certo.append(int(line[3]))


# In[264]:

teste["num"]=sera


# In[265]:

teste["nome"]=vai


# In[266]:

teste["col"]=da


# In[267]:

teste["votos"]=certo


# In[268]:

teste.sort_values("votos", inplace=True, ascending=False)


# In[269]:

teste


# A partir deste ponto não sei mais como mexer para organizar. Vou procurar mais
#             

# In[ ]:



