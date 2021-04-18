class Budget:
    '''
    We define a class Budget here
    '''

    def __init__(self, allocation, expenses):
        '''
        constructs the necessary attributes for the Budget object
        Parameters
        --------
        allocation: int
            amount of money assigned to each category of the budget
        expenses: int
            amount spent In the budget Category
        balance: int
        
        '''

        self.allocation = allocation
        self.expenses = expenses
        '''
        Balance is the amount of the allocation remaining in the budget category after the expenses
        have been deducted
        '''
        self.balance = allocation - expenses
    
        
    def withdrawal(self, amount):
        '''
        returns the balance after a certain amount has been removed
        Parameters
        --------
        amount: int
            amount of money to be removed from the balance
            '''
        return self.balance - amount

    def transfer_balance(self, other, transfer_amount):
        '''
        returns the balance after a transfer of balance between two categories
        Parameters
        -------
        transfer_amount: int
            This the amount of money to be transferred from the self category to the other category.
            '''
        self.balance -= transfer_amount
        other.balance += transfer_amount
        return other.balance

    def cat_balance(self):
        '''
        returns the balance of a category
        Parameters
        --------
        None
            '''
        print(self.balance)

    def deposit(self,amount):
        '''
        returns the balance after a certain amount has been added to a category's balance
        Parameters
        --------
        amopunt: int
            amount of money to be added to the balance
            '''
        self.balance += amount
        return self.balance

food = Budget(allocation = 20000,expenses = 5000)
clothing = Budget (allocation = 4000, expenses = 0)
Entertainment = Budget (allocation = 5000, expenses = 2500)
# Trying out some of the methods on the categories
print(food.withdrawal(3000))

print(clothing.transfer_balance(food,2000))
