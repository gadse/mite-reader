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
        print(f"{e['id']:20d} | {e['user_name']:30s} | {e['minutes']:03d} min | {e['note']:60s}")


if __name__ == "__main__":
    main()


