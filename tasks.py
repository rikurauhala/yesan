from invoke import task


@task
def init(ctx):
    ctx.run("python3 src/database.py")


@task
def start(ctx):
    ctx.run("python3 src/index.py")


@task
def test(ctx):
    ctx.run("pytest src", pty=True)


@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=True)


@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html")


@task
def lint(ctx):
    ctx.run("pylint src")


@task
def format(ctx):
    ctx.run("autopep8 --in-place --recursive src")

