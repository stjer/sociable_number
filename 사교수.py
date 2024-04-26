import time


def findn(num,slash,rep=0):
    if slash>1 and num%slash == 0 :
        num = num//slash
        rep +=1
    else :
        return rep
    if num ==1:
        return rep
    else :
        return findn(num, slash, rep)

def isp(n):
    prime = [True for _ in range(n + 1)]
    p = 2
    while p ** 2 <= n:
        if prime[p] == True:
            for i in range(p ** 2, n + 1, p):
                prime[i] = False
        p += 1
    prime_numbers = [p for p in range(2, n + 1) if prime[p]]
    return prime_numbers

def ispfn(num):
    sumd=1
    #prime = isp(num)
    for i in prime:
        if i<num:
            a = findn(num,i)
        else:
            break
        if a!=0:
            #print(f"약수 : {i}, 횟수 : {a}")
            sumd*=(1-i**(a+1))//(1-i)
            #print(sumd)
    if sumd!=1:
        sumd -= num
    return sumd

def tryint(maxn = 100,s=""):
    try : 
        a = int(input(s))
        if (0<=a<=maxn):
            return a
        elif a== -1:
            return a
        else:
            print("메뉴에 있는 번호를 선택해 주세요.")
            a = tryint()
            return a
    except: 
        print("숫자를 입력해 주세요.")
        a = tryint()
        return a

def chain(a):#15000,15000 기준 42.6초 15000,*100 기준 503초(프포)
    s=[]
    #global g
    while True:
        if a==1:
            #break
            return# 0
        elif a in prime:
            #print(a)
            #break
            return# 0
        else:
            #print(a,end=" - ")
            s.append(a)
        a = ispfn(a)
        if a == 0:
            return# 0
        if a == s[0]:
            print(s)
            return s
        if a in s:
            return# 0
        if a>=prime[-1]:
            print(f"{s[0]}체인은 범위 밖입니다.")
            return# 0

def chain2(a):#속도 비교 용도.# 15000,15000 기준 40.4초 15000,*100 기준 431초(프x)
    s=[]
    global g
    while True:
        if a==1:
            #break
            return #0
        elif a in prime:
            #print(a)
            #break
            return #0
        else:
            #print(a,end=" - ")
            s.append(a)
        a = ispfn(a)
        if a == 0:
            return 0
        if a == s[0]:
            g.append(s[0])
            print(s)
            return s
        if a in s or a in g:
            if s[0] not in g:
                g.append(s[0])#그냥 s 전체 다 갈기면 뒤에 사교수 고리 들어가는 것들 검출 불가.
            return #0
        if a>=prime[-1]:
            #print(f"{s[0]}체인은 범위 밖입니다.")
            if s not in g:
                for i in s:
                    g.append(i)#15000,*100기준 280초로 줄임(프포).
            return #0
            #break
            

q = tryint(10000000000, "완전수를 찾을 범위를 알려주세요 : ")
start = time.time()
prime = isp(q*100)
g=[]
'''
print("완전수")
for i in range(2,q):#완전수 검출기
    if i == ispfn(i,prime):
        print(i)
        
print("\n친화수")
for i in range(2,q):#친화수 검출기
    if i == ispfn(ispfn(i,prime),prime):
        print(f"{i}, {ispfn(i,prime)}")

end = time.time()

print(f"{end - start:.2f} sec")
'''
#사교수 검출기
#단, 해당 수가 소수 범위 밖으로 간다면 검출 불가. 그렇다고 범위 넓히면 속도가 오지게 느려짐...
for i in range(2,q):
    chain2(i)
    #if a!=0:
        #print(a)#없애는 거로 280->265초로 줄어듬.
#input()

end = time.time()

print(f"{end-start:.2f} sec")
