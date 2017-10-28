# Program to determine corrolation between time of day and price change in the
# Bittrex BTC-BCC market

import json


def load_data_set(filename):
    file = open(filename)
    data = json.load(file)
    return data["result"]


def get_hour(record):
    return (int)(record['T'].split('T')[1][:2])


def get_price_change(record):
    return record['C'] - record['O']


def main():
    data = load_data_set("datasets/btc-eth-1hour.json")

    num_records_per_hour = {}
    total_change_per_hour = {}

    for hour in range(24):
        num_records_per_hour[hour] = 0
        total_change_per_hour[hour] = 0

    for record in data:
        hour = get_hour(record)
        num_records_per_hour[hour] += 1
        total_change_per_hour[hour] += get_price_change(record)

    for hour in num_records_per_hour:
        #print((str)(hour) + ": " + (str)(num_records_per_hour[hour]) +
        #      " records. avg change: " + (str)(total_change_per_hour[hour]))
        print((str)(total_change_per_hour[hour]))

main()
