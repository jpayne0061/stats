#this program will accept an array and identify an outliers
def mean_calc(arr):
    mean = 0
    for num in arr:
        mean += num
    mean = float(mean)/float(len(arr))
    print mean
    return mean

def stan_dev(arr):
    mean = 0
    for num in arr:
        mean += num
    mean = float(mean)/float(len(arr))
    print str(mean) + " mean"
    
    squared_results = 0
    
    for num in arr:
        squared_results += (float(mean) - float(num))**2 
    print str(squared_results/(len(arr))) + " squared results(variance)"
    
    print str(float((float(squared_results)/len(arr))**0.5)) + "std deviation"

def stan_dev_sample(arr):
    print "sample szie: " + str(len(arr))
    mean = mean_calc(arr)
    print str(mean) + " mean"
    
    squared_results = 0
    
    for num in arr:
        squared_results += (float(mean) - float(num))**2 
    print str(squared_results) + "sum of squares"
    print str(squared_results/(len(arr)-1)) + "variance"
    
    print str(float((float(squared_results)/(len(arr)-1))**0.5)) + "std deviation"
    return float((float(squared_results)/(len(arr)-1))**0.5)

def stan_dev_diff(arr, arr2):
    
    diffs = []
    count = 0
    for i in arr:
        diffs.append(float(i)-float(arr2[count]))
        count += 1
    
    mean = mean_calc(diffs)
    print str(mean) + " mean"
    
    squared_results = 0
    
    for num in diffs:
        squared_results += (float(mean) - float(num))**2 
    print str(squared_results/(len(diffs)-1)) + " squared results(variance)"
    
    print str(float((float(squared_results)/(len(diffs)-1))**0.5)) + "std deviation"
    return float((float(squared_results)/(len(diffs)-1))**0.5)



af = [9,4,6,3,12,7,9,5,6]
asd = [4,8,7,9,4,2,1,1,7]
q = [38946,43420, 49191,50430,50557,52580,53595,54135,60181,62076]
s = [18,20,21,18,23,15,17,22,21]

#this is here so you can copy and paste columns from Google Spreadsheets and place into an array/list
def column_to_list(file_name):
    with open(file_name):
    #with open(file_name) as f:
        lines = [float(line.rstrip('\n')) for line in open(file_name)]
        return lines
       
#can't remmeber why I wrote this
#outside = []
#for num in lines:
#    if (num < 155) or (num > 1014):
#        outside.append(num)
#print float(len(outside))/len(lines) + 1    

def z_score(x, arr):
    sd_sample = stan_dev_sample(arr)
    mean = mean_calc(arr)
    print str((mean - x)/sd_sample)
    return (mean - x)/sd_sample

dice = [1,2,3,4,5,6]
def sample_loop(dice):
    sample_dice = []
    for di in dice:
        for sec_di in dice:
            for three_di in dice:
                for four_di in dice:
                    for five_di in dice:
                        sample_dice.append((float(di)+float(sec_di)+float(three_di)+float(four_di)+float(five_di))/5.0)
    return sample_dice

def ci(sd, mean, size, ci_percent):
    std_error = sd/(size**0.5)
ls = [5,19,11,23,12,7,3,21]    

#stan_dev_diff(column_to_list('engage.txt'),column_to_list('engage2.txt'))
#stan_dev_sample(ls)
#mean_calc([8,9,12,13,14,16])

#stan_dev_sample(column_to_list('engage.txt'))

count2 = 0
newarr = []
for i in af:
    newarr.append(i - asd[count2])
    count2 += 1

def f_stat(*arg):
    #this function only works for sample groups of the same size
    
    samples_group = []
    for i in arg:
        samples_group.append(list(i))
    
    #calc df for bt groups
    df_bt = len(samples_group) - 1
    
    #calc df for within groups
    df_w = []
    for i in samples_group:
        df_w.append((len(i) - 1))
    df_within = sum(df_w)
    
    #collecting all samples into one list
    ind_samples = []
    for group in samples_group:
        for sample in group:
            ind_samples.append(sample)
    #calculate grand mean
    grand_mean = float(sum(ind_samples))/float(len(ind_samples))
    print "grand mean: " + str(grand_mean)
    
    #calculating means of each group
    group_means = []
    for group in samples_group:
        group_means.append(float(sum(group))/len(group))
    #calculating SS
    add_squared = []
    counter = 0
    for i in group_means:
        print "group mean " + str(counter + 1) +": " + str(i) 
        add_squared.append(((i - grand_mean)**2)*len(samples_group[counter]))
        counter += 1
    between_ss = sum(add_squared)
    print "in-between sum of squares: " + str(sum(add_squared))
    
    #calculate sum of squares within by subtracting each group mean from its ind samples, squaring and adding
    within_sum = []
    mean_count = 0
    for group in samples_group:
        for sample in group:
            #print sample
            #print (float(sample) - group_means[mean_count])**2
            within_sum.append((float(sample) - group_means[mean_count])**2)
        
        mean_count += 1
    within_ss = sum(within_sum)
    print "within sum of squares: " + str(sum(within_sum))
    print "MS-within: " + str(within_ss/df_within)
    #print df_within
    #calc f-stat
    f_stat = (between_ss/df_bt)/(within_ss/df_within)
    print "F-Stat: " + str(f_stat)
    
#f_stat([-8.,-11.,-17.,-9.,-10.,-5.], [12,9,16,8,15], [0.5,0.0,-1.0,1.5,0.5,-0.1,0])
#f_stat([6.,7.,8.,9.,10.], [4.,4.,6.,7.,9.], [2.,3.,4.,4.,7.])
a = [1.5,1.3,1.8,1.6,1.3]
b = [1.6,1.7,1.9,1.2]
c = [2.,1.4,1.5,1.5,1.8,1.7,1.4]
d = [2.9,3.1,2.8,2.7]
#f_stat(a,b,c,d)
#stan_dev_sample([8,7,10,6,9])
#stan_dev_sample([4,6,7,4,9])
#stan_dev_sample([4,4,7,2,3])