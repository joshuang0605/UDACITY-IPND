import media #import media module including class Movie and its methods
import fresh_tomatoes # import fresh_tomatoes module to generate the website

#The Last Samurai
the_last_samurai = media.Movie("The Last Samurai",
                        "Struggle between two eras and two worlds",
                        "https://upload.wikimedia.org/wikipedia/en/c/c6/The_Last_Samurai.jpg",
                        "https://www.youtube.com/watch?v=WdUyHe7XTEY")

#Zero Dark Thirty
zero_dark_thirty = media.Movie("Zero Dark Thirty",
                     "A chronicle of the decade-long hunt for al-Qaeda terrorist leader Osama bin Laden after the September 2001 attacks, and his death at the hands of the Navy S.E.A.L.s Team 6 in May 2011",
                     "https://duckduckgo.com/i/24a54bfb.jpg",
                     "https://www.youtube.com/watch?v=PqDl-YI3xKM")

#300
three_hundred = media.Movie("300",
                  "Battle against the Great Persian",
                  "http://orig05.deviantart.net/58e9/f/2010/087/7/c/300_movie_poster_by_beyondwonderwall.png",
                  "https://www.youtube.com/watch?v=UrIbxk7idYA")

#The Transporter
the_transporter = media.Movie("The Transporter", "A mercernary transporter who will deliver anything",
                           "http://3.bp.blogspot.com/__cfySUj2yhk/TFfdM2Q-YBI/AAAAAAAAAj0/UBx9zqm4VuI/s1600/the_transporter_movie_poster.jpg",
                           "https://www.youtube.com/watch?v=0poXFSvX0_4")

#King Arthur
king_arthur = media.Movie("King Arthur", "A demystified take on the tale of King Arthur and the Knights of the Round Table",
                          "https://cdn.flickeringmyth.com/wp-content/uploads/2017/03/jude-law-king-arthur-poster.jpg",
                          "https://www.youtube.com/watch?v=jIM4-HLtUM0")

#Thor Ragnarok
thor_ragnarok = media.Movie("Thor Ragnarok", "Thor must fight for survival and race against time to prevent the all-powerful Hela from destroying his home and the Asgardian civilization",
                            "http://orig02.deviantart.net/2f2a/f/2017/013/0/f/thor___ragnarok_movie_poster_2_by_jackjack671120-davb16o.jpg",
                            "https://www.youtube.com/watch?v=ue80QwXMRHg")

#List array of movies
movies = [the_last_samurai, zero_dark_thirty, three_hundred, the_transporter, king_arthur, thor_ragnarok]

#Display the website
fresh_tomatoes.open_movies_page(movies)
