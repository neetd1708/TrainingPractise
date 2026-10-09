# #
# # class Solution:
# #     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
# #         seen = {}
# #         for index,number in enumerate(nums):
# #             print(seen)
# #             if number in seen:
# #                 if abs(seen[number] - index) <=k:
# #                     print(number)
# #                     print(seen[number]-index)
# #                     return True
# #
# #             seen[number] = index
# #
# #         return False
# # x = Solution()
# # print(x.containsNearbyDuplicate(nums =
# # [1,0,1,1],k=1))
# #
#
#
# data = [
#     {"sku": "A1", "qty": 120, "status": "shipped"},
#     {"sku": "B2", "qty": 40,  "status": "pending"},
#     {"sku": "C3", "qty": 200, "status": "shipped"},
# ]
#
# x=[]
# for row in data:
#     if row['qty'] > 100:
#        x.append(row)
# print(x)
#
# shipped = [row for row in data if row['status'] == 'shipped']
# print(shipped)
#
# x = (r['sku'] for r in data if r['qty'] <200 or r['sku'] for r in data if r['status'] == 'pending')
#
# print(*x)
#
#
#
#
#
#
#
#
# x = 5
#
# def update_x():
#     global x
#     x = 10
#
# update_x()
# print(x)
#
# list1 = [1, 2, 3]
#
# def append_item(a_list, item):
#     a_list.append(item)
#
# append_item(list1, 4)
# print(list1)
#
# def do_nothing():
#     pass
#
# result = do_nothing()
# print(result)
#
#
# myString = "pynative"
# stringList = ["abc", "pynative", "xyz"]
#
# print(stringList[1] == myString)
# print(stringList[1] is myString)


s = "vamavama"
q = "zbabcbabmz"

half = len(s)//2

if s[half:] == s[:half]:
    print(True)

if q == q[::-1]:
    print(True)
len(s)

