#! /usr/bin/env python3
import json
import os

PARENT_DIR = "/home/db/stock_resource_center/resource/twse/json"

def format_date(date):
    return PARENT_DIR + "/" + date + ".json"

def get_14day_sample(file_data, date, stock_id, feature):
    if date+".json" in file_data:
        end = file_data.index(date + ".json")
        start = end-14
        print(end,start)
        print(file_data[start:end+1])
        output = []
        for stock_data in file_data[start:end+1]:
            with open ( PARENT_DIR +"/"+ stock_data,'r') as f:
                want_file = json.loads(f.read())
                output.append(want_file[stock_id][feature])
        return output

def main():
    file_data = os.listdir(PARENT_DIR)
    file_data = sorted(file_data)
    get_14day_sample(file_data,"2020-08-03", "0050", "close")
    print(get_14day_sample(file_data,"2020-08-03", "0050", "close"))

if __name__ == "__main__":
    main()
