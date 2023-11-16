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
class Farmer():
    
  
    property = {'field':1,'tiny_house':1}

    inv = {'money':15,'wheat_seed':15,
           'corn_seed':0,'cabbage_seed':0,
           'melon_seed':0,'wheat':0,'corn':0,'cabbage':0,'melon':0,'dought':0,'bread':0,'retirement_p':3}
    
    
                
    #where job begins
    def start_farmer():    
        
        print('Choose your action, 1-Check inventory, 2-Plant seed, 3-Check plants, 4-Sell, 5-Buy, 6-Crafting, 7-Retirement')
        time.sleep(1)

        try: 
            choice = int(input(": "))
        except ValueError:    
            print("you typing wrong!")
            Farmer.start_farmer()
        
        
        
        if choice < 1 or choice > 7:
            print("you typing wrong")
            Farmer.start_farmer()
        if choice == 1:   
            print("INVENTORY")
            for k,v in Farmer.inv.items():
                if v == 0:
                    pass
                else:
                   print(f"|{k}  ({v}) ")
            print('----------------------')       
            print('PROPERTY')
            for k,v in Farmer.property.items():
                if v == 0:
                    pass
                else:
                   print(f"|{k}  ({v}) ")       
            time.sleep(2)
            Farmer.start_farmer()
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
        if choice == 6:
            Farmer.crafting()    
        if choice == 7:
            Farmer.retirement()    

    #showing current inventory    

    
    #field for seeds, it will be updated soon
    sm = property['field'] 
    field_size = 25 * sm
    empty_field_size = field_size
    wheat_seed_field = 0
    cabbage_seed_field = 0
    melon_seed_field = 0
    corn_seed_field = 0
    
   # class Field():
    
# =============================================================================
#             [x x x x x]         [w w w w w]  w = wheat  
#             [x x x x x]         [w x x x x]  x = empty
#             [x x x x x]   ->    [x x x x x]  field update(it will come soon)
#             [x x x x x]         [x x x x x] 
#             [x x x x x]         [x x x x x]   
# =============================================================================
        # field_size = np.array((5,5))
    

    # function of planting seeds
    def plant_seed():
       print("")
       print('PLANT')
       print(f'|which seed will you plant?\n 1)wheat seed (you have {Farmer.inv["wheat_seed"]}) \n 2)corn seed (you have: {Farmer.inv["corn_seed"]}) \n 3)cabbage seed (you have: {Farmer.inv["cabbage_seed"]}) \n 4)melon seed (you have: {Farmer.inv["melon_seed"]} \n 0) Back to menu')
       try:
           choice = int(input())
       except ValueError:
           print("|you typing wrong!")
           Farmer.plant_seed()    
      
     
       # if not choice == 'wheat_seed' and  choice == 'corn_seed' and choice == 'cabbage_seed' and choice == 'melon_seed':
           # Farmer.plant_seed() 

       if choice < 0 or choice > 5:
           Farmer.plant_seed()    
       if choice == 0:
           print('|backing to menu...')
           time.sleep(1)
           Farmer.start_farmer() 
       if choice == 1: 
           if Farmer.inv['wheat_seed'] > 0:
               
               print(f'|how many seed will you plant? (you have {Farmer.inv["wheat_seed"]})')
               try: 
                  seed_count = int(input(": "))
               except ValueError:    
                  print("|you typing wrong!")
                  Farmer.start_farmer()      

               if Farmer.inv['wheat_seed'] == 0:
                  print('|you dont have enough seed')
                  print('|Returning to menu...')   
                  time.sleep(1)
                  Farmer.start_farmer() 
                
               if seed_count > Farmer.inv['wheat_seed'] or seed_count < 0:
                   print('|you dont have enough seed')
                   print('|Returning to menu...')   
                   time.sleep(1)
                   Farmer.start_farmer()
               print(Farmer.field_size)
               print(Farmer.property['field'])
               if  seed_count > Farmer.field_size * Farmer.property['field']: 
                   print('|you dont have enough field')
                   time.sleep(1)
                   Farmer.plant_seed()
               else:  
                    print('|Planting wheat seed...')
                    time.sleep(2)
                    print('|Planted!')
                    time.sleep(1) 
                    Farmer.inv['wheat_seed'] -= seed_count
                    Farmer.empty_field_size -= seed_count
                    Farmer.wheat_seed_field += seed_count

          


               for c,i in enumerate(list(np.ones(seed_count)), 1):
                       success = random.randrange(0,100)
                       
                       if success > 30:
                           print(f'|        {c}.crop have grown!')             
                           Farmer.inv['wheat'] += i*2
                           Farmer.wheat_seed_field = 0                    
                           time.sleep(0.1)   

                       else:
                           print(f'|        {c}.crop was not successful...')  
                           time.sleep(0.1) 
                           
               print("|returning to menu...")
               time.sleep(1)
               Farmer.empty_field_size = Farmer.field_size
               Farmer.plant_seed()
               
       if choice == 2:
           
           if Farmer.inv['corn_seed'] > 0:
               print(f'|how many seed will you plant? (you have {Farmer.inv["corn_seed"]})')

               try: 
                  seed_count = int(input(": "))
               except ValueError:    
                  print("|you typing wrong!")
                  Farmer.start_farmer()      

               if seed_count > Farmer.inv['corn_seed'] or seed_count < 0:
                   print('|you dont have enough seed')
                   print('|Returning to menu...')   
                   time.sleep(1)
                   Farmer.start_farmer() 
                
               
               if  seed_count > Farmer.field_size * Farmer.property['field']: 
                   print('|you dont have enough field')
                   time.sleep(1)
                   Farmer.plant_seed()
               else:  
                    Farmer.inv['corn_seed'] -= seed_count
                    Farmer.empty_field_size -= seed_count
                    Farmer.wheat_seed_field += seed_count


               print('|Planting corn seed...')
               time.sleep(2)
               print('|Planted!')     
               time.sleep(1)
               for c,i in enumerate(list(np.ones(seed_count)), 1):
                       success = random.randrange(0,100)
                       if success > 30:
                           print(f'|{c}.crop have grown!')             
                           Farmer.inv['corn'] += i
                           Farmer.corn_seed_field = 0                    
                           time.sleep(0.1) 
                           
                       else:
                           print(f'|{c}.crop planted was not successful...')
                           time.sleep(0.1) 
               print('|Returning to menu...')
               time.sleep(1)
               Farmer.empty_field_size = Farmer.field_size
               Farmer.plant_seed()             

       if choice == 3:
          
          if Farmer.inv['cabbage_seed'] > 0:
               print(f'|how many seed will you plant? (you have {Farmer.inv["cabbage_seed"]})')

               try: 
                  seed_count = int(input(": "))
               except ValueError:    
                  print("|you typing wrong!")
                  Farmer.start_farmer()      

               if seed_count > Farmer.inv['cabbage_seed'] or seed_count < 0:
                   print('|you dont have enough seed')
                   print('|Returning to menu...')   
                   time.sleep(1)
                   Farmer.start_farmer() 

              
               if  seed_count > Farmer.field_size * Farmer.property['field']: 
                   print('|you dont have enough field')
                   time.sleep(1)
                   Farmer.plant_seed()
               else:  
                    Farmer.inv['cabbage_seed'] -= seed_count
                    Farmer.empty_field_size -= seed_count
                    Farmer.wheat_seed_field += seed_count

               print('|Planting cabbage seed...')
               time.sleep(2)
               print('|Planted!')
               time.sleep(1)

               for c,i in enumerate(list(np.ones(seed_count)), 1):
                       success = random.randrange(0,100)
                       if success > 30:
                           print(f'|{c}.crop have grown!')             
                           Farmer.inv['cabbage'] += i
                           Farmer.cabbage_seed_field = 0                    
                           time.sleep(0.1) 
                           
                       else:
                           print(f'|{c}.crop planted was not successful...')
                           time.sleep(0.1) 
            
               print('|Returning to menu...')
               time.sleep(1)
               Farmer.empty_field_size = Farmer.field_size
               Farmer.start_farmer() 
               
       if choice == 4:
           if Farmer.inv['melon_seed'] > 0:
                print(f'|how many seed will you plant?  (you have {Farmer.inv["melon_seed"]})')
                try: 
                  seed_count = int(input(": "))
                except ValueError:    
                  print("|you typing wrong!")
                  Farmer.start_farmer()      

                if seed_count > Farmer.inv['melon_seed'] or seed_count < 0:
                    print('|you dont have enough seed')
                    print('|Returning to menu...')   
                    time.sleep(1)
                    Farmer.start_farmer()

                
                if  seed_count > Farmer.field_size * Farmer.property['field']: 
                   print('|you dont have enough field')
                   time.sleep(1)
                   Farmer.plant_seed()
                else:  
                    Farmer.inv['melon_seed'] -= seed_count
                    Farmer.empty_field_size -= seed_count
                    Farmer.wheat_seed_field += seed_count

                print('|Planting melon seed...')
                time.sleep(2)
                print('|Planted!')        
                time.sleep(1)
                for c,i in enumerate(list(np.ones(seed_count)), 1):
                        success = random.randrange(0,100)
                        if success > 45:
                            print(f'|{c}.crop have grown!')             
                            Farmer.inv['melon'] += i*3
                            Farmer.cabbage_seed_field = 0                    
                            time.sleep(0.1) 
                            
                        else:
                            print(f'|{c}.crop planted was not successful...')
                            time.sleep(0.1) 
                print('|Returning to menu...')
                time.sleep(1)
                Farmer.empty_field_size = Farmer.field_size
                Farmer.start_farmer()   
                
    # selling products            
    def sell():
        print("")
        print("SELLING")
        print(f"|Balance {Farmer.inv['money']}")
        print('|what will you sell?')
        print('|Sell Menu')
        print(f'|1)Wheat (0.5 $) ({Farmer.inv["wheat"]}) \n|2)Corn (1 $) ({Farmer.inv["corn"]})\n|3)Cabbage (1.25 $) ({Farmer.inv["cabbage"]})\n|4)Melon (3 $) ({Farmer.inv["melon"]}) \n|5)Bread (5$) ({Farmer.inv["bread"]})\n|0)Back to menu')

        try:
           choice = int(input())
        except ValueError:
           print("|you typing wrong!")
           Farmer.sell()    
        if choice < 0 or choice > 5:
            print("|you typing wrong!")
            Farmer.sell()
            
        if choice == 1:
           try: 
                  print('|enter a amount:')
                  amount = int(input(": "))
           except ValueError:    
                  print("|you typing wrong!")
                  Farmer.start_farmer()      
           if amount > Farmer.inv['wheat']:
               print('|You dont have enough wheat seed')
               Farmer.sell()
           print(f'|Selling {amount} wheat...') 
           time.sleep(2)
           # current_money = Farmer.inv['money']
           value = amount * 0.5
           Farmer.inv['money'] += value
           # current_wheat = Farmer.inv['wheat'] 
           Farmer.inv['wheat'] -= amount
           Farmer.sell()

        if choice == 2:
            try: 
                  print('|enter a amount:')
                  amount = int(input(": "))
            except ValueError:    
                  print("|you typing wrong!")
                  Farmer.start_farmer()      
            if amount > Farmer.inv['corn']:
                print('|You dont have enough corn seed')
                Farmer.sell()
            print(f'|Selling {amount} corn...') 
            time.sleep(2)
            value = amount * 1
            Farmer.inv['money'] += value
            Farmer.inv['corn'] -= amount
            Farmer.sell()

        if choice == 3:
            try: 
                  print('|enter a amount:')
                  amount = int(input(": "))
            except ValueError:    
                  print("|you typing wrong!")
                  Farmer.start_farmer()      
            if amount > Farmer.inv['cabbage']:
                print('|You dont have enough cabbage seed')
                Farmer.sell()
            print(f'|Selling {amount} cabbage...') 
            time.sleep(2)
            value = amount * 1.25
            Farmer.inv['money'] += value
            Farmer.inv['cabbage'] -= amount
            Farmer.sell()

        if choice == 4:
            try: 
                  print('|enter a amount:')

                  amount = int(input(": "))
            except ValueError:    
                  print("|you typing wrong!")
                  Farmer.start_farmer()   

            if amount > Farmer.inv['melon']:
                print('|You dont have enough melon seed')
                Farmer.sell()
            print(f'|Selling {amount} melon...') 
            time.sleep(2)
            value = amount * 3
            Farmer.inv['money'] += value
            Farmer.inv['melon'] -= amount
            Farmer.sell()
        
        if choice == 5:
            try:
                print('|enter a amount:')
                amount = int(input(": "))
            except ValueError:
                print('|you typing wrong!')

            try:
                Farmer.inv['bread']
            except KeyError:
                print('|you dont have a bread')
                time.sleep(1)
                Farmer.start_farmer()   

            if amount > Farmer.inv['bread']:
                print('|you dont  have enough bread')
                time.sleep(1)
                Farmer.sell()
            print(f'|selling {amount} bread...')
            time.sleep(2)
            value = amount * 5
            Farmer.inv['money'] += value
            Farmer.inv['bread'] -= amount    


        if choice == 0:
            Farmer.start_farmer()
           
        else:
            print('|you dont have this')
            Farmer.sell()
    # buying         
    def buy():
        print("")
        print('BUY')
        print(f"|Balance: {Farmer.inv['money']}")
        print('|what will you buy?')
        print('|1)Seeds 2)Properties 0)Exit')
        

        time.sleep(1)

        try:
           choice = int(input())
        except ValueError:
           print("|you typing wrong!")
           Farmer.buy()    
        if choice < 0 or choice > 2:
           print("|you typing wrong!")
           Farmer.buy()  

        if choice == 0:
            print('returning to menu...')
            time.sleep(1)
            Farmer.start_farmer()

        if choice == 1:
          
            if choice < 0 or choice > 2:
                print("|you typing wrong!")
                Farmer.buy()

            if choice == 0:
                print("backing to menu...")
                time.sleep(1)
                Farmer.start_farmer()

            if choice == 1:
                print('|1)Wheat seed(0.25 $)\n2)Corn seed(0.75 $)\n3)Cabbage seed(1 $)\n4)Melon seed(2 $)\n0)Back to menu')
                try: 
                    choice = int(input(": "))
                except ValueError:    
                    print("|you typing wrong!")
                    Farmer.plant_seed()      

                if choice == 0:
                    print('|backing to menu...')
                    time.sleep(1)
                    Farmer.start_farmer()

                if choice == 1:    
                    try: 
                        amount = int(input(": "))
                    except ValueError:    
                        print("|you typing wrong!")
                        Farmer.start_farmer() 

                    price = amount * 0.25
                    print(f'|Buying {amount} wheat seed...')    
                    time.sleep(1)
                    if price > Farmer.inv['money']:
                        print('|you dont have enough money')
                        time.sleep(1)
                        Farmer.buy()
                
                    Farmer.inv['wheat_seed'] += amount
                    Farmer.inv['money'] -= price
                    # Farmer.inv['money'] = current_money
                    Farmer.buy()

                if choice == 2:
                    try: 
                        amount = int(input(": "))
                    except ValueError:    
                        print("|you typing wrong!")
                        Farmer.start_farmer()      

                    price = amount * 0.75
                    print(f'|Buying {amount} corn seed...')    
                    time.sleep(1)

                    if price > Farmer.inv['money']:
                        print('|you dont have enough money')
                        time.sleep(1)
                        Farmer.buy()
                
                    Farmer.inv['corn_seed'] += amount
                    Farmer.inv['money'] -= price
                    Farmer.buy()

                if choice == 3:

                    try: 
                        amount = int(input(": "))
                    except ValueError:    
                        print("|you typing wrong!")
                        Farmer.start_farmer()  
                    
                    price = amount * 1
                    print(f'|Buying {amount} cabbage seed...')    
                    time.sleep(1)
            
                    if price > Farmer.inv['money']:
                        print('|you dont have enough money')
                        time.sleep(1)
                        Farmer.buy()

                
                    Farmer.inv['cabbage_seed'] += amount
                    Farmer.inv['money'] -= price
                    Farmer.buy()

                if choice == 4:

                    try: 
                        amount = int(input(": "))
                    except ValueError:    
                        print("|you typing wrong!")
                        Farmer.start_farmer()  
                    
                    price = amount * 2
                    print(f'|Buying {amount} melon seed...')    
                    time.sleep(1)
                    

                    if price > Farmer.inv['money']:
                        print('|you dont have enough money')
                        time.sleep(1)
                        Farmer.buy()
                
                Farmer.inv['melon_seed'] += amount
                Farmer.inv['money'] -= price
                Farmer.buy()
            
            

        if choice == 2:
            print("PROPERTY")
            print("1)Field $350 2)Info 0)Exit")        
            try: 
                choice = int(input(": "))
            except ValueError:    
                    print("|you typing wrong!")
            if choice < 0 or choice > 2:
                print("|you typing wrong!")
                Farmer.buy()
            if choice == 0:
                print("returning menu...")
                Farmer.start_farmer()

            if choice == 1:

                try: 
                    print("how much you wanna buy?")
                    amount = int(input(": "))
                except ValueError:    
                    print("|you typing wrong!")
                    Farmer.start_farmer()  
                    
                price = amount * 350
                print(f'|Buying {amount} amount of field..')    
                time.sleep(1)

                if price > Farmer.inv['money']:
                    print('|you dont have enough money')
                    time.sleep(1)
                    Farmer.buy()
                
                Farmer.property['field'] += amount
                Farmer.inv['money'] -= price
                Farmer.buy() 

            if choice == 2:
                print('Field increases your plant area (25 unit)')
                time.sleep(1)
                Farmer.buy()
                    
    # crafting
    def crafting():
        print("")
        print('CRAFT')
        print("|1)food 2)exit")
        
        try:
           choice = int(input())
        except ValueError:
           print("|you typing wrong!")
           Farmer.crafting()    

        if choice < 1 or choice > 2:
            print("|you typing wrong!")
            Farmer.crafting()

        if choice == 1:
          print("|1)Dough(3 Wheat)\n2)Bread(1 Dough)\n")

          try:
           choice = int(input())
          except ValueError:
           print("|you typing wrong!")
           Farmer.crafting()    

          if choice < 1 or choice > 2:
           print("|you typing wrong!")
           time.sleep(1)

          if choice == 1:
              
              print(f"|how many dough will you make? (you have {Farmer.inv['wheat']} wheat)")

              try:
                 n = int(input())
              except ValueError:
                print("|you typing wrong!")
                Farmer.crafting()   

              if Farmer.inv['wheat'] < 3*n:
                  print("|you dont have enough wheat")
                  time.sleep(1)
                  Farmer.start_farmer() 


              Farmer.inv['wheat'] -= 3*n
              print(f"|You maked {n} dought!")
              time.sleep(1)
              Farmer.inv['dought'] += n
              s = 0 + Farmer.inv['dought']
              Farmer.crafting()

          
          if choice == 2:
              
              print(f"|how many bread will you make? (you have {Farmer.inv['dought']} dought)")

              try:
                 n = int(input())
              except ValueError:
                print("|you typing wrong!")
                Farmer.crafting()
              
              if Farmer.inv['dought'] < 1*n:
                  print("|you dont have enough dought")
                  time.sleep(1)
                  Farmer.start_farmer()

              Farmer.inv['dought'] -= 1*n
              print(f'|You maked {n} bread!')
              time.sleep(1)
              Farmer.inv['bread'] += n
              s = 0 + Farmer.inv['dought']
              Farmer.crafting()

        if choice == 2:

            print("|returning to menu...")    
            time.sleep(1)  
            Farmer.start_farmer()
        pass        

    # end of the game
    def retirement():
        print("")
        print('RETIREMENT')
        print(f'|You must pay 1000$ for retirement debt (you must pay {Farmer.inv["retirement_p"]} more!)')
        print("|you wanna pay? (1-yes 2-no)")

        try:
           choice = int(input())
        except ValueError:
           print("|you typing wrong!")
           Farmer.retirement()   
        if choice < 1 or choice > 2:
            print("|you typing wrong!")
            Farmer.retirement()

        if choice == 1:

            if Farmer.inv['money'] < 1000:
                print("|you dont have enough money!")
                Farmer.retirement()
            Farmer.inv['money'] -= 1000
            Farmer.inv['retirement_p'] -= 1
            print(f"|Congrats! you paid debt! ")

        elif Farmer.inv['retirement_p'] == 0:
            print("|You paid all of your retirement debt, you can rest all of your life")
            print("|1-rest? 2-NO")
            while not ValueError:
                    try:
                        choice = int(input())
                    except ValueError:
                        print("|you typing wrong!")
                        print("|you paid all of your retirement debt, you can rest")
                        print("|1-rest? 2-NO")

                        if choice == 2:
                            print("|returning to menu...")
                            time.sleep(1)
                            Farmer.start_farmer()

        if choice == 2:
            print("|returning to menu...")
            time.sleep(1)
            Farmer.start_farmer()

#Lumberjack
class Lumberjack(City):
    pass
    # [][][][][][][]
    #def chop():
     #   a,s,d,f,g,h,j,k = random.randint(0,7)
      #  while i == x:
       #   print(f"[{}][{}][{}][{}][{}][{}][{}][{}][{}]")
        
destiny()
