# import json
#
# from django.http import HttpResponse
#
# from library.kakao import location_code_fetcher, kakao_local, weather_api
#
#
# def index(request):
#     return HttpResponse("Hello, world")
#
#
# def api(request):
#     if request.method == 'GET':
#         kakao = kakao_local.kakao_local()
#
#         x = request.GET.get('x')
#         y = request.GET.get('y')
#         radius = int(request.GET.get('radius'))
#
#         grid_x, grid_y = location_code_fetcher.mapToGrid(float(y), float(x))
#         weather = weather_api.today_weather(grid_x, grid_y)
#
#         res = []
#         for q in weather_api.query.get(weather, "맑음"):
#             res.extend(kakao.search_keyword(q, x=x, y=y, radius=radius, size=2)['documents'])
#
#         res = sorted(res, key=lambda x: int(x['distance']))
#
#         response = json.dumps(res, ensure_ascii=False)
#         return HttpResponse(response, content_type='application/json; charset=utf-8')
#         # return HttpResponse(x)
