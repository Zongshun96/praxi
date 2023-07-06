import matplotlib.pyplot as plt

f_score_l = [0.177, 0.284, 0.410, 0.459, 0.492, 0.466, 0.285]
precision_l = [0.105, 0.193, 0.340, 0.449, 0.685, 0.754, 0.559]
recall_l = [0.794, 0.699, 0.596, 0.536, 0.430, 0.380, 0.210]
eps_l = ['0.0001', '0.001', '0.005', '0.01', '0.05', '0.1', '0.5']


fig, ax = plt.subplots(1, 1, figsize=(6, 6), dpi=600)
# proba_array = proba_array
# c_l = [color_l[cluster_idx] for cluster_idx in yhats]
ax.plot(list(range(len(f_score_l))), f_score_l, label="f-score")
ax.plot(list(range(len(precision_l))), precision_l, label="precision")
ax.plot(list(range(len(recall_l))), recall_l, label="recall")
# ax.set_xlim(-2, len(proba_array)+1)
ax.set_xticks(list(range(len(f_score_l))))
ax.set_xticklabels(eps_l, rotation=45)
ax.set_title('with DBSCAN', fontdict={'fontsize': 30, 'fontweight': 'medium'})
ax.set_xlabel("eps", fontdict={'fontsize': 26})
ax.set_ylabel("Performance", fontdict={'fontsize': 26})
# ax.tick_params(axis='both', which='major', labelsize=12)
# ax.tick_params(axis='both', which='minor', labelsize=10)
# ax.bar_label(bar_plots, labels=yhats, fontsize=10)
# ax.hlines(y=set_th, xmin=0, xmax=len(proba_array), color='black')
ax.legend(prop={'size': 20})
plt.savefig('/home/cc/Praxi-study/praxi/demos/ic2e_demo/summary/DBSCAN_summary.png', bbox_inches='tight')
plt.close()



f_score_l = [0.448, 0.437, 0.410]
precision_l = [0.691, 0.757, 0.741]
recall_l = [0.373, 0.348, 0.317]
conf_thr_l = ['0.2', '0.3', '0.4']

fig, ax = plt.subplots(1, 1, figsize=(6, 6), dpi=600)
# proba_array = proba_array
# c_l = [color_l[cluster_idx] for cluster_idx in yhats]
ax.plot(list(range(len(f_score_l))), f_score_l, label="f-score")
ax.plot(list(range(len(precision_l))), precision_l, label="precision")
ax.plot(list(range(len(recall_l))), recall_l, label="recall")
# ax.set_xlim(-2, len(proba_array)+1)
ax.set_xticks(list(range(len(f_score_l))))
ax.set_xticklabels(conf_thr_l, rotation=45)
ax.set_title('with Confidence Thresholding', fontdict={'fontsize': 30, 'fontweight': 'medium'})
ax.set_xlabel("Thresholds", fontdict={'fontsize': 26})
ax.set_ylabel("Performance", fontdict={'fontsize': 26})
# ax.tick_params(axis='both', which='major', labelsize=12)
# ax.tick_params(axis='both', which='minor', labelsize=10)
# ax.bar_label(bar_plots, labels=yhats, fontsize=10)
# ax.hlines(y=set_th, xmin=0, xmax=len(proba_array), color='black')
ax.legend(prop={'size': 20})
plt.savefig('/home/cc/Praxi-study/praxi/demos/ic2e_demo/summary/thr_summary.png', bbox_inches='tight')
plt.close()