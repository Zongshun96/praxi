#!/bin/bash

alias list_pandas_training_examples="ls demo_tagsets/iter_init/*pandas*"

alias list_pandas_testing_examples="ls demo_tagsets/test_tags/*pandas*"

alias train_first_model="./demo_main.py -t demo_tagsets/iter_init -s demo_tagsets/test_tags -o results -i iter_model.vw -l"

alias show_results_1="less results/iter_exp_summary-0.txt"

alias record_pandas="./cs_rec.py -t demo_changesets/new_changesets -l pandas"

alias install_pandas="pip3 install pandas --user"

alias view_changeset="less demo_changesets/new_changesets/pandas.0.yaml"

alias generate_tagset="./tagset_gen.py -c demo_changesets/new_changesets -t demo_tagsets/new_tagsets"

alias view_tagset="less demo_tagsets/new_tagsets/pandas.0.tag"

alias retrain_model="./demo_main.py -t demo_tagsets/new_tagsets -s demo_tagsets/test_tags -o results -p iter_model.p"

alias show_results_2="less results/iter_exp_summary-1.txt"

alias go_home="cd ~/praxi/middleware_demo"

alias tutorial_reset="rm results/* iter_model* demo_changesets/new_changesets/* demo_tagsets/new_tagsets/*"
