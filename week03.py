groups = ['HOT', 'Seventeen', 'Black Pink', 'NJZ']
# ratings = [1, 2, 4, 3, 12]
ratings = [1, 2, 4, 3]

group_rating = list(zip(groups, ratings))   # zip -> 각 list의 대응 되는 인덱스 두개를 tuple 형태로 리턴. len 값이 작은 list 기준
print(group_rating)