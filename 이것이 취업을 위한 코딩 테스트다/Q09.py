# Q 09 문자열 압축, p.323 / 516
raw = input()

def solution(raw) :
    s = raw
    i = 0
    zip = len(raw)
    count = 1
    result = ""
    while i < len(s) / 2 :
        while 2*i+2 <= len(s) :
            if s[0:i+1] == s[i+1:2*i+2] :
                count += 1
                s = s[i+1:]
            else :
                if count != 1 :
                    result += str(count)
                count = 1
                result += s[0:i+1]
                s = s[i+1:]
        if count != 1:
            result += str(count)
        result += s

        s = raw
        i += 1
        zip = min(zip, len(result))
        count = 1
        result = ""
        count = 1
    
    return zip

zip = solution(raw)
print(zip)