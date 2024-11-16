# geo/__init__.py
# 패키지로 인식되도록 만드는 빈 파일입니다.

# geo/utils.py
def area_of_circle(radius):
    """주어진 반지름을 사용하여 원의 면적을 계산합니다."""
    import math
    return math.pi * (radius ** 2)

def perimeter_of_rectangle(length, width):
    """주어진 길이와 너비를 사용하여 직사각형의 둘레를 계산합니다."""
    return 2 * (length + width)

# tester.py
from geo.utils import area_of_circle, perimeter_of_rectangle

def main():
    # 원의 면적 테스트
    radius = 5
    print(f"반지름 {radius}의 원의 면적: {area_of_circle(radius)}")

    # 직사각형의 둘레 테스트
    length = 10
    width = 5
    print(f"길이 {length}와 너비 {width}의 직사각형 둘레: {perimeter_of_rectangle(length, width)}")

if __name__ == "__main__":
    main()

