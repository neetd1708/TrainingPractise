# class Solution:
#     def reverseWords(self, s):
#         # code here
#         sentence = s.split('.')
#         print(sentence)
#         #sentence = [remove(x) for x in sentence if x=='.']
#         for index,item in enumerate(sentence):
#             print(item,end='#')
#             print(sentence,end='|')
#             if item == '':
#                 sentence.remove(item)
#         print(sentence)
#         sentence = ".".join(reversed(sentence))
#         if sentence.startswith('.'):
#             sentence=sentence[1:]
#         if sentence.endswith('.'):
#             sentence = sentence[:-1]
#         return sentence
#
# x = Solution()
# print(x.reverseWords('ofm...mm..mfui.'))


class Solution2:
    def longestCommonPrefix(self, arr):
        # code here
        result = ''
        if len(arr) == 0:
            return ""
        if len(arr) == 1:
            return arr[0]

        try:
            char = arr[0][0]
        except exception:
            return ""
        index = 0
        for alp in arr[0]:
            print("Current alphabet:"+alp)
            match = False
            for item in arr[1:]:
                try:
                    if item[index] == alp:
                        print("Match true for:"+item)
                        match = True
                    else:
                        match = False
                        return result
                except IndexError:
                    return result
            if match:
                result = result + alp
            else:
                return result
            index = index + 1




y = Solution2()
print(y.longestCommonPrefix(['jyzvonn', 'xh', 'flixdx', 'bkfnsuhyrjxcuteukso', 'qclb', 'qykwljvnddylpr', 'wfhtexvuhlpgdiwjpeoy', 'hxkmzpscshlquz', 'kixnynohjaqjgrtz', 'gyxghbndaeqxhiali', 'klhwkqajxk', 'owjqrlszgzknupp', 'jbbwtrtoebqkgprro']))