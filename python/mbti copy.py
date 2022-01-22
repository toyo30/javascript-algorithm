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



yoon_rank = {"1": 0, "2": 0, "3": 0, "4": 0}
ahn_rank = {"1": 0, "2": 0, "3": 0, "4": 0}
sim_rank = {"1": 0, "2": 0, "3": 0, "4": 0}
lee_rank = {"1": 0, "2": 0, "3": 0, "4": 0}

yoon_rank["1"] += 1
yoon_rank["1"] += 1

print(yoon_rank["1"])


#최소값 구하는 함수
#2등 구하는 함수 
#3등 구하는 함수 
#4등 구하는 함수 






yoon_rate = {
    "1": yoon_rank["1"]/72900 * 100, 
    "2": yoon_rank["2"]/72900 * 100, 
    "3": yoon_rank["3"]/72900 * 100, 
    "4": yoon_rank["4"]/72900 * 100
}

ahn_rate = {
    "1": ahn_rank["1"]/72900 * 100, 
    "2": ahn_rank["2"]/72900 * 100, 
    "3": ahn_rank["3"]/72900 * 100, 
    "4": ahn_rank["4"]/72900 * 100
}

sim_rate = {
    "1": sim_rank["1"]/72900 * 100, 
    "2": sim_rank["2"]/72900 * 100, 
    "3": sim_rank["3"]/72900 * 100, 
    "4": sim_rank["4"]/72900 * 100
}

lee_rate = {
    "1": lee_rank["1"]/72900 * 100, 
    "2": lee_rank["2"]/72900 * 100, 
    "3": lee_rank["3"]/72900 * 100, 
    "4": lee_rank["4"]/72900 * 100
}



