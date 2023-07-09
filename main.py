from src.config import models
from src.config.database import engine, create_database
from src.api.api_client import get_timezones_api,get_timezones_detail_api
from src.crud.timezone import populate_timezones_table, populate_zone_details_table

def get_timezones():
    try:
         # Query TimezoneDB API to get timezones
        timezones = get_timezones_api()
        return timezones
    except Exception as e:
        print(f"Error from the API TimeZone {str(e)}")

def populate_table(timezones):
    # Populate Timezones table
        if timezones is not None:
            populate_timezones_table(timezones)

            # Populate ZoneDetails table
            for tz in timezones:
                detail = get_timezones_detail_api(tz['zonename'])
                if detail is not None:
                   populate_zone_details_table(detail)
        else:
            print(f"Error populate table")


def main():
    try: 
        create_database()
        models.Base.metadata.create_all(bind=engine)

        timezones = get_timezones()
        populate_table(timezones)

    except Exception as e:
        # Log the error
        error_message = str(e)
        print(f"Error: {error_message}")

if __name__ == '__main__':
    main()