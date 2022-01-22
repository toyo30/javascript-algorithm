# 9가지의 리스트 만들기 


# 리스트를 전부다 for 문 돌리기 

#그랬을 때 순서 매기기 


print(5*3*3*3*5*3*4*3*3)


totalNum = 5*3*3*3*5*3*4*3*3

print(totalNum)

yoon, ahn, sim, lee = 0, 0, 0, 0

num1 = [ 
{"yoon": 3, "ahn": 1, "sim": -3 , "lee": -1}, 
{"yoon": 1, "ahn": 0, "sim": -1 , "lee": 0}, 
{"yoon": 0, "ahn": 0, "sim": 0 , "lee": 0},
{"yoon": -1, "ahn": 0, "sim": 1 , "lee": 0},
{"yoon": -3, "ahn": -1, "sim": 3 , "lee": 1},
]

num2 = [ 
{"yoon": 0, "ahn": 0, "sim": 0, "lee": 0}, 
{"yoon": 0, "ahn": 0, "sim": 0 , "lee": 0}, 
{"yoon": -1, "ahn": 0, "sim": 0 , "lee": -3}
]


num3 = [ 
{"yoon": 3, "ahn": 1, "sim": -3, "lee": -3}, 
{"yoon": 0, "ahn": 0, "sim": 0 , "lee": 0}, 
{"yoon": -3, "ahn": -1, "sim": 3 , "lee": 3}
]

num4 = [ 
{"yoon": -3, "ahn": 2, "sim": 0, "lee": 3}, 
{"yoon": 0, "ahn": 0, "sim": 0 , "lee": 0}, 
{"yoon": 0, "ahn": 0, "sim": 0, "lee": 0}
]

num5 = [
{"yoon": 5, "ahn": 0, "sim": 0, "lee": 0}, 
{"yoon": 0, "ahn": 0, "sim": 0 , "lee": 5}, 
{"yoon": 0, "ahn": 5, "sim": 0, "lee": 0},
{"yoon": 0, "ahn": 0, "sim": 5 , "lee": 0},
{"yoon": 0, "ahn": 0, "sim": 0 , "lee": 0},
]

num6 = [
{"yoon": 0, "ahn": 0, "sim": 0 , "lee": 0},
{"yoon": 0, "ahn": 0, "sim": 0 , "lee": 0},
{"yoon": 0, "ahn": 0, "sim": 0, "lee": -5},
]

num7 = [
{"yoon": 0, "ahn": 3, "sim": 3 , "lee": 0},
{"yoon": 3, "ahn": 0, "sim": 0 , "lee": 0},
{"yoon": 0, "ahn": 0, "sim": 0, "lee": 3},
{"yoon": 0, "ahn": 0, "sim": 0 , "lee": 0},
]

num8 = [
{"yoon": 5, "ahn": 5, "sim": 3 , "lee": 0},
{"yoon": 0, "ahn": 0, "sim": 0 , "lee": 5},
{"yoon": 0, "ahn": 0, "sim": 0 , "lee": 0},
]

num9 = [
{"yoon": 0, "ahn": 3, "sim": 5 , "lee": 5},
{"yoon": 0, "ahn": 3, "sim": 0 , "lee": 0},
{"yoon": 0, "ahn": 0, "sim": 0 , "lee": 0},
]


box = num1[0]

que_list = [num1, num2, num3, num4, num5, num6, num7, num8, num9]

for k in que_list:
    for j in k:
        print(j)

# for i in range(0, len(num1)):
#     for key, value in num1[i].items():
#         print(key, value)
#         yoon += num1[i]["yoon"]
#         ahn += num1[i]["ahn"]
#         sim += num1[i]["sim"]
#         lee += num1[i]["lee"]
