def input_point():
    point_one = eval(input("Coordinate Point 1: "))
    point_two = eval(input("Coordinate Point 2: "))
    return point_one, point_two


#def connect_points(point1,point2):
#    connect_2points = (eval(point1),eval(point2))
#    return connect_2points
    
    
def slope_2points(point1,point2):
    point1_x = point1[0]
    point1_y = point1[1]
    point2_x = point2[0]
    point2_y = point2[1]
    slope = (point1_y - point2_y)/(point1_x - point2_x)
#    print(point1_x)
#    print(point1_y)
#    print(point2_x)
#    print(point2_y)
#    print(slope)
    return slope

    
def new_x():
    new_x_value = int(input("Enter new x-value: "))
    return new_x_value


def output_y(input_x,slope_of_line,point1):
    y_value = slope_of_line * (input_x - point1[0]) + point1[1]
    print("The corresponding y-value is {}".format(y_value))
    return(y_value)
    

def main():
    point1,point2 = input_point()
    slope_of_line = slope_2points(point1,point2)
    third_x = new_x()
    output_y(third_x,slope_of_line,point1)
#    print(point1)
#    print(point2)
#    two_points = connect_points(point1,point2)
#    print(two_points)
#    print(two_points[0])
#    print(two_points[1])
#    print(two_points[1][1])
#    print(third_x)


if __name__ == "__main__":
    main()