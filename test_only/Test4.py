import pandas as pd


    
df = pd.read_csv(".\merged data.csv", index_col=None, 
                sep=',', header=0, 
                usecols=None, skiprows=None)

# Remove duplicated rows
df = df.drop_duplicates()
# Merging data frames into one frame




print("Done")
