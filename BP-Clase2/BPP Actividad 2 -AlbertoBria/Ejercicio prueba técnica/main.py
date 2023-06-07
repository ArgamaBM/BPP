# Declaration of Classes

# Device Under Test Class
class DUT():
    '''
    It will be in charge of giving the commands to the SBStorage System.

    Returns:
        -Discharge: use battery for house consumption
        -Buy from grid: use grid power for house consumption
        -Charge: use surplus to charge the battery
        -Sell to grid: sell surplus to grid
        -PV supplies house: PV supply the power to the house
        -Reset
    '''
    def __init__(self,key:int,commands:str) -> bool:
        self.commands= commands
        self.key = key
        
    #Command control
    def set (self,key):
        try: 
            self.key = key
            if self.key == -1:
                self.commands = "Discharge"
                return self.commands

            elif self.key == 0:
                self.commands = "Buy from grid"
                return self.commands

            elif self.key == 1:
                self.commands = "Charge"
                return self.commands
            
            elif self.key == 2:
                self.commands = "Sell to grid"
                return self.commands
            
            elif self.key == 3:
                self.commands = "PV supplies house"
                return self.commands
            
            else: 
                print('Device Reset')
        
        except Exception as e:
            print('ERROR in DUT().set(): ',e)

    def get(self):
        try: 
            return self.commands
        except Exception as e:
            print('ERROR in DUT.get(): ',e)
    
    def reset_state(self):
        try: 
            self.commands = ""
            self.result = None
            return self.commands,self.key
        except Exception as e:
            print('ERROR in DUT().reset_state(): ',e)
    

#Energy Management Controller
class EMController(DUT):
    '''
    Initializes the EMController object.

        Parameters:
            - pv_production (int): Power produced by the Photovoltaic Panels.
            - house_consumption (int): Power consumed by the house.
            - storage_capacity (int): Capacity of the battery storage.
            - batt_state (int): State of the battery (1: charged, 0: discharged).
            - key (int): Key for accessing DUT.
            - commands (str): Commands to be sent to DUT.
            - result (str): Result of the power management operation.

        '''
    def __init__(self, pv_production: int, house_consumption: int, 
                 storage_capacity: int,batt_state:int,key:int,
                 commands:str, result:str):
        super().__init__(key,commands)
        self.pv_production= pv_production
        self.house_consumption= house_consumption
        self.storage_capacity= storage_capacity
        self.batt_state= batt_state # 1: charged ; 0: discharged
        self.result= result
        
        '''
        #Discoment this line for checking initial state of object.
        print(f'Pv_production: {self.pv_production} \
          House_consumption: {self.house_consumption}\
          Set_of_batterires: {self.storage_capacity}\
          batt_state:{self.batt_state}       \
          key: {self.key}         \
          Case: {self.result}')
        '''

    def power_management(self):
        '''
        Performs power management based on the readings.

        Algorithm:
        1. Check if PV production > house consumption.
            2. If true, check if the battery  discharged.
                3. If true, send the command to charge the battery.
            4. If false, send the command to sell excess power to the grid.
        
        If PV production < house consumption
            5. Check if the battery state is charged and if capacity >= consumption
                6. If true, send the command to discharge the battery.
                7. If battery state is charged but capacity < consumption
                    8. Send the command to buy from grid
                7. If false, send the command to get power from the grid.
        '''
        
        try: 
            #Clalc supplus
            surplus = self.pv_production - self.house_consumption

            #Energy Management Algorithm
            if surplus > 0:
                
                if self.batt_state == 0:      
                    self.set(1) #EMController().DUT().set(Key:str,value)
                    self.result = 'Charge'
                    return self.get() 

                elif self.batt_state == 1:
                    self.set(2)
                    self.result = 'Sell to grid'
                    return self.get()
            
                else: 
                    self.result = 'there is a bug'
                    return False
            

            elif surplus < 0:

                if self.batt_state == 1 and self.storage_capacity >= self.house_consumption:
                    self.set(-1)
                    self.result = 'Discharge'
                    return self.get()

                elif self.batt_state == 1 and self.storage_capacity < self.house_consumption: 
                    self.set(0)
                    self.result = 'Buy from grid'
                    return self.get()

                elif self.batt_state == 0: 
                    self.set(0)
                    self.result = 'Buy from grid'
                    return self.get()

                else:
                    self.result = 'Grid not available'          
                    return False
        

            else:
                self.set(3)
                self.result = 'PV supplies house'
                return self.get()
            
        except Exception as e:
            print('ERROR in EMCController.power_management(): ',e)


    def reset_state(self):
        '''
        Resets to default values. Ensures the recovery of DUT after test.
        '''
        try: 
            self.pv_production= 0
            self.house_consumption= 0
            self.storage_capacity= 0
            self.batt_state= None # 1: charged ; 0: discharged
            self.result= None
        
        except Exception as e:
            print('ERROR in EMCController.reset_state(): ',e)

  