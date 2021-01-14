def last_digit(n1, n2):
    
    if n1==0 or n2 ==0:
        return 1
    else:
        if int(str(n1)[-1]) == 5:
            return 5
        if int(str(n1)[-1]) == 6:
            return 6
        if int(str(n1)[-1]) == 0:
            return 0
        if int(str(n1)[-1]) == 1:
            return 1
        if int(str(n1)[-1]) == 2:
            if n2 % 4 == 0:
                return 6
            if n2 % 4 == 1:
                return 2
            if n2 % 4 == 2:
                return 4
            if n2 % 4 == 3:
                return 8
        if int(str(n1)[-1]) == 3:
            if n2 % 4 == 0:
                return 1
            if n2 % 4 == 1:
                return 3
            if n2 % 4 == 2:
                return 9
            if n2 % 4 == 3:
                return 7
        if int(str(n1)[-1]) == 4:
            if n2 % 2 == 0:
                return 6
            if n2 % 2 == 1:
                return 4
        if int(str(n1)[-1]) == 7:
            if n2 % 4 == 0:
                return 1
            if n2 % 4 == 1:
                return 7
            if n2 % 4 == 2:
                return 9
            if n2 % 4 == 3:
                return 3
        if int(str(n1)[-1]) == 8:
            if n2 % 4 == 0:
                return 6
            if n2 % 4 == 1:
                return 8
            if n2 % 4 == 2:
                return 4
            if n2 % 4 == 3:
                return 2
        if int(str(n1)[-1]) == 9:
            if n2 % 2 == 0:
                return 1
            if n2 % 2 == 1:
                return 9
  
 # Solution 2
  E = [
  [0, 0, 0, 0], [1, 1, 1, 1],
  [6, 2, 4, 8], [1, 3, 9, 7],
  [6, 4, 6, 4], [5, 5, 5, 5],
  [6, 6, 6, 6], [1, 7, 9, 3],
  [6, 8, 4, 2], [1, 9, 1, 9]
]

def last_digit(n1, n2):
    if n2 == 0: return 1
    return E[n1 % 10][n2 % 4]
