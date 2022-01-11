raw_data = open('data.txt', 'r')
list_data = raw_data.read()
list_data = list_data.split('>')

print list_data