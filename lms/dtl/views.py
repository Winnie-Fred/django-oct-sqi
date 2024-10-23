from django.shortcuts import render

# Create your views here.
def example_dtl(request):
    context = {
        "name": "Bolu",
        "position": "instructor",
        "languages": ["Java", "C++", "Python", "Ruby", "JavaScript", "FORTRAN", "Assembly"] 
    }

    return render(request, "dtl/dtl.html", context)

def test_dtl(request):
    context = {
        "food": "rice",
        "ingredients": ["tomatoes", "pepper", "onions", "maggi", "salt", "groundnut oil"],
        "is_favorite": False,
        "time_to_cook_in_mins": 30,
        "products": {"tomatoes": 300, "pepper": 500, "maggi": 4, "salt": 900, "groundnut oil": 10}
    }
    return render(request, "dtl/test-dtl.html", context)

# food => rice
# ingredients => tomatoes, pepper, onions, maggi, salt, groundnut oil
# is_favorite => False
# time_to_cook_in_mins => 30

# in a html template called test-dtl.html: 
# h1 => Show the name of the food
# using ul and li, display the list of ingredients
# if it is_favourite, show "Rice is my favorite food", else show "Rice is not my favorite food"
# p => It takes 30 minutes to cook rice