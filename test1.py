a = 10; b = 25; c = 100; d = ("cat", "dog", "bird")
if a==10:
    print("a is true")
    
    if b<40:
        print("b is true")
        
        if c>900:
            print("c is true")
            
            if "cat" in d:
                print("d is true")
                
            else:
                print("d is false")
            
        else:
            print("c is false")
            
    else:
        print("b is false")
        
else:
    print("a is false")