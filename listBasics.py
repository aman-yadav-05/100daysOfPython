states_of_India=["chhattisgarh","Madhya pradesh","jharkhand","maharashtra"]

print(states_of_India[1])

list_of_lists=[[1,2,3],['a','b']]

print(list_of_lists[0][2])

list_of_mulitpleData=[1,"aman",'b']
print(list_of_mulitpleData[2])

list_of_mulitpleData[0]="garima"
print(list_of_mulitpleData[0])

states_of_India.append("tamil nadu")
print(states_of_India)

states_of_India.extend(['meghalaya','karnatak','hyderabad'])

states_of_India.insert(1,'janjgir')
print(states_of_India)

num=states_of_India.count('meghalaya')
print(num)

states_of_India.pop()
print(states_of_India)

list=[]
list.insert(3,23)
list.insert(3,25)
# print(list[2])



fruits=["strawberries","apples","grapes","peaches","cherries","pears"]
vegetables=["spinach","kale","nectarines","tomatoes","potatoes","celeries"]
dirty_dozen=[fruits,vegetables]

print(dirty_dozen)