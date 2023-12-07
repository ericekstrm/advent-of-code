priority = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

class Hand:
    def __init__(self, s, bid):
        self.cards = s
        self.bid = bid

    def nr_same_card(self):
        counts = {}
        for c in self.cards:
            counts[c] = counts.get(c, 0) + 1

        j_count = counts.pop("J", 0)

        if len(counts) <= 1:
            return 10 * len(self.cards)

        f, s = sorted(list(counts.values()), reverse=True)[:2]

        return (f + j_count) * 10 + s

    def __eq__(self, other):
        return self.cards == other.cards

    def __lt__(self, other):

        if self.nr_same_card() != other.nr_same_card():
            return self.nr_same_card() < other.nr_same_card()

        for c1, c2 in zip(self.cards, other.cards):
           if priority.index(c1) != priority.index(c2):
               return priority.index(c1) > priority.index(c2)
        return False

    def __str__(self):
        return self.cards
        # handle 

hands = []
        
with open("7.in") as input_file:
    lines = input_file.readlines()

for line in lines:
    cards, bid = line.split(" ")
    hands.append(Hand(cards, int(bid)))

hands.sort()

total = 0
for i, hand in enumerate(hands):
    total += (i + 1) * hand.bid
print(total)
