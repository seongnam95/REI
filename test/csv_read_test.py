import pandas as pd


try: db = pd.read_csv('../test/20150710_서울특별시.txt', sep="|")
except FileNotFoundError: pass

print(db)
