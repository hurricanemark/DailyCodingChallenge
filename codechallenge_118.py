'''
Date: 05/10/2022

Challenge description:
======================
Convert Roman numerals to integers.

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
{'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

Convention: 
==========
Roman numerals are written from largest to smallest. 

Rules:
=====
I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.

Key concept to solve the problem:
================================
Multiple of 3 of the same symbol can be placed before a larger symbol.

Carviat:
Can we write roman numerals in unconvetional way? eg. IIIVIII ==> 3 - 8 = 5

'''
class solution:
    def romanToInt(s):
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        # Roman numurals are written from largest to smallest.
        # So, let's traverse the string from right to left.
        for i in range(len(s) -1, -1, -1):
            print('i: {} roman: {} Intval: {}'.format( i, s[i], roman_dict[s[i]]))
            val = roman_dict[s[i]]
            
            # no more than three of the same symbol in a row.
            # e.g. IV, IX, etc.  III is less than V and IX is less than X, etc.
            if 3 * val <= int_val:
                # case of subtracting a smaller value from a larger value
                int_val = int_val - val
            else:
                # case of adding a larger value to a smaller value
                int_val = int_val + val
                
        return int_val

    if __name__ == '__main__':
        '''
        input: "MXCIV"
        Iterate through the string from right to left.
        Starting index: len('MXCIV') -1 = 4
        int_val = 0
        i = 4, val = s[4] = 'V' = 5
            3*5 <= 0 = False
            int_val = int_val + 5 = 5
          
        i = 3, val = s[3] = 'I' = 1
            3*1 <= 5 = True
            int_val = int_val - 1 = 4
            
        i = 2, val = s[2] = 'C' = 100
            3*100 <= 4 = False
            int_val = int_val + 100 = 104
        
        i = 1, val = s[1] = 'X' = 10
            3*10 <= 104 = True
            int_val = int_val - 10 = 94
        
        i = 0, val = s[0] = 'M' = 1000
            3*1000 <= 94 = False
            int_val = int_val + 1000 = 1094
            
        Answer: 1094
        '''
        print('Roman numeral: {} Integer value: {}'.format('MXCIV', romanToInt('MXCIV')))
        print('Roman numeral: {} Integer value: {}'.format('MCMXCIV', romanToInt('MCMXCIV')))
        print('Roman numeral: {} Integer value: {}'.format('LVIII', romanToInt('LVIII')))
        print('Roman numeral: {} Integer value: {}'.format('III', romanToInt('III')))
        
        
        print('This violates the convention of largest to smallest.  However, it does not violate the rules', end='\n')
        print('Roman numeral: {} Integer value: {}'.format('IIIV', romanToInt('IIIV')))
        print('Roman numeral: {} Integer value: {}'.format('IIIVIII', romanToInt('IIIVIII')))
        
        
        
    