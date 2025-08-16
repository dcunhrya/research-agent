from __future__ import annotations

from pathlib import Path
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Runtime configuration (env-overridable)."""

    data_dir: Path = Field(default=Path("./data"))
    request_timeout: float = Field(default=30.0)
    user_agent: str = Field(default="ResearchWorkflowAgent/0.1")
    s2_api_key: str | None = Field(default=None)
    default_sources: list[str] = Field(default_factory=lambda: ["arxiv", "semanticscholar"])

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @property
    def papers_dir(self) -> Path:
        p = self.data_dir / "papers"
        p.mkdir(parents=True, exist_ok=True)
        return p


settings = Settings()