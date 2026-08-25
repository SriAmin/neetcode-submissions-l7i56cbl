class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        filterTriplets = []
        for trip in triplets:
            if trip[0] <= target[0] and trip[1] <= target[1] and trip[2] <= target[2]:
                filterTriplets.append(trip)
        foundA = False
        foundB = False
        foundC = False

        for trip in filterTriplets:
            if trip[0] == target[0]:
                foundA = True
            if trip[1] == target[1]:
                foundB = True
            if trip[2] == target[2]:
                foundC = True
        return foundA and foundB and foundC