#%% Parallax
# Traitements préliminaires
f=open("/home/alpha/Documents/PPR/PPR vscode/gaia-dr2-allwise-2mass-ppmxl.csv",'r')
g=open("/home/alpha/Documents/PPR/PPR vscode/parallax_results.txt",'w')

title=f.readline()
title=title.strip('\n')
titles=title.split(',')

g.write("source_id\tparallax (mas)\tparallax_error(mas)\tdistance(pc)\tdistance_error (pc)\n")

# Automatisation

for i in range(100):
    l=f.readline()
    id,par,perr,*_=l.split(',')

    par=float(par)+0.029 # erreur zero-point (-biais, biais=-0.029)
    dist=1/(par*1e-3)
    derr=dist*abs(float(perr)/par) # propagation de l'erreur

    g.write(f"{id}\t{par}\t{perr}\t{dist}\t{derr}\n")

g.close()
f.close()
print("Done")

"""
Gaia at Lagrange L2: 1.01 au from sun-> 149597870700 m = 1 au
So in D=2d/alpha, 2d= 302187698814 m
def parsec=648 000/pi au
"""
