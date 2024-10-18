from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "library/home.html")

# Create a view called all_authors in the authors app's views.py.
# It should return a rendered html page called 'all-authors.html'.
# Put that html file in a folder called authors


# 1. Create a folder called music_store
# 2. Create a django project config inside - django-admin startproject config .
# 3. Create an app called music
# 4. Create a view called favorites
# 5. Create a urls.py file in the music app
# 6. Add the url to link to the favorites view 
# 7. Include the url in the general project's config.urls
# 8. Start the development server and go to the view in the browser.