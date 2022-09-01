#file_name = raw_input('Input file name. ')

handle = open('/Users/macbookpro/Documents/Python/source.csv', 'r')
handle_result = open('/Users/macbookpro/Documents/Python/result.csv', 'w+')

#header = handle.readline()
#print(header)

text = handle.readlines()

i = 0

header = text[0]
handle_result.write(header)

while i < len(text):
    string0 = text[i]
    i = i + 1
    string1 = text[i]
    i = i + 1
    string2 = text[i]
    i = i + 1
    string3 = text[i]
    i = i + 1

    string1 = string1.split(';')[0]
    string2 = string2.split(';')[0]
    string3 = string3.split(';')[0]

    # 3 strings to 1
    big_string = string1 + ' ' + string2 + ' ' + string3

    #time
    index1 = string1.find('[')
    index2 = string1.find(']')
    time = string1[index1 + 1 : index2]
    #print time 
    
    #method
    splitted_string3 = string3.split(' ')
    method = splitted_string3[0]
    method = method[1 : ]
    #print method

    #price
    splitted_string2 = string2.split(' ')
    price = splitted_string2[len(splitted_string2)-1]
    temp = price.split(';')[0]
    price = temp
    #print price

    handle_result.write(big_string + ';' + time + ';' + method + ';' + price + '\n')


handle.close()
handle_result.close()
print ('Successfully processed ' + str(i-1) + ' strings')