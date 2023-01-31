from socket import gethostname
from urllib.parse import urljoin

from requests import get as requests_get
from requests.exceptions import JSONDecodeError


def get_nodes(token, base_url):
    """Returns node information from Kubernetes."""
    return _do_get(token, base_url, "/api/v1/nodes?limit=500")


def get_pods(token, base_url):
    """Returns pod information from Kubernetes."""
    return _do_get(token, base_url, "/api/v1/pods?limit=500")


def get_current_pod_name():
    """Returns the current pod name which is just the hostname."""
    return gethostname()


def _do_get(token, base_url, path, print_response=False):
    """Performs a GET request using the requests library. A JSON object is returned."""

    if not token or not base_url:
        raise ValueError("get_nodes: both token and base_url must be specified.")

    headers = { "Authorization": f"Bearer {token}" }
    url = urljoin(base_url, path)

    try:
        headers.update({
            "Accept": "application/json;as=Table;v=v1;g=meta.k8s.io,application/json;as=Table;v=v1beta1;g=meta.k8s.io,application/json"
        })
        response = requests_get(url=url, headers=headers, verify=False)
        json_response = response.json()

        if print_response:
            print(f"{json_response=}")

        return json_response
    except JSONDecodeError as err:
        print(response)
        print(err)
        raise(err)
