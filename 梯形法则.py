while 1:
	print("=====INPUT=====")
	width = float(input("width= "))
	if width < 0:
		break;
	y_lst = []
	y_len = int(input('enter the y_lst length'))
	# y_lst.append(float(input()) for _ in range(y_len))
	for i in range(y_len):
		y_lst.append(float(input(f"the {i + 1} y value ")))
	
	# mid = sum(y_lst[i] for i in range(1, y_len - 1))
	# for i in range(1, y_len - 1):
	#     mid += y_lst[i]
	print("=====OUTPUT=====")
	print(0.5 * width * (y_lst[0] + y_lst[len(y_lst) - 1] + 2 * sum(y_lst[i] for i in range(1, y_len - 1))))
	
	_ = input("press any button to continue...")