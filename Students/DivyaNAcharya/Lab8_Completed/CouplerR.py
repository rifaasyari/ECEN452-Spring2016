import matplotlib.pyplot as plt
import csv

#***Note: In order to use this code, all of the columns in the .csv file must have the same length. If your columns have
# different lengths, simply repeat the last value in each of the shorter columns until they are all the same size.

#Initialize arrays for x, y1, y2, y3
f1 = []
M = []
CT = []
HFSS = []
Y = []
M1 = []
CT1 = []
HFSS1 = []
Y1 = []

##Read .csv data file
#replace quoted text below with filepath to your .csv file
with open('RPort.csv', 'rU') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #items in '' below need to exactly match the entry in the first row of the columns in the .csv file
        #edit/add additional lines as needed for each column of data
        f1.append(float(row['Freq']))
        M.append(float(row['S11M']))
        CT.append(float(row['S22M']))
        HFSS.append(float(row['S33M']))
        Y.append(float(row['S44M']))
        M1.append(float(row['S11H']))
        CT1.append(float(row['S22H']))
        HFSS1.append(float(row['S33H']))
        Y1.append(float(row['S44H']))

##Plotting
plt.figure(1) #initialize plot1
ax1 = plt.subplot(211) #create axes handle for plot1
#ax1.plot(f1, M, '-b', label="S11 Milled") #plot y1 vs. x, solid-blue, add lable for legend
ax1.plot(f1, CT, '-r', label="S21 Milled") #plot y2 vs. x, solid-red, add lable for legend
ax1.plot(f1, HFSS, '-g', label="S31 Milled") #plot y2 vs. x, solid-red, add lable for legend
ax1.plot(f1, Y, '-k', label="S41 Milled") #plot y2 vs. x, solid-red, add lable for legend
ax1.set_xlim(min(f1), max(f1)) #set x-axis limits
ax1.set_ylim(-40,0) #set y-axis limits
ax1.legend(loc=4) #add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-') #add solid grey gridlines
plt.title('Rat Race Coupler:Isolation and Coupling') #add plot title
plt.ylabel('Magnitude in [dB]') #add y-axis title

ax1 = plt.subplot(212) #create axes handle for plot1
#ax1.plot(f1, M1, '--b', label="S11 HFSS") #plot y1 vs. x, solid-blue, add lable for legend
ax1.plot(f1, CT1, '--r', label="S21 HFSS") #plot y2 vs. x, solid-red, add lable for legend
ax1.plot(f1, HFSS1, '--g', label="S31 HFSS") #plot y2 vs. x, solid-red, add lable for legend
ax1.plot(f1, Y1, '--k', label="S41 HFSS") #plot y2 vs. x, solid-red, add lable for legend

ax1.set_xlim(min(f1), max(f1)) #set x-axis limits
ax1.set_ylim(-40,0) #set y-axis limits
ax1.legend(loc=4) #add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-') #add solid grey gridlines

plt.xlabel('Frequency [GHz]') #add x-axis title
plt.ylabel('Magnitude in [dB]') #add y-axis title

plt.show() #required to display plots