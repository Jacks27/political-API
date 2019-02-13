
candidates_list =[]
class CandidateModel:
    def __init__(self):
        self.candidates=candidates_list
    def create_candidates(self, office, party, candidate):
        """Create a new instance of cadidate in the list"""
        new_candidate = {
		"candidate_id" : len(self.candidates)+1,
		"office" : office,
		"party" : party,
		"candidate" : candidate,
		}
        self.candidates.append(new_candidate)
        return self.candidates

