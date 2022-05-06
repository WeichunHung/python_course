import pandas as pd

def create_series():

    iPhone = pd.Series(['iPhone 12','iPhone 12 Pro','iPhone 13'],
                         index = ['P1','P2','P3'])
    List1 = pd.concat([iPhone], keys=['iPhone'], names=['Product List1'])
    print('create_series:')
    print(List1)

    print(iPhone[0])
    print(iPhone['P2'])

create_series()
print('--------------------------------------------------------------------------------')

def concat_series():
    iPhone = pd.Series(['iPhone 12','iPhone 12 Pro','iPhone 13'],
                       index = ['P1','P2','P3'])
    Macbook = pd.Series(['Macbook Air','Macbook Pro'],
                        index = ['P4','P5'])
    List2 = pd.concat([iPhone,Macbook],
                      keys =['iPhone','Macbook'],
                      names=['Product List2'])
    print('concat_series')
    print(List2)

    AirPods = pd.Series(['AirPods 3','AirPods Pro','AirPods Max'], index =['P6','P7','P8'])
    List3 = pd.concat([iPhone,Macbook,AirPods],
                      keys= ['iPhone','Macbook','AirPods'],
                      names=['Product List3'])#, ignore_index=True)
    print(List3)

concat_series()
print('--------------------------------------------------------------------------------')

def extract_data():
    iPhone = pd.Series(['iPhone 12', 'iPhone 12 Pro', 'iPhone 13'], index=['P1', 'P2', 'P3'])
    Macbook = pd.Series(['Macbook Air', 'Macbook Pro'], index=['P1', 'P2'])
    AirPods = pd.Series(['AirPods 3', 'AirPods Pro', 'AirPods Max'], index=['P1', 'P2', 'P3'])

    List = pd.concat([iPhone, Macbook, AirPods],
                      keys=['iPhone', 'Macbook', 'AirPods'],
                      names=['Apple Products'])
    print('extract_data')
    print(List)

extract_data()
print('--------------------------------------------------------------------------------')

def modify_data():
    iPhone = pd.Series(['iPhone 12', 'iPhone 12 Pro', 'iPhone 13'], index=['P1', 'P2', 'P3'])
    Macbook = pd.Series(['Macbook Air', 'Macbook Pro'], index=['P1', 'P2'])
    AirPods = pd.Series(['AirPods 3', 'AirPods Pro', 'AirPods Max'], index=['P1', 'P2', 'P3'])
    iPhone[2] = 'iPhone 13 Mini'
    AirPods['P1'] = 'AirPods 2'

    List = pd.concat([iPhone, Macbook, AirPods],
                      keys=['iPhone', 'Macbook', 'AirPods'],
                      names=['Apple Products'],)
    print('modify_data:')
    print(List)
    print('Product Amount: ',List.size) #get_amount

modify_data()
print('--------------------------------------------------------------------------------')