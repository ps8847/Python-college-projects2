
from matplotlib import pyplot as plt
from os import system

def main():
    choice = int(input('''\tmatplotlib
    1. PROGRAM TO DISPLAY THE HEALTH RATING OF DIFFERENT KIND OF CEREALS - Grid
    2. PROGRAM TO SHOW AMOUNT OF SODIUM PRESENT IN DIFFERENT KIND OF CEREALS - Bars
    3. DISPLAYING THE QUANTITY OF DIFFERENT NUTRIENTS PRESENT IN CORN FLAKES ACCORDING TO THE PERCENTAGE - Pie Chart
    4. PROGRAM TO DISPLAY CEREAL CONSUMPTION BETWEEN DIFFERENT AGE GROUPS - Histogram
    5. PROGRAM TO COMPARE THE AMOUNT OF SODIUM AND POTASSIUM PRESENT IN DIFFERENT TYPE OF CEREALS - multigrid or Seasonal Plot
    6. PROGRAM TO DISPLAY STHE AMOUNT OF CALORIES PRESENT IN VARIOUS CEREALS - Scatter Plot
    0. Exit
    Enter : '''))
    return choice

choice = main()

while choice !=0:
    
    #DISPLAY THE HEALTH RATING OF DIFFERENT KIND OF CEREALS
    if choice == 1:
        system('cls')
        plt.style.use('ggplot')
        cereal_name=["100% Bran","All-Bran","Almond Delight","Apple Jacks","Basic 4","Bran Chex","Bran Flakes",
        "Cheerios","Clusters","Corn Chex","Corn Flakes"]
        health_rating=[68.402973,33.983679,59.425505,93.704912,34.384843,29.509541,33.174094,37.038562,49.120253,53.313813,18.042851]
        plt.plot(cereal_name,health_rating,linestyle='-',label='health rating',marker='.',color='c')
        plt.xlabel(' NAME OF CEREALS')
        plt.ylabel('HEALTH RATING')
        plt.legend()
        plt.title('CEREALS')
        plt.show()
        
    #SHOW AMOUNT OF SODIUM PRESENT IN DIFFERENT KIND OF CEREALS    
    elif choice == 2:
        system('cls')
        plt.style.use('ggplot')
        cereal_name=["100% Bran","All-Bran","Almond Delight","Apple Jacks","Basic 4","Bran Chex","Bran Flakes",
        "Cheerios","Clusters","Corn Chex","Corn Flakes"]
        sodium_amount=[130,260,200,180,125,200,210,290,140,280,290]
        plt.bar(cereal_name,sodium_amount)
        plt.xlabel('NAME OF CEREALS')
        plt.ylabel(' AMOUNT OF SODIUM')
        plt.title('CEREALS')
        plt.show()
            
    #DISPLAYING THE QUANTITY OF DIFFERENT NUTRIENTS PRESENT IN CORN FLAKES ACCORDING TO THE PERCENTAGE
    elif choice == 3:
        system('cls')
        plt.style.use('fivethirtyeight')
        slices=[4,21,2,35,5,25,290]
        labels=[ "PROTEINS","CARBOHYDRATES","SUGAR","POTASSIUM","FIBRE","VITAMINS","SODIUM"]
        colors=['blue','red','yellow','green','grey','purple','pink']
        explode=[0.1,0.1,0.1,0.1,0.1,0.1,0]
        plt.pie(slices,labels=labels,explode=explode,autopct='%1.1f%%',colors=colors, wedgeprops={'edgecolor':'black'})
        plt.title('DISPLAYING THE QUANTITY OF DIFFERENT NUTRIENTS PRESENT IN CORN FLAKES ')
        plt.show()
        
    #DISPLAY CEREAL CONSUMPTION BETWEEN DIFFERENT AGE GROUPS
    elif choice == 4:
        system('cls')
        plt.style.use('ggplot')
        ages=[6,20,50,35,17,40,15]
        bins=[10,20,30,40,50,60,70]
        plt.hist(ages,bins=bins,edgecolor='black',color='m')
        plt.xlabel('AGES')
        plt.ylabel('CEREAL CONSUMPTION')
        plt.title('DISPLAYING CEREAL CONSUMPTION BETWEEN DIFFERENT AGE GROUPS')
        plt.show()
        
    #COMPARE THE AMOUNT OF SODIUM AND POTASSIUM PRESENT IN DIFFERENT TYPE OF CEREALS
    elif choice == 5:
        system('cls')
        plt.style.use('ggplot')
        cereal_name=["100% Bran","All-Bran","Almond Delight","Apple Jacks","Basic 4","Bran Chex","Bran Flakes","Cheerios","Clusters","Corn Chex","Corn Flakes"]
        sodium_amount=[130,260,200,180,125,200,210,290,140,280,290]
        plt.plot(cereal_name,sodium_amount,linestyle='--',label='SODIUM',marker='o',color='c')
        potassium_amount=[280,135,320,330,1,70,30,100,125,190,35]
        plt.plot(cereal_name,potassium_amount,label='POTASSIUM',marker='o',color='m')
        fibre_amount=[10,2,9,14,1,1,1.5,1,2,4,5]
        plt.plot(cereal_name,fibre_amount,label='FIBRE',linestyle='--',marker='o',color='k')
        sugar_name=[6,8,5,0,8,10,14,8,6,5,12]
        plt.plot(cereal_name,sugar_name,label='SUGAR',marker='o',color='b')
        plt.xlabel(' NAME OF CEREALS')
        plt.ylabel('SODIUM AND POTASSIUM AMOUNT')
        plt.legend()
        plt.title('CEREALS')
        plt.show()

    #DISPLAY STHE AMOUNT OF CALORIES PRESENT IN VARIOUS CEREALS'
    elif choice == 6:
        system('cls')
        plt.style.use('seaborn')
        cereal_name=["100% Bran","All-Bran","Almond Delight","Apple Jacks","Basic 4","Bran Chex","Bran Flakes","Cheerios","Clusters","Corn Chex","Corn Flakes"]
        calories=[70,120,50,110,110,110,130,90,90,120,110]
        plt.scatter(cereal_name,calories ,s=100,edgecolor='black',linewidth=1,alpha=0.75)
        plt.xlabel('CEREALS')
        plt.ylabel('CALORIES')
        plt.title('DISPLAYING THE AMOUNT OF CALORIES PRESENT IN VARIOUS CEREALS')
        plt.show()

    else:
        system('cls')
        print("Invalid Input")
        input()
        system('cls')
    
    choice = main()
    
