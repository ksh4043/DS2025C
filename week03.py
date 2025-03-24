def inters(l1, l2):
    s1 = set(l1)
    s2 = set(l2)

    # return list(s1.intersection(s2))  set 타입 내부적으로 지원하는 중복값 찾기 메서드
    return list(s1 & s2)    # set 타입은 & 키워드로 중복값 찾기 가능 // | 기호는 합집합 // - 기호로 차집합

l1 = [45, 5, 22, 31, 7, 19]
l2 = [2, 1, 5, 22, 7, 38, 27, 19, 13, 41]

print(inters(l1, l2))