

dic = [ 
    {"a": {"score":  0, "rank": [0, 0, 0, 0], "rank-amount": 0, "rank-rate": 0}},
    {"b": {"score":  0, "rank": [0, 0, 0, 0], "rank-amount": 0, "rank-rate": 0}},
    {"c": {"score":  0, "rank": [0, 0, 0, 0], "rank-amount": 0, "rank-rate": 0}},
    {"d": {"score":  0, "rank": [0, 0, 0, 0], "rank-amount": 0, "rank-rate": 0}}
]

name = ["a", "b", "c", "d"]





def calRank(score):
    for i in range(0, 4):
        dic[i][name[i]]["score"] = score[i]

    score.sort()


    #score를 통한 랭킹 계산
    for i in range(0, 4):
        idx = 3 - i
        for j in range(0, 4):          
            if score[i] == dic[j][name[j]]["score"]:
                dic[j][name[j]]["rank"][idx] +=1
                break


    # 점수초기화
    for i in range(0, 4):
        dic[i][name[i]]["score"] = 0



    
calRank([3, 13, 2, 1])
calRank([5, 2, 1, 7])
calRank([3, 34, 5, 67])
calRank([7, 3, 2, 4])

# 점수보기
for i in range(0, 4):
    print(dic[i][name[i]])












'''
a["rank"] = 4
b["rank"] = 4
c["rank"] = 4
d["rank"] = 4

rank1, rank2, rank3, rank4 = 0, 0, 0, 0

list = [a, b, c, d]

list.sort(reverse=True)
print(list)


for i, y in 


if list[0] == a:
    a_rank["{}".format(0+1)] += 1 

elif list[1] == a:
    a_rank["{}".format(0+1+1)] += 1 

elif list[2] == a:
    a_rank["{}".format(0+1+1+1)] += 1 

elif list[3] == a:
    a_rank["{}".format(0+1+1+1+1)] += 1



print(a_rank["1"])
print(a_rank["2"])
print(a_rank["3"])
print(a_rank["4"])


'''




