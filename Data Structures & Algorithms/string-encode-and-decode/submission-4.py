class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for word in strs:
            encoded = encoded + str(len(word)) + "#" + word 
        print(encoded)
        return encoded

        

    def decode(self, s: str) -> List[str]:
        decodedList = []
        i = 0
        size = ""
        counter = 0
        while len(s) > 0:
           
            while s[i] != "#":
                size = size + s[i]
                i+=1
            print("This is the size " + size + " and the index " + str(i))
            decodedList.append(s[i+1:int(size) + i + 1])
            print("this is decoded " + decodedList[counter])
            s = s[int(size) + i + 1: ]
            print( "new s: " +  " " + s)
            i = 0
            size = ''
            counter +=1
     
        return decodedList
