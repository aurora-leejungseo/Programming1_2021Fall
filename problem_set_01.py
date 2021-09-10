# START PROBLEM SET 01
print('Problem Set 01')

# PROBLEM 01 (15 points)
print('\nProblem 01')
    # 1. Uncomment valid variables
#michigan theater = 'Michigan Theater'
michigan_theater = 'Michigan Theater'
state_theater = 'State Theater'
#state_theater = State Theater

    # 2. Create a list called ann_arbor_theaters
ann_arbor_theaters = [michigan_theater, state_theater] #TODO: Replace

## checking if all the variables are there
print(ann_arbor_theaters)

    # 3. Checking the type of three variables 
michigan_theater_type = type(michigan_theater) #TODO: Replace
state_theater_type = type(state_theater) #TODO: Replace
ann_arbor_theaters_type = type(ann_arbor_theaters) #TODO: Replace

print(f'michigan_theater is a {michigan_theater_type}.')
print(f'state_theater is a {state_theater_type}.')
print(f'ann_arbor_theaters is a {ann_arbor_theaters_type}.')


# PROBLEM 02 (20 points)
print('\nProblem 02')

movies_str_1 = 'Coda, On Broadway, Raiders of the Lost Ark, Selma, Let Them Lead, Rope, Star Wars: Return of the Jedi, Follies'
## split the strings 
michigan_theater_movies = movies_str_1.split(', ') #TODO: Replace

michigan_theater_movies

movie_str_2 = 'The Green Knight, Respect, Free Guy, Together, Shang-Chi and the Legend of the Ten Rings, The Alpinist, The Lost Leondardo'

state_theater_movies = movie_str_2.split(', ') #TODO: Replace

print(michigan_theater_movies)
print(state_theater_movies)

# PROBLEM 03 (10 points)
print('\nProblem 03')

num_movies_michigan = len(michigan_theater_movies) #TODO: Replace
num_movies_state = len(state_theater_movies) #TODO: Replace

print(f'The Michigan Theater is showing {num_movies_michigan} movies this week.')
print(f'The State Theater is showing {num_movies_state} movies this week.')

# PROBLEM 04 (25 points)
print('\nProblem 04')
theater_1_seats = 140
theater_2_seats = 100
theater_3_seats = 80
theater_4_seats = 50
    # 1. using the addition operator to carculate total_seats
total_seats_state = theater_1_seats + theater_2_seats + theater_3_seats + theater_4_seats
    # 2. avg_seats_state with floor division
avg_seats_state = total_seats_state // 4
#Uncomment once you've defined avg_seats_state
print(f'The average theater at the State Theater has {avg_seats_state} seats.')

# PROBLEM 05 (30 points)
print('\nProblem 05')

    # 1. declare a variable: main_auditorium_seats
main_auditorium_seats = int(1610)

    # 2. Declare a variable: screening_room_seats
screening_room_seats = int(200)

    # 3. addition, calculate the total number of seats 
total_seats_michigan = main_auditorium_seats + screening_room_seats

    # 4. floor division to calculate the avg number of seats 
avg_seats_michigan = total_seats_michigan // 2
#Uncommend once you've defined total_seats_michigan and avg_seats_michigan
print(f'The average theater at the Michigan Theater has {avg_seats_michigan} seats.')
