"""A simple blue-themed stopwatch GUI."""

from __future__ import annotations

import tkinter as tk
import time
from tkinter import ttk


def format_time(seconds: float) -> str:
    """Return elapsed seconds as HH:MM:SS.ss."""
    hundredths = int(seconds * 100) % 100
    total_seconds = int(seconds)
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds_part = divmod(remainder, 60)
    return f"{hours:02}:{minutes:02}:{seconds_part:02}.{hundredths:02}"


class Stopwatch:
    """A stopwatch that supports starting, pausing, and resetting."""

    def __init__(self) -> None:
        self._started_at: float | None = None
        self._elapsed = 0.0

    @property
    def is_running(self) -> bool:
        return self._started_at is not None

    @property
    def elapsed(self) -> float:
        if self._started_at is None:
            return self._elapsed
        return self._elapsed + (time.monotonic() - self._started_at)

    def start(self) -> None:
        if not self.is_running:
            self._started_at = time.monotonic()

    def pause(self) -> None:
        if self.is_running:
            self._elapsed = self.elapsed
            self._started_at = None

    def reset(self) -> None:
        self._started_at = None
        self._elapsed = 0.0


def main() -> None:
    stopwatch = Stopwatch()

    root = tk.Tk()
    root.title("Blue Stopwatch")
    root.geometry("360x230")
    root.resizable(False, False)
    root.configure(bg="#0d47a1")

    style = ttk.Style(root)
    style.theme_use("clam")
    style.configure(
        "Blue.TButton",
        background="#1976d2",
        foreground="white",
        font=("Segoe UI", 11, "bold"),
        padding=(14, 8),
    )
    style.map("Blue.TButton", background=[("active", "#42a5f5")])

    time_label = tk.Label(
        root,
        text=format_time(0),
        bg="#0d47a1",
        fg="white",
        font=("Segoe UI", 32, "bold"),
    )
    time_label.pack(pady=(35, 20))

    buttons = tk.Frame(root, bg="#0d47a1")
    buttons.pack()

    def update_display() -> None:
        time_label.config(text=format_time(stopwatch.elapsed))
        root.after(10, update_display)

    def toggle_start() -> None:
        if stopwatch.is_running:
            stopwatch.pause()
            start_button.config(text="Start")
        else:
            stopwatch.start()
            start_button.config(text="Pause")

    def reset() -> None:
        stopwatch.reset()
        start_button.config(text="Start")

    start_button = ttk.Button(
        buttons, text="Start", command=toggle_start, style="Blue.TButton"
    )
    start_button.grid(row=0, column=0, padx=5)
    ttk.Button(
        buttons, text="Reset", command=reset, style="Blue.TButton"
    ).grid(row=0, column=1, padx=5)

    update_display()
    root.mainloop()


if __name__ == "__main__":
    main()