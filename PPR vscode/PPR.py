#%% Parallax
# Traitements preliminaires
input=open("/home/alpha/Documents/PPR/PPR vscode/gaia-dr2-allwise-2mass-ppmxl.csv",'r')
output=open("/home/alpha/Documents/PPR/PPR vscode/parallax_results.txt",'w')

title=input.readline()
title=title.strip('\n')
titles=title.split(',')

output.write("source_id\tparallax (mas)\tparallax_error(mas)\tdistance(pc)\tdistance_error (pc)\n")

# Automatisation
i=0 # compte les échecs
n=100 # nombre de lignes à lire, arbitraire

for _ in range(n):
    l=input.readline()
    id,par,perr,*_=l.split(',')

    par=float(par)+0.029 # erreur zero-point (-biais, biais=-0.029)
    f=abs(float(perr)/par) # calcul de la qualité
    dist=1/(par*1e-3) 

    if f<0.2 and dist>0:
        derr=dist*f # propagation de l'erreur
        output.write(f"{id}\t{par}\t{perr}\t{dist}\t{derr}\n")
    else:
        i+=1

output.close()
input.close()
print(f"Done. {i} errors over {n}: Success rate {1-i/n:.2f}")