class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        cards = {}
        hand.sort()

        for i in range( len(hand) ):
            if hand[i] not in cards.keys():
                cards[ hand[i] ] = 1
            else:
                cards[ hand[i] ] += 1

        while len(cards.keys()) > 0:
            start = min(cards.keys())
            cards[start] -= 1

            if cards[start] == 0:
                del cards[start] 

            for i in range( 1, groupSize ):
                currentNumber = start + i
                if currentNumber not in cards.keys() or cards[ currentNumber ] == 0:
                    return False
                else:
                    cards[ currentNumber ] -= 1
                    if cards[currentNumber] == 0:
                        del cards[currentNumber] 
        
        return True


                     