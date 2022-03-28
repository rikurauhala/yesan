from invoke import task


@task
def start(ctx):
    """Run the application."""
    ctx.run("python3 src/index.py")
