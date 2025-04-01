# models/song_map.py

from datetime import datetime

from sqlalchemy import Column, DateTime, Index, String, Text, UniqueConstraint

from app.models import (
    Base,
)  # Adjust the import based on your project structure


class Sample(Base):
    __tablename__ = "sample"

    class Meta:
        load_instance = True

    email_id: str = Column(String(255), primary_key=True)
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(DateTime, onupdate=datetime.now, nullable=False)
