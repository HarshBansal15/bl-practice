reviews = [
  {"movie": "Inception",  "user": "alice", "rating": 9},
  {"movie": "Dune",       "user": "bob",   "rating": 8},
  {"movie": "Inception",  "user": "bob",   "rating": 7},
  {"movie": "Interstellar","user":"alice",  "rating": 10},
  {"movie": "Dune",       "user": "charlie","rating": 9},
  {"movie": "Interstellar","user":"charlie","rating": 8},
]

movie_dict = {}

for r in reviews:
    movie = r["movie"]
    rating = r["rating"]

    if movie in movie_dict:
        movie_dict[movie].append(rating)
    else:
        movie_dict[movie] = [rating]

avg_ratings = {}

for movie in movie_dict:
    total = 0
    for rating in movie_dict[movie]:
        total += rating
    avg = total / len(movie_dict[movie])
    avg_ratings[movie] = avg

top_movie = ""
max_rating = 0

for movie in avg_ratings:
    if avg_ratings[movie] > max_rating:
        max_rating = avg_ratings[movie]
        top_movie = movie

must_watch = []

for movie in avg_ratings:
    if avg_ratings[movie] >= 8.5:
        must_watch.append(movie)

user_favs = {}
user_max = {}

for r in reviews:
    user = r["user"]
    movie = r["movie"]
    rating = r["rating"]

    if user not in user_max:
        user_max[user] = rating
        user_favs[user] = movie
    else:
        if rating > user_max[user]:
            user_max[user] = rating
            user_favs[user] = movie

print("avg_ratings =", avg_ratings)
print("top_movie =", top_movie)
print("must_watch =", must_watch)
print("user_favs =", user_favs)