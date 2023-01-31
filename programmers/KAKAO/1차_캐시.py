def solution(cacheSize, cities):
    answer = 0
    arr = []

    for i, city in enumerate(cities):
        city = city.lower()
        if city in arr:
            answer += 1
            arr.remove(city)
            arr.append(city)
        else:
            arr.append(city)
            answer += 5
            if len(arr) > cacheSize:
                arr.pop(0)

    return answer


solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"])
