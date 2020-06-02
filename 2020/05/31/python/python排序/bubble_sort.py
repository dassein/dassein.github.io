def bubble_sort(origin_list):
	for i in range(len(origin_list), 0, -1):
		print(i)  # (0, len] equals [1, len]
		for j in range(0, i - 1):  # [0, len - 1) equals [0, len-2]
			if origin_list[j] > origin_list[j + 1]:
				origin_list[j], origin_list[j + 1] = origin_list[j + 1], origin_list[j]

origin_list = [5, 3, 1, 7, 9, 8]
bubble_sort(origin_list)
print(origin_list)
