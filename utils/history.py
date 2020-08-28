from datetime import datetime, timezone

def open_history():
    with open('history.txt', 'w'):
        pass

def show_history():
    with open("history.txt", 'r') as file:
        history = [line.strip() for line in file.readlines()]
        for row in history:
            print(row)

class Save_to_history:
    def __init__(self, history):
        self.history = history

    @property
    def date_time(self):
        time = datetime.now(timezone.utc)
        return time.strftime('%H:%M:%S %d-%m-%Y')

    def save(self):
        data = f'{self.date_time}: {self.history}\n'
        with open("history.txt", 'a') as file:
            file.write(data)