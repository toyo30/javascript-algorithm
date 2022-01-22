# 9가지의 리스트 만들기 


# 리스트를 전부다 for 문 돌리기 

#그랬을 때 순서 매기기 

dic = [ 
    {"a": {"score":  0, "rank": [0, 0, 0, 0], "rank-amount": 0, "rank-rate": 0}},
    {"b": {"score":  0, "rank": [0, 0, 0, 0], "rank-amount": 0, "rank-rate": 0}},
    {"c": {"score":  0, "rank": [0, 0, 0, 0], "rank-amount": 0, "rank-rate": 0}},
    {"d": {"score":  0, "rank": [0, 0, 0, 0], "rank-amount": 0, "rank-rate": 0}}
]





name = ["a", "b", "c", "d"]

# dic[0]["a"]["rank"][0]/21600 * 100, 

num1 = [ 
[3, 1, -3 , -1],
[1, 0, -1 , 0], 
[0, 0, 0, 0],
[-1, 0, 1, 0],
[-3, -1, 3 ,1]
]

num2 = [ 
[0, 0, 0, 0],
[-1, 0, 0, -3]
]

num3 = [ 
[3, 1, -3 , -3],
[0, 0, 0, 0],
[-3, -1, 3 ,3]
]

num4 = [ 
[-2, 1, 0 , 2],
[0, 0, 0, 0]
]


num5 = [ 
[5, 0, 0, 0],
[0, 0, 0 ,5],
[0, 5, 0 ,0],
[0, 0, 5 ,0],
[0, 0, 0 ,0]
]


num6 = [ 
[-1, 0, 0, 0],
[0, 0, 0 ,-2]
]

num7 = [ 
[0, 3, 3, 0],
[3, 0, 0, 0],
[0, 0, 0, 3],
[0, 0, 0, 0]
]

num8 = [ 
[5, 3, 3, 0],
[0, 0, 0, 5],
[0, 0, 0, 0]
]

num9 = [ 
[0, 3, 5, 5],
[5, 3, 0, 0],
[0, 0, 0, 0]
]



def calRank(score):
    for i in range(0, 4):
        dic[i][name[i]]["score"] = score[i]

   
    score.sort(reverse=True)

    #score를 통한 랭킹 계산
    
    for j in range(0, 4):
        for i in range(0, 4):     
            if score[i] == dic[j][name[j]]["score"]:
                dic[j][name[j]]["rank"][i] +=1
                break

    # 점수초기화
    for i in range(0, 4):
        dic[i][name[i]]["score"] = 0


# for a in range(0, len(num1)):
#     for i in range(0, 4):
#         print(num1[a][i])


count = 0
for a in range(0, len(num1)):
    for b in range(0, len(num2)):
        for c in range(0, len(num3)):
            for d in range(0, len(num4)):
                for f in range(0, len(num5)):
                    for g in range(0, len(num6)):
                        for h in range(0, len(num7)):
                            for i in range(0, len(num8)):
                                for j in range(0, len(num9)):
                                    totalNum = [0, 0, 0, 0]
                                    count += 1   
                                    totalNum[0] += num1[a][0] + num2[b][0] + num3[c][0] + num4[d][0] + num5[f][0] + num6[g][0] + num7[h][0] + num8[i][0] + num9[j][0]
                                    totalNum[1] += num1[a][1] + num2[b][1] + num3[c][1] + num4[d][1] + num5[f][1] + num6[g][1] + num7[h][1] + num8[i][1] + num9[j][1]
                                    totalNum[2] += num1[a][2] + num2[b][2] + num3[c][2] + num4[d][2] + num5[f][2] + num6[g][2] + num7[h][2] + num8[i][2] + num9[j][2]
                                    totalNum[3] += num1[a][3] + num2[b][3] + num3[c][3] + num4[d][3] + num5[f][3] + num6[g][3] + num7[h][3] + num8[i][3] + num9[j][3]
                                    # print(totalNum)
                                    print(totalNum, count)
                                    calRank(totalNum)
                                       


print(count)



# 점수보기
for i in range(0, 4):
    print(dic[i][name[i]])



rank_rate = [
    {"윤석열": [dic[0]["a"]["rank"][0]/21600 * 100, dic[0]["a"]["rank"][1]/21600 * 100, dic[0]["a"]["rank"][2]/21600 * 100, dic[0]["a"]["rank"][3]/21600 * 100]},
    {"안철수": [dic[1]["b"]["rank"][0]/21600 * 100, dic[1]["b"]["rank"][1]/21600 * 100, dic[1]["b"]["rank"][2]/21600 * 100, dic[1]["b"]["rank"][3]/21600 * 100]},
    {"심상정": [dic[2]["c"]["rank"][0]/21600 * 100, dic[2]["c"]["rank"][1]/21600 * 100, dic[2]["c"]["rank"][2]/21600 * 100, dic[2]["c"]["rank"][3]/21600 * 100]},
    {"이재명": [dic[3]["d"]["rank"][0]/21600 * 100, dic[3]["d"]["rank"][1]/21600 * 100, dic[3]["d"]["rank"][2]/21600 * 100, dic[3]["d"]["rank"][3]/21600 * 100]},
]

print(rank_rate)



'''
rank_rate = [
    {"윤석열": ["1등 확률" + round(dic[0]["a"]["rank"][0]/21600 * 100, dic[0]["a"]["rank"][1]/21600 * 100, 0), "2등 확률" + round(dic[0]["a"]["rank"][2]/21600 * 100, 0), "3등 확률" dic[0]["a"]["rank"][3]/21600 * 100]},
    {"안철수": [dic[1]["b"]["rank"][0]/21600 * 100, dic[1]["b"]["rank"][1]/21600 * 100, dic[1]["b"]["rank"][2]/21600 * 100, dic[1]["b"]["rank"][3]/21600 * 100]},
    {"심상정": [dic[2]["c"]["rank"][0]/21600 * 100, dic[2]["c"]["rank"][1]/21600 * 100, dic[2]["c"]["rank"][2]/21600 * 100, dic[2]["c"]["rank"][3]/21600 * 100]},
    {"이재명": [dic[3]["d"]["rank"][0]/21600 * 100, dic[3]["d"]["rank"][1]/21600 * 100, dic[3]["d"]["rank"][2]/21600 * 100, dic[3]["d"]["rank"][3]/21600 * 100]},
]
'''



'''
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
'''

# for i in range(0, len(num1)):
#     for key, value in num1[i].items():
#         print(key, value)
#         yoon += num1[i]["yoon"]
#         ahn += num1[i]["ahn"]
#         sim += num1[i]["sim"]
#         lee += num1[i]["lee"]
