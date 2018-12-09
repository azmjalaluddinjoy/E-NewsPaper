from django.shortcuts import render

# Create your views here.


def show_user_info(request):
    """
    A django view to show user's Information
    """
    return render(request, 'user_info/user_info.html')