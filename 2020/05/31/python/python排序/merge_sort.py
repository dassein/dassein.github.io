import sys
sys.setrecursionlimit(1000000)  # add depth of recursion


def merge_sort(origin_list, start, end):
	if end <= start:
		return
	mid = int((start + end) / 2)
	merge_sort(origin_list, start, mid)
	merge_sort(origin_list, mid + 1, end)
	left_head = int(start)
	right_head = int(mid +1)
	tmp_list = []
	while left_head <= mid and right_head <= end:
		if origin_list[left_head] < origin_list[right_head]:
			tmp_list.append(origin_list[left_head])
			left_head += 1
		if origin_list[left_head] >= origin_list[right_head]:
			tmp_list.append(origin_list[right_head])
			right_head += 1
	if left_head <= mid:
		tmp_list += origin_list[left_head:mid + 1]
	if right_head <= end:
		tmp_list += origin_list[right_head:end +1]
	for i in range(0, len(tmp_list)):
		origin_list[i + start] = tmp_list[i]

origin_list = [5, 3, 1, 3, 7, 9, 8]
merge_sort(origin_list, 0, len(origin_list) - 1)
print(origin_list)
