class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for detail in details:
            ten = ord(detail[11]) - ord('0')
            one = ord(detail[12]) - ord('0')
            age = one + 10 * ten
            if age > 60:
                count += 1
        return count

        