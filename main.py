from os import system,chdir
from datetime import datetime
from time import sleep

TIME_SLEEP = 3

REPO_DIR = [
    r"C:\Users\alexa\OneDrive\Documents\TS",
    r"C:\Users\alexa\OneDrive\Documents\Tesis",
]


def commit_all():
    date_now = datetime.now().strftime("%d%m%Y%S")
    command("git add .")
    command(f'git commit -m "🤖 Autocommit - {date_now}"')  # Name repo?
    command(f"git push --force")


def command(cmd: str):
    system(cmd)
    sleep(TIME_SLEEP)


def main():
    for dir in REPO_DIR:
        chdir(dir)
        commit_all()
        pass


if __name__ == "__main__":
    main()
