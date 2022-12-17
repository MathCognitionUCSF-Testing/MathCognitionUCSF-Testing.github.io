# %%
import pandas as pd
import json
from scipy.optimize import curve_fit
# %%
sheet_id = "1bpAoVPO71IJSbSPyr4FE97hSMcCEW75v1qEOBW4S_oo"
sheet_name = "Sheet1"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
df_all = pd.read_csv(url)

# upload my data
df_all = pd.read_csv('/Users/mkersey/Downloads/mydata3 (1).csv')
# %%
df_response_pidn = df_all[df_all['task']=='response']
# %%
df_stimuli = pd.read_csv('/Users/mkersey/code/MathCognitionUCSF-Testing.github.io/experiments/nonsymbolic_comparison/stimuli.csv')
# %%
# select all data from a specific PIDN based on the sheet_sub_id associated with that PIDN
# NOTE: sometimes the PIDN is in the response column says 'PIDN' and sometimes 'subID'
pidn = input("Enter PIDN: ") # i.e. margotesting
# %%
sheet_sub_id = df_all.loc[df_all['response']=='{""subID"":""'+pidn+'""}'].sheet_sub_id.values[0]
df_response_pidn = df_response[df_response['sheet_sub_id']==sheet_sub_id]
# %%
# select relevant columns
df_response_pidn_filter = df_response_pidn[['rt','stimulus','response','correct_response','correct']]
print("Results for PIDN: ", pidn)
display(df_response_pidn_filter)
# %%
# print some stats for this participant
print(f"Number of trials: {df_response_pidn_filter.shape[0]}")
print(f"Number of correct trials: {df_response_pidn_filter['correct'].sum()}")
print(f"Number of incorrect trials: {df_response_pidn_filter.shape[0]-df_response_pidn_filter['correct'].sum()}")
print(f"Percent correct: {(df_response_pidn_filter['correct'].sum()/df_response_pidn_filter.shape[0])*100}%")

# %%
# horizontally concatenate the df_response_pidn_filter and df_stimuli
df_response_pidn_filter = df_response_pidn_filter.reset_index(drop=True)
df_stimuli = df_stimuli.reset_index(drop=True)
df_response_pidn_filter = pd.concat([df_response_pidn_filter, df_stimuli], axis=1)
# %%
# plot rt as a function of log of ratio
import numpy as np
import matplotlib.pyplot as plt
plt.plot(np.log(df_response_pidn_filter['ratio']), df_response_pidn_filter['rt'], 'o')
plt.xlabel('ratio')
plt.ylabel('rt')
plt.show()
# %%
# write a gaussian function
def func_gauss(x, a, b, c):
    y = a * np.exp(-(x - b)**2 / (2 * c**2))
    return y
# %%
#############################
# Define exponential function
# def func_nl_reg(x, a, b, c):
#     y = a * np.exp(-b * x) + c
#     return y
# %%
ydata = df_response_pidn_filter['rt']
xdata = np.log(df_response_pidn_filter['ratio'])
# %%
p0 = (1, 1, 1)
# Curve fit
popt, pcov = curve_fit(func_gauss, xdata, ydata, p0)
fit_A = popt[0]
fit_B = popt[1]
fit_C = popt[2]
# %%
fit_y = func_gauss(xdata, popt[0], popt[1], popt[2])
# %%
plt.plot(xdata, ydata, 'o', label='data')
plt.plot(xdata, fit_y, 'o', label='fit')
# change y limit to 700
plt.ylim(500, 700)
# %%
# take the average of each ratio of unique values of xdata
