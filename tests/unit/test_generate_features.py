import pytest
from match.generate_features import generate_applicant_ranks, generate_program_ranks, \
        generate_program_slots
import numpy as np
import numpy.random as npr


RANDOM_SEED = 10

def test_gen_app_ranks():
    npr.seed(RANDOM_SEED)
    observed = generate_applicant_ranks(4, 5)
    expected = np.array([
        [2, 3, 0, 4, 1],
        [2, 3, 4, 1, 0],
        [2, 4, 3, 1, 0],
        [3, 2, 4, 1, 0]
    ])
    assert np.all(observed == expected)


def test_gen_prog_ranks():
    npr.seed(RANDOM_SEED)
    observed = generate_program_ranks(6, 4)
    expected = np.array([
        [2, 5, 0, 3, 4, 1],
        [2, 0, 5, 1, 4, 3],
        [3, 4, 0, 2, 1, 5],
        [1, 3, 4, 5, 2, 0]
    ])
    assert np.all(observed == expected)


def test_gen_prog_slots():
    npr.seed(RANDOM_SEED)
    observed = generate_program_slots(8)
    expected = np.array([5, 1, 2, 1, 2, 9, 1, 9])
    assert np.all(observed == expected)
