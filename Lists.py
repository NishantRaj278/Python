list1 = ["apples","oranges","grapes","banana","pear"]
print(list1[4])
print(list1)
print(type(list1))

list2 = [100,200,300,400,500,600]
print(list2[-5])
print(list2[1:4])
print(list2[:3])
print(list2[1:])

list3 = [1,2,3,4,5,6,7,8,9,10]
list3[2] = 2.5
list3[4] = 4.5
print(list3)

list3[5:6] = [200, 400]
print(list3)

list4 = [10,20,30,40,60]
list4.insert(4, 50)
print(list4)

list4.append(70)
list4.append(80)
list4.append(90)
print(list4)


list5 = [11,22,33,44,55]
list6 = [66,77,88,99]
list5.extend(list6)
print(list5)

tuple1=(5,6,7,8,9,10)
list6.extend(tuple1)
print(list6)


List7 = ['Ram', 'Shyam', 'Rohit','Akshat','Tushar','Yash']
List7.remove('Rohit')
print(List7)

List7.pop(4)
print(List7)
List7.pop()
print(List7)



List8= ['Ram', 'Shyam', 'Rohit','Akshat','Tushar','Yash']
List8.clear()
print(List8)