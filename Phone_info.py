import phonenumbers
from phonenumbers import geocoder, carrier, timezone

def gather_phone_info(phone_number):
    try:
        # Parse the phone number
        parsed_number = phonenumbers.parse(phone_number)

        # Validate if the phone number is valid
        if not phonenumbers.is_valid_number(parsed_number):
            return "Invalid phone number!"

        # Get the country and region
        country = geocoder.description_for_number(parsed_number, "en")

        # Get the carrier (service provider)
        service_provider = carrier.name_for_number(parsed_number, "en")

        # Get the timezone
        time_zones = timezone.time_zones_for_number(parsed_number)

        # Compile information
        info = f"""
        Phone Number: {phone_number}
        Country/Region: {country}
        Carrier: {service_provider}
        Timezone(s): {', '.join(time_zones)}
        """
        return info

    except phonenumbers.NumberParseException as e:
        return f"Error: {e}"

if __name__ == "__main__":
    print("Welcome to Almus Production!")
    print("Gathering information about an international phone number.\n")

    # Input phone number from the user
    phone_number = input("Enter the phone number (with country code, e.g., +2348021133690): ")
    info = gather_phone_info(phone_number)
    print("\n" + info)
