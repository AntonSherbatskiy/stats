from tabulate import tabulate

class console_interface:
    @staticmethod
    def print_sample_variance(statistical_range_distribution: dict) -> None:
        print(f"\nРозподіл вибірки")
        print(tabulate(statistical_range_distribution, headers='keys', tablefmt='fancy_grid'), '\n')


    @staticmethod
    def print_clustered_variation(clustered_variation: dict) -> None:
        print(f'Інтервальний ряд')
        print(tabulate(clustered_variation, headers='keys', tablefmt='fancy_grid'), '\n')

    
    @staticmethod
    def print_average_variation_range(av_variation_range: dict) -> None:
        print('Середній інтервальний ряд')
        print(tabulate(av_variation_range, headers='keys', tablefmt='fancy_grid'), '\n')


    @staticmethod
    def print_sample_table(sample_table: dict) -> None:
        print('Перша таблиця')
        print(tabulate(sample_table, headers='keys', tablefmt='fancy_grid'), '\n')


    @staticmethod
    def print_x_squared_table(x_squared_table: dict) -> None:
        print("Таблиця x^2")
        print(tabulate(x_squared_table, headers='keys', tablefmt='fancy_grid'), '\n')
