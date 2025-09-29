# Standard library imports
from os import system
from time import sleep
from urllib.parse import urlparse
from typing import List, Dict
import logging

# Third-party imports
from rich.console import Console
from rich.table import Table
from rich.progress import Progress
from rich.style import Style
from rich.panel import Panel
from rich.box import SIMPLE_HEAVY, DOUBLE
from requests import Session
from requests.adapters import HTTPAdapter

# Configure logging
logging.basicConfig(
    filename="xtoolbox.log",
    level=logging.INFO,
    format="[%(asctime)s] [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)

# Explicitly import tools_data*.py files
PAGES = []
try:
    from tools_data import PAGES as PAGES1
    PAGES.extend(PAGES1)
    logger.info(f"Successfully imported {len(PAGES1)} pages from tools_data.py")
except ImportError as e:
    logger.error(f"Failed to import tools_data.py: {e}")
    print(f"[ERROR] Failed to import tools_data.py: {e}")
try:
    from tools_data2 import PAGES as PAGES2
    PAGES.extend(PAGES2)
    logger.info(f"Successfully imported {len(PAGES2)} pages from tools_data2.py")
except ImportError as e:
    logger.error(f"Failed to import tools_data2.py: {e}")
    print(f"[ERROR] Failed to import tools_data2.py: {e}")
try:
    from tools_data3 import PAGES as PAGES3
    PAGES.extend(PAGES3)
    logger.info(f"Successfully imported {len(PAGES3)} pages from tools_data3.py")
except ImportError as e:
    logger.info(f"tools_data3.py not found, skipping: {e}")

# Log the number of tools per page
for page in PAGES:
    logger.info(f"Page '{page['name']}' has {len(page['tools'])} tools")

# Initialize Console for colorful UI
c = Console()
VERSION = "5.2.4"

# Define styles
LIGHT_BLUE_STYLE = Style(color="cyan", bold=True)
GREEN_STYLE = Style(color="green", bold=True)
ERROR_STYLE = Style(color="red", bold=True)
ACTIVE_PAGE_STYLE = Style(color="red", bold=True)

# HTTP session for downloads
headers = {"User-Agent": "Mozilla/5.0"}
session = Session()
session.mount("https://", HTTPAdapter(max_retries=3))
 
def cls():
    """Clear the console."""
    system("cls" if os.name == "nt" else "clear")

def download(url: str, filename: str, name: str) -> None:
    """Download a file with progress."""
    try:
        url = urlparse(url)._replace(scheme="https").geturl()
        c.print(f"Downloading [cyan]{name}[/cyan]...", style=LIGHT_BLUE_STYLE)
        
        response = session.head(url, headers=headers)
        total_size = int(response.headers.get("content-length", 0))
        c.print(f"Size: {round(total_size / 1024 / 1024, 1)}MB", style=LIGHT_BLUE_STYLE)

        with Progress() as progress:
            task = progress.add_task("[green]→[/green]", total=total_size)
            with open(filename, "wb") as f:
                for data in session.get(url, stream=True, headers=headers).iter_content(1024):
                    f.write(data)
                    progress.update(task, advance=len(data))
        c.print(f"[✓] Downloaded {name}", style=GREEN_STYLE)
        logger.info(f"Downloaded {name} to {filename}")
    except Exception as e:
        c.print(f"[✗] Failed: {str(e)}", style=ERROR_STYLE)
        logger.error(f"Download failed for {name}: {e}")

def yn_prompt(prompt: str) -> bool:
    """Yes/no prompt."""
    c.print(f"{prompt} ([green]Y[/green]/[red]n[/red]): ", style=LIGHT_BLUE_STYLE, end="")
    return c.input().strip().lower() in ("y", "")

def display_menu(page_group: List[Dict], page_index: int, total_groups: int) -> None:
    """Display tool menu with all tools in each page, with unique numbering across all tools."""
    cls()
    # Title with double box
    c.print(Panel(
        f"[cyan]XToolBox {VERSION}, by Vampeyer[/cyan]",
        box=DOUBLE,
        style=LIGHT_BLUE_STYLE,
        border_style=LIGHT_BLUE_STYLE,
        expand=False
    ))
    
    # Create pages table with three columns
    pages_table = Table(show_header=False, box=SIMPLE_HEAVY, style=LIGHT_BLUE_STYLE)
    pages_table.add_column(justify="center")
    pages_table.add_column(justify="center")
    pages_table.add_column(justify="center")
    
    for i in range(0, len(PAGES), 3):
        row = []
        # First column
        if i < len(PAGES):
            marker = "- " if i // 3 == page_index else "  "
            row.append(f"{marker}[cyan]{PAGES[i]['name']}[/cyan]" if i // 3 != page_index else f"[red]- [/red][cyan]{PAGES[i]['name']}[/cyan]")
        else:
            row.append("")
        # Second column
        if i + 1 < len(PAGES):
            marker = "- " if (i + 1) // 3 == page_index else "  "
            row.append(f"{marker}[cyan]{PAGES[i + 1]['name']}[/cyan]" if (i + 1) // 3 != page_index else f"[red]- [/red][cyan]{PAGES[i + 1]['name']}[/cyan]")
        else:
            row.append("")
        # Third column
        if i + 2 < len(PAGES):
            marker = "- " if (i + 2) // 3 == page_index else "  "
            row.append(f"{marker}[cyan]{PAGES[i + 2]['name']}[/cyan]" if (i + 2) // 3 != page_index else f"[red]- [/red][cyan]{PAGES[i + 2]['name']}[/cyan]")
        else:
            row.append("")
        pages_table.add_row(*row)
    
    c.print(Panel(pages_table, title="Pages", style=LIGHT_BLUE_STYLE, border_style=LIGHT_BLUE_STYLE, expand=False))
    
    # Display all tools in each page, with unique numbering
    tool_index = 1
    tool_mapping = []
    for idx, page in enumerate(page_group):
        table = Table(border_style=LIGHT_BLUE_STYLE)
        table.add_column(
            f"[cyan]{page['name']}[/cyan]",
            footer=f"[cyan]{tool_index}-{tool_index + len(page['tools']) - 1}[/cyan], [cyan]N[/cyan]/[cyan]B[/cyan], [cyan]Q[/cyan]",
            style=GREEN_STYLE
        )
        table.add_column(
            "Description",
            style=GREEN_STYLE
        )
        # Display all tools
        for tool in page['tools']:
            table.add_row(
                f"[cyan][{tool_index}][/cyan] {tool['name']}",
                tool.get('description', 'No description available.')
            )
            tool_mapping.append((page, tool))
            tool_index += 1
        c.print(table)
        c.print()  # Add spacing between tables
    
    c.print(f"[cyan]Page Group {page_index + 1}/{total_groups}[/cyan]", style=LIGHT_BLUE_STYLE)
    c.print("[cyan]Use N/B to change page groups[/cyan]", style=LIGHT_BLUE_STYLE)
    c.print(f"[cyan]Select a number (1-{tool_index - 1}) to choose a tool[/cyan]", style=LIGHT_BLUE_STYLE)
    c.print("[cyan]Press Enter to download after selecting[/cyan]", style=LIGHT_BLUE_STYLE)

    return tool_mapping

def select_and_download(pages: List[Dict]) -> None:
    """Handle tool selection and download."""
    if not pages:
        c.print("[✗] No tools found in tools_data files! Check xtoolbox.log for details.", style=ERROR_STYLE)
        logger.error("No tools found in tools_data files")
        c.print("Press ENTER to exit...", style=LIGHT_BLUE_STYLE)
        input()
        return

    # Group pages into sets of 3
    group_size = 3
    page_groups = [pages[i:i + group_size] for i in range(0, len(pages), group_size)]
    if not page_groups:
        c.print("[✗] No page groups available! Check xtoolbox.log for details.", style=ERROR_STYLE)
        logger.error("No page groups available")
        c.print("Press ENTER to exit...", style=LIGHT_BLUE_STYLE)
        input()
        return

    logger.info(f"Loaded {len(pages)} pages, grouped into {len(page_groups)} groups")
    current_group = 0

    while True:
        tool_mapping = display_menu(page_groups[current_group], current_group, len(page_groups))
        c.print("[cyan]> [/cyan]", end="")
        choice = c.input().strip().lower()

        if choice == "q":
            c.print("[cyan]Exiting...[/cyan]", style=LIGHT_BLUE_STYLE)
            logger.info("User exited the application")
            break
        if choice == "n":
            current_group = (current_group + 1) % len(page_groups)
            logger.info(f"Navigated to page group {current_group + 1}")
            continue
        if choice == "b":
            current_group = (current_group - 1) % len(page_groups)
            logger.info(f"Navigated to page group {current_group + 1}")
            continue
        if not choice.isnumeric() or int(choice) < 1 or int(choice) > len(tool_mapping):
            c.print("[✗] Invalid choice", style=ERROR_STYLE)
            logger.warning(f"Invalid choice entered: {choice}")
            sleep(1)
            continue

        # Select tool based on the unique index
        selected_index = int(choice) - 1
        page, tool = tool_mapping[selected_index]
        c.print(f"Selected: [green]{tool['name']} from {page['name']}[/green]", style=GREEN_STYLE)
        logger.info(f"Selected tool: {tool['name']} from {page['name']}")
        if yn_prompt("Download?"):
            download(tool["url"], tool["filename"], tool["name"])
            if tool["filename"].endswith((".exe", ".msi", ".paf")) and yn_prompt(f"Run {tool['filename']}?"):
                system(tool["filename"])
                logger.info(f"Running {tool['filename']}")
        c.print("Press ENTER...", style=LIGHT_BLUE_STYLE)
        input()

def main():
    """Run the toolbox."""
    try:
        logger.info(f"Starting XToolBox v{VERSION}")
        select_and_download(PAGES)
    except Exception as e:
        c.print(f"[✗] Error: {str(e)}", style=ERROR_STYLE)
        logger.error(f"Application error: {e}")
        c.print("Press ENTER to exit...", style=LIGHT_BLUE_STYLE)
        input()

if __name__ == "__main__":
    main()