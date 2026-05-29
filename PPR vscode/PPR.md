[Papier officiel de la mission Gaia](https://www.aanda.org/articles/aa/full_html/2018/08/aa32727-18/aa32727-18.html#S17)
# Parallax
[source dataset csv](https://www.kaggle.com/datasets/solorzano/783k-gaia-dr2-stars)

## precision inquiries
[on parallax precisions and possible errors (10pc sample compilation)](https://www.aanda.org/articles/aa/full_html/2021/06/aa40985-21/aa40985-21.html)

[on the true bayesian method and the shortcomings of other ones, ie incertitudes de la paralaxe](https://www.aanda.org/articles/aa/abs/2018/08/aa32964-18/aa32964-18.html)

> l'approche bayésienne est probabiliste.

On devrait etre + precis sur prblms pr ca, car tt le reste se calibre a parallax

Gaia DR2 article calcule l'erreur moyenne de la parallaxe et retient un décalage de $− 0.029\, mas\approx -0.03\,mas$ *(5.2 Parallax zero point)*. On applique dc cette correction dans le code.

## propagation erreur
Vérifier avec roueff

On a une formule de type $d=\frac{cte}\varpi$. Ainsi on peut propager l'erreur avec :

$$
\frac{\sigma_\varpi}{\varpi}=\left|\frac{\sigma_d}{d}\right| \Longrightarrow
\sigma_d=d\left|\frac{\sigma_\varpi}{\varpi}\right|
$$

vient de 

$$
dw=cte \Leftrightarrow \partial (dw)=0 \Leftrightarrow d\partial w=|-w\partial d|
$$

un ecart type (sigmea est +) (racine d'un carré). remplace $\partial$ par $\sigma$

## Formula and units for python
old notes, to format

>- Gaia at Lagrange L2: 1.01 au from sun-> 149597870700 m = 1 au
>- So in D=2d/alpha, 2d= 302187698814 m
>- def parsec=648 000/pi au

1. We know: 
   
$pc\Rightarrow$ parsec ; $au\Rightarrow$ astronomical unit *(distance earth-sun)*

$$
1 pc := \frac{648\ 000}{\pi} au 
$$

# Candle
> voir pdf

## céphéide variable
[Las cumbres observatory, distance modulus](https://lco.global/spacebook/distance/cepheid-variable-stars-supernovae-and-distance-measurement/)

[Pépite: article sourcé avec papiers](https://ned.ipac.caltech.edu/level5/Sept11/Freedman/Freedman3.html) saved to pdf but better online for sources

1. dét lien entre **période** et luminosité totale par parallaxe
2. utiliser lien pr distance lointaine.

voir 2 pdfs, général et pr gaia
## Supernovae 1a
> encore autre chose ?

# effet doppler
> on oublie ? Faisons choses bien !