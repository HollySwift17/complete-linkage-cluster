import sys
import pandas as pd
import math


def complete_cluster(q):     
    clusters = []    
    while(True): 
        f = []
        minm = q[0][1]
        z,y = 0,1
        for i in range(len(q)): 
            for j in range(len(q)): 
                if(i !=j ): 
                    if(min(minm, q[i][j]) != minm): 
                        minm = q[i][j]
                        z= i 
                        y = j
        t = []
        t.append(files[min(z,y)])
        t.append(files[max(z,y)])        
        
        clusters.append(t)
         
        files.remove(files[max(z,y)])
        for i in range(len(q)):     
            if(i == max(z,y)):         
                continue
            else: 
                t = []
                for j in range(len(q)): 
                    if(j == max(z,y)): 
                            continue
                    else: 
                        if( j == min(z,y) and i != min(z,y)):                     
                            t.append(max(q[i][z],q[i][y]))
                            continue
                        if( i == min(z,y) and j != min(z,y)):                         
                            t.append(max(q[z][j],q[y][j]))
                            continue

                    t.append(q[i][j])                         
                f.append(t)
        q = f
        if(len(f) == k): 
            break
    return clusters


def histogram(text, chars): 
    dic = {c: 0 for c in chars}
    for x in text: 
        if x in chars: 
            
            dic[x] = dic[x] + 1        
    return {x: dic[x]/sum(dic.values()) for x in dic}                        


def euclidean_distance(files): 
    q = []
    for i in range(len(files)):
        t  = []
        index = 0
        while(index < len(files)): 
            temp = 0
            for l in letters:             
                temp = temp + (A.loc[files[index]][l] - A.loc[files[i]][l])**2
            index = index + 1        
            t.append(math.sqrt(temp))
        q.append(t)
    return q


pos_k = sys.argv.index('-k')
files = sys.argv[1:pos_k]
k = int(sys.argv[pos_k+1])
letters = sys.argv[pos_k+3:]


A = pd.DataFrame(index = files, columns = letters, dtype= float)
for F in files:  
    with open(F, encoding = "utf-8") as f:         
        text = f.read().lower()
        A.loc[F] = histogram(text, letters)


q = euclidean_distance(files)
clusters = complete_cluster(q)

c = []
soc = []      
for t in clusters:        
        if any(t[0] in s for s in files):            
            if any(t[0] in soc[j] for j in range(len(soc))):
                for v in range(len(soc)): 
                    if(t[0] == soc[v][0]): 
                        soc[v].append(t[1])                                                
            else: 
                soc.append(t)                 
            for e in c:                     
                for v in range(len(soc)): 
                    if(e[0] in soc[v]): 
                        soc[v].append(e[1])                        
                        c.remove(e)
        else: 
            c.append(t)

FF = files[:]
for c in soc:
    for z in c: 
        try: 
            FF.remove(z)
        except: 
            pass
for i in FF: 
    soc.append([i])

print(A.round(2))
for f in range(len(files)): 
    for i in range(len(soc)):                 
        if files[f] in soc[i]: 
            print(f, end = ' ')
            for j in soc[i]:
                print(j , end = ' ')
            print(end = '\n')
