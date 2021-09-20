"""
Performs requests towards the mite.yo.lk api.
"""

import requests

import config


BASE_URL = f"https://{config.auth_info()['account_name']}.mite.yo.lk"
AUTH_PARAM = f"api_key={config.auth_info()['api_key']}"


def get_base_info():
    """
    Retrieves basic account info.

    returns (dict):
        A dictionary of basic info.
    """
    url = f"{BASE_URL}/account.json?{AUTH_PARAM}"
    response = requests.get(url, timeout=3)
    response.raise_for_status()

    result = response.json()
    return result


def get_time_entries_of_project(project):
    project_id = project['project']['id']
    project_param = f"project_id={project_id}"
    url = f"{BASE_URL}/time_entries.json?{AUTH_PARAM}&{project_param}"
    response = requests.get(url, timeout=3)
    response.raise_for_status()

    result = response.json()
    return result


def get_projects():
    url = f"{BASE_URL}/projects.json?{AUTH_PARAM}"
    response = requests.get(url, timeout=3)
    response.raise_for_status()

    result = response.json()
    return result