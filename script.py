# Import libraries
import codecademylib3
import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency
from scipy.stats import binom_test

# Read in the `clicks.csv` file as `abdata`
abdata = pd.read_csv('clicks.csv')

#1 checking the data
print(abdata.head(), '\n')

#2, 3 is there an association btw group and purchase? lest use chi-square test
Xtab = pd.crosstab(abdata.group, abdata.is_purchase)
print(Xtab,'\n')

#null: dont have an association
#althernative: have an association
chi2, pval, dof, expected = chi2_contingency(Xtab)
print('The p-value for group and purchase is:', pval, '\n')
#using a significance threshold of 0.05 i can reject the null hypothesis

#4 calculating the num of a visitors in a week
num_visits = len(abdata)
# print(num_visits)

#5, 6 calculating the number of sales that would be needed to reach 1000
num_sales_needed_099 = 1000/0.99
print('The num 0.99 sales needed to reach 1000 dollars are:', num_sales_needed_099, '\n')

p_sales_needed_099 = num_sales_needed_099/num_visits
print('The proportion of 0.99 buyers we need to reach the target are:', round(p_sales_needed_099, 4), '\n')

#7 repeating the last step to the other price points (1.99, 4.99)
num_sales_needed_199 = 1000/1.99
num_sales_needed_499 = 1000/4.99

print('The num 1.99 sales needed to reach 1000 dollars are:', round(num_sales_needed_199, 2), '\n')
print('The num 4.99 sales needed to reach 1000 dollars are:', round(num_sales_needed_499, 2), '\n')

p_sales_needed_199 = num_sales_needed_199/num_visits
p_sales_needed_499 = num_sales_needed_499/num_visits

print('The proportion of 1.99 buyers we need to reach the target are:', round(p_sales_needed_199, 4), '\n')
print('The proportion of 4.99 buyers we need to reach the target are:', round(p_sales_needed_499, 4), '\n')

#8 comparing if the percent of group A is significantly greater than p_sales_needed_099
samp_size_099 = np.sum(abdata.group == 'A')
sales_099 = np.sum((abdata.group == 'A') & (abdata.is_purchase == 'Yes'))
# print(sales_099)

samp_size_199 = np.sum(abdata.group == 'B')
samp_size_499 = np.sum(abdata.group == 'C')

sales_199 = np.sum((abdata.group == 'B') & (abdata.is_purchase == 'Yes'))
sales_499 = np.sum((abdata.group == 'C') & (abdata.is_purchase == 'Yes'))

#null: rate dont is significantly 'greater' than the purchase rate
#alternative: rate is significantly 'greater' than the purchase rate
pvalueA = binom_test(sales_099, n=samp_size_099, p=p_sales_needed_099, alternative='greater')

print('The p-value for group A is:', pvalueA,'\n')

#making the binomial test for the other 2 groups
pvalueB = binom_test(sales_199, n=samp_size_199, p=p_sales_needed_199, alternative='greater')
print('The p-value for group B is:', pvalueB,'\n')

pvalueC = binom_test(sales_499, n=samp_size_499, p=p_sales_needed_499, alternative='greater')
print('The p-value for group C is:', pvalueC,'\n')

#based on this analyse i can conclude the group that have a significantly ihgher purchase rate than the target is the C group, using the significance threshold of 0.05
