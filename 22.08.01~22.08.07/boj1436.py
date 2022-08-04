N = int(input())
series_num = 666
series_num_list = []
while len(series_num_list) != N:
    str_series_num = str(series_num)
    if "666" in str_series_num:
        series_num_list.append(series_num)
        series_num += 1
    else:
        series_num += 1

print(series_num_list[N-1])