import requests

from tqdm import tqdm
from stations.models import Station, ParkingLorry, Closure, Warning, Roadwork
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Fetches loading stations data."

    def handle(self, *args, **options):
        Station.objects.all().delete()
        ParkingLorry.objects.all().delete()
        Closure.objects.all().delete()
        Warning.objects.all().delete()
        Roadwork.objects.all().delete()

        data_keys = {
            "roadworks": self.process_roadworks,
            "parking_lorry": self.process_lorries,
            "warning": self.process_warnings,
            "closure": self.process_closures,
            "electric_charging_station": self.process_stations,
        }

        data = self.fetch_api("/")
        roads = data["roads"]
        for road in tqdm(roads, desc="Fetching Progress"):
            for k, v in data_keys.items():
                self.get_data(road, k, v)
        self.stdout.write(self.style.SUCCESS("Fetched and saved successfully."))

    def fetch_api(self, endpoint):
        try:
            response = requests.get(f"https://verkehr.autobahn.de/o/autobahn{endpoint}")
            return response.json()
        
        except Exception as e:
            print(f"Fetching Error: {e}")

    def get_data(self, road, key, fetch_fn):
        data = self.fetch_api(f"/{road}/services/{key}")
        stations = data[key]
        for station in stations:
            station_id = station["identifier"]
            detail_data = self.fetch_api(f"/details/{key}/{station_id}")
            fetch_fn(road, detail_data)


    def process_stations(self, road, detail_data):
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

    def process_lorries(self, road, detail_data):
        if (descr := detail_data.get("description")) is not None:
            car, lorry = descr
        if (coor := detail_data.get("coordinate")) is not None:
            lat = coor["lat"]
            long = coor["long"]
        title = detail_data.get("title").split("|")
        
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

    def process_closures(self, road, detail_data):
        if (descr := detail_data.get("description")) is not None:
            descr = " ".join(descr)
        if (coor := detail_data.get("coordinate")) is not None:
            lat = coor["lat"]
            long = coor["long"]
        title = detail_data.get("title")[4:].strip()
        

        Closure.objects.create(
            road=road,
            isBlocked=detail_data.get("isBlocked"),
            future=detail_data.get("future"),
            startLcPosition=detail_data.get("startLcPosition"),
            impact=detail_data.get("impact"),
            display_type=detail_data.get("display_type"),
            subtitle=detail_data.get("subtitle"),
            title=title,
            startTimestamp=detail_data.get("startTimestamp"),
            latitude=lat,
            longitude=long,
            description=descr[:2000],
            routeRecommendation=detail_data.get("routeRecommendation"),
            footer=detail_data.get("footer"),
            lorryParkingFeatureIcons=detail_data.get("lorryParkingFeatureIcons"),
            geometry=detail_data.get("geometry")["coordinates"],
        )


    def process_warnings(self, road, detail_data):
        if (descr := detail_data.get("description")) is not None:
            descr = " ".join(descr)
        if (coor := detail_data.get("coordinate")) is not None:
            lat = coor["lat"]
            long = coor["long"]
        title = detail_data.get("title").split("|")
        

        Warning.objects.create(
            road=road,
            isBlocked=detail_data.get("isBlocked"),
            future=detail_data.get("future"),
            startLcPosition=detail_data.get("startLcPosition"),
            impact=detail_data.get("impact"),
            display_type=detail_data.get("display_type"),
            subtitle=detail_data.get("subtitle"),
            title=" - ".join(title[1:]),
            startTimestamp=detail_data.get("startTimestamp"),
            latitude=lat,
            longitude=long,
            description=descr[:2000],
            routeRecommendation=detail_data.get("routeRecommendation"),
            footer=detail_data.get("footer"),
            lorryParkingFeatureIcons=detail_data.get("lorryParkingFeatureIcons"),
            geometry=detail_data.get("geometry")["coordinates"],
        )


    def process_roadworks(self, road, detail_data):
        if (descr := detail_data.get("description")) is not None:
            descr = " ".join(descr)
        if (coor := detail_data.get("coordinate")) is not None:
            lat = coor["lat"]
            long = coor["long"]
        title_parts = detail_data["title"].split(" ")
        if "|" in title_parts:
            pipe_index = title_parts.index("|")
            title_parts = title_parts[pipe_index + 1:]
        
        for idx, part in enumerate(title_parts):
            if part.isalpha():
                title_parts = title_parts[idx:]
                break

        Roadwork.objects.create(
            road=road,
            isBlocked=detail_data.get("isBlocked"),
            future=detail_data.get("future"),
            startLcPosition=detail_data.get("startLcPosition"),
            impact=detail_data.get("impact"),
            display_type=detail_data.get("display_type"),
            subtitle=detail_data.get("subtitle"),
            title=" ".join(title_parts),
            startTimestamp=detail_data.get("startTimestamp"),
            latitude=lat,
            longitude=long,
            description=descr[:2000],
            routeRecommendation=detail_data.get("routeRecommendation"),
            footer=detail_data.get("footer"),
            lorryParkingFeatureIcons=detail_data.get("lorryParkingFeatureIcons"),
            geometry=detail_data.get("geometry")["coordinates"],
        )