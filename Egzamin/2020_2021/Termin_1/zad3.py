from zad3testy import runtests

  
def kintersect(A, k):
    interval = [(i, A[i][0], A[i][1]) for i in range(len(A))]
    interval.sort(key=lambda x: x[2], reverse=True)
    max_length = 0
    if k == 1:
        result = [0]
        for i in range(len(A)):
            if interval[i][2] - interval[i][1] > max_length:
                max_length = interval[i][2] - interval[i][1]
                result[0] = interval[i][0]
        return result
    result = []
    for i in range(len(A)):
        current = [interval[i][0]]
        for j in range(len(A)):
            if i != j and interval[j][1] <= interval[i][1] < interval[j][2]:
                current.append(interval[j][0])
                if len(current) == k:
                    actual_length = min(interval[j][2] - interval[i][1], interval[i][2] - interval[i][1])
                    if actual_length > max_length:
                        max_length = actual_length
                        result.clear()
                        result = [current[i] for i in range(k)]
                        print("INDEKS i:",i)
                    break
    return result


if __name__=="__main__":
  A=[(2,100),(97,99),(97,98),(5,50),(30,90)]
  print(kintersect(A,3))

# runtests( kintersect )