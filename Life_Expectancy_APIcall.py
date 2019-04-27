import json

import matplotlib.pyplot as plt
import pandas as pd
import requests

# data Set up
#########################################
path = "data_sources/"
filename = "life_expectancy.txt"

r = requests
data1 = {}
data2 = []
responce_dict = {}

# see if the file of the data exists and use this if not try and api call and dafe the resut for next time
try:
    with open(path + filename, 'r') as file_object:
        responce_dict = json.load(file_object)
        print("file object opened and using this for source of data")
except:
    print("file opening or reading error, trying online API call")
    try:
        url = "http://apps.who.int/gho/athena/api/GHO/WHOSIS_000001.json?profile=simple"
        r = requests.get(url)
        print(r.content)
        print("Status Code:", r.status_code)
        responce_dict = r.json()
        with open(path + filename, 'w') as outfile:
            outfile.write(r.json)

    except:
        print("failed to open file or make online API call")

# Data Formating
#######################################

# get to the data areas
data1 = responce_dict["fact"]

for item in data1:
    # combine any comments and the data values dict and out it into new data 2 list
    data = dict(item["dim"])
    try:
        data["Comments"] = str(item["Comments"])
    except:
        print("no comment")
        data["Comments"] = str("No Comments")

    data["Value"] = float(item["Value"])

    data2.append((data))

# create dataframe and pass in the list of combind data
df = pd.DataFrame(data2)

# Data selection
#######################################

# get the table of justy Rwanda and
male = (df["COUNTRY"] == "Rwanda") & (df["SEX"] == "Male") & (df["Comments"] == "No Comments")
female = (df["COUNTRY"] == "Rwanda") & (df["SEX"] == "Female") & (df["Comments"] == "No Comments")
combined = (df["Comments"] == "No Comments")
female_df = df[female].sort_values(by="YEAR")
male_df = df[male].sort_values(by="YEAR")
combined_df = df[combined].sort_values(by="YEAR")
combined_df = combined_df.loc[:, ['YEAR', 'Value']]
combined_df = combined_df.groupby('YEAR').mean().reset_index()
# smooth the data
combined_df['rolling_Mean'] = combined_df['Value'].rolling(2).mean()



# Data Visualisation
##################################

print(male_df)
print(female_df)

print(combined_df)


# get current axis
ax = plt.gca()

female_df.plot(kind='line', x="YEAR", y="Value", color='red', ax=ax)
male_df.plot(kind='line', x="YEAR", y="Value", color='blue', ax=ax)
combined_df.plot(kind='line', x="YEAR", y="rolling_Mean", color='orange', ax=ax)

L = plt.legend()
L.get_texts()[0].set_text('Female')
L.get_texts()[1].set_text('Male')
L.get_texts()[2].set_text('Global Combined sex Avg.')
plt.title("Life Expectancy at birth in Rwanda")
plt.ylabel("Years")

plt.show()
# combined_df.plot.bar()
# todo plot global average and Africa Aferage
