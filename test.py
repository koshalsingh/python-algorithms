# Python code to merge dict using a single 
# expression 
def Merge(dict1, dict2): 
	res = {dict1 + dict2} 
	return res 
	
# Driver code 
dict1 = {'a': 10, 'b': 8} 
dict2 = {'d': 6, 'c': 4} 
#dict3 = dict(dict1.items()+dict2.items())

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x,y in dict1,dict2:
  print(dict1[x])


