#-----------------------------------------------
# Virat Kohli Year Wise Bar Chart Representation
# ----------------------------------------------
#-----------------------------------------------
# import Libraries
#-----------------------------------------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#-----------------------------------------------
# Virat Kohli Prime era (Year)
#-----------------------------------------------
Year=np.array([2016,2017,2018,2019,2020,2021,2022,2023,2024,2025])           #using numpy
#-----------------------------------------------
# Virat Kohli Year Wise Odi Runs 
#-----------------------------------------------
Runs={
    "Run":[1215,1460,1202,1377,431,129,302,1377,58,651]                      # using pandas
}
df=pd.DataFrame(Runs)
#-----------------------------------------------
# Bar Representation
#-----------------------------------------------
plt.subplot(2, 2, 1)                               # subplot is use for adjust multiple chart in one frame
plt.bar(Year,df["Run"],color="darkorange",            # Bar color
        edgecolor="green",                        # Border Color
        linewidth=2,                               # Border Thickness90
        width=0.6,                                 # Bar Width
        label="ODI Runs Stats",                    #Legend Label
        bottom=0
        )
#-----------------------------------------------
# Title Box
#-----------------------------------------------
plt.title("Virat Kohli Year Wise ODI Runs",color="Brown",fontsize=12)
plt.ylabel("Scores",fontweight="bold",fontsize=15)                                   #using matplotlib
plt.xlabel("Year",fontweight="bold",fontsize=15)

# ************************************************
# Virat Kohli Run percentage in Field
# ************************************************
Areas={
    "area":["Straight","Off Side","Leg Side","Closein","Boundry"]                # using pandas
    }
df=pd.DataFrame(Areas)
Run2=np.array([30,40,35,20,25])                                                  # using numpy
#-----------------------------------------------
# Pie Chart Representation
#-----------------------------------------------
plt.subplot(2, 2, 2)                             
plt.pie(Run2,labels=df["area"],autopct="%1.1f%%",explode=[0.1,0,0,0,0],shadow=True,startangle=90)      # using matplotlib
#-----------------------------------------------
# Title of Pie Chart
#-----------------------------------------------
plt.title(" Virat Kohli shot Area",color="brown",fontsize=13)

#-----------------------------------------------
# How many times virat out in single digit
#-----------------------------------------------
year=np.array([2016,2017,2018,2019,2020,2021,2022,2023,2024,2025])           #using numpy
out=np.array([4,2,3,1,3,11,5,0,10,6])                                                         #using numpy
#-----------------------------------------------
# Scatter Plot Representation
#-----------------------------------------------
plt.subplot(2, 2, 3)                             
plt.scatter(year,out,label="Single Digit Dismisel",edgecolor="black")
plt.title("How many times virat out in single digit year wise",color="brown",fontsize=13)
plt.xlabel("year",fontweight="bold",fontsize=15)
plt.ylabel("out",fontweight="bold",fontsize=15)

#-----------------------------------------------
# Virat Kohli Prime era (Year)
#-----------------------------------------------
Year=np.array([2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025])           #using numpy
#-----------------------------------------------
# Virat Kohli Year Wise Odi Average 
#-----------------------------------------------
avj={
    "avg":[31.80,54.17,47.38,47.62,68.40,52.83,58.56,36.65,92.38,76.84,133.56,59.87,47.89,43.00,27.45,72.47,19.3,54.75]                      # using pandas
}
df=pd.DataFrame(avj)
#-----------------------------------------------
# Bar Representation
#-----------------------------------------------
plt.subplot(2, 2, 4)                               # subplot is use for adjust multiple chart in one frame
plt.bar(Year,df["avg"],color="green",              # Bar color
        edgecolor="blue",                       # Border Color
        linewidth=1,                               # Border Thickness
        width=0.6,                                 # Bar Width
        label="ODI Average",                       #Legend Label
        bottom=0
        )
#-----------------------------------------------
# Title Box
#-----------------------------------------------
plt.title("Virat Kohli Year Wise Average",color="Brown",fontsize=12)
plt.ylabel("Average",fontweight="bold",fontsize=15)                                   #using matplotlib
plt.xlabel("Year",fontweight="bold",fontsize=15)


#------------------------------------------------------
# Show All The Ploting 
#------------------------------------------------------

plt.tight_layout()   
plt.show()
