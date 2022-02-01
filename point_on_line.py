def input_point():
    point_one = input("Coordinate Point 1: ")
    point_two = input("Coordinate Point 2: ")
    return point_one, point_two

#def connect_points():
#    connect_points = (eval(point_one),eval(point_two))
#    return connect_points
    
    
def main():
    point1,point2 = input_point()
    print(point1)
    print(point2)

#    two_points = input_point()
#    print(two_points)
#    print(two_points[0])
#    print(two_points[1])
#    print(two_points[1][1])


if __name__ == "__main__":
    main()