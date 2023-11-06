#leetcode daily challenge: day 08
# 06/11/23
class SeatManager:
    def __init__(self, n: int):
        self.seats = [number for number in range(1, n+1)]
        self.seats.sort()
    def reserve(self) -> int:
        if self.seats:
            return heapq.heappop(self.seats)
        return -1
    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.seats, seatNumber)
        #self.available_seats.sort()


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
