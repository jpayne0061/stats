from scipy import stats
import numpy
import itertools
#import webcrawler
#import stats
mileage = [11225, 11837, 15400, 20230, 20782, 21694, 22230, 22249, 22721, 22783, 22902, 23708, 24060, 24164, 24309, 24450, 25094, 25429, 25833, 25956, 26470, 26514, 26837, 27216, 27730, 27790, 28026, 28522, 28817, 29144, 29388, 29405, 29511, 29596, 29850, 30080, 30267, 30376, 30481, 30506, 30780, 30930, 31023, 31064, 31229]
prices = [20995, 21409, 17950, 16794, 16777, 18389, 17089, 16777, 18389, 17089, 18389, 17089, 18389, 18389, 18389, 17995, 15999, 16070, 17889, 17889, 17889, 16589, 17889, 17889, 17889, 17889, 17889, 16589, 17889, 16589, 17889, 17889, 17889, 17889, 16589, 17289, 22989, 17289, 17289, 17289, 17289, 17289, 17289, 17289, 17289]
age = [1,2,3,4]
banana = [2,4,6,9]

#list_of_files = ["../data_sets/age.txt", "../data_sets/party.txt", "../data_sets/pets.txt"]
list_of_files = ["../data_sets/longevity.txt", "../data_sets/gestation.txt"]

def column_to_list(file_name):
    with open(file_name):
    #with open(file_name) as f:
        lines = [float(line.rstrip('\n')) for line in open(file_name)]
        
        return lines

for x,y in itertools.combinations(list_of_files, 2):
    p = " pearson"
    
    print stats.pearsonr(column_to_list(x), column_to_list(y)), x, y, p
    
print stats.pearsonr(mileage, prices)
print stats.pearsonr(age, banana)