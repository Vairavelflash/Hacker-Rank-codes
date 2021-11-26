# my code
def is_leap(year):
    if(year % 4) == 0:
        if(year % 100) != 0:
            leap = True
            return leap
            
        elif(year %400) == 0:
            leap = True
            return leap
        else:
            leap = False
            return leap
    else:
        leap = False
        return leap
    # leap = False
    
    # Write your logic here
    

    
year = int(input())
print(is_leap(year))

# standard code
def is_leap(year):
    leap = False    
    leap = (year%400==0) or (year%4==0 and year%100!=0)    
    return leap

year = int(input())
print(is_leap(year))