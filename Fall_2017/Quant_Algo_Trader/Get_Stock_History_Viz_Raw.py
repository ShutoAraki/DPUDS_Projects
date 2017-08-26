###########################################
#                                         #
#     Historical Stock Data API           #
#     and Visualizations                  #
#                                         #
#     Created By: Sam Showalter           #
#     Creation Date: 5/23/2017            #
#                                         #
###########################################


#Matplotlib related imports
import matplotlib
matplotlib.use("Qt5Agg")     #MUST be Qt4Agg, otherwise mouse scroll events cause TkInter to crash
import matplotlib.pyplot as plt
from matplotlib import dates as mdates
import matplotlib.ticker as mticker
from matplotlib.finance import candlestick_ohlc
import pandas as pd

#Other necessary modules for data and display
import quandl 
from tkinter import *
import numpy as np
import tkinter as tk
import datetime as dt

#Authenticate the Quandl API with token
quandl.ApiConfig.api_key = 'N1j_H8avpLu-8zwvDdsH'

class getHistorical:
    
    def __init__(self):
        
       #STRUCTURE SIZING
       self.root = tk.Tk()
       self.root.lift()
       self.root.geometry('400x350')
       

       #INPUT TEXT BOXES
       self.ready = False
       label1=tk.Label(self.root,text="Stock Ticker")
       self.entry1=tk.Entry(self.root)
       label2=tk.Label(self.root,text="Start Date (YYYY-MM-DD)")
       self.entry2=tk.Entry(self.root)
       label3=tk.Label(self.root,text="End Date (YYYY-MM-DD)")
       self.entry3=tk.Entry(self.root)
       
       #PREDICTIVE TEXT BOXES
       label4=tk.Label(self.root,text="Number of Days")
       self.entry4=tk.Entry(self.root)
       self.var5 = IntVar()
       check = Checkbutton(self.root, text="Predict?", variable=self.var5)
       

       #BUTTON
       button = tk.Button(self.root, text = 'Submit', command=self.quit, cursor = 'heart', relief = RAISED)
       self.root.bind('<Return>',lambda e: self.quit())

       #PACKING IN ALL VALUES
       label1.pack()
       self.entry1.pack()
       label2.pack()
       self.entry2.pack()
       label3.pack()
       self.entry3.pack()
       button.pack()
    
       #MESSAGES TO SHOW (PACKED)
       mes = Message(self.root, text="You will be prompted with a warning if improper inputs are given. Refer to messages for further information.", width=350)
       mes.pack()
       
       #PACK PREDICTIVE STUFF
       
       label4.pack()
       self.entry4.pack()
       label4.place(relx = 0.51, rely = 0.73)
       check.pack()
       
       
       self.entry4.place(relx = 0.44, rely = 0.80)
       check.place(relx = 0.24, rely = 0.795)


       #MAINLOOP AND ASSIGNING DATAFRAME, STOCK PRICE VALUES
       self.root.mainloop()
       self.delta
       self.dataframe
       self.stock
    
    #FORMAL EXIT LOGIC     
    def quit(self):

        def MessageBox(message, details):
            root = Tk()
            warningMessage = Message(root, text= ("Message: " + message), width=350)
            warningMessage.pack() 
            messageDetails = Message(root, text= ("Details: " + details), width=350)
            messageDetails.pack() 
            button = Button(root, text = 'Ok', command=root.destroy, relief = RAISED)
            button.pack()
            root.mainloop()
        
        #GET ALL INPUT VALUES
        sTicker = self.entry1.get()
        pred = self.var5.get()
        self.stock = sTicker.upper()
        date_start = self.entry2.get()
        date_end = self.entry3.get()

        #IF INPUTS ARE NOT VALID
        if (sTicker == "" 
            or date_start == "" 
            or date_end == ""):

            MessageBox("EMPTY FIELD ERROR", "\n - PLEASE ENTER A VALUE FOR ALL FIELDS")

        elif (date_start > date_end or date_start.isalpha() 
              or date_end.isalpha() 
              or '-' not in date_start 
              or '-' not in date_end 
              or date_start > dt.date.today().strftime("%Y-%m-%d") 
              or date_end > dt.date.today().strftime("%Y-%m-%d")):

            MessageBox("DATE ERROR", "\n - CHECK DATE FORMATTING\n - END DATE MAY BE LATER THAN START DATE\n - DATES MAY NOT BE LATER THAN TODAY")

        elif date_end > dt.date.today().strftime("%Y-%m-%d"):
            MessageBox("FUTURE DATE ERROR", "\n - CANNOT ENTER A DATE PAST TODAY")
        
       

        #IF INPUTS CONDITIONS ABOVE ARE SATISFIED
        
        while not self.ready:

            try:
                #Format dates to get number of days
                date_format = "%Y-%m-%d"
                date_start = dt.datetime.strptime(date_start, date_format)
                date_end = dt.datetime.strptime(date_end, date_format)
                days = date_end - date_start
                self.delta = days.days
                self.ready = True
            
            #EXCEPTION IF DATES ARE INVALID
            except Exception as e:
                MessageBox('DATES ARE INVALID',str(e))
            
            if self.delta < 5:
                MessageBox('DATE RANGE TOO SHORT','\n - MUST PULL AT LEAST 7 DAYS OF DATA')

            
            
        try:
            self.dataframe = quandl.get(("WIKI/" + sTicker), trim_start = date_start, trim_end = date_end)
            self.root.destroy()
            print("Successful API Call")
            return 1
        
        #IF THERE IS AN UNAHNDLED EXCEPTION WITH THE API   
        except Exception as e:
          error = str(e)
          if error[:12]=='(Status 404)':
            MessageBox('UNHANDLED API ERROR: CHECK INPUTS',('\n' + error))

                    
#Creates an array of moving averages       
def moving_average(values,window):
    weights = np.repeat(1.0, window) / window
    mov_avgs = np.convolve(values, weights, 'valid')
    return mov_avgs

#Creates an array of high minus low values
def high_minus_low(highs,lows):
    return highs - lows

#Plots all stock data
def plot_stock_data(data):

  #Alter dataframe index so that date can be utilized as a float
  data.dataframe.reset_index(inplace=True)
  data.dataframe.Date=mdates.date2num(data.dataframe.Date.astype(dt.date))
  
  #10 day moving average (dynamic for date ranges so program does not error out) [Max = 10, Min = 2]
  MA1 = min(max(2,(data.delta//8)), 10)

  #30 day moving average (dynamic for date ranges so program does not error out) [Max = 30, Min = 3]
  MA2 = min(max(3,data.delta//5),30)

  #Start point variable to line up moving averages
  start = len(data.dataframe.Date[MA2 - 1:])   

  #Assemble general plot design
  fig = plt.figure()

  #Subplot for high minus Low data 
  ax1 = plt.subplot2grid((6,1),(0,0),rowspan = 1, colspan = 1)
  plt.title('High-Low, Stock Price, and Moving Avg. for ' + data.stock)
  plt.ylabel('H_L')

  #Plot high minus low data
  hml = list(map(high_minus_low,data.dataframe.High,data.dataframe.Low))
  ax1.plot(data.dataframe.Date[-start:],hml[-start:], linewidth = 1, label = 'H-L')

  #Subplot for stock price in central grid
  ax2 = plt.subplot2grid((6,1), (1,0),rowspan = 4, colspan = 4, sharex = ax1)
  plt.ylabel('Stock Price')

  #Plot stock price on central grid
  candlestick_ohlc(ax2,A.dataframe.values[-start:],colorup = '#41ad49', colordown = '#ff1717', width=0.4)
  
  #Plot volume (twin subplot for xaxis)
  ax2v = ax2.twinx()
  ax2v.fill_between(data.dataframe.Date[-start:],0,data.dataframe.Volume[-start:],facecolor = '#0079a3', alpha = 0.35)
  ax2v.plot_date([],[], '-', color = '#0079a3', label = 'Volume', alpha = 0.35)
  ax2v.axes.yaxis.set_ticklabels([])
  ax2v.set_ylim(0, 3*data.dataframe.Volume.max())

  #Create moving averages
  ma1 = moving_average(data.dataframe.Close, MA1)
  ma2 = moving_average(data.dataframe.Close, MA2)
  

  #Subplot for moving averages
  ax3 = plt.subplot2grid((6,1),(5,0), rowspan = 1, colspan = 1, sharex = ax1)
  plt.ylabel('MAvg')

  #Plotting 10 day and 30 day moving averages
  ax3.plot(data.dataframe.Date[-start:],ma1[-start:], linewidth = 1, label = str(MA1) + 'MA',color = '#05090f')
  ax3.plot(data.dataframe.Date[-start:],ma2[-start:], linewidth = 1,label = str(MA2) + 'MA', color = '#2461c9')

  #Filling the difference between moving averages
  ax3.fill_between(data.dataframe.Date[-start:], ma2[-start:], ma1[-start:], where = (ma2[-start:] >= ma1[-start:]), facecolor = '#db1a1a', edgecolor = '#db1a1a', alpha = 0.4)
  ax3.fill_between(data.dataframe.Date[-start:], ma2[-start:], ma1[-start:], where = (ma2[-start:] <= ma1[-start:]), facecolor = 'g', edgecolor = 'g', alpha = 0.4)
  
  #Giving ax1 a legend
  ax3.legend()
  
  #Changing tick labels for lowest graph
  ax3.xaxis.set_major_locator(mticker.MaxNLocator(10))
  ax3.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

  #Removing axes for other grids and cleaning up visualization
  plt.setp(ax1.get_xticklabels(), visible = False)
  plt.setp(ax2.get_xticklabels(), visible = False)

  #Turn date labels sideways
  for label in ax3.xaxis.get_ticklabels():
    label.set_rotation(45)

  ax1.plot()
  plt.show()


###################################################################  
    
#Runs the code to get query about stocks
A = getHistorical()

#Plots queried stock data
plot_stock_data(A)