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
    if job == 'farmer' or '1':
        print('Welcome to your new farmer life, never forget that you are one of the things that built civilization so lets begin!')
        Farmer.start_farmer()
    else:
        destiny()

class City:
    population = 10000
    
#Farmer job    
class Farmer():

    # luck 
    l = 0
    price_scythe,price_shovel,price_hoe = 0,0,0
    
    # rent

    d = 30
    rent = 150
    
    # leveling
    
    level = 1
    level_maxp = 2500
    level_curxp = 0

    equipment = {'scythe':0,'shovel':0,'hoe':0} 

    property = {'field':1,'tiny_house':1,'truck':0,}

    inv = {'money':50,'wheat_seed':10,
           'corn_seed':0,'cabbage_seed':0,
           'melon_seed':0,'wheat':0,'corn':0,'cabbage':0,'melon':0,'dought':0,'bread':0,'retirement_p':3}
    
    
                
    #where job begins
    def start_farmer():    
        
        print('Choose your action, 1-Check inventory, 2-Planting seed, 3-Character status, 4-Sell, 5-Buy, 6-Crafting, 7-Retirement, 8-Rent')
        time.sleep(1)

        try: 
            choice = int(input(": "))
        except ValueError:    
            print("you typing wrong!")
            Farmer.start_farmer()
        
        
        
        if choice < 1 or choice > 8:
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
            Farmer.character_s()

        if choice == 4:
            Farmer.sell()

        if choice == 5:
            Farmer.buy()

        if choice == 6:
            Farmer.crafting()

        if choice == 7:
            Farmer.retirement()

        if choice == 8:
            Farmer.rent()
    
                

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
    
    def rent():

        print(f"your rent payment is 150$ (Current money: {Farmer.inv['money']})")
        print(f"you will pay after {Farmer.d} turn, otherwise you will lose your tiny home ")
        print("1-Pay 0-Exit")

        try: 
            choice = int(input(": "))
        except ValueError:    
                print("|you typing wrong!")
                Farmer.start_farmer()

        if choice == 1:
            if Farmer.d > 3:
                print("You still have time to pay, come back when your day has come. ")
                time.sleep(2)
                Farmer.start_farmer()

            if Farmer.inv['money'] < 150:
                print("you dont have enough money")
                time.sleep(1)
                Farmer.start_farmer()
            print("Paying rent...")
            Farmer.inv['money'] -= 150
            Farmer.d += 30
        if choice == 0:
            print("returning menu...")
            time.sleep(1)
            Farmer.start_farmer()

            
    # function of planting seeds
    def plant_seed():
       print("")
       print('PLANT')
       print(f'|which seed will you plant?\n 1)wheat seed (you have {Farmer.inv["wheat_seed"]}) \n 2)corn seed (you have: {Farmer.inv["corn_seed"]} (level 3) ) \n 3)cabbage seed (you have: {Farmer.inv["cabbage_seed"]} (level 5) ) \n 4)melon seed (you have: {Farmer.inv["melon_seed"]} (level 8) )\n 0) Back to menu')

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
               exptotal = 0
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
                           
                           exptotal += 25
                           Farmer.level_curxp += 25

                           time.sleep(0.1)
                           

                       else:
                           print(f'|        {c}.crop was not successful...') 
                           exptotal += 5
                           Farmer.level_curxp += 5 
                           time.sleep(0.1) 
                                   

               print(f"you gained {exptotal} experience...")                                 
               print("|returning to menu...")
               time.sleep(1)
               Farmer.empty_field_size = Farmer.field_size

               Farmer.d -= random.randint(1,3)   
               if Farmer.d <= 5:
                    print(f"you must pay in {Farmer.d} turn, otherwise you will lose your tiny home")
               time.sleep(3)
               
               if Farmer.d <= 0:
                   print("You kicked out from your house, you LOSE")
                   exit()
               
               Farmer.plant_seed()
              
               
       if choice == 2:
           
           if not Farmer.level >= 3:
               print("Your level is not enough")
               time.sleep(1)
               Farmer.plant_seed()

           if Farmer.inv['corn_seed'] > 0:
               exptotal = 0
               print(f'|how many seed will you plant? (you have {Farmer.inv["corn_seed"]})')

               try: 
                  seed_count = int(input(": "))
               except ValueError:    
                  print("|you typing wrong!")
                  Farmer.start_farmer() 
                  

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
                       success = random.randrange(0,100) + Farmer.l
                       if success > 30: 
                           print(f'|{c}.crop have grown!')     
                           exptotal += 50        
                           Farmer.level_curxp += 50
                           Farmer.inv['corn'] += i
                           Farmer.corn_seed_field = 0                    
                           time.sleep(0.1) 
                           
                       else:
                           print(f'|{c}.crop planted was not successful...')
                           exptotal += 5
                           Farmer.level_curxp += 5
                           time.sleep(0.1) 

               print(f"you gained {exptotal} experience...")                
               print('|Returning to menu...')
               time.sleep(1)
               Farmer.empty_field_size = Farmer.field_size
               Farmer.d -= random.randint(1,3)                
               if Farmer.d <= 5:
                    print(f"you must pay after {Farmer.d} turn, otherwise you will lose your tiny home")
                    time.sleep(3)
               
               if Farmer.d <= 0:
                   print("You kicked out from your house, you LOSE")
                   exit
                   
               Farmer.plant_seed()   

       if choice == 3:
          
          if not Farmer.level >= 5:
               print("Your level is not enough")
               time.sleep(1)
               Farmer.plant_seed()


          if Farmer.inv['cabbage_seed'] > 0:
               exptotal = 0
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
                       success = random.randrange(0,100) + Farmer.l
                       if success > 30:
                           print(f'|{c}.crop have grown!')  
                           exptotal += 100 
                           Farmer.level_curxp += 100          
                           Farmer.inv['cabbage'] += i
                           Farmer.cabbage_seed_field = 0                    
                           time.sleep(0.1) 
                           


                       else:
                           print(f'|{c}.crop planted was not successful...')
                           exptotal += 5
                           Farmer.level_curxp += 5
                           time.sleep(0.1) 

               print(f"you gained {exptotal} experience...")      
               print('|Returning to menu...')
               time.sleep(1)
               Farmer.empty_field_size = Farmer.field_size
               Farmer.d -= random.randint(1,3)   
               if Farmer.d <= 3:
                    print(f"you must pay in {Farmer.d} turn, otherwise you will lose your tiny home")
                    time.sleep(3)
               
               if Farmer.d <= 0:
                   print("You kicked out from your house, you LOSE")
                   exit()
               
               Farmer.plant_seed()   
       if choice == 4:
           
           if not Farmer.level >= 8:
               print("Your level is not enough")
               time.sleep(1)
               Farmer.plant_seed()

           if Farmer.inv['melon_seed'] > 0:
                exptotal = 0
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
                        success = random.randrange(0,100) + Farmer.l
                        if success > 85:
                            print(f'|{c}.crop have grown!')     
                            exptotal += 150
                            Farmer.level_curxp += 150        
                            Farmer.inv['melon'] += i*3
                            Farmer.cabbage_seed_field = 0                    
                            time.sleep(0.1) 
                            
                        else:
                            print(f'|{c}.crop planted was not successful...')
                            exptotal += 5
                            Farmer.level_curxp += 5
                            time.sleep(0.1) 

                print(f"you gained {exptotal} experience...")                  
                print('|Returning to menu...')
                time.sleep(1)
                Farmer.empty_field_size = Farmer.field_size
                Farmer.d -= random.randint(1,3)      
                if Farmer.d <= 4:
                    print(f"you must pay in {Farmer.d} turn, otherwise you will lose your tiny home")
                    time.sleep(3)
                
                if Farmer.d <= 0:
                   print("You kicked out from your house, you LOSE")
                   exit()

                 
                Farmer.plant_seed()      
    # selling products            
    def sell():
        print("")
        print("SELLING")
        print(f"|Balance {Farmer.inv['money']}")
        print('|what will you sell?')
        print('|Sell Menu')
        print(f'|1)Wheat (0.5 $) ({Farmer.inv["wheat"]}) \n|2)Corn (1 $) ({Farmer.inv["corn"]})\n|3)Cabbage (1.25 $) ({Farmer.inv["cabbage"]})\n|4)Melon (10 $) ({Farmer.inv["melon"]}) \n|5)Bread (5$) ({Farmer.inv["bread"]})\n|0)Back to menu')

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
            value = amount * 10
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
            value = amount * 4.5
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
        print('|1)Seeds 2)Equipments 3)Properties (level 5) \n 0)Exit')

        

        time.sleep(1)

        try:
           choice = int(input())
        except ValueError:
           print("|you typing wrong!")
           Farmer.buy()    
        if choice < 0 or choice > 2:
            print("you typing wrong")
            time.sleep(1)
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
                print(f"| balance: {Farmer.inv['money']}")
                print('| 1)Wheat seed(0.25 $)\n2)Corn seed(0.50 $) (level 3)\n3)Cabbage seed(1 $) (level 5)\n4)Melon seed(2 $) (level 8) \n0)Back to menu')
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
                        print("how many you will buy?")
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
                    
                    if not Farmer.level >= 3:
                        print("Your level is not enough")
                        time.sleep(1)
                        Farmer.buy()
                    try: 
                        print("how many you will buy?")
                        amount = int(input(": "))
                    except ValueError:    
                        print("|you typing wrong!")
                        Farmer.start_farmer()      

                    price = amount * 0.50
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
                    
                    if not Farmer.level >= 5:
                        print("Your level is not enough")
                        time.sleep(1)
                        Farmer.buy()
                    try: 
                        print("how many you will buy?")
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
                    
                    if not Farmer.level >= 8:
                        print("Your level is not enough")
                        time.sleep(1)
                        Farmer.buy()

                    try: 
                        print("how many you will buy?")
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
           
           print(f"| balance: {Farmer.inv['money']}")
           print(f'|1)Scythe (${85 * Farmer.equipment['scythe'] + }) (+3) (level 2) 2)Shovel (${Farmer.price_shovel * Farmer.equipment['shovel'] + 0.5 }) (+5) (level 5) 3)Hoe (${Farmer.price_hoe * Farmer.equipment['hoe'] + 0.5 }) (+10) (level 10) 0)Exit')
           try:
               choice = int(input())
           except ValueError:
               print("|you typing wrong!")
               Farmer.buy()    
           if choice < 0 or choice > 3:
                print("|You typing wrong!.")
                Farmer.buy()

           if choice == 1:
               if Farmer.inv['money'] >= Farmer.price_scythe:
                   print('you dont have enough money')
                   time.sleep(1)
                   Farmer.buy()
               print("Buying...")
               print("Your chances have increased by 3%!")
               Farmer.equipment['scythe'] += 1
               if Farmer.equipment['scythe'] == 1:
                   Farmer.
               Farmer.l += 3

           if choice == 2:
               if Farmer.inv['money'] >= 150:
                   print('you dont have enough money')
                   time.sleep(1)
                   Farmer.buy()
               print("Buying...")
               print("Your chances have increased by 5%!")
               Farmer.l += 5

           if choice == 3:
               if Farmer.inv['money'] >= 500:
                   print('you dont have enough money')
                   time.sleep(1)
                   Farmer.buy()
               print("Buying...")
               print("Your chances have increased by 10%!")
               Farmer.l += 10

           if choice == 0:
               print('Returning menu...')
               time.sleep(1)
               Farmer.buy()

        if choice == 3:

            if not Farmer.level >= 5:
               print("Your level is not enough")
               time.sleep(1)
               Farmer.buy()

            print("PROPERTY")
            print(f"1)Field ${350*Farmer.property['field']} 2)Info 0)Exit")        
            try: 
                choice = int(input(": "))
            except ValueError:    
                    print("|You typing wrong!.")
            if choice < 0 or choice > 2:
                print("|You typing wrong!.")
                Farmer.buy()
            if choice == 0:
                print("returning menu...")
                Farmer.start_farmer()

            if choice == 1:

                try: 
                    print("How much you wanna buy?")
                    amount = int(input(": "))
                except ValueError:    
                    print("|You typing wrong!")
                    Farmer.start_farmer()  
                    
                price = amount * 350
                print(f'|Buying {amount} amount of field...')    
                time.sleep(1)

                if price > Farmer.inv['money']:
                    print('|You dont have enough money.')
                    time.sleep(1)
                    Farmer.buy()
                
                Farmer.property['field'] += amount
                Farmer.inv['money'] -= price
                Farmer.buy() 

            if choice == 2:
                print('|Field increases your plant area (25 unit)')
                time.sleep(1)
                Farmer.buy()
                    
    # crafting
    def crafting():
        print("")
        print('CRAFT')
        print("|0)Exit \n|1)Food")
        
        try:
           choice = int(input())
        except ValueError:
           print("|you typing wrong!")
           Farmer.crafting()    

        if choice < 0 or choice > 1:
            print("|you typing wrong!")
            Farmer.crafting()

        if choice == 0:
            Farmer.start_farmer()

        if choice == 1:
          print("|0)Exit\n|1)Dough(3 Wheat) (level 10) \n|2)Bread(1 Dough) (level 10)\n")
          try:
           choice = int(input())
          except ValueError:
           print("|you typing wrong!")
           Farmer.crafting()    

          if choice < 0 or choice > 2:
           print("|you typing wrong!")
           time.sleep(1)
           Farmer.crafting()
          
          if choice == 0:
              print("|Returning menu...")
              time.sleep(1)
              Farmer.start_farmer()

          if choice == 1:
              
              if not Farmer.level >= 10:
               print("Your level is not enough")
               time.sleep(1)
               Farmer.crafting()

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
              print(f"|You made {n} dought!")
              time.sleep(1)
              Farmer.inv['dought'] += n
              s = 0 + Farmer.inv['dought']
              Farmer.crafting()


        
          if choice == 2:
              
              if not Farmer.level >= 10:
               print("Your level is not enough")
               time.sleep(1)
               Farmer.crafting()

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
              print(f'|You made {n} bread!')
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
        
        if Farmer.inv['retirement_p'] == 0:
            print("|You paid all of your retirement debt, you can rest all of your life")
            print("|1-rest? 2-NO!")
            try:
                        
                        choice = int(input())
                        
                        if choice == 1:
                            print("Congrats!, you can rest all of your life time!")
                            

                        if choice == 2:
                            print("You will be never know how to get tired, lets back!")    
                            Farmer.start_farmer()
                        
            except ValueError:
                        print("you typing wrong!")
                        Farmer.retirement()    

            
        
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
                Farmer.start_farmer()
            Farmer.inv['money'] -= 1000
            Farmer.inv['retirement_p'] -= 1
            print(f"|Congrats! you paid debt! ")
            Farmer.start_farmer()
        
        if choice == 2:
            print("|returning to menu...")
            time.sleep(1)
            Farmer.start_farmer()


    def character_s():
       
        while Farmer.level_curxp >= Farmer.level_maxp:
            Farmer.level += 1
            Farmer.level_curxp -= Farmer.level_maxp
            Farmer.level_maxp += (Farmer.level_maxp / 2)            

        print("#################")
        print(f"#   Character Level: {Farmer.level}           #")
        print(f"#   Current Experience: {Farmer.level_curxp}      #")
        print(f"#   You need {Farmer.level_maxp - Farmer.level_curxp} to be level {Farmer.level + 1}  #")       
        time.sleep(3)
        print("|returning to menu...")
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
