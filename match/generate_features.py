"""
Generate features (rank lists, program slots) for Match instances.

TODO
 * non-uniform distributions (given as string params) to simulate 'desirability'
   of some applicants
 * program slots
   * maybe try to get some real-world data
   * provide distribution as arg
 * programs shouldn't always rank every possible applicant obviously
"""
import numpy as np
import numpy.random as npr


def generate_applicant_ranks(num_applicants: int, num_programs: int) -> np.ndarray:
    """Create initial applicant ranks matrix

    :param int num_applicants: total number of applicants
    :param int num_programs: total number of possible programs to rank
    :return: ndarray containing applicant ranks
    """
    ranks = np.zeros((num_applicants, num_programs))
    for applicant in range(num_applicants):
        ranks[applicant] = npr.choice(num_programs, size=num_programs,
                                      replace=False)
    return ranks


def generate_program_ranks(num_applicants: int, num_programs: int) -> np.ndarray:
    """Create initial program ranks matrix.

    :param int num_applicants: total number of applicants
    :param int num_programs: total number of possible programs to rank
    :return: ndarray containing applicant ranks
    """
    ranks = np.zeros((num_programs, num_applicants))
    for program in range(num_programs):
        ranks[program] = npr.choice(num_applicants, size=num_applicants,
                                    replace=False)
    return ranks

def generate_program_slots(num_programs: int, min_slots: int = 1,
                           max_slots: int = 10) -> np.ndarray:
    """Create program slots array.

    :param int num_programs: # of programs
    :param int min_slots: min # of slots per program
    :param int max_slots: max # of slots per program
    :return: 1d array containing # of slots for each program
    """
    return npr.choice(np.arange(min_slots, max_slots), size=num_programs)

