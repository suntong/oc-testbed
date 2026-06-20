import sys
from rich.console import Console
from rich.panel import Panel
from agents.planner import PlannerAgent
from agents.researcher import ResearchAgent
from agents.coder import CoderAgent
from agents.reviewer import ReviewerAgent
from agents.config import NVIDIA_API_KEY

def main():
    console = Console()
    if not NVIDIA_API_KEY:
        console.print("[bold red]NVIDIA_API_KEY missing.[/bold red]")
        sys.exit(1)
    request = console.input("[bold cyan]Feature request > [/bold cyan]").strip()
    if not request: return
    try:
        with console.status("Planning..."): plan = PlannerAgent().plan(request)
        console.print(Panel(plan, title="PLAN", border_style="green"))
        with console.status("Researching..."): context = ResearchAgent().lookup(plan)
        console.print(Panel(context, title="RESEARCH", border_style="blue"))
        with console.status("Coding..."): code = CoderAgent().implement(plan, context)
        console.print(Panel(code, title="CODE", border_style="magenta"))
        with console.status("Reviewing..."): review = ReviewerAgent().review(code)
        console.print(Panel(review, title="REVIEW", border_style="yellow"))
    except RuntimeError as e:
        console.print(f"\n[bold red]Failed:[/bold red] {e}")
if __name__ == '__main__': main()