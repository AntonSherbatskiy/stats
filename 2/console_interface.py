from tabulate import tabulate
from data import *

class console_interface:
    @staticmethod
    def print_data() -> None:
        print(f"\nДані")
        print(tabulate(dt, headers='keys', tablefmt='fancy_grid'), '\n')

    
    @staticmethod
    def print_dt_minus(dt_minus: dict) -> None:
        print(f"Дані з мінусом tringle")
        print(tabulate(dt_minus, headers='keys', tablefmt='fancy_grid'), '\n')

    
    @staticmethod
    def print_data_with_sum(dt_with_sum: dict) -> None:
        print(f'Дані з сумою по рядкам і стовпцям')
        print(tabulate(dt_with_sum, headers='keys', tablefmt='fancy_grid'), '\n')

    @staticmethod
    def print_future_data(future_dt: dict) -> None:
        print(f'Очікувані дані')
        print(tabulate(future_dt, headers='keys', tablefmt='fancy_grid'), '\n')
