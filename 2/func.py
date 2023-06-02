from data import *
import math as mt
import scipy.stats

def get_x_triangle() -> float:
    return sum(dt['x']) / n


def get_y_triangle() -> float:
    return sum(dt['y']) / n


def get_data_minus(x_triangle: float, y_triangle: float) -> dict:
    dt_minus = {
        'xi-x_triangle': [],
        'yi-y_triangle': []
    }

    for xi, yi in zip(dt['x'], dt['y']):
        dt_minus['xi-x_triangle'].append(xi - x_triangle)
        dt_minus['yi-y_triangle'].append(yi - y_triangle)

    return dt_minus


def get_Sx(dt_minus: dict) -> float:
    _sum = 0

    for xi in dt_minus['xi-x_triangle']:
        _sum += pow(xi, 2)

    return _sum * (1 / (n - 1))

def get_Sy(dt_minus: dict) -> float:
    _sum = 0

    for xi in dt_minus['yi-y_triangle']:
        _sum += pow(xi, 2)

    return _sum * (1 / (n - 1))


def get_6x(Sx: float) -> float:
    return mt.sqrt(Sx)


def get_6y(Sy: float) -> float:
    return mt.sqrt(Sy)

def add_multiplyiyng_to_dt_minus(dt_minus: dict) -> dict:
    dt_minus['(xi-x_triangle)*(yi-y_triangle)'] = []

    for xi, yi in zip(dt_minus['xi-x_triangle'], dt_minus['yi-y_triangle']):
        dt_minus['(xi-x_triangle)*(yi-y_triangle)'].append(xi * yi)

    return dt_minus
    

def get_Kxy(dt_minus: dict) -> float:
    return sum(dt_minus['(xi-x_triangle)*(yi-y_triangle)']) / (n - 1)


def get_Cxy(Kxy: float, bx: float, by: float) -> float:
    return Kxy / (bx * by)


def add_sum_by_rows_and_cols_to_data() -> dict:
    dt_added_sum = dt.copy()

    dt_added_sum['sum by rows'] = [0, 0]
    dt_added_sum['sum by cols'] = []
    dt_added_sum['n overall'] = [0]

    for xi, yi in zip(dt_added_sum['x'], dt_added_sum['y']):
        dt_added_sum['sum by cols'].append(xi + yi)
        dt_added_sum['sum by rows'][0] += xi
        dt_added_sum['sum by rows'][1] += yi

    dt_added_sum['n overall'][0] = sum(dt_added_sum['sum by rows'])

    return dt_added_sum 


def get_k() -> float:
    return (n - 1) * (len(dt) - 1)


def get_future_data(dt_added_sum: dict) -> dict:
    future_data = {
        'x': [],
        'y': []
    }

    counter = 0

    for xi, yi in zip(dt_added_sum['x'], dt_added_sum['y']):
        future_data['x'].append( ( dt_added_sum['sum by rows'][0] * dt_added_sum['sum by cols'][counter] ) / dt_added_sum['n overall'][0])
        future_data['y'].append( ( dt_added_sum['sum by rows'][1] * dt_added_sum['sum by cols'][counter] ) / dt_added_sum['n overall'][0])
        counter += 1

    return future_data


def get_x_squared_seen(future_data: dict) -> float:
    x_squared = 0
    
    for xi, yi, xi_future, yi_future in zip(dt['x'], dt['y'], future_data['x'], future_data['y']):
        x_squared += (pow(xi - xi_future, 2) / xi_future) + (pow(yi - yi_future, 2) / yi_future)

    return x_squared


def get_x_squared_real(k: int) -> float:
    return scipy.stats.chi2._ppf(chance, 6)