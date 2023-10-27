import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
import itertools
from random import randint, choice
from matplotlib.patches import RegularPolygon

# Nonsymbolic stimuli
num1 = np.arange(10, 35, 5)
num2 = np.arange(10, 35, 5)

allcombs = np.array(list(itertools.product(num1, num2)))
allcombs = allcombs[allcombs[:, 0] / allcombs[:, 1] != 1]

stim_table = pd.DataFrame(columns=['correct_response', 'stimulus', 'fixation', 'fixation_duration'])

for i in range(allcombs.shape[0]):
    fig, ax = plt.subplots(figsize=(3, 3))

    ax.plot(np.random.rand(allcombs[i, 0]), '.', markersize=30, color='blue')
    ax.plot(np.random.rand(allcombs[i, 1]), '.', markersize=30, color='red')

    ax.axis('square')
    ax.axis('off')
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')

    filename = f"img/dots_{allcombs[i, 0]}_{allcombs[i, 1]}.png"

    if allcombs[i, 0] > allcombs[i, 1]:
        resp = 'f'
    else:
        resp = 'j'

    stim_table = stim_table.append({'correct_response': resp,
                                     'stimulus': filename,
                                     'fixation': '<div style="font-size:60px;">+</div>',
                                     'fixation_duration': randint(250, 1000)}, ignore_index=True)

    plt.savefig(filename, dpi=100)
    plt.close(fig)

js_str = json.dumps(stim_table.to_dict(orient='records'), indent=2)
js_str = f"var test_stimuli = {js_str};"

with open('stimuli.js', 'w') as f:
    f.write(js_str)

stim_table.to_csv('list.csv', index=False)

# Symbolic stimuli
allcombs = np.array(list(itertools.product(num1, num2)))
allcombs = allcombs[allcombs[:, 0] / allcombs[:, 1] != 1]

dot_size_range = np.arange(20, 45, 5)

for i in range(allcombs.shape[0]):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(5, 5))

    v11 = np.random.standard_normal(size=(allcombs[i, 0], 1))
    v12 = np.random.standard_normal(size=(allcombs[i, 0], 1))

    for ii in range(len(v11)):
        ax1.plot(v11[ii], v12[ii], '.', markersize=choice(dot_size_range), color='k')

    ax1.add_patch(RegularPolygon((0, 0), 1000, radius=2, fill=True, alpha=0))
    ax1.axis('square')
    ax1.axis('off')
    ax1.set_facecolor('white')

    v21 = np.random.standard_normal(size=(allcombs[i, 1], 1))
    v22 = np.random.standard_normal(size=(allcombs[i, 1], 1))

    for ii in range(len(v21)):
        ax2.plot(v21[ii], v22[ii], '.', markersize=choice(dot_size_range), color='k')
        ax2.add_patch(RegularPolygon((0, 0), 1000, radius=2, fill=True, alpha=0))
        ax2.axis('square')
        ax2.axis('off')
        ax2.set_facecolor('white')

        filename = f"dots_{allcombs[i, 0]}_{allcombs[i, 1]}.png"

        if allcombs[i, 0] > allcombs[i, 1]:
            resp = 'f'
        else:
            resp = 'j'

        fig.tight_layout()

        plt.savefig(f"img/{filename}", dpi=100)
        plt.close(fig)

