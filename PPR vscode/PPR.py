##%% Parallax
## Traitements preliminaires
#input=open("/home/alpha/Documents/PPR/PPR vscode/gaia-dr2-allwise-2mass-ppmxl.csv",'r')
#output=open("/home/alpha/Documents/PPR/PPR vscode/parallax_results.txt",'w')
#
#title=input.readline()
#title=title.strip('\n')
#titles=title.split(',')
#
#output.write("source_id\tparallax (mas)\tparallax_error(mas)\tdistance(pc)\tdistance_error (pc)\n")
#
## Automatisation
#i=0 # compte les échecs
#n=100 # nombre de lignes à lire, arbitraire
#
#for _ in range(n):
#    l=input.readline()
#    id,par,perr,*_=l.split(',')
#
#    par=float(par)+0.029 # erreur zero-point (-biais, biais=-0.029)
#    f=abs(float(perr)/par) # calcul de la qualité
#    dist=1/(par*1e-3) 
#
#    if f<0.2 and dist>0:
#        derr=dist*f # propagation de l'erreur
#        output.write(f"{id}\t{par}\t{perr}\t{dist}\t{derr}\n")
#    else:
#        i+=1
#
#output.close()
#input.close()
#print(f"Done. {i} errors over {n}: Success rate {1-i/n:.2f}")

#%%
from numpy import log10, log

n=2000
count=0

input=open("/home/alpha/Documents/PPR/cepheid_source.tsv",'r')
output=open("/home/alpha/Documents/PPR/results.txt",'w')

for _ in range(52): # la 53e est les premières données
    input.readline()

output.write("source_id\tdistance_parallax(pc)\tdistance_error_parallax (pc)\tdistance_cepheid\tdistance_error_cepheid\n")


for _ in range(n):
    line=input.readline().replace(' ','').strip().split(';')
    if line[16]=='DCEP_F':
        count+=1 # ouverture
        id=line[0]
        period,G,Gbp,Grp,parallax,errparallax=line[6:12]

        # Paralaxe
        parallax=float(parallax)+0.046 # celle adaptée selon ripepi p.4
        f=abs(float(errparallax)/parallax)
        pardist=1/(parallax*1e-3) 
        if f<0.2 and pardist>0:
            parderr=str(pardist*f)
            pardist=str(pardist)
        else:
            pardist='NULL'
            parderr='NULL'

        # Cepheide
        if float(period)<=1.0: # test: necessaire ?
            print(f"période faible pour le {count}è calcul.")
            #continue # on skippe ??

        M=-2.837-3.183*log10(float(period))
        m=float(G)-1.9*(float(Gbp)-float(Grp))

        cepdist=10**((m-M+5)/5)
        ceperr=0.2*log(10)*cepdist*0.011
        
        output.write(f"{id}\t{pardist}\t{parderr}\t{cepdist}\t{ceperr}\n")

input.close()
output.close()
print(count)