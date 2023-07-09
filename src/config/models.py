from sqlalchemy import Column, Integer, String, DateTime, PrimaryKeyConstraint, func
from .database import Base

class Timezones(Base):
    __tablename__ = "TZDB_TIMEZONES"

    countrycode = Column(String(2), nullable=False)
    countryname = Column(String(100), nullable=False)
    zonename = Column(String(100), primary_key=True, index=True, nullable=False)
    gmtoffset = Column(Integer)
    import_date = Column(DateTime(timezone=True), server_default=func.now())


class ZoneDetails(Base):
    __tablename__ = "TZDB_ZONE_DETAILS"

    countrycode = Column(String(2), nullable=False)
    countryname = Column(String(100), nullable=False)
    zonename = Column(String(100), nullable=False)
    gmtoffset = Column(Integer, nullable=False)
    dst = Column(Integer, nullable=False)
    zonestart = Column(Integer, nullable=False)
    zoneend = Column(Integer, nullable=False)
    import_date = Column(DateTime(timezone=True), server_default=func.now())

    __table_args__ = (
        PrimaryKeyConstraint('zonename', 'zonestart', 'zoneend'),
    )

class ErrorLog(Base):
    __tablename__ = "TZDB_ERROR_LOG"

    id = Column(Integer, primary_key=True)
    error_date = Column(DateTime(timezone=True), server_default=func.now())
    error_message = Column(String(1000))