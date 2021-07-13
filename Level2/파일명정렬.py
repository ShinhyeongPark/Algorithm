import sys
import re


def solution(files):
    # files의 각 파일당 분리를 하는데, 숫자가 있는 부분을 기준으로 분리
    temp = [re.split(r"([0-9]+)", s) for s in files]

    # 정렬 순서
    # 1. Header (대소문자 구분 없이 -> lambda를 사용해 lower()한 결과를 기준으로 정렬)
    # 2. Number (001, 10, 11 -> 001,10, 11)
    sort = sorted(temp, key=lambda x: (x[0].lower(), int(x[1])))

    return [''.join(s) for s in sort]


def main():
    print(solution(["img12.png", "img10.png", "img02.png",
          "img1.png", "IMG01.GIF", "img2.JPG"]))


main()
