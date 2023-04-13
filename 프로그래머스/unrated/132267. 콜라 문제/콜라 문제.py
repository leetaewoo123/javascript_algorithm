def solution(a, b, n):
    answer = 0
    ## a : 마트에 주어야하는 병 수
    ## b : 빈 병을 주면 받는 병 수
    ## n : 가지고 있는 빈 병 수
    while n>=a: # 가지고 있는 빈 병의 수가 마트에 주어야하는 병 수보다 크면 안됨
        coke = int(n/a) # 현재 가지고 있는 빈 병 수를 마트에 주어야하는 병 수로 나눠서 콜라를 받을 수 있는 횟수
        answer += coke*b # 횟수와 마트에서 주는 병 수를 곱하여 받을 수 있는 콜라의 병 수 
        n = n-(coke*a)+coke*b #원래 병 수에서 마트에 준 병 수를 빼고 받은 병 수는 더한다.
    return answer