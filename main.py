## dependencies
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from api import check_api
from hash_util import encrypt_and_log

# Cloudflare Worker URL
url = "https://start-api-phonetracker.dev-lorenzo.workers.dev/"

# Check API status
if not check_api(url):
    print("Service Unavailable. Check your billing if an enterprise. Otherwise check your internet connection.")
else:
    ## info + start
    print("Phone Tracker")
    print("by continuing you accept the ToS and Privacy Policy")

    ## phone input
    phone = input("Enter phone number with country code: ").strip()
    encrypt_and_log(phone)

    try:
        parsed_number = phonenumbers.parse(phone)

        # Carrier
        phone_carrier = carrier.name_for_number(parsed_number, "en")

        # Region (approx. location based on number block)
        phone_region = geocoder.description_for_number(parsed_number, "en")

        # Timezones
        phone_timezones = timezone.time_zones_for_number(parsed_number)

        # Country (from country code)
        country_name = geocoder.country_name_for_number(parsed_number, "en")

        print("\n--- Phone Information ---")
        print(f"Number: {phone}")
        print(f"Carrier: {phone_carrier if phone_carrier else 'Unknown'} ({country_name})")
        print(f"Region: {phone_region if phone_region else 'Unknown'}")
        print(f"Timezones: {', '.join(phone_timezones) if phone_timezones else 'Unknown'}")

    except phonenumbers.NumberParseException as e:
        print(f"Error parsing phone number: {e}")
