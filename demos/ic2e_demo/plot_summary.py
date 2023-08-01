import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict
import yaml

x_label = "thr"
data_d = defaultdict(list)
# params_l = [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
params_l = list(np.arange(0.0, 1, 0.05))
params_l = [str(params) for params in params_l]

for param in params_l:
    with open('/home/cc/Praxi-study/praxi/demos/ic2e_demo/results/multi_exp_param_'+param+'-0.txt', 'r') as f:
        for line in f:
            if line[:8] == "F1 SCORE":
                data_d["F1 SCORE"].append(float(line[12:17]))
            if line[:9] == "PRECISION":
                data_d["PRECISION"].append(float(line[12:17]))
            if line[:6] == "RECALL":
                data_d["RECALL"].append(float(line[12:17]))

with open('/home/cc/Praxi-study/praxi/demos/ic2e_demo/results/summary.yaml', 'w') as file:
    yaml.dump(data_d, file)
# with open('/home/cc/Praxi-study/praxi/demos/ic2e_demo/results/summary.yaml', 'r') as file:
#     data_d = yaml.load(file, Loader=yaml.Loader)

fig, ax = plt.subplots(1, 1, figsize=(6, 6), dpi=600)
# proba_array = proba_array
# c_l = [color_l[cluster_idx] for cluster_idx in yhats]
ax.plot(list(range(len(data_d["F1 SCORE"]))), data_d["F1 SCORE"], label="f-score")
ax.plot(list(range(len(data_d["PRECISION"]))), data_d["PRECISION"], label="precision")
ax.plot(list(range(len(data_d["RECALL"]))), data_d["RECALL"], label="recall")
# ax.set_xlim(-2, len(proba_array)+1)
ax.set_xticks(list(range(len(params_l))))
ax.set_xticklabels(params_l, rotation=90)
ax.set_title('with '+x_label, fontdict={'fontsize': 30, 'fontweight': 'medium'})
ax.set_xlabel(x_label, fontdict={'fontsize': 26})
ax.set_ylabel("Performance", fontdict={'fontsize': 26})
# ax.tick_params(axis='both', which='major', labelsize=12)
# ax.tick_params(axis='both', which='minor', labelsize=10)
# ax.bar_label(bar_plots, labels=yhats, fontsize=10)
# ax.hlines(y=set_th, xmin=0, xmax=len(proba_array), color='black')
ax.legend(prop={'size': 20})
plt.savefig('/home/cc/Praxi-study/praxi/demos/ic2e_demo/results/summary.png', bbox_inches='tight')
plt.close()

