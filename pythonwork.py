import pandas as pd
import os

def pythonfunction(x, y):
   df = pd.read_excel(x, sheet_name='Sheet1')
   df.to_csv(fr'{y}', index=True)


def deleteupload (x):
   os.remove(x)