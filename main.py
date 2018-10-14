from view import View
from controller import Controller
from repositoryDB import Repository
from MySQL import DB


def main():
    database=DB()
    repository = Repository(database)
    controller = Controller(repository)
    view = View(controller)
    view.mainMenu()


if __name__ == '__main__':
    main()
