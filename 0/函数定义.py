def calculate_area(angle,radius):
    area = angle / 360 *3.14 * radius  ** 2
    print(f'此扇形面积为：{area}')
    return area

area1 = calculate_area(90,20)
area2 = calculate_area(50,30)

print(area1)
print(area2)