#What is the average price of used cars with a specific fuel - petrol in the dataset, and 
#how has this average price changed over two different timeframes, 1973-2000 and 2000-2022?


import csv


# What is the average price of used cars with a specific fuel - petrol in the dataset
def ave_price():
    with open('used_cars_UK.csv', 'r') as csv_file:
        data = list(csv.reader(csv_file))
        header = data[0]
        type_index = header.index('Fuel type')
        price_index = header.index('Price')
        fuel = str(input('Enter the fuel type: '))
        total = 0
        count = 0
        for row in data[1:]: 
            if str(row[type_index]).lower() == str(fuel).lower():
                total += float(row[price_index])
                count += 1
        print('The average price for used cars with a fuel:', fuel, ' is:', total/count)




# How has that average price changed over two different timeframes, 1973-2000 and 2000-2022
def different_average_price():
    '''how has this average price changed over two different timeframes, 1973-2000 and 2000-2022'''
    data = list(csv.reader(open('used_cars_UK.csv',newline='',encoding='utf-8')))
    header = data[0]
    price_index =  header.index('Price')
    year_index=  header.index('Registration_Year')
    fuel_type = input('Please enter the type of fuel for comparision:')
    type_index = header.index('Fuel type')
    total1=0
    count1=0
    total2=0
    count2=0
    avg_1 = 0
    avg_2=0
    for row in data[1:]:
        if str(row[type_index]).lower()==str(fuel_type).lower() and int(row[year_index]) >= 1973 and int(row[year_index])<=2000:
            total1 += int(row[price_index])
            count1+=1
    avg_1=total1/count1
    for row in data[1:]:
        if str(row[type_index]).lower()==str(fuel_type).lower() and int(row[year_index]) >= 2000 and int(row[year_index])<=2022:
            total2 += int(row[price_index])
            count2+=1
    avg_2=total2/count2
    if avg_1>avg_2:
        print('The average price has increased from 1973-2000 to 2000-2022 about:', avg_1-avg_2)
    elif avg_1<avg_2:  
        print('The average price has decreased from 1973-2000 to 2000-2022 about:', avg_2 - avg_1)
    else: 
        print('No Change')

def main():
    ave_price()
    different_average_price()


main()