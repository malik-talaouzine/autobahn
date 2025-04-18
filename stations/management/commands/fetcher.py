import requests

from tqdm import tqdm
from stations.models import Station, ParkingLorry
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Fetches loading stations data."

    def handle(self, *args, **options):
        Station.objects.all().delete()
        ParkingLorry.objects.all().delete()

        data = self.fetch_api("/")
        roads = data["roads"]
        for road in tqdm(roads, desc="Fetching Progress"):
            self.fetch_stations(road)
            self.fetch_lorries(road)
        self.stdout.write(self.style.SUCCESS("Fetched and saved successfully."))

    def fetch_api(self, endpoint):
        try:
            response = requests.get(f"https://verkehr.autobahn.de/o/autobahn{endpoint}")
            return response.json()
        
        except Exception as e:
            print(f"Fetching Error: {e}")

    def fetch_stations(self, road):
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
                is_blocked=detail_data.get("isBlocked"),
                lorry_parking_feature_icons=detail_data.get("lorryParkingFeatureIcons"),
                point=detail_data.get("point"),
                route_recommendation=detail_data.get("routeRecommendation"),
            )

    def fetch_lorries(self, road):
        data = self.fetch_api(f"/{road}/services/parking_lorry")
        lorries = data["parking_lorry"]

        for lorry in lorries:
            lorry_id = lorry["identifier"]
            
            # Fetch detailed data for each lorry
            detail_data = self.fetch_api(f"/details/parking_lorry/{lorry_id}")
            
            # Process description field if it exists
            if (descr := detail_data.get("description")) is not None:
                car, lorry = descr

            # Process coordinates if they exist
            if (coor := detail_data.get("coordinate")) is not None:
                lat = coor["lat"]
                long = coor["long"]
            else:
                lat, long = None, None
            
            title = detail_data.get("title").split("|")
            
            # Create or update ParkingLorry instance
            ParkingLorry.objects.create(
                road=road,
                area=title[1].strip(),
                car_parking_spaces=car,
                lorry_parking_spaces=lorry,
                icon=detail_data.get("icon"),
                is_blocked=detail_data.get("isBlocked"),
                future=detail_data.get("future"),
                start_lc_position=detail_data.get("startLcPosition"),
                display_type=detail_data.get("display_type"),
                subtitle=detail_data.get("subtitle"),
                latitude=lat,
                longitude=long,
                description=descr,
                route_recommendation=detail_data.get("routeRecommendation"),
                footer=detail_data.get("footer"),
                lorry_parking_feature_icons=detail_data.get("lorryParkingFeatureIcons"),
            )