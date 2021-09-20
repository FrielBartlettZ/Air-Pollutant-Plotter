import pandas as pd
years = ['2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']

# For data files downloaded from http://www.airqualityontario.com/history/ as of 2021-09-20
# Must convert csv to .xlsx
# Will split a ten year file from 01-01-2011 to 31-12-2020 into its component years.
# Will create new sheets in excel representing each year, with year as label.



class YearDivider:

    def __init__(self, region, green_gas):

        self.file = green_gas + region + '.xlsx'
        self.data = pd.read_excel(self.file, skiprows=20)


    # Finds the specified year in the data
    def find_year(self, offset, year, column):
        for i in self.data.index[offset:]:
            if year in str(self.data[column][i]):
                return i

        return 'Year not Found'

    def split_file(self):
        offset = 0
        for year in years:
            year_index = self.find_year(offset, year, 'Date')

            if year_index == 'Year not Found':
                df1 = None
            elif year == '2012' or year == '2016' or year == '2020':
                df1 = self.data.copy()[self.data.columns][year_index:year_index + 366]
                offset += 366
            else:
                df1 = self.data.copy()[self.data.columns][year_index:year_index + 365]
                offset += 365

            if df1 is not None:
                with pd.ExcelWriter(self.file, mode='a') as writer:
                    df1.to_excel(writer, sheet_name=year)
