from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.cache import cache
import requests


CACHE_TTL = getattr(settings , 'CACHE_TTL' , DEFAULT_TIMEOUT)

@api_view(['GET'])
def getFixtures(request):
    api_url = "https://v3.football.api-sports.io/fixtures"  # Replace this with the actual API URL

    try:
        # Get user-defined query parameters from the request
        params = request.GET

        # Append user-defined parameters to the API URL
        api_url += "?" + "&".join([f"{key}={value}" for key, value in params.items()])

        # Try to get data from cache first
        cached_data = cache.get(api_url)
        if cached_data:
            return Response(cached_data)

        # Define custom headers
        headers = {
            'x-rapidapi-key': '87e65c940821f0c5c7c6af99224cfc4d',
            'x-rapidapi-host': 'v3.football.api-sports.io'
        }

        # Make a GET request to the external API with custom headers
        response = requests.get(api_url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Get the JSON data from the response
            data_from_api = response.json()

            # Store data in cache
            cache.set(api_url, data_from_api, timeout=settings.CACHE_TTL)

            # Return the fetched data as the API response
            return Response(data_from_api)
        else:
            # If the request was not successful, return an error response
            return Response({"message": "Failed to fetch data from the API"}, status=response.status_code)

    except requests.RequestException as e:
        # Handle exceptions (e.g., connection error, timeout)
        return Response({"message": f"Request error: {str(e)}"}, status=500)  # Return a server error status

@api_view(['GET'])
def getLeague(request):
    api_url = "https://v3.football.api-sports.io/leagues"

    try:
        # Get user-defined query parameters from the request
        params = request.GET

        # Append user-defined parameters to the API URL
        api_url += "?" + "&".join([f"{key}={value}" for key, value in params.items()])

        # Try to get data from cache first
        cached_data = cache.get(api_url)
        if cached_data:
            return Response(cached_data)

        # Define custom headers
        headers = {
            'x-rapidapi-key': '87e65c940821f0c5c7c6af99224cfc4d',
            'x-rapidapi-host': 'v3.football.api-sports.io'
        }

        # Make a GET request to the external API with custom headers
        response = requests.get(api_url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Get the JSON data from the response
            data_from_api = response.json()

            # Return the fetched data as the API response
            return Response(data_from_api)
        else:

            # If the request was not successful, return an error response
            return Response({"message": "Failed to fetch data from the API"}, status=response.status_code)

    except requests.RequestException as e:
        # Handle exceptions (e.g., connection error, timeout)
        return Response({"message": f"Request error: {str(e)}"}, status=500)

@api_view(['GET'])
def getStandings(request):
    api_url = "https://v3.football.api-sports.io/leagues/standings"

    try:
        # Get user-defined query parameters from the request
        params = request.GET

        # Append user-defined parameters to the API URL
        api_url += "?" + "&".join([f"{key}={value}" for key, value in params.items()])

        # Try to get data from cache first
        cached_data = cache.get(api_url)
        if cached_data:
            return Response(cached_data)

        # Define custom headers
        headers = {
            'x-rapidapi-key': '87e65c940821f0c5c7c6af99224cfc4d',
            'x-rapidapi-host': 'v3.football.api-sports.io'
        }

        # Make a GET request to the external API with custom headers
        response = requests.get(api_url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Get the JSON data from the response
            data_from_api = response.json()

            # Return the fetched data as the API response
            return Response(data_from_api)
        else:

            # If the request was not successful, return an error response
            return Response({"message": "Failed to fetch data from the API"}, status=response.status_code)

    except requests.RequestException as e:
        # Handle exceptions (e.g., connection error, timeout)
        return Response({"message": f"Request error: {str(e)}"}, status=500)

@api_view(['GET'])
def getTeams(request):
    api_url = "https://v3.football.api-sports.io/teams"
    
    try:
        # Get user-defined query parameters from the request
        params = request.GET

        # Append user-defined parameters to the API URL
        api_url += "?" + "&".join([f"{key}={value}" for key, value in params.items()])

        # Try to get data from cache first
        cached_data = cache.get(api_url)
        if cached_data:
            return Response(cached_data)

        # Define custom headers
        headers = {
            'x-rapidapi-key': '87e65c940821f0c5c7c6af99224cfc4d',
            'x-rapidapi-host': 'v3.football.api-sports.io'
        }

        # Make a GET request to the external API with custom headers
        response = requests.get(api_url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Get the JSON data from the response
            data_from_api = response.json()

            # Return the fetched data as the API response
            return Response(data_from_api)
        else:

            # If the request was not successful, return an error response
            return Response({"message": "Failed to fetch data from the API"}, status=response.status_code)

    except requests.RequestException as e:
        # Handle exceptions (e.g., connection error, timeout)
        return Response({"message": f"Request error: {str(e)}"}, status=500)

@api_view(['GET'])
def getFixturesStatistics(request):
    api_url = "https://v3.football.api-sports.io/fixtures/statistics"
    
    try:
        # Get user-defined query parameters from the request
        params = request.GET

        # Append user-defined parameters to the API URL
        api_url += "?" + "&".join([f"{key}={value}" for key, value in params.items()])

        # Define custom headers
        headers = {
            'x-rapidapi-key': '87e65c940821f0c5c7c6af99224cfc4d',
            'x-rapidapi-host': 'v3.football.api-sports.io'
        }

        # Make a GET request to the external API with custom headers
        response = requests.get(api_url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Get the JSON data from the response
            data_from_api = response.json()

            # Return the fetched data as the API response
            return Response(data_from_api)
        else:

            # If the request was not successful, return an error response
            return Response({"message": "Failed to fetch data from the API"}, status=response.status_code)

    except requests.RequestException as e:
        # Handle exceptions (e.g., connection error, timeout)
        return Response({"message": f"Request error: {str(e)}"}, status=500)

@api_view(['GET'])
def getFixturesEvents(request):
    api_url = "https://v3.football.api-sports.io/fixtures/events"

    try:
        # Get user-defined query parameters from the request
        params = request.GET

        # Append user-defined parameters to the API URL
        api_url += "?" + "&".join([f"{key}={value}" for key, value in params.items()])

        # Define custom headers
        headers = {
            'x-rapidapi-key': '87e65c940821f0c5c7c6af99224cfc4d',
            'x-rapidapi-host': 'v3.football.api-sports.io'
        }

        # Make a GET request to the external API with custom headers
        response = requests.get(api_url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Get the JSON data from the response
            data_from_api = response.json()

            # Return the fetched data as the API response
            return Response(data_from_api)
        else:

            # If the request was not successful, return an error response
            return Response({"message": "Failed to fetch data from the API"}, status=response.status_code)

    except requests.RequestException as e:
        # Handle exceptions (e.g., connection error, timeout)
        return Response({"message": f"Request error: {str(e)}"}, status=500)

@api_view(['GET'])
def getHeadToHead(request):
    api_url = "https://v3.football.api-sports.io/fixtures/headtohead"
    try:
        # Get user-defined query parameters from the request
        params = request.GET

        # Append user-defined parameters to the API URL
        api_url += "?" + "&".join([f"{key}={value}" for key, value in params.items()])
        
        # Define custom headers
        headers = {
            'x-rapidapi-key': '87e65c940821f0c5c7c6af99224cfc4d',
            'x-rapidapi-host': 'v3.football.api-sports.io'
        }

        # Make a GET request to the external API with custom headers
        response = requests.get(api_url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Get the JSON data from the response
            data_from_api = response.json()

            # Return the fetched data as the API response
            return Response(data_from_api)
        else:
            # If the request was not successful, return an error response
            return Response({"message": "Failed to fetch data from the API"}, status=response.status_code)

    except requests.RequestException as e:
        # Handle exceptions (e.g., connection error, timeout)
        return Response({"message": f"Request error: {str(e)}"}, status=500)  # Return a server error status

@api_view(['GET'])
def getLineup(request):
    api_url = "https://v3.football.api-sports.io/fixtures/lineups"
    try:
        # Get user-defined query parameters from the request
        params = request.GET

        # Append user-defined parameters to the API URL
        api_url += "?" + "&".join([f"{key}={value}" for key, value in params.items()])
        
        # Define custom headers
        headers = {
            'x-rapidapi-key': '87e65c940821f0c5c7c6af99224cfc4d',
            'x-rapidapi-host': 'v3.football.api-sports.io'
        }

        # Make a GET request to the external API with custom headers
        response = requests.get(api_url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Get the JSON data from the response
            data_from_api = response.json()

            # Return the fetched data as the API response
            return Response(data_from_api)
        else:
            # If the request was not successful, return an error response
            return Response({"message": "Failed to fetch data from the API"}, status=response.status_code)

    except requests.RequestException as e:
        # Handle exceptions (e.g., connection error, timeout)
        return Response({"message": f"Request error: {str(e)}"}, status=500)  # Return a server error status

@api_view(['GET'])
def getPredictions(request):
    api_url = "https://v3.football.api-sports.io/predictions"
    try:
        # Get user-defined query parameters from the request
        params = request.GET

        # Append user-defined parameters to the API URL
        api_url += "?" + "&".join([f"{key}={value}" for key, value in params.items()])
        
        # Define custom headers
        headers = {
            'x-rapidapi-key': '87e65c940821f0c5c7c6af99224cfc4d',
            'x-rapidapi-host': 'v3.football.api-sports.io'
        }

        # Make a GET request to the external API with custom headers
        response = requests.get(api_url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Get the JSON data from the response
            data_from_api = response.json()

            # Return the fetched data as the API response
            return Response(data_from_api)
        else:
            # If the request was not successful, return an error response
            return Response({"message": "Failed to fetch data from the API"}, status=response.status_code)

    except requests.RequestException as e:
        # Handle exceptions (e.g., connection error, timeout)
        return Response({"message": f"Request error: {str(e)}"}, status=500)  # Return a server error status

@api_view(['GET'])
def dailyQuiz(request):
    if request.method == 'GET':
        # Get the current day of the week (Monday=0, Sunday=6)
        current_day = datetime.now().weekday()
        
        # Calculate the day index starting from Monday=1
        day_index = (current_day + 1) % 7

        # List of questions
        data = [{
            "backgroundImage": "https://staticg.sportskeeda.com/editor/2019/01/0b7b6-15487684614586-800.jpg",
            "question": "When did Messi first debut in Barcelona?",
            "answer": "2004",
            "option1": "2002",
            "option2": "2004",
            "option3": "2003",
            "option4": "2005"
        },
        {
           "backgroundImage": "https://www.theweek.in/content/dam/week/news/sports/images/2018/5/20/fifa-world-cup-trophy-ball.jpg.transform/schema-4x3/image.jpg",
            "question": "Who won the FIFA World Cup in 2018?",
            "answer": "France",
            "option1": "Brazil",
            "option2": "France",
            "option3": "Germany",
            "option4": "Argentina" 
        }, 
        {
            "backgroundImage": "https://pbs.twimg.com/media/EK0jKDNX0AAJEZX.jpg",
            "question": "Which player has won the most Ballon d'Or awards?",
            "answer": "Lionel Messi",
            "option1": "Cristiano Ronaldo",
            "option2": "Michel Platini",
            "option3": "Diego Maradona",
            "option4": "Lionel Messi"
        },
        {
            "backgroundImage": "https://ss-i.thgim.com/public/football/champions-league/article38497462.ece/alternates/LANDSCAPE_1200/Champions-League-trophy",
            "question": "Which team has won the UEFA Champions League the most times?",
            "answer": "Real Madrid",
            "option1": "FC Barcelona",
            "option2": "Real Madrid",
            "option3": "Bayern Munich",
            "option4": "Liverpool"
        },
        {
            "backgroundImage": "https://cdnuploads.aa.com.tr/uploads/Contents/2023/01/13/thumbs_b_c_7982afecfc0cefec23851b81850809c9.jpg?v=165134",
            "question": "Who is the top scorer in the history of the English Premier League?",
            "answer": "Alan Shearer",
            "option1": "Wayne Rooney",
            "option2": "Alan Shearer",
            "option3": "Thierry Henry",
            "option4": "Frank Lampard"
        },
        {
            "backgroundImage": "https://phantom-marca.unidadeditorial.es/583193fbd8375b7d6eade997aaf30d7e/resize/828/f/jpg/assets/multimedia/imagenes/2023/06/21/16873090268501.jpg",
            "question": "Which country has won the most Copa America titles?",
            "answer": "Brazil",
            "option1": "Argentina",
            "option2": "Chile",
            "option3": "Brazil",
            "option4": "Uruguay"
        },
        {
            "backgroundImage": "https://imgs.search.brave.com/Fj7iwEVf1kaflUKk1F20rKfYnN_wLs_8I5oaYRqmqcE/rs:fit:860:0:0/g:ce/aHR0cHM6Ly93d3cu/YWxqYXplZXJhLmNv/bS93cC1jb250ZW50/L3VwbG9hZHMvMjAy/NC8wMS9HZXR0eUlt/YWdlcy04OTM3NDUz/MTItMTcwNDczOTA1/Mi5qcGc_cmVzaXpl/PTc3MCw1MTMmcXVh/bGl0eT04MA",
            "question": "Who is the only player to have won the FIFA World Cup as both a player and a manager?",
            "answer": "Franz Beckenbauer",
            "option1": "Diego Maradona",
            "option2": "Zinedine Zidane",
            "option3": "Franz Beckenbauer",
            "option4": "Johan Cruyff"
        }
        ]
        
        # Return data based on the day index
        if 1 <= day_index <= len(data):
            return Response(data[day_index - 1], status=200)
        else:
            return Response({"message": "No quiz available for today"}, status=404)
