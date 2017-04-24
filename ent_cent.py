import media
import fresh_tomatoes

#Below is the list of fav movies
city_of_god = media.Movie("City of God","Survive in Rio","https://upload.wikimedia.org/wikipedia/en/1/10/CidadedeDeus.jpg","https://www.youtube.com/watch?v=dcUOO4Itgmw")
#print (toy_story.storyline)

easy_rider = media.Movie("Easy Rider","Starring Peter Fonda, Dennis Hopper, and Jack Nicholson","https://upload.wikimedia.org/wikipedia/en/3/32/EasyRider.jpg","https://www.youtube.com/watch?v=GwST6mpT7Ds")
#easy_rider.show_trailer()

bloodsport = media.Movie("Bloodsport","Frank Dux has entered the kumite, an illegal underground martial-arts competition where serious injury and even death are not unknown.","https://upload.wikimedia.org/wikipedia/en/4/4f/Bloodsport_%28movie_poster%29.jpg","https://www.youtube.com/watch?v=WaT9dYalyU0")
#print(bloodsport.storyline)
#bloodsport.show_trailer()

fantastic_planet = media.Movie("Fantastic Planet","This futuristic story takes place on a faraway planet where giants rule, and oppressed humanoids rebel against the machine-like leaders.","https://upload.wikimedia.org/wikipedia/en/5/55/Fantstic-planet-poster.jpg","https://www.youtube.com/watch?v=SgCxCZNkQ9E")

the_wedding_singer = media.Movie("The Wedding Singer","Funny","https://upload.wikimedia.org/wikipedia/en/8/84/The_Wedding_Singer_film_poster.jpg","https://www.youtube.com/watch?v=_bhU3NsCIDs")

beverly_hills_ninja = media.Movie("Beverly Hills Ninja","The main plot revolves around Haru (portrayed by Farley), the white orphan boy was found by a clan of ninjas as an infant in an abandoned treasure chest and was raised by them.","https://upload.wikimedia.org/wikipedia/en/1/16/Beverly_Hills_Ninja_poster.jpg","https://www.youtube.com/watch?v=L7wjZZDmyhY")

movies =[city_of_god,easy_rider,bloodsport,fantastic_planet,the_wedding_singer,beverly_hills_ninja]
fresh_tomatoes.open_movies_page(movies)
# print (media.Movie.VALID_RATINGS)
#print (media.Movie.__doc__)
#print (media.Movie.__module__)