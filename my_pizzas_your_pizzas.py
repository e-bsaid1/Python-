    pizzas = ['trois saisons','thon','poulet'];
    friend_pizzas = pizzas[:];
    pizzas.append('anchois');
    friend_pizzas.append('oignon');

    for pizza1 in pizzas:
        print(f"My favorite pizzas are: {pizza1.title()}");
    
    for pizza2 in friend_pizzas:
        print(f"My friend's favorite pizzas are: {pizza2.title()}");
    
    