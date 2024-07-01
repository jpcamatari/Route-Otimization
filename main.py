from decouple import config
import googlemaps
GOOGLE_KEY = config('GOOGLE_KEY')

maps = googlemaps.Client(key=GOOGLE_KEY)


