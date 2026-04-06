_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

list_chan = []
list_le = []

for i in _list:
    if i % 2 == 0:
        list_chan.append(i)
    else:
        list_le.append(i)

print("Danh sách số chẵn:", list_chan)
print("Danh sách số lẻ:", list_le)