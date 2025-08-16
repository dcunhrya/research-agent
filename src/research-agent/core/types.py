from __future__ import annotations

from typing import Literal
from pydantic import BaseModel, Field


class Author(BaseModel):
    name: str
    affiliation: str | None = None


class Paper(BaseModel):
    id: str = Field(description="Canonical paper id for de-dup (doi/arXiv/S2)")
    title: str
    abstract: str | None = None
    authors: list[Author] = Field(default_factory=list)
    year: int | None = None
    venue: str | None = None
    url: str | None = None
    pdf_url: str | None = None
    source: Literal["arxiv", "semanticscholar"]
    external_ids: dict[str, str] = Field(default_factory=dict)
    topics: list[str] = Field(default_factory=list)

    def display_author_line(self, k: int = 3) -> str:
        if not self.authors:
            return ""
        names = [a.name for a in self.authors]
        return ", ".join(names[:k]) + (" et al." if len(names) > k else "")