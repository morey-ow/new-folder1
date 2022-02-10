
#%%
import mpmath

#%%
var('y')
L = lcalc.zeros_in_interval(10,50,0.1)
@interact
def _(n=(100,(60,10^3))):
   P = plot(prime_pi,n-50,n, color='black', legend_label=r'$\pi(x)$')
   P += plot(Li,n-50,n, color='green', legend_label='$Li(x)$')
   G = lambda x: sum([mpmath.li(x^(1/j)) * moebius(j)/j for j in [1..3]])
   P += plot(G,n-50,n, color='red', legend_label = r'$\sum_{j=1}^{%s} \frac{\mu(j)}{j} Li(x^{1/j})$'%3)
   F = lambda x: sum([(mpmath.li(x^(1/j))-log(2) + numerical_integral( 1/(y*(y^2-1)*log(y)), x^(1/j),oo)[0] )*moebius(j)/j for j in [1..3]]) - sum([(mpmath.ei(log(x)*((0.5+l[0]*i)/j)) + mpmath.ei(log(x)*((0.5-l[0]*i)/j))).real for l in L for j in [1..3]])
   P += plot(F,n-50,n,color='blue', legend_label='Really good estimate',plot_points=50)
   show(P)
# %%
