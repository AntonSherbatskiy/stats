from data import *
from func import *
from console_interface import console_interface as ci
import os
from test_data import *

os.system('cls')

sample_variation_range = get_sample_variation_range(arr)
m = get_m(n)
h = 7
clustered_variation_range = get_clustered_variation_range(sample_variation_range, h)
average_variation_range = get_average_variation_range(clustered_variation_range)
xv = get_Xv(average_variation_range, n)
xv_squared = get_Xv_squared(average_variation_range, n)
lambda_star = get_6_star(xv_squared, xv)
sample_table = get_sample_table(clustered_variation_range, xv, lambda_star, n)
x_squared_table = get_x_squared_table(clustered_variation_range, sample_table)
x_squared_seen = get_x_squared_seen(x_squared_table)
k = get_k(step=h)
x_squared_real = get_x_squared_real(k, chance)

print(f"n: {n}")
print(f'm: {m}')
print(f'step: {h}')
print(f'Хв: {xv}')
print(f'Хв^2: {xv_squared}')
print(f'6*: {lambda_star}')
print(f'x_squared seen: {x_squared_seen}')
print(f'k: {k}')
print(f'x_squared_real: {x_squared_real}')
ci.print_sample_variance(sample_variation_range)
ci.print_clustered_variation(clustered_variation_range)
ci.print_average_variation_range(average_variation_range)
ci.print_sample_table(sample_table)
ci.print_x_squared_table(x_squared_table)