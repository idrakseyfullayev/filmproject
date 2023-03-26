from django.shortcuts import render, HttpResponse, get_object_or_404, get_list_or_404, redirect
from film.models import FilmModel, ActorModel, LikeModel, CommentModel, CategoryModel, ViewNumberModel
from account.models import Account
from django.views import generic
from django.contrib import messages
from django.db.models import Q
from film.forms import FilmForm
# Create your views here.

 

class IndexView(generic.View):
     def get(self, request, *args, **kwargs):
          films = FilmModel.objects.all()
          print(films,3)
          query = request.GET.get("query")
          
     
          if query:
               films = FilmModel.objects.filter(
                    Q(name__contains = query) | Q(about__contains = query)
               )

          print(films, 5)     
     
          context = {
               "films": films
          }
          
          return render(request, "index.html", context)     

     # def post():
     #      pass
     # queryset = FilmModel.objects.all()
     # context_object_name = "films"
     # template_name = "index.html"


# def index(request):

#      films = FilmModel.objects.all()
#      # actors = ActorModel.objects.all()
#      accounts = Account.objects.order_by("user__username")
#      # list1 = []
     
#      # for i in accounts:
#      #      print(i)
#      #      list1.append(i)
#      # print(list1)
#      # list1.sort()
#      # print(list1)
    

#      context = {
#           "title": "index page",
#           "films": films,
#           # "actors": actors,
#           "accounts": accounts
#      }



#      return render(request, "index.html", context)



class DetailView(generic.View):
     def get(self, request, id, *args, **kwargs):
          film = get_object_or_404(FilmModel, id=id)
          print(film)
          

               
               
          if request.user.is_authenticated:
               if not ViewNumberModel.objects.filter(user = request.user).exists():
                    ViewNumberModel.objects.create(
                         user = request.user,
                         film = film
                    )
                    film.views_number += 1
                    film.save()
                    
          else:
               film.views_number += 1
               film.save()

                         
          
          

          # like_number = len(film.film_likes.all())

          

          context = {
               "film": film,
               # "like_number": like_number
          }

          

          return render(request, "detail.html", context)
     
     def post(self, request, *args, **kwargs):
          if request.POST.get("choice") == "Like":
               filmid = request.POST.get("filmid")
               film = FilmModel.objects.get(id = filmid)
               print(film)

               if not LikeModel.objects.filter(user=request.user, film=film).exists(): # modelin obyekti var ya yox
                    LikeModel.objects.create(
                         user = request.user,
                         film = film
                    )
               else:
                    messages.info(request, "Alredy like")

               return redirect("film:detail", filmid)

          elif request.POST.get("choice") == "comment":
               filmid = request.POST.get("filmid")
               film = FilmModel.objects.get(id=filmid)
               comment = request.POST.get("comment")

               CommentModel.objects.create(
                    film = film,
                    user = request.user,
                    comment = comment,
               )
               # print(CommentModel.objects.get(comment=comment)) #  niye film = film islemir
               # print(CommentModel.objects.create(
               #      film = film,
               #      user = request.user,
               #      comment = comment,
               # ))
                          

               messages.info(request, "Comment created")

               return redirect("film:detail", filmid)

# def details(requst, id):
#      film = get_object_or_404(FilmModel, id=id)
     
#      film.views_number += 1
#      film.save()


#      context = {
#           "film": film,
#      }

#      return render(requst, 'detail.html', context)


class Actor_detailsView(generic.View):
     def get(self, request, id, *args, **kwargs):
          actor = get_object_or_404(ActorModel, id = id)

          context = {
               "actor": actor
          }

          return render(request, "actor_details.html", context)



# def actor_details(request, id):
#      actor = get_object_or_404(ActorModel, id=id)

#      contex = {
#           "actor": actor
#      }     

#      return render(request, 'actor_details.html', contex )



class ActorsView(generic.View):
     def get(self, request, id, *args, **kwargs):
          film = get_object_or_404(FilmModel, id = id)
          actors = get_list_or_404(ActorModel, films = film)
          
          
          

          query = request.GET.get("query")
          # query = query.replace(" ", "")
          # print(query)
         
          
     
          if query:
               film_actors = ActorModel.objects.filter(films = film)
               # actors = film_actors.all().filter( Q(name__contains = query) | Q(surname__contains = query))
               actors = film_actors.filter(Q(name__contains = query) | Q(surname__contains = query))
               # print(actors, 1)
              

          context = {
               'actors': actors
          }

          return render(request, 'actors.html', context)


# def actors(request, id):
#      film = get_object_or_404(FilmModel, id=id)
#      # actors = film.actors.all()
#      actors = get_list_or_404(ActorModel, films = film)   
     
#      # actors = ActorModel.objects.filter(film__id = id)
#      # actors = get_list_or_404(ActorModel, film__id = id)

#      context = {
#           "actors": actors,
#           "film": film,
#      }

#      return render(request, 'actors.html', context)


class CreateFilmView(generic.View):
     def get(self, request, *args, **kwargs):
          form = FilmForm()

          context = {
               "forms": form
          }

          return render(request, 'film-create.html', context)

     def post(self, request, *args, **kwargs):
          form = FilmForm(request.POST)

          if form.is_valid():
               poster = form.changed_data.get("poster")
               video = form.changed_data.get("video")
               name = form.changed_data.get("name")
               rating = form.changed_data.get("rating")
               pub_date = form.changed_data.get("pub_date")
               about = form.changed_data.get("about")
               actors = form.changed_data.get("actors")

               FilmModel.objects.create(
                    poster = poster,
                    video = video,
                    name = name,
                    rating = rating,
                    pub_date = pub_date,
                    about = about,
                    actors = actors
               )
          return redirect('film:film-create')     


             

#     rating_list = []
#     for film in films:
#          rating_list.append([film.name,film.rating])     

#     print(rating_list)     

#     list_film_min_rat = []
#     min_rat = rating_list[1][1]
#     for film, rat in rating_list:
#          if rat < min_rat:
#               min_rat = rat
#               min_film_rating = film
#               list_film_min_rat = [min_film_rating, str(min_rat)]

#     print(list_film_min_rat)
#     print(" ".join(list_film_min_rat))
#     print(min_film_rating, min_rat)

#     context["lower_rating"] =  f"{min_film_rating} {min_rat}"  




#      context = {
#           'title': "index page123",
#           "heading": "index page12345",
#           "paragraph": "This about index page"
#      }

#      a = request.GET.get("a")
#      b = request.GET.get("b")

#      if a and b:
#           context["a"] = a
#           context["b"] = b
#           sum = int(a) + int(b)

#           context["sum"] = sum
     


#      if request.method == "POST":
#           info = request.POST.get("info")
#           context["info"] = info.title()

#      return render(request, 'index.html', context)



# def fib(request):

#      fib_context = {
#           "title": "fibonacci",
#           "heading": "Fibonacci sequences",
#           "general_information": """The Fibonacci Sequence is the series of numbers:
#           (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...).The next number is found by adding up the two numbers before
#           it."""
#      }

#      if request.method == "POST":
          
#           def fib_n(n):
#                if n == 1:
#                     return 0
#                elif n == 2:
#                     return 1
#                n1 = 0
#                n2 = 1     
#                for i in range(3, n+1):
#                     n1, n2 = n2, n1+n2
#                return n2
 
#           n = request.POST.get("n")
#           try:
#                if int(n) < 1:
#                     fib_context["n"] = "Enter natural number"
#                else:
#                     y = fib_n(int(n))
#                     fib_context["n"] = f"This element of the Fibonacci sequence is {y}"
#           except ValueError:
#                fib_context["error"] = "Enter natural number"

#      import datetime
#      now = datetime.datetime.now().strftime("%d.""%m.""%Y ""%H:""%M")
#      print(now)
#      fib_context["now"] = now                
     
#      return render(request, "fib.html", fib_context)



# def test(request):
#      return HttpResponse([3,5])




# def list_intersection(request):
#      org_list_1 = [1, 2, 3, 5, 7, 8, 9, 10]
#      list_intrscn = {
#           'title': "List intersection",
#           'heading': "List intersection",
#           'information': "Insert the elements of the list into the button to get the intersection with list1",
#           'org_list': f"List1 = {org_list_1}"

#      }

#      string1 = request.GET.get("list_from_site")

#      if string1:
#           list_get = string1.split(",")
#           list_get = list(map(lambda x: int(x), list_get)) # burda deyisenin adini deyismedim problem yoxdu ki??
#           list_intrscn["list_get"] = f"Your list = {list_get}"
#           list_get_org_intrsc = []
#           for i in org_list_1:
#                if i in list_get:
#                     list_get_org_intrsc.append(i)     
#           list_intrscn["list_get_org_intrsc"] = f"Lists_intersection{list_get_org_intrsc}"          


#      if request.method == "POST":
#           string2 = request.POST.get("list_1_from site")
#           list_get_1 = string2.split(",")
#           list_get_1 = list(map(lambda x: int(x), list_get_1))
#           list_intrscn["list_get_1"] = f'Your list = {list_get_1}'
#           list_get_org_intrsc_1 = []
#           for i in org_list_1:
#                if i in list_get_1:
#                     list_get_org_intrsc_1.append(i)
#           list_intrscn["list_get_org_intrsc_1"] = f"Lists_intersection{list_get_org_intrsc_1}"


#      import datetime
#      now = datetime.datetime.now().strftime("%d.""%m.""%Y ""%H:""%M")
#      print(now)
#      list_intrscn["now"] = now     

          


#      return render(request, "list_intersection.html" ,list_intrscn)

# # ele elemek olar ki 2 funksiya bir html faylda islesin ???????????????


# def python_prog_re_pos_neg(request):
     
#      pos_neg_dict = {
#           "title": "Python",
#           "heading": "Python program to rearrange positive and negative numbers in a given array"


#      }

#      string_1 = request.GET.get("list_from_site")
#      if string_1:
#           list_get = string_1.split(",")
#           # print(list_get)
#           list_get_int = list(map(lambda x: int(x), list_get))
#           # print(list_get_int)
#           list_get_int_pos = list(filter(lambda x: x>0, list_get_int))
#           list_get_int_pos.sort()
#           # print(list_get_int_pos)
#           list_get_int_neg = list(filter(lambda x: x<0, list_get_int))
#           list_get_int_neg.sort()
#           # print(list_get_int_neg)
#           list_get_result = list_get_int_pos + list_get_int_neg
#           # print(list_get_result)
#           pos_neg_dict["list_get_result"] = f"Rearrange list {list_get_result}"



#      if request.method == "POST":
#           string_2 = request.POST.get("list_1_from_site")
#           list_get_2 = string_2.split(",")
#           list_get_2_pos = []
#           list_get_2_neg = [] 
#           for i in list_get_2:
#                if int(i) > 0:
#                     list_get_2_pos.append(int(i))
#                else:
#                     list_get_2_neg.append(int(i))
#           list_get_2_pos.sort()
#           list_get_2_neg.sort()          
#           print(list_get_2_pos)
#           print(list_get_2_neg)
#           list_get_result_2 = list_get_2_pos + list_get_2_neg
#           print(list_get_result_2)

#           pos_neg_dict["list_get_result_2"] = f"Rearrange list {list_get_result_2}"

#      import datetime
#      now = datetime.datetime.now()
#      pos_neg_dict["now"] = now

#      return render(request, 'python_prog.html', pos_neg_dict) 




# def movie_time(requset):

#      film_dict = {
#           "Title":"Movies",
#           "Film": 'Film: "Mind Man"',
#           "Director": 'Director: "Idrak"',
#           "Rating": f'Rating: {4.9}',
#           "About": 'About:" Is it important to have a lot of intelligence or to use it properly?"',
#      }

#      import datetime
#      day_sequence_get = requset.GET.get("day sequence")
#      if day_sequence_get:
#           list_dates = []
#           time_1 = 0
#           for i in range(int(day_sequence_get)):
#                print(time_1) 
#                list_dates.append((((datetime.date.today() + datetime.timedelta(i)).strftime("Date: %d." "%m." "%Y"))
#                + "  " + (datetime.datetime(year=1, month=1, day=1,hour=15, minute=45)+
#                datetime.timedelta(minutes=time_1)).strftime(" Time: %H:" "%M")))
#                time_1 += 60
          
#           film_dict["date"] = list_dates
#           print(film_dict["date"])
          
#      return render(requset, 'movie_time.html', film_dict) 





     # films = FilmModel.objects.all()
     # my_film = films.get(name="The Truman Show")
     # my_film_actors_ = my_film.actors.all()
     # print(my_film_actors_)
     # for my_actor in my_film_actors_:
     #      print (my_actor)

     # actors = ActorModel.objects.all()
     # my_film_actors = actors.filter(films__name ="The Truman Show")
     # print(my_film_actors)


     # myactors1 = ActorModel.objects.filter(films__name ="Catch Me If You Can" )
     # print(myactors1)

     # myfilm = FilmModel.objects.get(name = "Catch Me If You Can")
     # rating = myfilm.rating
     # print(rating)
     # context["myfilm"] = myfilm
     # myfilmactors = myfilm.actors.all()
     # context["myfilmactors"] = myfilmactors
     
     # x = films.get(name="Catch Me If You Can").actors.get(name= "Jim").films.all().get(name = "Catch Me If You Can")
     # print(x)
     # myactor_ex = myfilm.actors.all().get(name = "Jim")
     # myactor_ex = myfilm.actors.get(name = "Jim")
     # myactor_ex = myfilmactors.get(name = "Jim")
     # print(myactor_ex)
     # context[myactor_ex] = myactor_ex
     # myactorfilms_ex = myactor_ex.films.all()
     # context["myactorfilms_ex"] = myactorfilms_ex


     
     
     # myactor = ActorModel.objects.get(surname= "Carrey")
     # context["myactor"] = myactor
     # myactorfilms = myactor.films.all()
     # context["myactorfilms"] = myactorfilms


     
     # rating = {}
     # for film in films:
     #      rating[film.name] = film.rating
     
     # print(rating)
     # min =100
     # for key, value in rating.items():
     #      if value < min:
     #           min = value
     #           min_key = key
     # print(min_key, min)

     # rating = []
     # for film in films:
     #      rating.append(film.rating)

     # print(rating)

     # mid_rating = sum(rating) / len(rating)
     # print(mid_rating)

     # context["mid_rating"] = mid_rating 


     # min_rating = rating[0]
     # for film in films:
     #      if film.rating < min_rating:
     #           min_rating = film.rating
     # print(min_rating)

     # for film in films:
     #      if film.rating == min_rating:
     #           film_min_rating = film          
     # print(film_min_rating)  