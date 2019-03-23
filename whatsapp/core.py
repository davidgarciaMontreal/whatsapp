import itertools
import matplotlib.pyplot as plt
import pandas as pd
import re
import os
import numpy as np
import seaborn as sns
class WhatsApp():

    def parse_file(self):
        '''Convert WhatsApp chat log text file to a Pandas dataframe.'''
        text_file = self.chat_log

        # some regex to account for messages taking up multiple lines
        # pat = re.compile(r'^(\d\d\/\d\d\/\d\d\d\d.*?)(?=^^\d\d\/\d\d\/\d\d\d\d|\Z)', re.S | re.M)
        pat = re.compile(r'^(\[\d\d\d\d-\d\d-\d\d,.*?)(?=^^\[\d\d\d\d-\d\d-\d\d,|\Z)', re.S | re.M)
        with open(text_file) as f:
            # for m in pat.finditer(f.read()):
            #     a = m.group(1).strip().replace('\n', ' ')
            data = [m.group(1).strip().replace('\n', ' ') for m in pat.finditer(f.read())]
        sender = [];
        message = [];
        datetime = []
        for row in data:

            # timestamp is before the first dash
            date_str = re.search('\[(.*?)\w\w\]', row).group(1)
            datetime.append(date_str.split(',')[0])

            # sender is between am/pm, dash and colon
            try:
                s = re.search('] (.*?):', row).group(1)
                sender.append(s)
            except:
                sender.append('')

            # message content is after the first colon
            try:
                message.append(row.split(': ', 1)[1])
            except:
                message.append('')

        df = pd.DataFrame(zip(datetime, sender, message), columns=['timestamp', 'sender', 'message'])
        # df['timestamp'] = pd.to_datetime(df.timestamp, format='%Y-%m-%d, %I:%M:%S ')
        df['timestamp'] = pd.to_datetime(df.timestamp, format='%Y-%m-%d')
        df = df[df.sender != ''].reset_index(drop=True)
        # df.plot.bar()
        print("*"*100)
        print("*"*100)
        print(df)
        print("*"*100)
        x = df.sender.values

        names = [];
        message_length = []
        # generates a new group every time the value of the list changes
        # https://docs.python.org/2/library/itertools.html#itertools.groupby
        for k, g in itertools.groupby(x):
            names.append(k)
            message_length.append(len(list(g)))

        df['characters'] = df.message.apply(len)
        df['words'] = df.message.apply(lambda x: len(x.split()))

        # df.groupby('sender').mean().sort_values('characters').round(2)
        # df.groupby("timestamp").agg({"sender": np.sum, "": lambda x: x.nunique()})
        print(df)
        #df.groupby('sender')['words'].nunique().plot(kind='bar')
        # plt.show()
        #df.hist(bins=100, grid=False, xlabelsize=12, ylabelsize=12)
        df1 = df[df.sender == 'David']
        df2 = df[df.sender == 'Ros']
        bins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        df1.hist(column='words', bins=bins)
        plt.xlabel("David: Numero de Palabras en el Mensaje", fontsize=15)
        plt.ylabel("Mensajes Enviados", fontsize=15)
        df2.hist(column='words', bins=bins)
        plt.xlabel("Ros: Numbero de Palabras en el Mensaje", fontsize=15)
        plt.ylabel("Mensajes Enviados", fontsize=15)

        fig, ax = plt.subplots()
        df1.hist(column=['words'], ax=ax, bins=bins)
        df2.hist(column=['words'], ax=ax, bins=bins)

        plt.xlabel("David/Ros: Numero de Palabras en el Mensaje", fontsize=15)
        plt.ylabel("Mensajes Enviados", fontsize=15)
        # plt.xlim([22.0, 90.0])
        plt.show()
        # df2 = pd.DataFrame(zip(names, message_length), columns=['sender', 'length'])
        # print (df2)
        # df2.plot(kind='bar',x='sender', y='length')
        # plt.show()
    def __init__(self, file):
        self.file = "Hello"
        self.chat_log = file
        pass