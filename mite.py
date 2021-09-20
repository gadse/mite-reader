"""
Performs requests towards the mite.yo.lk api.
"""

import requests

import config
import endpoints


def get_base_info():
    """
    Retrieves basic account info.

    returns (dict):
        A dictionary of basic info.
    """
    result = fetch(endpoints.ACCOUNT)
    return result


def get_time_entries_of_project(project):
    """
    Fetches all time entries of a given project.

    Args:
        project (dict): The project

    Returns (dict):
        All corresponding time entries
    """
    params = {"project_id": project['project']['id']}
    result = fetch(endpoints.ENTRIES, params=params)
    return result


def get_projects():
    result = fetch(endpoints.PROJECTS)
    return result


def fetch(endpoint, **params):
    base_url = f"https://{config.auth_info()['account_name']}.mite.yo.lk"
    auth_param = f"api_key={config.auth_info()['api_key']}"

    url = f"{base_url}/{endpoint}?{auth_param}"
    for param, value in params.items():
        url += f"&{param}={value}"

    response = requests.get(url, timeout=3)
    response.raise_for_status()

    result = response.json()
    return result
