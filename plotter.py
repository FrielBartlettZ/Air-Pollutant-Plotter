import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


location = "TorontoNorth"
month_thirty_one = ['01', '03', '05', '07', '08', '10', '12']
month_thirty = ['04', '06', '09', '11']


class Plotter:

    # day_plotter(year, month, day, gas, colour): Plots a graphs of levels of gas for the entire day specified by
    # year, month, day, with line in colour. Prints standard deviation, mean, max and min to screen.
    # Effects: Plots a graph, reads from file, prints to screen
    # day_plotter: Str Str Str Str Str -> None
    #      Requires: Each parameter must be a valid value from the corresponding list in main
    # Examples:
    # hour_plotter("2011", "01", "02", "Ozone", "Blue")
    #           => Collects the data corresponding to every hour on January 2, 2011, from the Ozone file. Plots with
    #           blue line

    @staticmethod
    def day_plotter(year, month, day, gas, colour):

        # Plots whole 24 hour days
        # Needs: Dates, Gas

        data = pd.read_excel(gas + location + '.xlsx', sheet_name=year)
        date = year + '-' + month + '-' + day
        index = 'Date not Valid'

        for i in data.index:
            if date in str(data['Date'][i]):
                index = i
                break

        labels = np.array(data.columns)[4:]
        y = np.array(data.loc[index, labels])

        index1 = 0

        for i in range(len(y)):
            if (y[i] > 100) or (y[i] < -10):
                index2 = i
                y[i] = np.nan
                if index1 != index2:
                    plt.plot(labels[index1:index2], y[index1:index2], c=colour, alpha=0.7, linewidth=0.7)
                plt.plot(labels[i], 0, c='white', alpha=0)
                index1 = i + 1
            elif i == (len(y) - 1) and index1 != i + 1:
                plt.plot(labels[index1:], y[index1:], c=colour, alpha=0.7, linewidth=0.7)

        print('Gas: ' + gas + ' (' + colour + ')')
        print(date)
        print('Mean: ' + str(np.nanmean(y)))
        print('Standard Deviation: ' + str(np.nanstd(y)))
        print('Minimum: ' + str(np.nanmin(y))
               + ' - Maximum: ' + str(np.nanmax(y)))

    # hour_plotter(hour, period_length, year, month, increment, gas, colour): Pulls a period_length amount of data
    # specified by year, month, hour, from a file specified by gas and plots it with a colour line. The plot will move
    # through the data by increment, plotting the level of gas for each day at that hour. Prints standard deviation,
    # mean, max and min to screen.
    # Effects: Plots a graph, reads from file, prints to screen
    # hour_plotter: Str Str Str Str Int Str Str -> None
    #      Requires: Each parameter must be a valid value from the corresponding list in main
    # Examples:
    # hour_plotter("H01", "Year", "2011", "02", 1, "Ozone", "Blue")
    #           => Collects a years worth of data for hour 1 from the Ozone file, starting at 01-01-2011, and in
    #           increments of one day plots it with a blue line. Does not show graph

    @staticmethod
    def hour_plotter(hour, period_length, year, month, increment, gas, colour):

        # Plots the same hour over a period of days
        # Needs: Hour, Period, Start Date, Increment, Gas

        data = pd.read_excel(gas + location + '.xlsx', sheet_name=year)
        date = year + '-' + month
        index1 = 0

        if period_length == 'Year':
            y = np.array(data[hour])
            if year == '2012' or year == '2016' or year == '2020':
                x = np.array(range(1, 367))
            else:
                x = np.array(range(1, 366))
        else:
            for i in data.index:
                if date in str(data['Date'][i]):
                    index1 = i
                    break

            if month in month_thirty_one:
                x = np.array(range(1, 32))
                index2 = index1 + 31
            elif month in month_thirty:
                x = np.array(range(1, 31))
                index2 = index1 + 30
            else:
                if year == '2012' or year == '2016' or year == '2020':
                    x = np.array(range(1, 30))
                    index2 = index1 + 29
                else:
                    x = np.array(range(1, 29))
                    index2 = index1 + 28

            y = np.array(data[hour][index1:index2])

        index1 = 0

        for i in range(len(y)):
            if (y[i] > 100) or (y[i] < -10):
                index2 = i
                y[i] = np.nan
                if index1 != index2:
                    plt.plot(x[index1:index2:increment], y[index1:index2:increment], c=colour, alpha=0.7, linewidth=0.7)
                plt.plot(x[i], 0, c='white', alpha=0)
                index1 = i + 1
            elif i == (len(y) - 1) and index1 != i + 1:
                plt.plot(x[index1::increment], y[index1::increment], c=colour, alpha=0.7, linewidth=0.7)

        print('Gas: ' + gas + ' (' + colour + ')')
        if period_length == "Month":
            print(month + "-" + year)
        else:
            print(year)
        print('Mean: ' + str(np.nanmean(y)))
        print('Standard Deviation: ' + str(np.nanstd(y)))
        print('Minimum: ' + str(np.nanmin(y))
              + ' - Maximum: ' + str(np.nanmax(y)))


