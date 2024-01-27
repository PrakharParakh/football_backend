from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests

@api_view(['GET'])
def getFixtures(request):
    api_url = "https://v3.football.api-sports.io/fixtures"  # Replace this with the actual API URL

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
def getLeague(request):
    api_url = "https://v3.football.api-sports.io/leagues"

    try:
        # Get user-defined query parameters from the request
        params = request.GET

        # Append user-defined parameters to the API URL
        api_url += "?" + "&".join([f"{key}={value}" for key, value in params.items()])

        headers = {
            'x-rapidapi-key': '87e65c940821f0c5c7c6af99224cfc4d',
            'x-rapidapi-host': 'v3.football.api-sports.io'
        }

        response = requests.get(api_url, headers=headers)

        if response.status_code == 200:
            data_from_api = response.json()

            return Response(data_from_api)
        else:

            return Response({"message": "Failed to fetch data from the API"}, status=500)

    except requests.RequestException as e:
        return Response({"message": f"Request error: {str(e)}"}, status=500)

@api_view(['GET'])
def getStandings(request):
    api_url = "https://v3.football.api-sports.io/leagues/standings"

    try:
        # Get user-defined query parameters from the request
        params = request.GET

        # Append user-defined parameters to the API URL
        api_url += "?" + "&".join([f"{key}={value}" for key, value in params.items()])

        headers = {
            'x-rapidapi-key': '87e65c940821f0c5c7c6af99224cfc4d',
            'x-rapidapi-host': 'v3.football.api-sports.io'
        }

        response = requests.get(api_url, headers=headers)

        if response.status_code == 200:
            data_from_api = response.json()

            return Response(data_from_api)
        else:

            return Response({"message": "Failed to fetch data from the API"}, status=500)

    except requests.RequestException as e:
        return Response({"message": f"Request error: {str(e)}"}, status=500)

@api_view(['GET'])
def getTeams(request):
    api_url = "https://v3.football.api-sports.io/teams"

    try:
        # Get user-defined query parameters from the request
        params = request.GET

        # Append user-defined parameters to the API URL
        api_url += "?" + "&".join([f"{key}={value}" for key, value in params.items()])

        headers = {
            'x-rapidapi-key': '87e65c940821f0c5c7c6af99224cfc4d',
            'x-rapidapi-host': 'v3.football.api-sports.io'
        }

        response = requests.get(api_url, headers=headers)

        if response.status_code == 200:
            data_from_api = response.json()
            return Response(data_from_api)
        else:
            return Response({"message": "Failed to fetch data from the API"}, status=500)

    except requests.RequestException as e:
        return Response({"message": f"Request error: {str(e)}"}, status=500)

@api_view(['GET'])
def getFixturesStatistics(request):
    api_url = "https://v3.football.api-sports.io/fixtures/statistics"

    try:
        # Get user-defined query parameters from the request
        params = request.GET

        # Append user-defined parameters to the API URL
        api_url += "?" + "&".join([f"{key}={value}" for key, value in params.items()])

        headers = {
            'x-rapidapi-key': '87e65c940821f0c5c7c6af99224cfc4d',
            'x-rapidapi-host': 'v3.football.api-sports.io'
        }

        response = requests.get(api_url, headers=headers)

        if response.status_code == 200:
            data_from_api = response.json()
            return Response(data_from_api)
        else:
            return Response({"message": "Failed to fetch data from the API"}, status=500)

    except requests.RequestException as e:
        return Response({"message": f"Request error: {str(e)}"}, status=500)

@api_view(['GET'])
def getFixturesEvents(request):
    api_url = "https://v3.football.api-sports.io/fixtures/events"

    try:
        # Get user-defined query parameters from the request
        params = request.GET

        # Append user-defined parameters to the API URL
        api_url += "?" + "&".join([f"{key}={value}" for key, value in params.items()])

        headers = {
            'x-rapidapi-key': '87e65c940821f0c5c7c6af99224cfc4d',
            'x-rapidapi-host': 'v3.football.api-sports.io'
        }

        response = requests.get(api_url, headers=headers)

        if response.status_code == 200:
            data_from_api = response.json()
            return Response(data_from_api)
        else:
            return Response({"message": "Failed to fetch data from the API"}, status=500)

    except requests.RequestException as e:
        return Response({"message": f"Request error: {str(e)}"}, status=500)
    

    api_url = "https://v3.football.api-sports.io/fixtures/predictions"

    try:
        # Get user-defined query parameters from the request
        params = request.GET

        # Append user-defined parameters to the API URL
        api_url += "?" + "&".join([f"{key}={value}" for key, value in params.items()])

        headers = {
            'x-rapidapi-key': '87e65c940821f0c5c7c6af99224cfc4d',
            'x-rapidapi-host': 'v3.football.api-sports.io'
        }

        response = requests.get(api_url, headers=headers)

        if response.status_code == 200:
            data_from_api = response.json()
            return Response(data_from_api)
        else:
            return Response({"message": "Failed to fetch data from the API"}, status=500)

    except requests.RequestException as e:
        return Response({"message": f"Request error: {str(e)}"}, status=500)
