#! /usr/bin/env python3
# source dir: /home/db/stock_resource_center/resource/twse/json

# get_sample("0050", "2020-02-01", "close")
# 1. list all files in directory
# 2. load json file
# 3. sorting
# 4. list subindex
import json
import os

'''
#print(type(sdata))
# data = json.loads(sdata[])
#
#print(sdata)

#jf = json.load(open(path+"2004-04-23.json"))

#print(jf['0050'])

for f in sdata:
    with open (path+f,'r') as reader:
        jf = json.loads(reader.read())
        print(jf['0050']['close'])
'''
#print(jf['stock_id']['data']['feature'])

PARENT_DIR = "/home/db/stock_resource_center/resource/twse/json"

def format_date(date):
    return PARENT_DIR + date + ".json"

def get_14day_sample(date, stick_id, feature):
    if format_date(date) in sdata:
        for f in sdata:
             with open (path+f,'r') as reader:
                 jf = json.loads(reader.read())
        ed = sdata.index("/home/db/stock_resource_center/resource/twse/json" + date + ".json")
        sd = ed-14
        jf=sorted(jf)
        return print(jf[sd:ed+1]['stock_id']['feature'])

def main():
    sdata = os.listdir(PARENT_DIR)
    get_14day_sample("2020-08-03", "5050", "close")

if __name__ == "__main__":
    main()


#def get_sample(stock_id, date, feature):
 #   data = listdir(/home/db/stock_resource_center/resource/twse/json)


  #  return [10.5, 12.5, 13.4 ...] # 14 value

