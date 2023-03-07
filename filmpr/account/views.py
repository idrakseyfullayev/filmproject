from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from account.models import Account
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from film.models import ViewNumberModel, LikeModel, CommentModel, FilmModel


def has_num_alpha_symbol(t):
    num = "0123456789"
    alpha = "abcdefghijklmnopqrstuvwxyz"
    symbol = "~!@#$%^&*()_+:|\\/?><.,"
    x = False
    y = False
    z = False
    for i in t:   
        if i in num:
            x = True 
        if i in alpha:
            y = True 
        if i in symbol:
            z = True
        if x and y and z:
                break
    if x and y and z:        
        return True
    else:
        return False


class RegisterView(generic.View):
    def get(self, request, *args, **kwargs):
        return render(request, 'register.html') # get metodda bi defe render yazmdimsa post metodda redirect istifade ede bileremde?
    
    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")
        # username = username.capitalize()
        # print(username)

        
        if username and password:
            # if Account.objects.filter(user__username = username):
            if User.objects.filter(username = username):    
                messages.info(request, "Please, enter another username")
            # elif not has_num_alpha_symbol(password):
                # messages.info(request, "password must consist of letters and numbers")
            elif password.isdigit():
                messages.info(request, "password must consist of letters and numbers")  
            else:
                user = User.objects.create_user(username = username, password = password)
                print(type(user))

                Account.objects.create(user = user)
                print(type(user))
                messages.success(request, "User created")

                login(request, user)
                messages.success(request, "%s login in." % (user.username))
                return redirect("film:index")
                
                
        print(3)        
        print(username)
        print(5)      
        # if username is "":
        if not username:
            messages.info(request, "Please, enter username")
        if not password:
            messages.info(request, "Please, enter password")

        return redirect("account:register")    

            
    
            

        
            
        

# def register(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")

        
#         if username and password:
#             if Account.objects.filter(user__username = username):
#                 messages.info(request, "Please, enter another username")
#             # elif not has_num_alpha_symbol(password):
#             #     messages.info(request, "password must consist of letters and numbers")
#             elif password.isdigit():
#                 messages.info(request, "password must consist of letters and numbers")  
#             else:
#                 user = User.objects.create_user(username = username,password = password,)

#                 Account.objects.create(user = user,)
#                 messages.success(request, "User created")
#         print(3)        
#         print(username)
#         print(5)      
#         # if username is "":
#         if not username:
#             messages.info(request, "Please, enter username")
#         if not password:
#             messages.info(request, "Please, enter password")


                  

#         # return redirect('film:index')

#     return render(request, 'register.html')



class LoginUserView(generic.View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')
    
    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(username = username, password = password)
        print(user)
        if user is None:
            messages.info(request, "User was not found")
            return redirect("account:login")

        else:
            login(request, user)
            # return redirect("film:index")
            messages.success(request, "%s login in." % (user.username))
            return redirect("film:index")    

       


class LogoutUserView(generic.View):
    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request,"Logging out")
        return redirect("film:index")
    

class LoginPageView(generic.View):
    def get(self, request, *args, **kwargs):
        # login_view_films = ViewNumberModel.objects.filter(user__username = request.user.username)
        # film_likes0 = LikeModel.objects.filter(user = request.user)
        # print(login_view_films)
        # print(film_likes0)
        # film_likes1 = FilmModel.objects.all()
        # list1 = []
        # for i in film_likes1:
        #     list1.append(i.film_likes.all().filter(user=request.user))
        # print(list1)    


        # context = {
            # "login_view_films": login_view_films,
            # "film_likes": film_likes0

        # }

        # user = User.objects.get(username=request.user.username)

        user_likes = request.user.user_likes.all()
        # print(request.user.user_likes.all())
        # list1 = []
        # for i in user_likes:
        #     x = i.strip("|")
        #     list1.append(i)
        # print(list1)    


        context = {
            "user_likes": user_likes,
        }
        



        return render(request, "loginpage.html", context)    



# def loginUser(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
        
#         user = authenticate(username = username, password = password)
#         print(user)
#         if user is None:
#             messages.info(request, "User was not found")

#         else:
#             login(request, user)
#             # return redirect("film:index")
#             messages.success(request, "%s login in." % (user.username))    

#     return render(request, 'login.html')
