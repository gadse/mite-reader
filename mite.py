"""
Performs requests towards the mite.yo.lk api.
"""

import requests

import config


def get_base_info():
    """
    Retrieves basic account info.

    returns (dict):
        A dictionary of basic info.
    """
    auth_info = config.auth_info()
    url = f"https://{auth_info['account_name']}.mite.yo.lk/account.json?api_key={auth_info['api_key']}"

    response = requests.get(url, timeout=3)
    response.raise_for_status()

    result = response.json()
    return result
