#Name - Tota Anumita Dayal
#Date - 02/22/2020
#Time taken - 20 minutes
#Version of Python - 2.7.15
#This code will names of countries and number of refugees

countrypop = dict()
countrypop['Chad'] = 16504+12062+15162+28932+18947+12624+17380+13315+15557+26786+22358+14921+12402+15260
countrypop['India'] = 69609
countrypop['Jordan'] = 0
countrypop['Yemen'] = 9298
countrypop['Rwanda'] = 17732+17978

global_names = []
global_pop = []

def country_name():
    for names in countrypop.keys():
        print(names)
        global_names.append(names)
country_name()

def population_values():
    for values in countrypop.values():
        print(values)
        global_pop.append(values)
population_values()

for i in range(len(global_pop)):
    print('Country '+global_names[i]+' has '+str(global_pop[i])+' refugees')



         
