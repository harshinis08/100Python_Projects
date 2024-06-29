from django.shortcuts import render
import json, requests


# Create your views here.
def home(request):


    if request.method == "POST":
        zipcode = request.POST['zipcode']
        api_url = f"https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={zipcode}" \
                  "&distance=25&API_KEY=F92858B8-9ADA-4235-A926-54FB7A5C8873"
        api_request = requests.get(api_url)

        try:
            api_result = json.loads(api_request.content)
        except Exception as e:
            api_result = "Error ....."

        category_name = api_result[0]['Category']['Name']

        if category_name == "Good":
            category_description = "(0 - 50) Air quality is satisfactory, and air pollution poses little or no risk."
            category_color = "good"
        elif category_name == "Moderate":
            category_description = "(51 - 100) Air quality is acceptable.However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
            category_color = "moderate"
        elif category_name == 'Unhealthy for Sensitive Groups':
            category_description = "(101 - 150) Members of sensitive groups may experience health effects.The general public is less likely to be affected."
            category_color = "usg"
        elif category_name == 'Unhealthy':
            category_description = "(151 - 200) Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
            category_color = "unhealthy"
        elif category_name == 'Very Unhealthy':
            category_description = "(201 - 250) Health alert: The risk of health effects is increased for everyone."
            category_color = "veryUnhealthy"
        elif category_name == 'Hazardous':
            category_description = "(251 - 300) Health warning of emergency conditions: everyone is more likely to be affected."
            category_color = "hazardous"

        return render(request, 'home.html', {'api': api_result, 'category_description': category_description,
                                             'category_color': category_color})

    else:

        api_url = "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=78665" \
                  "&distance=25&API_KEY=F92858B8-9ADA-4235-A926-54FB7A5C8873"
        api_request = requests.get(api_url)

        try:
            api_result = json.loads(api_request.content)
        except Exception as e:
            api_result = "Error ....."

        category_name = api_result[0]['Category']['Name']

        if category_name == "Good":
            category_description = "(0 - 50) Air quality is satisfactory, and air pollution poses little or no risk."
            category_color = "good"
        elif category_name == "Moderate":
            category_description = "(51 - 100) Air quality is acceptable.However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
            category_color = "moderate"
        elif category_name == 'Unhealthy for Sensitive Groups':
            category_description = "(101 - 150) Members of sensitive groups may experience health effects.The general public is less likely to be affected."
            category_color = "usg"
        elif category_name == 'Unhealthy':
            category_description = "(151 - 200) Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
            category_color = "unhealthy"
        elif category_name == 'Very Unhealthy':
            category_description = "(201 - 250) Health alert: The risk of health effects is increased for everyone."
            category_color = "veryUnhealthy"
        elif category_name == 'Hazardous':
            category_description = "(251 - 300) Health warning of emergency conditions: everyone is more likely to be affected."
            category_color = "hazardous"

        return render(request, 'home.html', {'api': api_result, 'category_description': category_description, 'category_color':  category_color})
