import pandas as pd

def calculate_and_display_average_price(data):

    close_data = data["Close"]
    data_number = 0
    data_all = 0
    for data_temp in close_data:
        data_all += data_temp
        data_number += 1
        print(data_temp)

    data_average = data_all/data_number

    print(data_average)