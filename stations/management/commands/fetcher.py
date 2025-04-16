import requests

from tqdm import tqdm
from stations.models import Station
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Fetches loading stations data."

    def handle(self, *args, **options):
        Station.objects.all().delete()

        data = self.fetch_api("/")
        roads = data["roads"]
        for road in tqdm(roads, desc="Fetching Progress"):
            data = self.fetch_api(f"/{road}/services/electric_charging_station")
            stations = data["electric_charging_station"]
            for station in stations:
                station_id = station["identifier"]
                detail_data = self.fetch_api(f"/details/electric_charging_station/{station_id}")
                if (descr := detail_data.get("description")) is not None:
                    descr = " ".join(descr[1:])
                if (coor := detail_data.get("coordinate")) is not None:
                    lat = coor["lat"]
                    long = coor["long"]
                else:
                    lat, long = None, None
                title = detail_data.get("title").split("|")

                Station.objects.create(
                    road=road,
                    area=f"{title[1].strip()} -> {title[2].strip()}" if title is not None and len(title) == 3 else None,
                    subtitle=detail_data.get("subtitle"),
                    latitude=lat,
                    longitude=long,
                    description=descr,
                    display_type=detail_data.get("display_type"),
                    extent=detail_data.get("extent"),
                    footer=detail_data.get("footer"),
                    future=detail_data.get("future"),
                    icon=detail_data.get("icon"),
                    isBlocked=detail_data.get("isBlocked"),
                    lorryParkingFeatureIcons=detail_data.get("lorryParkingFeatureIcons"),
                    point=detail_data.get("point"),
                    routeRecommendation=detail_data.get("routeRecommendation"),
                )
        
        self.stdout.write(self.style.SUCCESS("Stations fetched and saved successfully."))

    def fetch_api(self, endpoint):
        try:
            response = requests.get(f"https://verkehr.autobahn.de/o/autobahn{endpoint}")
            return response.json()
        
        except Exception as e:
            print(f"Fetching Error: {e}")