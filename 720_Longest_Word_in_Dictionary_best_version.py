class Solution(object):
    def longestWord(self, words):
        words.sort(key=len) # Sorting the list by len
        words_set = set(words) # Creating a set of all words
        result = "" # Temporary result

        # Looping on words from the largest one to the smallest
        for w in words[::-1]:

            # If the actual word is smaller than the best one
            # selected then no need to continue
            if len(w) < len(result):
                return result

            # If len is one we can select this
            # solution in specific cases
            if len(w) == 1:
                if len(result) == 0:
                    result = w
                elif len(result) == 1 and w < result:
                    result = w
            # Otherwise, we check is the word can be the solution
            else:
                sub_w = w[:-1]

                # Progressively checking that substrings
                # are in the given list
                while(True):
                    if sub_w in words_set:
                        if len(sub_w) > 1:
                            sub_w = sub_w[:-1]
                        else:
                            # If the substring len is 1, we check if the
                            # word can be the solution
                            if len(w) > len(result) or (len(w) == len(result) and (w < result)):
                                result = w
                            break   
                    else:
                        break
        return result
        