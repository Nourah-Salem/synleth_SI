
#need to import the CSV file 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv (r'C:/Users/Mrs_Youssef/Desktop/SII INTERNSHIP/week2/csv/your_csv_file.csv')
print (df)

#delete empty raws
df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)

df.mean(axis = 0)

df.max(axis = 0)

df.min(axis = 0)

df.median(axis = 0)

df.std(axis = 0)

df.var(axis = 0)


#Visualization
df.plot.scatter(x='homozygous_del', y='expression_up_down')
df.plot.scatter(x='heterozygous_del', y='expression_up_down')
df.plot.scatter(x='mixed_del', y='expression_up_down')

# could be helpful representations
df.plot(x='class', y='expression_up_down') 

df.plot.barh(y='homozygous_del', x='expression_up_down')

df['mixed_del'].plot.pie(subplots=True)
plt.savefig('pie.png')
