import numpy as np

class Match:

    def __init__(self, applicant_ranks: np.ndarray, program_ranks: np.ndarray,
                 program_slots: np.ndarray):
        """Initialize Match experiment instance.

        :param np.ndarray applicant_ranks: 2D array, where row indices are
            applicant IDs and columns contain program IDs in rank order
        :param np.ndarray program_ranks: 2D array, where row indices are
            program IDs and columsn contain applicant IDs in rank order
        :param np.ndarray program_slots: 1D array, contains slots # for program
            i at index i
        """
        self.applicant_ranks = applicant_ranks
        self.program_ranks = program_ranks
        self.program_slots = program_slots
        self.applicant_matches = np.full([applicant_ranks.shape[0]], np.nan)
        self.program_matches = np.full([program_ranks.shape[0]], np.nan)

    def check_match_over(self) -> bool:
        """Check for match completion conditions


        :return: True if match complete, False otherwise
        """
        # check if programs filled
        self.program_is_full = [any(~np.isnan(program[:self.program_slots[i]]))
                                for i, program in enumerate(self.program_matches)]
        if np.all(self.program_is_full):
            return True

        # check if candidates matched
        # I think this is inaccurate -- a candidate can tentatively match but not
        # fully match?
        self.applicant_is_matched = self.applicant_matches != -1
        if np.all(self.applicant_is_matched):
            return True

        # check for overlap between unfilled programs and unmatched applicants
        for i, program_matched in enumerate(self.program_is_full):
            if not program_matched:
                for j, applicant_matched in enumerate(self.applicant_is_matched):
                    if not applicant_matched:
                        if i in self.applicant_ranks[j] and j in self.program_ranks[i]:
                            return True

        # otherwise, match isn't over
        return False

    def perform_match(self):
        """
        The algorithm:
            while programs have open slots, unmatched candidates remain, and possible
            matches remain for open slots and unmatched candidates:
                gather each candidate's highest-ranked program,
                gather each unfilled program's rank list,
                group candidates by program
                whichever candidate is ranked + ranked highest by that program takes a
                    slot and becomes matched.
        """
        while not self.check_match_over():
            pass

            # for each candidate
            # for each ranked program
            # find the lowest-ranked person for that program
            # if candidate outranks them, replace them
            # if replaced, remove that program from their rank list
            # if not replaced, remove that program fron rank list
