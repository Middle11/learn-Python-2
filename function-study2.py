#python中的五种数据容器：
#列表list， 元组touple， 字符串str， 集合set， 字典dict

#列表

"""name_list = ["df","dg","as"]
name_list[0] = 1 #修改元素
name_list.insert(2,"dfgh") #插入元素
name_list.append([6,7,8]) #在列表尾部追加元素
print(name_list)
print(type(name_list))

print(name_list[0])
print(name_list[1])
print(name_list[2])

print(name_list.index("dg"))

list_test = [[1,2,3],["df","dg","as"]]
print(list_test)
print(type(list_test))

print(list_test[0])
print(list_test[1])

print(list_test[0][0])
print(list_test[0][1])
print(list_test[0][2])

print(list_test[1][0])
print(list_test[1][1])
print(list_test[1][2])

anyway_list1 = ["df","dg","as"]
anyway_list1.extend([1]) #在列表尾部追加元素
print(anyway_list1)

anyway_list2 = ["df","dg","as"]
del anyway_list2[1] #删除元素（下标）
print(anyway_list2)

anyway_list3 = ["df","dg","as"]
anyway_list3.pop(1) #删除元素（下标）
print(anyway_list3)

anyway_list4 = ["df","dg","as","df"]
anyway_list4.remove("df") #删除第一个匹配到的元素（元素）
print(anyway_list4)

anyway_list5 = ["df","dg","as","df"]
anyway_list5.clear() #清空列表内容
print(anyway_list5)

anyway_list6 = ["df","dg","as","df"]
print(anyway_list6.count("df")) #统计某元素在列表内的数量

anyway_list8 = ["df","dg","as","df"]
print(len(anyway_list8))

#列表的遍历
index = 0
while index < len(anyway_list8):
    x = anyway_list8 [index]
    index += 1
    print(x)

for i in anyway_list8:
    print(i)

#元组touple

t1 = (1,"hey",True)
t2 = ("hey",) #元组内只有一个数据时，数据后面也要加逗号
print(t1,t2)

t3 = ((1,"hey",True),(1,2,3))
print(t3)

t4 = (1,2,"hey",2,3,4,"hey")
print(t4[2])
print(t4.index(2))
print(t4.count("hey"))
print(t4.count(2))
print(len(t4))"""

#字符串
str1 = "ituj and ti itfgh"
print(str1.count("it")) #count用于统计字符串中某字符出现的次数，其中it是作为一个整体统计

str2 = "12fgdfh and fdyfdy21"
print(str2.strip("12")) #字符串的规整操作，字符串.strip（字符串）是去前后指定字符串，传入的是“12”，其实就是1和2都会被移除，是按照单个字符

str3 = " ituj and ti itfgh "
print(str3.strip()) #字符串的规整操作，字符串.strip（）是去前后空格
print(len(str3)) #空格，数字，符号，中文，字母算在字符串的长度里面

#集合set


