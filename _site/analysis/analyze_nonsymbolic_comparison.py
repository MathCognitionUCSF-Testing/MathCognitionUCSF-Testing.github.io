# %%
import pandas as pd
import json
# %%
sheet_id = "1dPeBZbRMQDMLTgm0DU6QbtS2z3E7Qs1-vBTfzftzpIo"
sheet_name = "Sheet1"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
df_all = pd.read_csv(url)
# %%
df_response = df_all[df_all['task']=='response']
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
