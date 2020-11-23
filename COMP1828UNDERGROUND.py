import pandas as pd
from pathlib import Path

class Dijkstra:

    def __init__(self, start, end, time=""):

        self.start = start.upper()
        self.end = end.upper()
        self.time = time
        self.train_map = {}
        self.load_info()
        self.dijk()

    def load_info(self):
        file_str = Path('.').absolute()
        file_str = str(file_str.joinpath('Stations.xls'))
        train_df = pd.read_excel(file_str)
        train_df.columns = ['Line', 'Direction', 'StationA', 'StationB', 'KMs', 'unimpeded', 'Peak', 'Offpeak']
        drop_list = ['Direction', 'KMs', 'unimpeded']
        if self.inspect_time() == 'offpeak':
            drop_list.append('Peak')
        else:
            drop_list.append('Offpeak')
        train_df = train_df.drop(drop_list, axis=1)
        train_df.columns = ['Line', 'StationA', 'StationB', 'Time']
        for station in set(train_df['StationA']):
            connected_stations_df = train_df[train_df['StationA'] == station]
            connected_stations = {connected_stations_df.iloc[x, 2]: connected_stations_df.iloc[x, 3]
                                  for x in range(0, connected_stations_df.shape[0])}
            self.train_map[station] = connected_stations

    def inspect_time(self):
        hour = 0
        if "am" in self.time or "pm" in self.time:
            day_time = "am" if "am" in self.time else "pm"
            hour += 0 if "am" in self.time else 12
            if ":" in self.time:
                minutes = int(self.time[self.time.find(":") + 1:self.time.find(day_time)])
                hour += 1 if minutes >= 30 else 0
                hour += int(self.time[:self.time.find(':')])
            else:
                hour += int(self.time[:self.time.find(day_time)])
        elif ":" in self.time:
            minutes = int(self.time[self.time.find(":") + 1:])
            hour += 1 if minutes >= 30 else 0
            hour += int(self.time[:self.time.find(':')])
        else:
            print("time in invalid format")
            return None
        if (hour >= 10 and hour <= 16) or hour > 19:
            return 'offpeak'
        else:
            return 'peak'

    def least_cost(self, costs, processed):
        least = float("inf")
        station_name = None
        for station in costs.keys():
            cost = costs[station]
            if cost < least and station not in processed:
                station_name = station
                least = cost
        return station_name

    def dijk(self):
        parents = {x: self.start for x in self.train_map[self.start].keys()}
        costs = self.train_map[self.start]
        processed = []
        for station in self.train_map.keys():
            if station not in costs.keys():
                costs[station] = float('inf')
        current_stop = self.least_cost(costs, processed)
        while current_stop is not None:
            cost = costs[current_stop]
            neighbours = self.train_map[current_stop]
            for n in neighbours.keys():
                new_cost = cost + neighbours[n]
                if new_cost < costs[n]:
                    costs[n] = new_cost
                    parents[n] = current_stop
            processed.append(current_stop)
            current_stop = self.least_cost(costs, processed)
        print('Time to get from {0} to {1} is: {2} minutes.'.format(self.start, self.end, costs[self.end]))
        last = self.end
        route = [self.end]
        while last != self.start:
            last = parents[last]
            route += [last]
        print(f'Stops along the way: {route}')
