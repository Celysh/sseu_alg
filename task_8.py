k = int(input())
n = int(input())
flash = []
list = []
c = 0
def copy(list, flash):
    while (sum(flash) + list[0]) < k:
        flash.append(list[0])
        list.pop(0)
        if list == []:
            break
    for i in range (len(list) - 1):
        if sum(flash) + list[i] < k:
            flash.append(list[i])
            list.pop(i)
            i -= 1


for i in range(n):
    nums = int(input(":"))
    if nums > k:
        print('')
        exit
    list.append(nums)


# while (sum(flash) + list[1]) < k:
#     flash.append(list[0])
#     list.pop(0)

#     if len(list) == 1 and sum(flash) + list[0] < k:
#         flash.append(list[0])
#         list.pop(0)
#         print(flash)
#         break
#     else:
#         break

while list != []:
    flash.clear()
    copy(list,flash)    
    c += 1


print(c)