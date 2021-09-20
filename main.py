from pprint import pprint

import config
import mite


def main():
    pprint("### AUTH INFO")
    pprint(config.auth_info())

    print("### ACCOUNT INFO")
    pprint(mite.get_base_info())

    print("### PROJECT")
    projects = mite.get_projects()
    pprint(projects)

    print("### TASKS OF FIRST PROJECT")
    entries = mite.get_time_entries_of_project(projects[0])
    for entry in entries:
        e = entry["time_entry"]
        pprint(f"{e['id']} | {e['user_name']} | {e['minutes']:03d} min | {e['note']}")


if __name__ == "__main__":
    main()


