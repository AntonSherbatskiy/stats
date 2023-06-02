from data import *
import math as mt
from grouped import grouped as g
import scipy.stats

def get_sample_variation_range(arr: list) -> dict:
    d = {
        'xi': [],
        'ni': []
    }

    for i in set(arr):
        d['xi'].append(i)
        d['ni'].append(arr.count(i))

    return d

def get_n(d: dict) -> int:
    return sum(d['ni'])

def get_m(n: int) -> int:
    return round(mt.sqrt(n))

def get_h(d: dict, m: int) -> float:
    return (max(d['xi']) - min(d['xi'])) / m

def get_clustered_variation_range(statistical_sample_distribution: dict, h: float) -> dict:
    clustered_variation_series = {
        'xi + h': [],
        'ni': []
    }

    clustered_variation_series['xi + h'].append([min(statistical_sample_distribution['xi']), min(statistical_sample_distribution['xi']) + h])
    
    i = 0
    while True:
        next_distribution = clustered_variation_series['xi + h'][i][1] + h
        if round(next_distribution, 2) > max(statistical_sample_distribution['xi']):
            break
        clustered_variation_series['xi + h'].append([clustered_variation_series['xi + h'][i][1], clustered_variation_series['xi + h'][i][1] + h])
        i += 1
        
    for cluster in clustered_variation_series['xi + h']:
        values = []
        for xi, ni in zip(statistical_sample_distribution['xi'], statistical_sample_distribution['ni']):
            if cluster != clustered_variation_series['xi + h'][-1]:
                if xi >= cluster[0] and xi < cluster[1]:
                    values.append(ni)
            else:
                if xi >= cluster[0] and xi <= cluster[1]:
                    values.append(ni)
        clustered_variation_series['ni'].append(sum(values))
            
    return clustered_variation_series


def get_average_variation_range(clustered_variation_range: dict) -> dict:
    av_variation = {
        'x*': [],
        'ni': []
    }

    for xi, ni in zip(clustered_variation_range['xi + h'], clustered_variation_range['ni']):
        av_variation['x*'].append( ( xi[0] + xi[1] ) / 2 )
        av_variation['ni'].append(ni)
    return av_variation


def get_Xv(sample_variation_range: dict, n: int) -> float:
    xv = 0
    for xi, ni in zip(sample_variation_range['x*'], sample_variation_range['ni']):
        xv += xi * ni
    return xv / n


def get_Xv_squared(average_variation_range: dict, n: int) -> float:
    xv_squared = 0
    for x_star, ni in zip(average_variation_range['x*'], average_variation_range['ni']):
        xv_squared += pow(x_star, 2) * ni
    return xv_squared / n


def get_6_star(xv_squared: float, xv: float) -> float:
    return mt.sqrt(xv_squared - pow(xv, 2))


def get_sample_table(clustered_variation_range: dict, xv: float, lambda_star: float, n: int) -> dict:
    table = {
        'id': [],
        'xi': [],
        'xi + 1': [],
        'zi': [],
        'zi + 1': [],
        'F(zi)': [],
        'F(zi + 1)': [],
        'pi': [],
        'ni*': []
    }

    id = 1
    for xi_clustered, ni in zip(clustered_variation_range['xi + h'], clustered_variation_range['ni']):
        table['id'].append(id)
        table['xi'].append(xi_clustered[0])
        table['xi + 1'].append(xi_clustered[1])
        table['zi'].append((xi_clustered[0] - xv) / lambda_star)
        table['zi + 1'].append((xi_clustered[1] - xv) / lambda_star)
        table['F(zi)'].append(scipy.stats.norm.cdf(table['zi'][-1]) - 0.5)
        table['F(zi + 1)'].append(scipy.stats.norm.cdf(table['zi + 1'][-1]) - 0.5)
        table['pi'].append(table['F(zi + 1)'][-1] - table['F(zi)'][-1])
        table['ni*'].append(table['pi'][-1] * n)
        id += 1
        
    table['zi'][0] = float('-inf')
    table['zi + 1'][-1] = float('+inf')

    return table


def get_x_squared_table(interval_variation_range: dict, sample_table: dict) -> dict:
    x_squared_table = {
        'ni':[],
        'ni*': [],
        'ni - ni*': [],
        '(ni - ni*)^2':[],
        '(ni - ni*)^2 / ni*': []
    }

    for ni, ni_star in zip(interval_variation_range['ni'], sample_table['ni*']):
        x_squared_table['ni'].append(ni)
        x_squared_table['ni*'].append(ni_star)
        x_squared_table['ni - ni*'].append(x_squared_table['ni'][-1] - x_squared_table['ni*'][-1])
        x_squared_table['(ni - ni*)^2'].append(pow(x_squared_table['ni - ni*'][-1], 2))
        x_squared_table['(ni - ni*)^2 / ni*'].append(round(x_squared_table['(ni - ni*)^2'][-1] / x_squared_table['ni*'][-1], 3))

    return x_squared_table


def get_x_squared_seen(x_squared_table: dict) -> float:
    return sum(x_squared_table['(ni - ni*)^2 / ni*'])


def get_k(step: int) -> float:
    return step - 3


def get_x_squared_real(freedom_count: int, chance: float) -> float:
    return scipy.stats.chi2.ppf(chance, df=freedom_count)