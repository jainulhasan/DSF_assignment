import pandas as pd
from pandas_profiling import ProfileReport
df = pd.read_csv('housing.csv')
print(df)

#generate report
profile = ProfileReport(df)
profile.to_file(output_file="housing.html") 
