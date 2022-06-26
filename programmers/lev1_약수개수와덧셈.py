def get_div_cnt(num):
    cnt=1
    for x in range(1,num):
        if num%x==0:
            cnt+=1
    if cnt%2==0:
        return True
    return False

def solution(left, right):
    answer=0
    for i in range(left,right+1):
        if get_div_cnt(i):
            answer+=i
        else:
            answer-=i
    return answer
# def solution(left, right):
#     answer = 0
#     for i in range(left,right+1):
#         if int(i**0.5)==i**0.5:
#             answer -= i
#         else:
#             answer += i
#     return answer