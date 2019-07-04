017. Number letter counts
#Problem
https://projecteuler.net/problem=17

#Solution
one two three four five six seven eight nine ten
eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen
twenty, twenty one ~ twenty nine
thirty, thirty one ~ thirty nine
forty, forty one ~ forty nine
fifty, fifty one ~ fifty nine
sixty, sixty one ~ sixty nine
seventy, seventy one ~ seventy nine
eighty, eighty one ~ eighty nine
ninety, ninety one ~ ninety nine
one hundred
two hundred
...
nine hundred
one thousand

---

[ ] [ ] [ ] + 3 + 8
 0   0   1~10 : 3 + 3 + 5 + 4 + 4 + 3 + 5 + 5 + 4 + 3 = 39
 0   1   1~9  : 6 + 6 + 8 + 8 + 7 + 7 + 9 + 8 + 8 = 67
 0   2~9 0~9  : (6 + 6 + 5 + 5 + 5 + 7 + 6 + 6) * 10 + 36 * 8 = 46 * 10 + 36 * 8 = 460 + 288 = 748
 =========================================================== 39 + 67 + 748 = 854
 1   x   x    : (3 + 7) * 99 + 854
 2   x   x    : (3 + 7) * 99 + 854
    ...
 9   x   x    : (4 + 7) * 99 + 854
 1~9 0   0    : 36 + 63 = 99
 =========================================================== 99 * 99 + 854 * 9 + 99 = 9801 + 7686 + 99 = 17586
 and          : 99 * 9 * 3 = 891 * 3 = 2673
 ===========================================================
 result = 854 + 17586 + 2673 + 11 = 21124
