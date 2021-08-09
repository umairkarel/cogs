from __future__ import annotations

from typing import Union

from sqlalchemy import Column, BigInteger, Integer

from PyDrocsid.database import db


class AutoClearChannel(db.Base):
    __tablename__ = "autoclear_channel"

    channel: Union[Column, int] = Column(BigInteger, primary_key=True, unique=True)
    minutes: Union[Column, int] = Column(Integer)

    @staticmethod
    async def create(channel: int, minutes: int) -> AutoClearChannel:
        row = AutoClearChannel(channel=channel, minutes=minutes)
        await db.add(row)
        return row
