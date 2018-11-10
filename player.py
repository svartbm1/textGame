import item

class Player:
    def __init__(self, name):
        self.name = name
        self.pointbuy = 30
        self.stats = {
            "str" : 8,
            "dex" : 8,
            "con" : 8,
            "int" : 8,
            "wis" : 8,
            "cha" : 8
        }

    def stat_cost(self, new, old):
        cost = new-8
        if new > 13:
            cost += new - 13
        if new > 17:
            cost += new - 17
        if old != 8:
            cost -= self.stat_cost(old, 8)
        return cost

    def assign_stat(self, stat, value):
        s = stat.lower()
        if value < 5 or value > 18:
            print "Scores must be between 5 and 18."
        elif s in self.stats:                
            if self.pointbuy >= self.stat_cost(value, self.stats[s]):
                self.pointbuy -= self.stat_cost(value, self.stats[s])
                self.stats.update({s: value})
        else: 
            print stat + "is not a valid stat."

    def print_info(self):
        print self.name + "\n Points left:" + str(self.pointbuy) + "\n Stats: " + str(self.stats['str']) + " " + str(self.stats['dex'])+ " " + str(self.stats['con'])+ " " + str(self.stats['int'])+ " " + str(self.stats['wis'])+ " " + str(self.stats['cha'])
