import os
import sys
import time
import subprocess
from datetime import datetime
import matplotlib.pyplot as plt
import yaml, statistics
from tqdm import tqdm
from collections import defaultdict

def plot_size():
    # sizes_l, p_l = [], []
    c_size_d = defaultdict(int)
    p_size_d = {}
    # packages_l = ["pandas", "pillow", "matplotlib", "scipy", "boto3", "cmake", "nvidia-cuda-nvrtc-cu11", "jinja2", "nvidia-cuda-runtime-cu11", "wheel", "triton==2.0.0", "scikit-learn", ]
    # packages_l_1 = ["requests", "Scrapy", "six", "opencv-python", "simplejson", "opacus", "redis", "astropy", "biopython", "bokeh", "dask", "deap", "pyspark", "nilearn", "networkx", "SQLAlchemy"]
    # packages_l_2 = ["scikit-image", "scoop", "Theano", "beautifulsoup4", "Scrapy", "plotly", "pycaret", "mahotas", "statsmodels"]
    # # packages_l = ["pandas", "pillow", "matplotlib"]
    # packages_l.extend(packages_l_1)
    # packages_l.extend(packages_l_2)
    # from itertools import combinations
    # # for length in range(1, len(packages_l)+1):
    # for length in range(1, 2):
    #     for package_names in combinations(packages_l, length):
    target_dir = "mix_test_tag"
    dirname = os.path.dirname(__file__)
    # out_dirname = dirname
    out_dirname = dirname+"/demo_tagsets/"+target_dir+"/"
    # print(out_dirname)
    tagsets_l = [name for name in os.listdir(out_dirname) if os.path.isfile(out_dirname+name)]
    # print(tagsets_l)
    # if len(tagsets_l) == 2:
    for tagsets_name in tqdm(tagsets_l):
        # print(out_dirname+tagsets_name)
        with open(out_dirname+tagsets_name, "r") as stream:
            try:
                tagset = yaml.safe_load(stream)
                if 'labels' in tagset:
                    label_count = len(tagset['labels'])
                    c_size_d[str(label_count)] += 1

                    labels_str = '&&'.join(tagset['labels'])
                    if labels_str in p_size_d:
                        p_size_d[labels_str] += 1
                    else:
                        p_size_d[labels_str] = 1
                else:
                    if tagset['label'] in p_size_d:
                        p_size_d[tagset['label']] += 1
                    else:
                        p_size_d[tagset['label']] = 1
            except yaml.YAMLError as exc:
                print(exc)

    p_size_d = {k: v for k, v in sorted(p_size_d.items(), key=lambda item: item[1])}
    fig, ax = plt.subplots(1, 1, figsize=(26, 6), dpi=600)
    # proba_array = proba_array.reshape(-1)
    # c_l = [color_l[cluster_idx] for cluster_idx in yhats]
    bar_plots = ax.bar(list(range(len(p_size_d))), list(p_size_d.values()))
    # ax.set_xlim(-2, len(proba_array)+1)
    ax.set_xticks(list(range(len(p_size_d))))
    ax.set_xticklabels(list(p_size_d.keys()), rotation=90)
    # ax.set_title('Probability Plot', fontdict={'fontsize': 30, 'fontweight': 'medium'})
    ax.set_xlabel("label idx", fontdict={'fontsize': 26})
    ax.set_ylabel("Tags Count", fontdict={'fontsize': 26})
    ax.tick_params(axis='both', which='major', labelsize=12)
    ax.tick_params(axis='both', which='minor', labelsize=10)
    # ax.bar_label(bar_plots, labels=yhats, fontsize=10)
    # ax.vlines(x=biggest_yhat_idx-0.5, ymin=min(proba_array), ymax=max(proba_array), color='black')
    plt.savefig('/home/cc/Praxi-study/praxi/demos/ic2e_demo/results/'+target_dir+'_distribution_tags_count.png', bbox_inches='tight')
    plt.close()

    c_size_d = {k: v for k, v in sorted(c_size_d.items(), key=lambda item: item[0])}
    fig, ax = plt.subplots(1, 1, figsize=(6, 6), dpi=600)
    # proba_array = proba_array.reshape(-1)
    # c_l = [color_l[cluster_idx] for cluster_idx in yhats]
    bar_plots = ax.bar(list(range(len(c_size_d))), list(c_size_d.values()))
    # ax.set_xlim(-2, len(proba_array)+1)
    ax.set_xticks(list(range(len(c_size_d))))
    ax.set_xticklabels(list(c_size_d.keys()), rotation=90)
    # ax.set_title('Probability Plot', fontdict={'fontsize': 30, 'fontweight': 'medium'})
    ax.set_xlabel("Combination Length", fontdict={'fontsize': 26})
    ax.set_ylabel("Combination Length Count", fontdict={'fontsize': 26})
    ax.tick_params(axis='both', which='major', labelsize=12)
    ax.tick_params(axis='both', which='minor', labelsize=10)
    # ax.bar_label(bar_plots, labels=yhats, fontsize=10)
    # ax.vlines(x=biggest_yhat_idx-0.5, ymin=min(proba_array), ymax=max(proba_array), color='black')
    plt.savefig('/home/cc/Praxi-study/praxi/demos/ic2e_demo/results/'+target_dir+'_distribution_combination_length.png', bbox_inches='tight')
    plt.close()



    return

if __name__ == '__main__':
    plot_size()