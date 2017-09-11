import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")
#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(avatar.storyline)
#avatar.show_trailer()

three_hundred = media.Movie("300",
                  "Battle against the Great Persian",
                  "http://orig05.deviantart.net/58e9/f/2010/087/7/c/300_movie_poster_by_beyondwonderwall.png",
                  "https://www.youtube.com/watch?v=UrIbxk7idYA")

hunger_games = media.Movie("Hunger Games", "Storyline",
                           "https:/upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch?v=mfmrPu43DF8")

king_arthur = media.Movie("King Arthur", "Storyline",
                          "https://cdn.flickeringmyth.com/wp-content/uploads/2017/03/jude-law-king-arthur-poster.jpg",
                          "https://www.youtube.com/watch?v=jIM4-HLtUM0")


thor_ragnarok = media.Movie("Thor Ragnarok", "Storyline",
                            "http://orig02.deviantart.net/2f2a/f/2017/013/0/f/thor___ragnarok_movie_poster_2_by_jackjack671120-davb16o.jpg",
                            "https://www.youtube.com/watch?v=ue80QwXMRHg")

movies = [toy_story, avatar, three_hundred, hunger_games, king_arthur, thor_ragnarok]
fresh_tomatoes.open_movies_page(movies)
