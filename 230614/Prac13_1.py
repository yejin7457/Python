from Rect import Rectangle
import Circle

if __name__ == "__main__":
    shapeList = []        
    for i in range(3):
        s = input("도형 모양을 입력하세요: ")
        if s == "사각형":
            x1 = int(input("왼쪽 상단의 x좌표를 입력: "))
            y1 = int(input("왼쪽 상단의 y좌표를 입력: "))
            x2 = int(input("오른쪽 하단의 x좌표를 입력: "))
            y2 = int(input("오른쪽 하단의 y좌표를 입력: "))
            shapeList.append(Rectangle(x1, y1, x2, y2))
        elif s == "원":
            x = int(input("원의 중심 x 좌표를 입력: "))
            y = int(input("원의 중심 y 좌표를 입력: "))
            r = int(input("원의 반지름을 입력: "))
            shapeList.append(Circle.Circle(x, y, r))
     
    for s in shapeList:
        print(f"면적: {s.calcArea()}")
