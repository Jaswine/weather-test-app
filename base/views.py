from django.shortcuts import render

from base.services import get_data_from_api, create_or_update_city
from urllib.parse import quote, unquote


def main(request):
    """
        Главная страница
    """
    last_city = request.COOKIES.get('last_city')
    weather_data = None

    if last_city:
        last_city = unquote(last_city)

    if request.method == 'POST':
        last_city = request.POST.get('city')

        create_or_update_city(last_city)
        weather_data = get_data_from_api(last_city)

        response = render(request, 'main.html', {
            'last_city': last_city,
            'data': weather_data
        })
        response.set_cookie('last_city', quote(last_city))
        return response

    return render(request, 'main.html', {
        'last_city': last_city,
        'data': weather_data
    })
