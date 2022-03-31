from invoke import task


@task
def start(ctx):
    """Run the application."""
    ctx.run("python3 src/index.py")


@task
def test(ctx):
    """Run automated tests."""
    ctx.run("pytest src")


@task
def coverage(ctx):
    """Check the coverage of the automated tests."""
    ctx.run("coverage run --branch -m pytest src")


@task(coverage)
def coverage_report(ctx):
    """Generate a test coverage report."""
    ctx.run("coverage html")


@task
def lint(ctx):
    """Check the quality of source code."""
    ctx.run("pylint src")
