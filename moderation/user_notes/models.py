from __future__ import annotations

from datetime import datetime
from typing import Union

from discord.utils import utcnow
from sqlalchemy import Column, Text, BigInteger

from PyDrocsid.database import db, UTCDateTime


class UserNote(db.Base):
    __tablename__ = "user_notes"

    id: Union[Column, int] = Column(BigInteger, primary_key=True, unique=True, autoincrement=True)
    member_id: Union[Column, int] = Column(BigInteger)
    author_id: Union[Column, int] = Column(BigInteger)
    content: Union[Column, str] = Column(Text(collation="utf8mb4_bin"))
    timestamp: Union[Column, datetime] = Column(UTCDateTime)

    @staticmethod
    async def create(member_id: int, author_id: int, content: str) -> UserNote:
        row = UserNote(
            member_id=member_id,
            author_id=author_id,
            content=content,
            timestamp=utcnow(),
        )
        await db.add(row)
        return row
