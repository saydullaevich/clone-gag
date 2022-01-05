from main.models import Category, PostComment


def categories(request):
    return {
        'categories': Category.objects.all()
    }

def comments(request):
    return {
        'comments': PostComment.objects.all()
    }