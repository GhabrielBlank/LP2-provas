
# coding: utf-8

# In[105]:

tc = 29
QE = 12684
votos_partido={}
partidos= []
with open("eleicao.csv", encoding="utf-8") as f:
    f.readline()
    for line in f:
        line= line.split(";")
        partidos.append (line[2])


# In[106]:

set (partidos)


# In[107]:

for i in partidos:
    votos_partido[i] = 0


# In[114]:

pegar_valor = 0
with open("eleicao.csv", encoding="utf-8") as f:
    f.readline()
    for line in f:
        line= line.split(";")
        pegar_valor= votos_partido.get(line[2]) + int(line[3])
        votos_partido [line[2]] = pegar_valor
        


# In[115]:

print (votos_partido)


# In[117]:

QP= {}
for i in votos_partido:
    QP [i]= votos_partido.get(i)/ QE


# In[118]:

print (QP)


# In[ ]:

Media_partido= {}

