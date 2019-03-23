import itertools
import matplotlib.pyplot as plt
import pandas as pd
import re
class WhatsApp():

    def parse_file(self):
        text_file = self.chat_log
        pat = re.compile(r'^(\[\d\d\d\d-\d\d-\d\d,.*?)(?=^^\[\d\d\d\d-\d\d-\d\d,|\Z)', re.S | re.M)
        with open(text_file) as f:
            data = [m.group(1).strip().replace('\n', ' ') for m in pat.finditer(f.read())]
        sender = []
        message = []
        datetime = []
        for row in data:
            date_str = re.search('\[(.*?)\w\w\]', row).group(1)
            datetime.append(date_str.split(',')[0])

            try:
                s = re.search('] (.*?):', row).group(1)
                sender.append(s)
            except:
                sender.append('')

            try:
                message.append(row.split(': ', 1)[1])
            except:
                message.append('')

        df = pd.DataFrame(zip(datetime, sender, message), columns=['timestamp', 'sender', 'message'])
        df['timestamp'] = pd.to_datetime(df.timestamp, format='%Y-%m-%d')
        df = df[df.sender != ''].reset_index(drop=True)
        print("*"*100)
        print("*"*100)
        print(df)
        print("*"*100)
        x = df.sender.values

        names = [];
        message_length = []
        for k, g in itertools.groupby(x):
            names.append(k)
            message_length.append(len(list(g)))

        df['characters'] = df.message.apply(len)
        df['words'] = df.message.apply(lambda x: len(x.split()))

        print(df)
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
        plt.show()
    def __init__(self, file):
        self.file = "Hello"
        self.chat_log = file
        pass