from __future__ import annotations

import logging
from rich.console import Console
from rich.logging import RichHandler


def setup_logging(level: int = logging.INFO) -> None:
    console = Console(force_terminal=True)
    handler = RichHandler(console=console, show_time=True, rich_tracebacks=True)
    logging.basicConfig(
        level=level,
        format="%(message)s",
        datefmt="%H:%M:%S",
        handlers=[handler],
    )