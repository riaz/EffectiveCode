class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        """
        We need to verify that word can be compressed as per abbr's representation
        if yes, word will be completely processed
        else word will either be expended or will have more chars remaining to be processed.

        Lets process abbr and scan word accordingly
        """

        word_s = 0
        abbr_s = 0
        w_len = len(word)
        abr_len = len(abbr)
        
        num = 0

        while abbr_s < abr_len: 
            # edge case word_s reached end
            if word_s >= w_len:
                return False
            
            if num > 0:
                # we need to expend word
                num -= 1
                word_s += 1   

            elif abbr[abbr_s].isalpha():
                # we need to check for parity
                num = 0
                if abbr[abbr_s] != word[word_s]:
                    return False
                else:
                    word_s += 1
                    abbr_s += 1
            else:  
                num = 0      
                while abbr_s < abr_len and abbr[abbr_s].isnumeric():
                    if num > w_len - word_s + 1: # large number
                        return False 
                    
                    val = int(abbr[abbr_s])
                    if num == 0 and val == 0:
                        return False # leading zeros not allowed
                    # construct the number and increment abbr pointer
                    num = num*10 + int(abbr[abbr_s])
                    abbr_s += 1 

        while num > 0:
            # we need to expend word
            num -= 1
            word_s += 1   

        return word_s == w_len and abbr_s == abr_len


        



