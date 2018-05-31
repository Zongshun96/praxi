#!/usr/bin/env python3

import os
import sys
import pickle
from pathlib import Path
import tempfile
import yaml

from tqdm import tqdm

from columbus.columbus import columbus

PROJECT_ROOT = Path('~/hybrid-method').expanduser()
CHANGESET_ROOT = Path('~/yaml/testing/').expanduser()


def main():
    get_scores([], [101289, 102580, 102585, 99234])
    with (PROJECT_ROOT / 'changeset_sets' /
          'threek_dirty_chunks.p').open('rb') as f:
        threeks = pickle.load(f)
    with (PROJECT_ROOT / 'changeset_sets' /
          'tenk_clean_chunks.p').open('rb') as f:
        tenks = pickle.load(f)
    for idx, test_set in enumerate(threeks):
        train_idx = [0, 1, 2]
        train_idx.remove(idx)
        train_set = threeks[train_idx[0]] + threeks[train_idx[1]]
        get_scores(test_set, train_set)
        for idx, extra_cleans in enumerate(tenks):
            train_set += extra_cleans
            get_scores(test_set, train_set)


class Hybrid:
    """ scikit style class for hybrid method """
    def __init__(self, k=5, vw_args=''):
        self.k = k

    def fit(self, X, y):
        counter = 1
        indexed_labels = {}
        for label in set(y):
            indexed_labels[label] = counter
            counter += 1
        tags = [columbus(x, k=self.k) for x in X]
        with tempfile.NamedTemporaryFile('w') as f:
            for tag, label in zip(tags, y):
                f.write('{} {} | {}\n'.format(
                    indexed_labels[label],
                    label, ' '.join(tag)))
                print('{} {} | {}\n'.format(
                    indexed_labels[label],
                    label, ' '.join(tag)))
            print(f.name)
            os.system('cat {} > ~/test.out'.format(f.name))
        sys.exit(0)

    def predict(self, X):
        pass

    def score(self, X, y):
        pass


def get_changeset(csid):
    changeset = None
    for csfile in CHANGESET_ROOT.glob('*{}*'.format(csid)):
        if changeset is not None:
            raise IOError("Too many changesets match the csid {}".format(csid))
        with csfile.open('r') as f:
            changeset = yaml.load(f)
    if changeset is None:
        raise IOError("No changesets match the csid {}".format(csid))
    return changeset


def parse_csids(csids):
    """ Returns labels and features from csids, features are file sets
    file sets: list of string of format '644 /usr/.../file' """
    features = []
    labels = []
    for csid in csids:
        changeset = get_changeset(csid)
        labels.append(changeset['label'])
        features.append(changeset['changes'])
    return features, labels


def get_scores(test_set, train_set):
    """ Gets two lists of changeset ids, does training+testing """
    clf = Hybrid()
    X, y = parse_csids(train_set)
    clf.fit(X, y)
    X, y = parse_csids(test_set)
    clf.score(X, y)


if __name__ == '__main__':
    main()
