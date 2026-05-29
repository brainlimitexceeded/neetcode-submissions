class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        for s in strs:
            ss = str(sorted(s))
            if ss not in d:
                d.update({ss:[s]})
            else:
                d[ss].append(s)
        # print([v for v in d.values()])
        return [v for v in d.values()]