def orderListBubble(list):
    for num in range(len(list)-1,0,-1):
        for i in range(num):
            if list[i] > list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp

def main():
    alist = [3,7,1,9,5,8,2,0,10,15,6,11,4,12]
    orderListBubble(alist)
    print(alist)
    
main()
