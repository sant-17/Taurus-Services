class UndergroundSystem:
    def __init__(self):
        self.check_ins = []
        self.check_outs = []


    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if self.check_ins:
            index_to_replace = next((i for i, subcheckin in enumerate(self.check_ins) if subcheckin[0] == id), None)

            if index_to_replace is not None:
                self.check_ins[index_to_replace] = [id, stationName, t]
                print(f"The previous check-in with ID:{id} has been replaced. Its new values are StationName:{stationName} and time:{t}")
            else:
                self.check_ins.append([id, stationName, t])
                print(f"A new check-in has been added: ID:{id}, stationName:{stationName}, time:{t}")
        else:
            self.check_ins.append([id, stationName, t])
            print(f"A new check-in has been added: ID:{id}, stationName:{stationName}, time:{t}")


    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if self.check_outs:
            index_to_replace = next((i for i, subcheckin in enumerate(self.check_outs) if subcheckin[0] == id), None)

            if index_to_replace is not None:
                self.check_outs[index_to_replace] = [id, stationName, t]
                print(f"The previous check-out with ID:{id} has been replaced. Its new values are StationName:{stationName} and time:{t}")
            else:
                self.check_outs.append([id, stationName, t])
                print(f"A new check-out has been added: ID:{id}, stationName:{stationName}, time:{t}")
        else:
            self.check_outs.append([id, stationName, t])
            print(f"A new check-out has been added: ID:{id}, stationName:{stationName}, time:{t}")


    def getAverageTime(self, startStation: str, endStation: str):
        matchs = 0
        total = 0
        average = 0

        filteredCheckIn = [check_in for check_in in self.check_ins if check_in[1] == startStation]

        if not filteredCheckIn:
            print(f"\nNo trips have been made with that initial destination -> {startStation}")
            return 0
        
        print("")
        for viaje in filteredCheckIn:
            for checkout in self.check_outs:
                if viaje[0] == checkout[0] and checkout[1] == endStation:
                    print(f"A travel has been made between {startStation} and {endStation} -> time: {checkout[2] - viaje[2]}")
                    matchs += 1
                    total += checkout[2] - viaje[2]

        if matchs == 0:
            print(f"\nNo trips have been made with that final destination -> {endStation}")
            return 0
        
        average = total/matchs
        print(f"Average time between {startStation} and {endStation} -> {average}")
        return average


if __name__ == "__main__":
    undergroundSystem = UndergroundSystem()

    undergroundSystem.checkIn(45, "Leyton", 3)
    undergroundSystem.checkOut(45, "Juarez", 15)
    undergroundSystem.checkIn(55, "Leyton", 3)
    undergroundSystem.checkOut(55, "Juarez", 99)
    undergroundSystem.checkIn(65, "Cancun", 3)
    undergroundSystem.checkOut(65, "Juarez", 15)
    undergroundSystem.checkIn(75, "Juarez", 3)

    print("")

    print(undergroundSystem.getAverageTime("Leyton", "Juarez"))
    print(undergroundSystem.getAverageTime("Cancun", "Juarez"))
    print(undergroundSystem.getAverageTime("Bogota", "Juarez"))
    print(undergroundSystem.getAverageTime("Cancun", "Leyton"))

    undergroundSystem.checkIn(45, "Juarez", 9)
    undergroundSystem.checkOut(45, "Leyton", 55)

    print("")

    print(undergroundSystem.getAverageTime("Leyton", "Juarez"))
    print(undergroundSystem.getAverageTime("Juarez", "Leyton"))
    

    