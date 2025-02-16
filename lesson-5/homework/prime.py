def is_prime(n):
    boool =True
    if n==1:
       return False
    else:
        for i in range(2, n+1):
          if n%i ==0:
             boool= False
             break
          return boool
        


    