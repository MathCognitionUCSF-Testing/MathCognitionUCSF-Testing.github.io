# %%
import pandas as pd
import json
# %%
sheet_id = "1dPeBZbRMQDMLTgm0DU6QbtS2z3E7Qs1-vBTfzftzpIo"
sheet_name = "Sheet1"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
data = pd.read_csv(url)
# %%
df_response = data[data['task']=='response']
# %%
stimuli_file_name = '/Users/mkersey/code/MathCognitionUCSF-Testing.github.io/experiments/stimuli.js'
stimuli = json.loads(stimuli_file_name)
# %%
df_stimuli = pd.json_normalize(stimuli)

# %%
