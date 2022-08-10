# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 09:46:15 2022
@author: Mehmet
"""
import numpy as np
import time
import random


#Job selection
def destiny():
    print('what job will you choose? (Available jobs: Farmer)')
    job = input(': ')
    job = job.lower()
    if job == 'farmer':
        print('Welcome to your new farmer life, never forget that you are one of the things that built civilization so lets begin!')
        Farmer.start_farmer()
    else:
        destiny()
class City:
    population = 10000
    
#Farmer job    
class Farmer(City):
    
  
    # property = {'field':1,'tiny_house':1}
    
    inv = {'money':15,'wheat_seed':5,'corn_seed':0,'cabbage_seed':0,'melon_seed':0,
                 'wheat':0,'corn':0,'cabbage':0,'melon':0}
    
    #where job begins
    def start_farmer():    
        
        print('Choose your action, 1-Check inventory, 2-Plant seed, 3-Check plants, 4-Sell, 5-Buy')
        time.sleep(1)
        choice = int(input())
        
        if not choice < 1 and choice > 5:
            Farmer.start_farmer()
        if choice == 1:   
            Farmer.show_inventory()
        if choice == 2:
             Farmer.plant_seed()
        if choice == 3:
            print('this feature will come soon')
            time.sleep(1)
            Farmer.start_farmer()
        if choice == 4:
            Farmer.sell()
        if choice == 5:
            Farmer.buy()
            
    #showing current inventory    
    def show_inventory():
        print(Farmer.inv)
        print('back to menu...')
        time.sleep(3)
        Farmer.start_farmer()
    
    #field for seeds, it will be updated soon
    class Field():
# =============================================================================
#             [x x x x x]         [w w w w w]  w = wheat  
#             [x x x x x]         [w x x x x]  x = empty
#             [x x x x x]   ->    [x x x x x]  field update(it will come soon)
#             [x x x x x]         [x x x x x] 
#             [x x x x x]         [x x x x x]   
# =============================================================================
        
        
        # field_size = np.array((5,5))
        field_size = 25
        empty_field_size = field_size
        wheat_seed_field = 0
        cabbage_seed_field = 0
        melon_seed_field = 0
        corn_seed_field = 0

    # function of planting seeds
    def plant_seed():
       print(f'which seed will you plant?\n 1)wheat seed (you have {Farmer.inv["wheat_seed"]}) \n 2)corn seed (you have: {Farmer.inv["corn_seed"]}) \n 3)cabbage seed (you have: {Farmer.inv["cabbage_seed"]}) \n 4)melon seed (you have: {Farmer.inv["melon_seed"]}')
       choice = int(input(': '))
       # if not choice == 'wheat_seed' and  choice == 'corn_seed' and choice == 'cabbage_seed' and choice == 'melon_seed':
           # Farmer.plant_seed()
           
       if choice == '1': 
           if Farmer.inv['wheat_seed'] > 0:
               print(f'how many seed will you plant? (you have {Farmer.inv["wheat_seed"]})')
               seed_count = int(input(': '))
               if seed_count == str:
                   Farmer.plant_seed()
               if seed_count > Farmer.inv['wheat_seed'] or seed_count < 0:
                   print('you dont have enough seed')
                   print('Returning to menu...')   
                   time.sleep(1)
                   Farmer.start_farmer() 
               Farmer.inv['wheat_seed'] -= seed_count
               Farmer.Field.field_size -= seed_count
               Farmer.Field.wheat_seed_field += seed_count
               print('Planting wheat seed...')
               time.sleep(2)
               print('Planted!')
               time.sleep(1)
               for c,i in enumerate(list(np.ones(seed_count)), 1):
                       success = random.randrange(0,100)
                       if success > 30:
                           print(f'{c}.crop have grown!')             
                           Farmer.inv['wheat'] += i*2
                           Farmer.Field.wheat_seed_field = 0                    
                           time.sleep(1)  
                       else:
                           print(f'{c}.crop planted was not successful...')  
           else:
               print('you dont have enough seed')
           print('Returning to menu...')   
           time.sleep(1)
           Farmer.start_farmer() 
       if choice == '2':
           if Farmer.inv['corn_seed'] > 0:
               print(f'how many seed will you plant? (you have {Farmer.inv["corn_seed"]})')
               seed_count = int(input(': '))
               if seed_count > Farmer.inv['corn_seed'] or seed_count < 0:
                   print('you dont have enough seed')
                   print('Returning to menu...')   
                   time.sleep(1)
                   Farmer.start_farmer() 
               Farmer.inv['corn_seed'] -= seed_count
               Farmer.Field.field_size -= seed_count
               Farmer.Field.corn_seed_field += seed_count
               print('Planting corn seed...')
               time.sleep(2)
               print('Planted!')     
               time.sleep(1)
               for c,i in enumerate(list(np.ones(seed_count)), 1):
                       success = random.randrange(0,100)
                       if success > 45:
                           print(f'{c}.crop have grown!')             
                           Farmer.inv['corn'] += i
                           Farmer.Field.corn_seed_field = 0                    
                           time.sleep(1) 
                           
                       else:
                           print(f'{c}.crop planted was not successful...')
               print('Returning to menu...')
               time.sleep(1)
               Farmer.start_farmer()             
       if choice == '3':
          if Farmer.inv['cabbage_seed'] > 0:
               print(f'how many seed will you plant? (you have {Farmer.inv["cabbage_seed"]})')
               seed_count = int(input(': '))
               if seed_count > Farmer.inv['cabbage_seed'] or seed_count < 0:
                   print('you dont have enough seed')
                   print('Returning to menu...')   
                   time.sleep(1)
                   Farmer.start_farmer() 
               Farmer.inv['cabbage_seed'] -= seed_count
               Farmer.Field.field_size -= seed_count
               Farmer.Field.cabbage_seed_field += seed_count
               print('Planting cabbage seed...')
               time.sleep(2)
               print('Planted!')
               time.sleep(1)
               for c,i in enumerate(list(np.ones(seed_count)), 1):
                       success = random.randrange(0,100)
                       if success > 45:
                           print(f'{c}.crop have grown!')             
                           Farmer.inv['cabbage'] += i
                           Farmer.Field.cabbage_seed_field = 0                    
                           time.sleep(1) 
                           
                       else:
                           print(f'{c}.crop planted was not successful...')
               print('Returning to menu...')
               time.sleep(1)
               Farmer.start_farmer() 
       if choice == '4':
           if Farmer.inv['melon_seed'] > 0:
                print(f'how many seed will you plant?  (you have {Farmer.inv["melon_seed"]})')
                seed_count = int(input(': '))
                if seed_count > Farmer.inv['melon_seed'] or seed_count < 0:
                    print('you dont have enough seed')
                    print('Returning to menu...')   
                    time.sleep(1)
                    Farmer.start_farmer()
                Farmer.inv['melon_seed'] -= seed_count
                Farmer.Field.field_size -= seed_count
                Farmer.Field.melon_seed_field += seed_count
                print('Planting melon seed...')
                time.sleep(2)
                print('Planted!')        
                time.sleep(1)
                for c,i in enumerate(list(np.ones(seed_count)), 1):
                        success = random.randrange(0,100)
                        if success > 55:
                            print(f'{c}.crop have grown!')             
                            Farmer.inv['melon'] += i*3
                            Farmer.Field.cabbage_seed_field = 0                    
                            time.sleep(1) 
                            
                        else:
                            print(f'{c}.crop planted was not successful...')
                print('Returning to menu...')
                time.sleep(1)
                Farmer.start_farmer()   
                
    # selling products            
    def sell():
        
        print('your inventory')
        print('---------------------------------------------')
        print(Farmer.inv)
        print('---------------------------------------------')
        print('what will you sell?')
        print('1)Wheat(10 $)\n2)Corn(15 $)\n3)Cabbage(20 $)\n4)Melon(30 $)\n0)Back to menu')
        choice = int(input(': '))
        if choice == 1:
           amount = int(input('how much will you sell wheat? '))
           if amount > Farmer.inv['wheat']:
               print('You dont have enough wheat seed')
               Farmer.sell()
           print(f'Selling {amount} wheat...') 
           time.sleep(2)
           # current_money = Farmer.inv['money']
           value = amount * 10
           Farmer.inv['money'] += value
           # current_wheat = Farmer.inv['wheat'] 
           Farmer.inv['wheat'] -= amount
           Farmer.sell()
        if choice == 2:
            amount = int(input('how much will you sell corn? '))
            if amount > Farmer.inv['corn']:
                print('You dont have enough corn seed')
                Farmer.sell()
            print(f'Selling {amount} corn...') 
            time.sleep(2)
            value = amount * 15
            Farmer.inv['money'] += value
            Farmer.inv['corn'] -= amount
            Farmer.sell()
        if choice == 3:
            amount = int(input('how much will you sell corn? '))
            if amount > Farmer.inv['cabbage']:
                print('You dont have enough cabbage seed')
                Farmer.sell()
            print(f'Selling {amount} cabbage...') 
            time.sleep(2)
            value = amount * 20
            Farmer.inv['money'] += value
            Farmer.inv['cabbage'] -= amount
            Farmer.sell()
        if choice == 4:
            amount = int(input('how much will you sell melon? '))
            if amount > Farmer.inv['melon']:
                print('You dont have enough melon seed')
                Farmer.sell()
            print(f'Selling {amount} melon...') 
            time.sleep(2)
            value = amount * 30
            Farmer.inv['money'] += value
            Farmer.inv['melon'] -= amount
            Farmer.sell()
        if choice == 0:
            Farmer.start_farmer()
            
           
        else:
            print('you dont have this')
            Farmer.sell()
    # buying seeds        
    def buy():
        print('your inventory')
        print('---------------------------------------------')
        print(Farmer.inv)
        print('---------------------------------------------')
        print('what will you buy?')
        print('1)Wheat seed(5 $)\n2)Corn seed(7.5 $)\n3)Cabbage seed(10 $)\n4)Melon seed(15 $)\n0)Back to menu')
        time.sleep(1)
        choice = int(input(': '))
        if choice == 1:
            amount = int(input('how much will you buy wheat seed?'))
            price = amount * 5
            print(f'Buying {amount} wheat seed...')    
            time.sleep(1)
            if price > Farmer.inv['money']:
                print('you dont have enough money')
                Farmer.buy()
            else:
                 Farmer.inv['wheat_seed'] += amount
                 Farmer.inv['money'] -= price
                 # Farmer.inv['money'] = current_money
                 Farmer.buy()
        if choice == 2:
            amount = int(input('how much will you buy corn seed?'))
            price = amount * 7.5
            print(f'Buying {amount} corn seed...')    
            time.sleep(1)
            if price > Farmer.inv['money']:
                print('you dont have enough money')
                Farmer.buy()
            else:
                 Farmer.inv['corn_seed'] += amount
                 Farmer.inv['money'] -= price

                 Farmer.buy()
        if choice == 3:
            amount = int(input('how much will you buy cabbage seed?'))
            price = amount * 10
            print(f'Buying {amount} cabbage seed...')    
            time.sleep(1)
            if price > Farmer.inv['money']:
                print('you dont have enough money')
                Farmer.buy()
            else:
                 Farmer.inv['cabbage_seed'] += amount
                 Farmer.inv['money'] -= price
          
                 Farmer.buy()
        if choice == 4:
            amount = int(input('how much will you buy melon seed?'))
            price = amount * 15
            print(f'Buying {amount} melon seed...')    
            time.sleep(1)
            if price > Farmer.inv['money']:
                print('you dont have enough money')
                Farmer.buy()
            else:
                 Farmer.inv['melon_seed'] += amount
                 Farmer.inv['money'] -= price
         
        if choice == 0:
            print('backing to menu...')
            time.sleep(1)
            Farmer.start_farmer()
destiny()
