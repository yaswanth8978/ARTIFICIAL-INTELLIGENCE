iList = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print('iList: ',iList)
print('first element: ',iList[0]) 
print('fourth element: ',iList[3]) 
print('iList elements from 0 to 4 index:',iList[0: 5]) 
print('3rd or -7th element:',iList[-7])
 
ilist1 = [12, 14, 16, 18, 20]
print('ilist1: ',ilist1)
ilist2 = [9, 10, 32, 54, 86]
print('ilist2: ',ilist2)
 
l = ilist1 + ilist2  
print(l)
 
ilist3 = [12, 14, 16, 18, 20, 23, 27, 39, 40]
print('ilist3: ',ilist3)

print("Total Elements: ", len(ilist3))    
 
ilist4 = [12, 14, 16, 39, 40]
print('ilist4: ',ilist4)
 
for i in ilist4:   
    print(i)
ilist5 = ['a', 'b', ['cc', 'dd', ['eee', 'fff']], 'g', 'h']
print('ilist5: ',ilist5)
print(ilist5[2])

print(ilist5[2][2])

print(ilist5[2][2][0])
