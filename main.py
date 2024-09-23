import pandas as pd
import random

def filter_genre(genre):
    if genre == 'Action' or genre == 'action':
        print(df.loc[(df['Genre'].str.contains('Action', case=False))])
    elif genre == 'Drama' or genre == 'drama':
        print(df.loc[(df['Genre'].str.contains('Drama', case=False))])
    elif genre == 'Fantasy' or genre == 'fantasy':
        print(df.loc[(df['Genre'].str.contains('Fantasy', case=False))])
    elif genre == 'Comedy' or genre == 'comedy':
        print(df.loc[(df['Genre'].str.contains('Comedy', case=False))])
    elif genre == 'Supernatural' or genre == 'supernatural':
        print(df.loc[(df['Genre'].str.contains('Supernatural', case=False))])
    elif genre == 'Adventure' or genre == 'adventure':
        print(df.loc[(df['Genre'].str.contains('Adventure', case=False))])
    elif genre == 'Thriller' or genre == 'thriller':
        print(df.loc[(df['Genre'].str.contains('Thriller', case=False))])
    elif genre == 'Sci-Fi' or genre == 'sci-fi':
        print(df.loc[(df['Genre'].str.contains('Sci-Fi', case=False))])
    

def add_row(name, type, genre, rating, eps):
    df.loc[len(df.index)] = [name, type, genre, rating, eps]
    
    
print('Your Anime Watchlist')
df = pd.read_csv('./watchlist.csv')

while(True):
    show_all = input('Click ENTER to show your list or 0 to exit --> ')
    if show_all=='':
        print(df)
    else:
        break
    print('-- ENTER to choose a random anime\n-- 1 to filter by genre\n-- 2 to add anime')
    choice = input()
    if choice=='':
        print(df.sample())
    elif choice=='1':
        genre = input('Filter by genre --> ')
        filter_genre(genre)
    elif choice=='2':
        name = input('Enter name --> ')
        type = input('Enter type --> ')
        genre = input('Enter genre --> ')
        rating = float(input('Enter rating --> '))
        eps = int(input('Enter number of episodes --> '))
        add_row(name, type, genre, rating, eps)
        print('Anime added!')
    
    
