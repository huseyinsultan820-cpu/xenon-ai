from pyfiglet import Figlet
from rich.console import Console
from rich.panel import Panel
from rich.align import Align

console = Console()


def show_banner():
    fig = Figlet(font="slant")

    logo = fig.renderText("XENON AI")

    console.print(
        Panel(
            Align.center(f"[bold bright_cyan]{logo}[/bold bright_cyan]"),
            title="[bold bright_green]XENON AI[/bold bright_green]",
            subtitle="[bold yellow]Neural Intelligence System[/bold yellow]",
            border_style="bright_green",
            padding=(1, 2),
        )
    )

    console.print("[bold bright_green]✓[/] AI Core Ready")
    console.print("[bold bright_cyan]✓[/] Neural Engine Loaded")
    console.print("[bold yellow]✓[/] Security Enabled")
    console.print("[bold magenta]✓[/] Ollama Connected")
    console.print()
