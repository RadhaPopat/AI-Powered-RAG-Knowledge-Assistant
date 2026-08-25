from datetime import datetime, timezone
from typing import Optional

from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: Optional[int] = Field(default=None, primary_key=True)

    name: str
    email: str = Field(index=True, unique=True)
    password_hash: str

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )


class Document(SQLModel, table=True):
    __tablename__ = "documents"

    id: Optional[int] = Field(default=None, primary_key=True)

    user_id: int = Field(foreign_key="users.id", index=True)

    name: str

    s3_url: Optional[str] = None

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )


class DocumentChunk(SQLModel, table=True):
    __tablename__ = "document_chunks"

    id: Optional[int] = Field(default=None, primary_key=True)

    document_id: int = Field(
        foreign_key="documents.id",
        index=True
    )

    chunk_text: str

    chunk_index: int

    page_number: Optional[int] = None

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )