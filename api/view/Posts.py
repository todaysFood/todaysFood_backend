from rest_framework.response import Response

from posts.models import Posts


# Create your views here.
def post_write(request):
    if request.method == 'POST':
        if request.POST['mainphoto']:
            pass
        else:
            new_article = Posts.objects.create(
                title=request.POST['postname'],
                contents=request.POST['contents'],
                author=request.POST['author'],
                rating=request.POST['rating'],
                place_id=request.POST['place_id']
            )

    return Response({
        "status": 200,
    })