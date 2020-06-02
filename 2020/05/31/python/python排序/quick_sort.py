def quick_sort(origin_list, start, end):
	if start >= end:
		return
	left = int(start)
	right = int(end)
	flag_index = left  # pivot
	while left < right:
		while right > left:
			if origin_list[right] < origin_list[flag_index]:
				origin_list[right], origin_list[flag_index] = origin_list[flag_index], origin_list[right]
				flag_index = right
				break
			right -= 1
		while left < right:
			if origin_list[left] > origin_list[flag_index]:
				origin_list[left], origin_list[flag_index] = origin_list[flag_index], origin_list[left]
				flag_index = left
				break
			left += 1
	quick_sort(origin_list, start, flag_index)
	quick_sort(origin_list, flag_index + 1, end)

origin_list = [5, 3, 1, 3, 7, 9, 8]
quick_sort(origin_list, 0, len(origin_list) - 1)
print(origin_list)
