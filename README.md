# letterboxdpy

[![PyPI version](https://badge.fury.io/py/letterboxdpy.svg)](https://badge.fury.io/py/letterboxdpy)
[![Downloads](https://static.pepy.tech/personalized-badge/letterboxdpy?period=total&units=none&left_color=grey&right_color=blue&left_text=Downloads)](https://pepy.tech/project/letterboxdpy)
![format](https://img.shields.io/pypi/format/letterboxdpy)

## Installation

```
pip install letterboxdpy
```

## **User Objects**

```python
from letterboxdpy import user
nick = user.User("nmcassa")
print(nick.jsonify())
```

```json
{
    "username": "nmcassa",
    "favorites": [
        "The Grand Budapest Hotel",
        "The King of Comedy",
        "The Alpinist",
        "The Graduate"
    ],
    "stats": {
        "Films": "360",
        "This year": "86",
        "List": "1",
        "Following": "7",
        "Followers": "6"
    },
    "watchlist_length": "73"
}
```

## **user_genre_info(user object)**

```python
from letterboxdpy import user
nick = user.User("nmcassa")
print(user.user_genre_info(nick))
```

```python
{'action': 55, 'adventure': 101, 'animation': 95, 'comedy': 188, 'crime': 22, 'documentary': 16, 'drama': 94, 'family': 109, 'fantasy': 54, 'history': 5, 'horror': 27, 'music': 9, 'mystery': 30, 'romance': 29, 'science-fiction': 48, 'thriller': 43, 'tv-movie': 13, 'war': 4, 'western': 5}
```

## **user_following(user object) / user_followers(user object)**

```python
from letterboxdpy import user
nick = user.User("nmcassa")
print(user.user_following(nick))
print(user.user_followers(nick))
```

```python
['ryanshubert', 'Sean Baker', '24framesofnick', 'ConnorEatsPants', 'IHE', 'karsten', 'jordynhf']
['ryanshubert', 'Crescendo House', 'Brendonyu668', 'Parker Bobbitt', 'jordynhf', 'Dan']
```

## **user_films_watched(user object)**

```python
from letterboxdpy import user
nick = user.User("nmcassa")
print(user.user_films_watched(nick))
```

```
...all of the users watched movies...
```

## **user_reviews(user object)**

```python
from letterboxdpy import user
nick = user.User("nmcassa")
print(user.user_reviews(nick))
```

```python
[{'movie': 'Beast', 'rating': ' ★½ ', 'date': '23 Aug 2022', 'review': 'Did not like it'}, {'movie': 'Men', 'rating': ' ★ ', 'date': '25 May 2022', 'review': 'What could he possibly be trying to say with this'}, {'movie': 'Nightcrawler', 'rating': ' ★★★ ', 'date': '04 May 2022', 'review': 'Jake is a pussy nerd loser in this'}, {'movie': 'The Graduate', 'rating': ' ★★★★ ', 'date': '30 Jan 2022', 'review': 'If only they didn’t play the same song like 20 times'}, {'movie': "I'm Thinking of Ending Things", 'rating': ' ★★★★ ', 'date': '14 Feb 2021', 'review': 'yeah i dont get it'}]
```

## **Movie Object**

```python
from letterboxdpy import movie
king = movie.Movie("king kong")
print(king.jsonify())

king = movie.Movie("king kong", 2005)
print(king.jsonify())
```

```json
{
    "title": "king-kong",
    "director": [
        "Merian C. Cooper",
        "Ernest B. Schoedsack"
    ],
    "rating": "3.85 out of 5",
    "year": "1933",
    "genres": [
        "horror",
        "adventure",
        "fantasy"
    ]
}
{
    "title": "king-kong-2005",
    "director": "Peter Jackson",
    "rating": "3.33 out of 5",
    "year": "2005",
    "genres": [
        "action",
        "adventure",
        "drama"
    ]
}

```

## **movie_details(movie object)**

```python
from letterboxdpy import movie
king = movie.Movie("king kong", 2005)
print(movie.movie_details(king))
```

```python
{'Country': ['New Zealand', 'USA', 'Germany'], 'Studio': ['Universal Pictures', 'WingNut Films', 'Big Primate Pictures', 'MFPV Film'], 'Language': ['English']}
```

## **movie_description(movie object)**

```python
from letterboxdpy import movie
king = movie.Movie("king kong", 2005)
print(movie.movie_description(king))
```

```
In 1933 New York, an overly ambitious movie producer coerces his cast and hired ship crew to travel to mysterious Skull Island, where they encounter Kong, a giant ape who is immediately smitten with...
```

## **movie_popular_reviews(movie object)**

```python
from letterboxdpy import movie
king = movie.Movie("king kong" 2005)
print(movie.movie_popular_reviews(king))
```

```
[{'reviewer': 'BRAT', 'rating': ' ★★★½ ', 'review': 'naomi watts: bitch, it’s king kongking kong: yes, i’m king kongadrien brody: this is king kong?jack black: yes, miss king kong!!kyle chandler: and i’m kyle chandler :)'}, {'reviewer': 'josh lewis', 'rating': ' ★★★★ ', 'review': 'This review may contain spoilers. I can handle the truth.'}, {'reviewer': 'ashley 🥀', 'rating': ' ★½ ', 'review': 'To quote one of the funniest tweets I have ever seen: did King Kong really think he was gonna date that lady?'}, ...
```

## **List Object**

```python
from letterboxdpy import list
list = list.List("Horrorville", "The Official Top 25 Horror Films of 2022")
print(list.jsonify())
```

```json
{
    "url": "https://letterboxd.com/horrorville/list/the-official-top-25-horror-films-of-2022/",
    "title": "The Official Top 25 Horror Films of 2022",
    "author": "Horrorville",
    "description": "To be updated monthly. It's ranked by average Letterboxd member rating. See the official top 50 of 2021 on Horrroville here. Eligibility rules: \u2022\u00a0Feature-length narrative films included only. \u2022\u00a0Shorts, documentaries, and TV are excluded. \u2022\u00a0Films must have their festival premiere in 2022 or their first national release in any country in 2022. \u2022\u00a0Films must have the horror genre tag on TMDb and Letterboxd. \u2022\u00a0There is a 1,000 minimum view threshold. Curated by Letterboxd Head of Platform Content Jack Moulton.",
    "movies": [
        "Nope",
        "Mad God",
        "Prey",
        "Bodies Bodies Bodies",
        "You Won't Be Alone",
        "X",
        "The House",
        "Fresh",
        "Final Cut",
        "Saloum",
        "The Black Phone",
        "Bhoothakaalam",
        "Nanny",
        "Resurrection",
        "15 Ways to Kill Your Neighbour",
        "Speak No Evil",
        "Watcher",
        "Scream",
        "Crimes of the Future",
        "Flux Gourmet",
        "Medusa",
        "What Josiah Saw",
        "Satan's Slaves 2: Communion",
        "Piggy",
        "Dawn Breaks Behind the Eyes"
    ],
    "filmCount": 25
}
```

## **list_tags(list object)**

```python
from letterboxdpy import list
a = list.List("Horrorville", "The Official Top 25 Horror Films of 2022")
print(list.list_tags(a))
```

```python
['official', 'horror', 'letterboxd official', 'letterboxd', '2022', 'topprofile', 'top 25']
```