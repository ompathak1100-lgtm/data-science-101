def user_input():
    a=int(input("Enter your weight here Astronaut: "))
    while a<=0 or a>300:
        print("I know you follow the rules of physics astronaut enter correct weight")
        a=int(input("Enter your weight here Astronaut: "))
    return a

def multi_planatery_weight(x):
    gravity_list={'Mercury':3.7,
             'Venus':8.87,
             'Mars':3.71,
             'Jupiter':24.79,
             'Saturn':10.44,
             'Uranus':8.69,
             'Neptune':11.15}
    
    for planets,gravity in gravity_list.items():
        y=lambda p,q: (p/9.81)*q
        z=round(y(gravity,x),2)
        q=f'your weight on {planets} is {z}Kg'
        print(q)
        with open("weight_log.txt","a") as f:
            f.write(q)

def single_planetery_weight(x):
    planet_list={1:'Mercury',
             2:'Venus',
             3:'Mars',
             4:'Jupiter',
             5:'Saturn',
             6:'Uranus',
             7:'Neptune'}
    
    print(planet_list)    

    planet=int(input('enter a number from 1 to 7 to choose the planet: '))
    while planet<=0 or planet>7:
        print("Choose wisely astronaut we have got only 7 planets here")
        planet=int(input('enter a number from 1 to 7 to choose the planet: '))

    gravity_list={'Mercury':3.7,
             'Venus':8.87,
             'Mars':3.71,
             'Jupiter':24.79,
             'Saturn':10.44,
             'Uranus':8.69,
             'Neptune':11.15}

    

    planet_selected=planet_list[planet]
    planet_gravity=gravity_list[planet_selected]
    planet_weight=round(((planet_gravity/9.81)*x),2)

    w=f"Your weight on {planet_selected} is {planet_weight}kg"
    print(w)
    with open("weight_log.txt","a") as f:
        f.write(w)

def main():
    name=input('What is your name Astronaut: ')
    print(f'Greetings Astronaut {name}')
    print("Let's calculate your weight on different planets")
    x=user_input()
    while True:    
        choice=input("Type 'one' if you want to choose a planet \nType 'all' if you want to select all planets at once: ")
        if choice=="all":
            multi_planatery_weight(x)
            break
        elif choice=="one":
            single_planetery_weight(x)
            break
        else:
            print("You got only 2 choices one or all")    
main()
