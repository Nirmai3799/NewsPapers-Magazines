# importing pandas as pd
import pandas as pd

# read an excel file and convert
# into a dataframe object
# df = pd.DataFrame(pd.read_excel(""))

# show the dataframe
read_file = pd.read_excel ("Translated_magzines.xlsx")
  
# Write the dataframe object
# into csv file
read_file.to_csv ("Test.csv", 
                  index = None,
                  header=True)


print(read_file)
