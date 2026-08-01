from rich.console import Console
from rich.progress import Progress, BarColumn, TextColumn
import time

console = Console()

def loading_screen():
    console.print("\n[bold bright_green]Initializing Xenon AI...[/]\n")

    tasks = [
        "Loading AI Core",
        "Loading Neural Engine",
        "Connecting Ollama",
        "Checking Security",
        "Starting Interface"
    ]

    for task in tasks:
        with Progress(
            TextColumn("[cyan]{task.description}"),
            BarColumn(bar_width=40),
            TextColumn("{task.percentage:>3.0f}%"),
            console=console,
        ) as progress:

            t = progress.add_task(task, total=100)

            while not progress.finished:
                progress.update(t, advance=4)
                time.sleep(0.03)

    console.print("\n[bold bright_green]✓ Xenon AI Ready![/]\n")
