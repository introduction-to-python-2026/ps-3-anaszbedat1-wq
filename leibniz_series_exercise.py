def approximate_pi (n_terms):
leibniz_sum = 0
for n in range(n_terms):
leibniz_sum += (-1)**n/ (2*n+1)
return
4 * leibniz_sum
