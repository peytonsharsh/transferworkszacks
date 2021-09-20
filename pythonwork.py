import pandas as pd

def pythonfunction(x, y):
   df = pd.read_excel(x, sheet_name='Sheet1')
   datarange = df.max()
   df['test'] = datarange
   ##savetarget = r'C:\Users\pharsh\Desktop\target\new.csv'
   df.to_csv(fr'{y}', index=True)