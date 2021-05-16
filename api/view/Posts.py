from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

from posts.models import Posts


# Create your views here.


# def post_write(request):
#     if request.method == 'POST':
#         if request.POST['mainphoto']:
#             pass
#         else:
#             new_article = Posts.objects.create(
#                 title=request.POST['postname'],
#                 contents=request.POST['contents'],
#                 author=request.POST['author'],
#                 rating=request.POST['rating'],
#                 place_id=request.POST['place_id']
#             )
#
#     return Response({
#         "status": 200,
#     })
@csrf_exempt
def new(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        pub_date = request.POST.get('pub_date')
        author = request.POST.get('author')
        rating = request.POST.get('rating')
        place_id = request.POST.get('place_id')

        post = Posts(title=title, content=content, pub_date=pub_date, author=author, rating=rating, place_id=place_id)
        post.save()

        return Response({
            "status": 200,
        })

