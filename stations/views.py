from django.shortcuts import render, HttpResponse
from .models import Station

# Create your views here.

def home(request):
    return render(request, "home.html")

def stations(request):
    stations = Station.objects.all()
    return render(request, "stations.html", {"stations": stations})


# def home(request):
#     stations = Station.objects.all()
#     text = f"""
#         Station Table - {len(stations)}
#         <table border="1">
#             <thead>
#                 <tr>
#                     <th>Title</th>
#                     <th>Subtitle</th>
#                     <th>Coordinate</th>
#                     <th>Description</th>
#                     <th>Display Type</th>
#                     <th>Extent</th>
#                     <th>Footer</th>
#                     <th>Future</th>
#                     <th>Icon</th>
#                     <th>Is Blocked</th>
#                     <th>Lorry Parking Feature Icons</th>
#                     <th>Point</th>
#                     <th>Route Recommendation</th>
#                 </tr>
#             </thead>
#             <tbody>
#     """

#     # Loop through stations to generate table rows
#     for station in stations:
#         text += f"""
#             <tr>
#                 <td>{station.title}</td>
#                 <td>{station.subtitle}</td>
#                 <td>{f"{station.latitude} | {station.longitude}"}</td>
#                 <td>{station.description}</td>
#                 <td>{station.display_type}</td>
#                 <td>{station.extent}</td>
#                 <td>{station.footer}</td>
#                 <td>{station.future}</td>
#                 <td>{station.icon}</td>
#                 <td>{station.isBlocked}</td>
#                 <td>{station.lorryParkingFeatureIcons}</td>
#                 <td>{station.point}</td>
#                 <td>{station.routeRecommendation}</td>
#             </tr>
#         """

#     # Closing the table HTML tag
#     text += """
#             </tbody>
#         </table>
#     """


#     return HttpResponse(text)