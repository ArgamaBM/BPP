

from main import *
import pytest
import numpy as np



# Main requirement: test the algorithm


# Register fixtures. Encapsulate functions
@pytest.fixture
def pv_production(request):
    return request.param

@pytest.fixture
def house_consumption(request):
    return request.param

@pytest.fixture
def storage_capacity(request):
    return request.param

@pytest.fixture
def batt_state(request):
    return request.param

@pytest.fixture
def key(request):
    return request.param

@pytest.fixture
def commands(request):
    return request.param

@pytest.fixture
def result(request):
    return request.param


@pytest.fixture
def controller(pv_production, house_consumption, storage_capacity, batt_state,
                key, commands,result):
    controller = EMController(pv_production, house_consumption, storage_capacity, batt_state,
                               key, commands,result)
    return controller



# Test Cases. We give list of tuples with different case scenarios, using "constructors" (fixtures)
@pytest.mark.parametrize("pv_production, house_consumption, storage_capacity,\
                          batt_state, key, commands,result",
                         [
# Basic Battery Scenarios
(6000, 4000, 5000, 0, None, "",'Charge'), #Scenario 1: Basic Battery -> Charge
(8000, 3000, 5000, 1, None, "",'Sell to grid'), #Scenario 2: Basic Battery -> Sell to grid
(2000, 6000, 5000, 1, None, "",'Discharge'), #Scenario 3: Basic Battery -> Discharge"
(1000, 8000, 5000, 0, None, "",'Buy from grid'), #Scenario 4: Basic Battery -> Buy from grid"
(5000, 5000, 5000, 0, None, "",'PV supplies house'), #Scenario 5: Basic Battery -> PV supplies house"
# Standard Battery Scenarios
(9000, 7000, 10000, 0, None, "",'Charge'), #Scenario 5: Standard Battery -> Charge
(10000, 5000, 10000, 1, None, "",'Sell to grid'), #Scenario 6: Standard Battery -> Sell to grid
(4000, 9000, 10000, 1, None, "",'Discharge'), #Scenario 7: Standard Battery -> Discharge
(1000, 17000, 10000, 0, None, "",'Buy from grid'), #Scenario 8: Standard Battery -> Buy from grid
(5000, 5000, 5000, 0, None, "",'PV supplies house'), #Scenario 5: Standard Battery -> PV supplies house"
# Pro Battery Scenario
(12000, 10000, 15000, 0, None, "",'Charge'), #Scenario 9: Pro Battery -> Charge
(13000, 9000, 15000, 1, None, "",'Sell to grid'), #Scenario 10: Pro Battery -> Sell to grid
(4000, 12000, 15000, 1, None, "",'Discharge'), #Scenario 11: Pro Battery -> Discharge
(2000, 17000, 15000, 0, None, "",'Buy from grid'),  #Scenario 12: Pro Battery -> Buy from grid
(5000, 5000, 5000, 0, None, "",'PV supplies house') #Scenario 5: Pro Battery -> PV supplies house"
                    ],
                                                                        
                         indirect=["pv_production", "house_consumption", "storage_capacity",
                                    "batt_state","key", "commands"])

def test_power_management_scenario(controller):
    try:

        controller.power_management()
        assert controller.get() == controller.result

        #Reset controller
        controller.reset_state()
        assert controller.get() != controller.result

    except Exception as e:
       print('ERROR in test_power_management_scenairo: ',e)




#Test case 2 (random).Requirement 2: Implement fibonacci serie for generate random numbers
@pytest.mark.parametrize("pv_production,house_consumption,storage_capacity, batt_state, \
                         key, commands, result",
                         [
        # Basic Battery Scenarios
        (0,0,5000, 0, None, "",None),    
        (0,0,5000, 1, None, "",None),    
        (0,0,5000, 1, None, "",None),    
        (0,0,5000, 0, None, "",None),    
        # Standard Battery Scenarios
        (0,0,10000, 0, None, "",None),   
        (0,0,10000, 1, None, "",None),   
        (0,0,10000, 1, None, "",None),   
        (0,0,10000, 0, None, "",None),   
        # Pro Battery Scenario
        (0,0,15000, 0, None, "",None),   
        (0,0,15000, 1, None, "",None),   
        (0,0,15000, 1, None, "",None),   
        (0,0,15000, 0, None, "",None)    
                        ],
                                                                        
                         indirect=["pv_production","house_consumption","storage_capacity", 
                                   "batt_state","key","commands","result"])

def test_power_management_random_scenario(controller):
    try:
        
        def fibonacci(n):
          fib_sequence = np.array([0, 1])
          for i in range(2, n):
              fib_sequence = np.append(fib_sequence, 
                                       fib_sequence[i-1] + fib_sequence[i-2])
          return fib_sequence
        
        #Generate Fibonacci sequence up to 20 numbers
        fib_sequence = fibonacci(10)
        random_fib = np.random.choice(fib_sequence)*500
        random_fib2 = np.random.choice(fib_sequence)*500

        #Update values
        controller.pv_production = random_fib
        controller.house_consumption = random_fib2

        #Run algorithm
        controller.power_management()

        '''
        #Discoment this line for checking the random numbers.
        print(f'Pv_production:{controller.pv_production}\
            House_consumption:{controller.house_consumption}\
            Set_of_batterires:{controller.storage_capacity}\
            batt_state:{str(controller.batt_state)}\
            Key: {controller.key}\
            Case: {controller.result}')
        '''
        
        assert controller.get() == controller.result
        
        #Reset controller
        controller.reset_state()
        assert controller.get() != controller.result
    
    except Exception as e:
       print('ERROR in test_power_management_random_scenairo: ',e)

#Inicialize the script
if __name__ == '__main__':
    '''
    # Discoment this part of the code for debbug. All parameter can be modified
    # for testing specific scenarios.

    aux = EMController(0, 0, 10000, 1, None, "",'')
    aux2 = EMController(0, 0, 10000, 0, None, "",'')
    test_power_management_random_scenario(aux)
    test_power_management_random_scenario(aux2)
    '''
    pytest.main(['-vv'])


