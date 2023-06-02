from func import *
from console_interface import *


# 1 task
dt_with_sum = add_sum_by_rows_and_cols_to_data()
k = get_k()
future_dt = get_future_data(dt_with_sum)
x_squared_seen = get_x_squared_seen(future_dt)
x_squared_real = get_x_squared_real(k)

print(f'k: {k}')
print(f'x squared seen: {x_squared_seen}')
print(f'x squared real: {x_squared_real}\n')
console_interface.print_data_with_sum(dt_with_sum)
console_interface.print_future_data(future_dt)

if x_squared_real < x_squared_seen:
    print(f"Відхиляємо нульову гіпотезу з вірогідністю {chance * 100}\n")
else:
    print(f'Приймаємо нульову гіпотезу з вірогідністю {chance * 100}\n')

print("===== 2 завдання =====\n")

# 2 task

x_triangle = get_x_triangle()
y_triangle = get_y_triangle()
dt_minus = get_data_minus(x_triangle, y_triangle)
add_multiplyiyng_to_dt_minus(dt_minus)
Sx = get_Sx(dt_minus)
Sy = get_Sy(dt_minus)
bx = get_6x(Sx)
by = get_6y(Sy)
Kxy = get_Kxy(dt_minus)
Cxy = get_Cxy(Kxy, bx, by)

print(f'x_triangle: {x_triangle}')
print(f'y_triangle: {y_triangle}')
print(f'Sx: {Sx}')
print(f'Sy: {Sy}')
print(f'6x: {bx}')
print(f'6y: {by}')
print(f'Kxy: {Kxy}')
print(f'Cxy: {Cxy}')

console_interface.print_data()
console_interface.print_dt_minus(dt_minus)