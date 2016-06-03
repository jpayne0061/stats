a = "Evan"
arr = list(a)

a_list = ['nEva', 'anEv', 'vanE', 'Evan']
count = []
for i in range(len(arr)):
    arr.insert(0, arr.pop())
    joined = ''.join(arr)
    if joined in a_list:
        count.append(joined)
    list(arr)
all(x in count for x in a_list)



def contain_all(a, b):
    if a == '':
        return True
    arr = list(a)

    count = []
    for i in range(len(arr)):
        arr.insert(0, arr.pop())
        joined = ''.join(arr)
        print joined
        if joined in b:
            count.append(joined)
        if joined not in b:
            return False
        list(arr)
    #if all(x in count for x in b):
        #print 'yes, all rotations are included'
    #print count
    #print b
    for item in count:
        if item not in b:
            return False
        return True
        
        
 
    
contain_all('XjYABhR', ["TzYxlgfnhf", "yqVAuoLjMLy", "BhRXjYA", "YABhRXj", "hRXjYAB", "jYABhRX", "XjYABhR", "ABhRXjY"])


