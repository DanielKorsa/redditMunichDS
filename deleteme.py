



# def whatever(pricelist):

#     if len(pricelist) > 0:
#         top = max(pricelist)
#         top_i = pricelist.index(top)
#         low = min(pricelist)
#         low_i = pricelist.index(low)
#         if top_i > low_i:
#             return top - low
#         else:
#             return 0
#     else:
#         return 0

#print(whatever([7,6,4,3,1]))


# def whatever(pricelist):


#     low = min(pricelist)
#     low_i = pricelist.index(low)
#     sliced = pricelist[low_i:]
#     if max(sliced) > low:
#         return max(sliced) - low
#     return 0
#     #print (sliced)


# print(whatever([2,4,1]))


# def whatever(prices):
#     max_gain = []
#     while len(prices) > 0:
#         #print(price)
#         low = min(prices)
#         low_i = prices.index(low)
#         sliced = prices[low_i:]
#         print(sliced)
#         if max(sliced) > low:
#             max_gain.append(max(sliced) - low)
#         else:
#             max_gain.append(0)
#         prices.remove(low)
#     return max(max_gain)


# a = whatever([4,7,1,2])
# print('RESULT IS')
# print(a)

# # a = [4,7,1,2]

# # print(a[2:])


columns = ['shit', 'lol', 'yolo']


togeza = ', '.join(columns)

print(togeza)