class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        finalList = []

        hm = defaultdict(list)

        for string in strs:
           
            sorted_string = "".join(sorted(string))
           
            hm[sorted_string].append(string)



        
        for anagrams in hm.values():
            finalList.append(anagrams)

        
        return finalList

                

        