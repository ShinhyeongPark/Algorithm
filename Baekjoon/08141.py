import sys


def solution(orderAmount, taxFreeAmount, serviceFee):
    if serviceFee > 0:
        orderAmount -= serviceFee

    if orderAmount - taxFreeAmount == 1:
        return 0
