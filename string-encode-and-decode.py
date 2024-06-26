class Solution:

    def encode(self, strs: List[str]) -> str:
        strencode = ""
        for word in strs :
            k = len(word)
            strencode += str(k)+"#"+str(word)
        return strencode

    def decode(self, s: str) -> List[str]:
        i = 0
        liste = []
        while i < len(s) : 
            j = i
            while s[j] != "#" : 
                j+=1
            number = int(s[i:j])
            word = s[j+1:j+1+number]
            liste.append(word)
            i = number + 1 + j
        return liste
