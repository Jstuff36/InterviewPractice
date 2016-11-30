rect1 = [[1, 1], [5, 4]]
rect2 = [[2, 2], [3, 5]]

def rec_intersection(rect1, rect2):
	x_min = max(rect1[0][0], rect2[0][0])
	x_max = min(rect1[1][0], rect2[1][0])

	y_min = max(rect1[0][1], rect2[0][1])
	y_max = min(rect1[1][1], rect2[1][1])

	if x_min > x_max or y_min > y_max:
		return(None)
	return([[x_min,y_min], [x_max, y_max]])

print(rec_intersection(rect1, rect2))