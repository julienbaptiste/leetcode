class Solution(object):
    def longestWord(self, words):
        words.sort(key=len) # Sorting words
        solutions = set()   # set of solutions
        longest_word=0      # tracking longest word
        result = ""         # result

        # Looping on increasing length words
        for w in words:
            if len(w) == 1:
                # if len == 1, it is a potential solution
                solutions.add(w)
                
                if longest_word == 0:
                    longest_word = 1
                    result = w
                if longest_word == 1:
                    result = min(w, result)
            else:
                # otherwise, we check if it can ben a solution
                # then we check it is the best solution
                if w[:-1] in solutions:
                    solutions.add(w)

                    if len(w) > longest_word:
                        longest_word = len(w)
                        result = w
                    if len(w) == longest_word:
                        result = min(w, result)

        return result
        