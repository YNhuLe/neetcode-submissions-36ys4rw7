class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # get the number of student in the queue, initially everyone is in the queue
        # count how many student prefer each type of sandwich
        # cnt[0] => number of students who want sandwich 0
        # cnt[1] => number of student who want sandwich 1
        #  loop through the sandwich stack from top to bottom
        # case 1: at least 1 student want the sandwich s
        # student take the sandwich and leave: 
                # res( 1 less student left)
                # cnt[s] one less student who want this type
        #  case 2: no one want the sandwich: so return how many student are left(res)

        # res = len(students)
        # cnt = Counter(students)

        # for s in sandwiches:
        #     if cnt[s] > 0:
        #         res -= 1
        #         cnt[s] -= 1
        #     else: 
        #         return res

        # return res

        count  = Counter(students)

        for s in sandwiches:
            if count[s] == 0:
                return count[0] + count[1] 
            count[s] -= 1

        return 0