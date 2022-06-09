"""Goal: return a+b, without using +/- operator.
Constaints1: a,b can be negative.
Constraints2: empty input are not possible. -> ignore empty cases

idea1: use bit manipulators and compute plus and difference.
<<1 to double, xor = a^b, and operation = &

case1: a + b
if a*b > 0
case2: a - b = a + (-b)
elif a*b < 0

ex) 7 + 1 = 8
    0111
    0111
    --------
 xor|0110 = 6 (missing +2)
carry = &<<1|0010 = 2
--------------
          = 8
_______________
xor, carry can make 8
while carry:
xor = x^carry

    6^2
    0110
    0010
    ____
xor 0100 = 4
carry = &<<1 = 0010<<1=0100 = 4
=> 4+4 = 8
    xor|4^4 =0
    carry = r&r <<1 = 0100 <<1 = 1000 = 8
    0^8=1000
    carry=0000&1000=0

    ex) 8 + (-1) = 7
    xor=1000^0001 = 1001 = 9 -> need 2 as carry
    carry = (8&1)<<1 = 0 not 2
    carry =
    flip 1000 -> 0111
    0111&1 = 0111
             0001
             _____
             0001 -> at 1st position needs to borrow 1
        <<1  0010 =2 yes, this is wanted!

"""
class Solution:
    def getSum(self,a,b):
        if a < b:
            x, y = abs(b), abs(a)
            # return self.getSum(b,a)
        else:
            x,y=abs(a),abs(b)
        sign = 1
        if a < 0:
            sign = -1
        #addition
        if a*b >= 0:
            while y:
                xor = x ^ y
                carry = (x & y) << 1
                x, y= xor, carry
        #difference
        else:
            while y:
                xor = x ^ y
                carry = (~x & y) << 1
                x, y = xor, carry
        return sign*x
if __name__ == '__main__':
    s = Solution()
    print(s.getSum(-16,14))