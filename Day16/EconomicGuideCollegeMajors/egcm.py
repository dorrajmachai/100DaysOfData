# Part 1: Introduction
import pandas as pd
import opendatasets as od
import matplotlib.pyplot as plt
import seaborn as sns

od.download('https://www.kaggle.com/datasets/williecosta/economic-guide-to-college-majors?select=college_majors.csv')

csv = './economic-guide-to-college-majors/college_majors.csv' # a string containing a relative link to the data
data: pd.DataFrame = pd.read_csv(csv)

# data.head(n = 10)

# Part 2: Exploration
data.info()
data.describe()

# looking at the total number of people in a major and comparing the number of men and women in them
total_comp = data[['Major', 'Total', 'Men', 'Women']]
total_comp.head(n = 15)

# it would probably be helpful to see this visually as well

fig, ax = plt.subplots(2, 2) # What type should this return? AxesSubplots?

fig.set_figheight(40)
fig.set_figwidth(40)

total_majors: pd.DataFrame = total_comp[['Major', 'Total']]
total_men: pd.DataFrame = total_comp[['Major', 'Men']]
total_women: pd.DataFrame = total_comp[['Major', 'Women']]

total_majors.plot(x = 'Major', kind = 'barh', ax = ax[0, 0])
total_men.plot(x = 'Major', kind = 'barh', ax = ax[0, 1])
total_women.plot(x = 'Major', kind = 'barh', ax = ax[1, 0])
total_comp.plot(x = 'Major', kind = 'barh', ax = ax[1, 1])

plt.show()
# plt.close()