# Q 30 가사 검색, p.371 / 561
words = ["frodo","front","frost","frozen","frame","kakao"]
queries = ["fro??","????o","fr???","fro???","pro?"]

def bsfirst(query, start, end):
    mid = (start+end) // 2
    if (query[mid] != '?' and query[mid-1] == '?') :
        return mid
    elif query[mid] != '?' and query[mid-1] != '?':
        return bsfirst(query, start, mid-1)
    elif query[mid] == '?' :
        return bsfirst(query, mid+1, end)

def bslast(query, start, end):
    mid = (start+end) // 2
    if (query[mid] != '?' and query[mid+1] == '?') :
        return mid
    elif query[mid] != '?' and query[mid+1] != '?' :
        return bslast(query, mid+1, end)
    elif query[mid] == '?':
        return bslast(query, start, mid-1) 

def solution(words,queries):
    result = []
    temp = []
    for query in queries :
        rcount = 0
        if query == '?':
            for word in words :
                if len('?') == len(word) :
                    rcount += 1
            result.append(rcount)
            break

        start = 0
        end = len(query)-1
        if query[0] == '?':
            f = bsfirst(query,start,end)
            l = len(query)
        else :
            f = 0
            l = bslast(query,start,end)+1
        if query not in temp :
            for word in words :
                if len(query) == len(word) :
                    if query[f:l] == word[f:l]:
                        rcount += 1
            result.append(rcount)
            temp.append(query)
        else :
            for i in range(len(queries)) :
                if queries[i] == query:
                    result.append(result[i])
                    break
    return result

print(solution(words,queries))