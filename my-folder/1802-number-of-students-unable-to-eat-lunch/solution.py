class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:       
        
        preference_count = {0: 0, 1: 0}
        for student in students:
            preference_count[student] += 1

        # Iterate over the sandwiches stack
        for sandwich in sandwiches:
            if preference_count[sandwich] == 0:
                break
            preference_count[sandwich] -= 1

        # Return the remaining count of students who couldn't eat
        return preference_count[0] + preference_count[1]




        # counts = [0, 0]
        # for student in students:
        #     counts[student] += 1

        # remaining = len(sandwiches)
        # for sandwich in sandwiches:
        #     if counts[sandwich] == 0:
        #         break
        #     if remaining == 0:
        #         break
        #     counts[sandwich] -= 1
        #     remaining -= 1
        
        # return remaining



