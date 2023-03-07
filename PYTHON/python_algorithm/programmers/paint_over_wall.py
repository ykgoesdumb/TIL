##link=https://school.programmers.co.kr/learn/courses/30/lessons/161989?language=python3

import math

def solution(n, m, section):
    answer = math.ceil((max(section)-min(section)+1)/m)
    return answer