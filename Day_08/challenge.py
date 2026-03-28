def calculate_love_score(name_1, name_2):

    combined = (name_1 + name_2).lower()
    
    true_count = 0
    love_count = 0
    
    for letter in combined:
        if letter in "true":
            true_count += 1
        if letter in "love":
            love_count += 1
    
    total = str(true_count) + str(love_count)
    
    print(total)
    
calculate_love_score("Kanye West", "Kim Kardashian")
