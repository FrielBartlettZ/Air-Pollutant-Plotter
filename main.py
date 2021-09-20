import plotter
import matplotlib.pyplot as plt
import PySimpleGUI as sg

import yearDivider

# Constants
YEARS = ['2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
MONTHS = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
DAYS = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
        '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
        '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
HOURS = ['H01', 'H02', 'H03', 'H04', 'H05', 'H06', 'H07', 'H08', 'H09', 'H10',
         'H11', 'H12', 'H13', 'H14', 'H15', 'H16', 'H17', 'H18', 'H19', 'H20',
         'H21', 'H22', 'H23', 'H24']
INCREMENTS = [1, 3, 5, 8, 10, 15]
GASES = ['Ozone', 'NitricOxide', 'NitrogenDioxide', 'NitrogenOxides', 'PM2.5', 'SulfurDioxide']

plot = plotter.Plotter()
plt.figure(figsize=(13, 10))

# Users must select data from pre-specified values
first_graph = [[sg.Text('Year'), sg.Combo(YEARS, key='year')],
               [sg.Text('Month'), sg.Combo(MONTHS, key='month')],
               [sg.Text('Day'), sg.Combo(DAYS, key='day')],
               [sg.Text('Hour'), sg.Combo(HOURS, key='hour')],
               [sg.Text('Increment of Days'), sg.Combo(INCREMENTS, key='increment')],
               [sg.Text('Gas'), sg.Combo(GASES, key='gas')]]
second_graph = [[sg.Text('Year'), sg.Combo(YEARS, key='year2')],
                [sg.Text('Month'), sg.Combo(MONTHS, key='month2')],
                [sg.Text('Day'), sg.Combo(DAYS, key='day2')],
                [sg.Text('Hour'), sg.Combo(HOURS, key='hour2')],
                [sg.Text('Increment of Days'), sg.Combo(INCREMENTS, key='increment2')],
                [sg.Text('Gas'), sg.Combo(GASES, key='gas2')]]
third_graph = [[sg.Text('Year'), sg.Combo(YEARS, key='year3')],
               [sg.Text('Month'), sg.Combo(MONTHS, key='month3')],
               [sg.Text('Day'), sg.Combo(DAYS, key='day3')],
               [sg.Text('Hour'), sg.Combo(HOURS, key='hour3')],
               [sg.Text('Increment of Days'), sg.Combo(INCREMENTS, key='increment3')],
               [sg.Text('Gas'), sg.Combo(GASES, key='gas3')]]

# Create the layout of the window
layout = [[sg.Text('Select Desired Data')],
          [sg.Text('Period'), sg.Combo(['Day', 'Month', 'Year'], key='period')],
          [sg.Text('Note: Plot will start at the beginning of selected period')],
          [sg.Text('Note 2: Sulfur Dioxide starts in 2017')],
          [sg.Text('(i.e. year will start January 1st, no matter the date selected)')],
          [sg.Frame(layout=first_graph, title='Plot 1: Blue'),
           sg.Frame(layout=second_graph, title='Plot 2: Red'),
           sg.Frame(layout=third_graph, title='Plot 3: Greens')],
          [sg.Button('Ok'), sg.Button('Cancel')]]

# Create the Window
sg.theme('Green')
window = sg.Window('Window Title', layout)

# Event Loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break
    elif event == 'Ok':
        try:
            plt.clf()
            if values['period'] == 'Year':
                if values['year'] != '':
                    plot.hour_plotter(values['hour'], 'Year', values['year'], '01',
                                      values['increment'], values['gas'], 'Blue')
                if values['year2'] != '':
                    plot.hour_plotter(values['hour2'], 'Year', values['year2'], '01',
                                      values['increment2'], values['gas2'], 'Red')
                if values['year3'] != '':
                    plot.hour_plotter(values['hour3'], 'Year', values['year3'], '01',
                                      values['increment3'], values['gas3'], 'Green')
                plt.show()
            elif values['period'] == 'Month':
                if values['year'] != '':
                    plot.hour_plotter(values['hour'], 'Month', values['year'], values['month'],
                                      values['increment'], values['gas'], 'Blue')
                if values['year2'] != '':
                    plot.hour_plotter(values['hour2'], 'Month', values['year2'], values['month'],
                                      values['increment2'], values['gas2'], 'Red')
                if values['year3'] != '':
                    plot.hour_plotter(values['hour3'], 'Month', values['year3'], values['month'],
                                      values['increment3'], values['gas3'], 'Green')
                plt.show()
            elif values['period'] == 'Day':
                if values['year'] != '':
                    plot.day_plotter(values['year'], values['month'], values['day'], values['gas'], 'Blue')
                if values['year2'] != '':
                    plot.day_plotter(values['year2'], values['month2'], values['day2'], values['gas2'], 'Red')
                if values['year3'] != '':
                    plot.day_plotter(values['year3'], values['month3'], values['day3'], values['gas3'], 'Green')
                plt.show()
            else:
                print("You didn't enter a period")
        except FileNotFoundError:
            print('Your gas was incorrect! Try again.')
        except ValueError:
            print('Your year is wrong :/ Please try again')
        except KeyError:
            print('Your day or month are wrong :/ Please try again')
        except TypeError:
            print('Your increment is wrong :/ Please try again')

window.close()
