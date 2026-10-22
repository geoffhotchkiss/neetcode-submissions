'''
i have my list of strings, i could wrap each in a prefix/postfix 

what if i kept the length of the string along with it

strs = ["Hello","World"]
--> "2|5|Hello5|World"
   --> My string is 5 chars long
   --> pipe to distinguish end of my count from the values



'''

class Solution:

    """         ,--------------------,   ,--------------------,   ,--------------------,
    len(strs) | len(strs[0]) | strs[0]   len(strs[1]) | strs[1]   len(strs[2]) | strs[2]
    """
    def encode(self, strs: List[str]) -> str:
        answer = str(len(strs)) + "|"
        for s in strs:
            answer += str(len(s)) + "|" + s
        return answer

    # "5|Hello", 1 + 1 = 2,  #10|0123456789 --> 2 + 1 = 3
    def decode(self, s: str) -> List[str]:
        answer = []

        if s == "":
            return [""]


        word_count = int(s.split("|")[0])
        words = "|".join(s.split("|")[1:])

        # len(strs[0]) | strs[0] len(strs[1]) | strs[1] len(strs[2]) | strs[2]
        #                   ^     
        def extract_word(e):
            word_length = int(e.split("|")[0])
            word_start = len(str(word_length)) + len("|")
            word_end = word_start+word_length
            return e[word_start : word_end], e[word_end:]
        
        for i in range(word_count):
            word, words = extract_word(words)
            answer.append(word)
        
        return answer

