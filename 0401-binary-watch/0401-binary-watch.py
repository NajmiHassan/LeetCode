class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        times = []

        for h in range(12):
            for m in range(60):

                total_bits = bin(h).count('1') + bin(m).count('1')

                if total_bits == turnedOn:
                    times.append(f"{h}:{m:02d}")
        return times