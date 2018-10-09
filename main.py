from view import View
from controller import Controller
from repositoryDB import Repository


def main():
    repository = Repository()
    controller = Controller(repository)
    view = View(controller)
    view.mainMenu()


if __name__ == '__main__':
    main()
