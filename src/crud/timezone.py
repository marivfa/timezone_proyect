from sqlalchemy.exc import IntegrityError
from src.config.database import SessionLocal
from ..config.models import Timezones, ZoneDetails, ErrorLog

def populate_timezones_table(timezones):
    with SessionLocal() as db:
        try: 
            db.query(Timezones).delete()
            for tz in timezones:
                timezone = Timezones(
                    countrycode=tz['countrycode'],
                    countryname=tz['countryname'],
                    zonename=tz['zonename'],
                    gmtoffset=tz['gmtoffset']
                )
                db.add(timezone)
            db.commit()
        except IntegrityError as e:
            db.rollback()
            error_message = f"Integrity error occurred while populating timezones table: {str(e)}"
            save_error_log(error_message)


def populate_zone_details_table(detail):
    with SessionLocal() as db:
        # Check if a row with the same zonename, zonestart, and zoneend already exists
        existing_row = db.query(ZoneDetails).filter_by(
            zonename=detail['zonename'],
            zonestart=detail['zonestart'],
            zoneend=detail['zoneend']
        ).first()

        if not existing_row:
            zone_detail = ZoneDetails(
                countrycode=detail['countrycode'],
                countryname=detail['countryname'],
                zonename=detail['zonename'],
                gmtoffset=detail['gmtoffset'],
                dst=detail['dst'],
                zonestart=detail['zonestart'],
                zoneend=detail['zoneend']
            )

            try: 
                db.add(zone_detail)
                db.commit()
            except IntegrityError as e:
                db.rollback()
                print(f"IntegrityError occurred: {str(e)}")


def save_error_log(error_message):
    with SessionLocal() as db:
        error_log = ErrorLog(error_message=error_message)
        db.add(error_log)
        db.commit()