#%% Parallax
# Opening and first line
f=open("gaia-dr2-allwise-2mass-ppmxl.csv",'r')
g=open("parallax_results.txt",'w')

title=f.readline()
title=title.strip('\n')
titles=title.split(',')

g.write(titles[0]+"\t"
        +titles[1]+"(mas)\t"
        +titles[2]
        +"\tdistance(m)\tdistance(pc)\n")

# Automation

for i in range(100):
    l=f.readline()
    id,par,err,*_=l.split(',')

    err=err # To be precised
    dist=str(2.02/(float(par)*1e-3))

    g.write(id+"\t"+par+"\t"+err+"\t"+dist+"\n")

g.close()
f.close()

"""
Gaia at Lagrange L2: 1.01 au from sun-> 149597870700 m = 1 au
So in D=2d/alpha, 2d= 302187698814 m
def parsec=648 000/pi au
"""

#%%
