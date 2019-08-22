#draw line from tow point
def  draw_line (point1 ,point2 , image):
        image = cv2.line(image,point1,point2,(255,255,255),5)
        return image

#draw  line  from list point  (point 0 -> point 1 , point 3->point 4 ...) on image
def draw_lines(list_point , image):
    for  i in range(0,len(list_point) ,2):
        image  = draw_line(list_point[i],list_point[i+1] ,image)
    return image

#draw list point on image    
def draw_point(points , image):
    for p in points:
        cv2.circle(image, (int(p[0]), int(p[1])), 5, (135, 206, 235), -1) 
    # draw_line((121,748) ,(249,772),image)
    return image