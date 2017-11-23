#Super Reduced String

import sys

def super_reduced_string(s):
    st = []
    for i in s:
        if st and st[len(st)-1] == i:
            st.pop()
        else:
            st.append(i)
    st = ''.join(st)
    return st or 'Empty String'
s = input().strip()
result = super_reduced_string(s)
print(result)




#Camle Case

s = input().strip()
count = 1
for i in s:
    if i.isupper():
        count += 1
print (count)



#Alternating Characters

def alternatingCharacters(s):
    for i in range(len(s)):
        S = s.strip()
    return(len([i for i in range(1, len(S)) if S[i-1]==S[i]]))


q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = alternatingCharacters(s)
    print(result)


#Game Of Thrones-pt1

def gameOfThrones(s):
    if len([i for i in set(s) if s.count(i) % 2 != 0]) < 2:
        return ('YES')

    else:
        return ('NO')


s = input().strip()
result = gameOfThrones(s)
print(result)


#Sherlock And Anagrams


def sherlockAndAnagrams(s):
    for i in range(len(s)):
        anag = 0
        map = {}
        for i in range(len(s)):
            for j in range(len(s) - i):
                s1 = ''.join(sorted(s[j:j + i + 1]))
                map[s1] = map.get(s1, 0) + 1
        for key in map:
            anag += (map[key] - 1) * map[key] // 2
        return(anag)

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = sherlockAndAnagrams(s)
    print(result)