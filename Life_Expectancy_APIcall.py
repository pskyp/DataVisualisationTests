import matplotlib.pyplot as plt
import pandas as pd
import requests

# make an API call and save the responce

url = "http://apps.who.int/gho/athena/api/GHO/WHOSIS_000001.json?profile=simple"
r = requests.get(url)
print("Status Code:", r.status_code)
data1 = {}
data2 = []

# Store API responce in a variable
repsonce_dict = r.json()

# respoce is nested dictionaries

# {
#   "dimension": [
#                  {
#                    "label": "GHO",
#                    "display": "Indicator"
#                  },
#                  {
#                    "label": "PUBLISHSTATE",
#                    "display": "PUBLISH STATES"
#                  },
#                  {
#                    "label": "YEAR",
#                    "display": "Year"
#                  },
#                  {
#                    "label": "REGION",
#                    "display": "WHO region"
#                  },
#                  {
#                    "label": "COUNTRY",
#                    "display": "Country"
#                  },
#                  {
#                    "label": "SEX",
#                    "display": "Sex"
#                  }
#                ],
#   "fact": [
#            {
#              "dim": {
#                       "PUBLISHSTATE": "Published",
#                       "REGION": "Europe",
#                       "SEX": "Female",
#                       "YEAR": "2011",
#                       "COUNTRY": "Albania",
#                       "GHO": "Life expectancy at birth (years)"
#                     },
#              "Comments": "WHO life table method: Vital registration",
#              "Value": "78.2"
#            # },
#

data1 = repsonce_dict["fact"]

for item in data1:
    # combine any commetns and the data values dict
    data = dict(item["dim"])
    try:
        data["Comments"] = str(item["Comments"])
    except:
        print("no comment")
        data["Comments"] = str("No Comments")

    data["Value"] = float(item["Value"])

    data2.append((data))

# create dataframe and pass in the list of data
df = pd.DataFrame(data2)

# get the table of justy Rwanda and
male = (df["COUNTRY"] == "Rwanda") & (df["SEX"] == "Male") & (df["Comments"] == "No Comments")
female = (df["COUNTRY"] == "Rwanda") & (df["SEX"] == "Female") & (df["Comments"] == "No Comments")
combined = (df["COUNTRY"] == "Rwanda") & ((df["SEX"] == "Female") | (df["SEX"] == "Male")) & (
            df["Comments"] == "No Comments")
female_df = df[female].sort_values(by="YEAR")
male_df = df[male].sort_values(by="YEAR")
combined_df = df[combined].sort_values(by="YEAR")

print(male_df)
print(female_df)
# get current axis
ax = plt.gca()

female_df.plot(kind='line', x="YEAR", y="Value", color='red', ax=ax)
male_df.plot(kind='line', x="YEAR", y="Value", color='blue', ax=ax)

L = plt.legend()
L.get_texts()[0].set_text('Male')
L.get_texts()[1].set_text('Female')

plt.show()
# combined_df.plot.bar()
