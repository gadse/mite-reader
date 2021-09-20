from pprint import pprint

import config
import mite


def main():
    pprint(config.auth_info())
    pprint(mite.get_base_info())
    projects = mite.get_projects()
    pprint(projects)
    tasks = mite.get_tasks_of_project(projects[0])
    pprint(tasks)


if __name__ == "__main__":
    main()


