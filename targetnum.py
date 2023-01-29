'''
import collections
def solution(numbers, target):
    bitreedic=collections.defaultdict(list)
    for i in range(len(numbers)):
        bitreedic[i+1]=[numbers[i],-numbers[i]]
    
    print('dic:',bitreedic)
    sums={i:0 for i in range(1,2**len(numbers)+1)}
    for i in range(1,len(numbers)+1):
        pulse=2**(len(numbers)-i)
        print('pulse:',pulse)
        for j in range(1,2**len(numbers)+1):
            print('j:',j)
            mok=(j-1)//pulse
            print('mok:',mok)
            toggle=mok%2
            sums[j]+=bitreedic[i][toggle]
        print('sum:',sums)
    print(sums)
    print(bitreedic)

    answer=0
    for i in range(1,2**len(numbers)+1):
        if sums[i]==target:
            answer+=1

    print('answer',answer)
    return answer


numbers=[4, 1, 2, 1]
target=4
solution(numbers,target)
'''

'''
모범 답안 idx=N일때 return 하는 방식이 너무 인상적임 answer 을 글로벌로 둬서 내부 함수에서도 +되게 만들었다.
def DFS(idx, numbers, target, value):   
    global answer
    N = len(numbers)                    #
    if(idx== N and target == value):
        answer += 1
        return
    if(idx == N):
        return

    DFS(idx+1,numbers,target,value+numbers[idx])
    DFS(idx+1,numbers,target,value-numbers[idx]) 
    global answer
    DFS(0,numbers,target,0)
    return answer
'''

class TestClass(object):
    def __init__(self):
        self.common_var = None
    def set_variable(self, values=[]):
        values.append("Set Variable")
        self.common_var = values

tc1 = TestClass()
tc2 = TestClass()
tc1.set_variable()
tc2.set_variable()
print(tc1.common_var)
print(tc2.common_var)