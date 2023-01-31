from flask import render_template

from app import app, cache

from app.kube import (
    get_nodes,
    get_pods,
    get_current_pod_name
)


@app.route("/")
@cache.cached(timeout=120)
def index():
    """index is the only route of the application. It pulls various information
    from the cluster and renders an HTML template for it.
    """
    token = app.config["AUTH_TOKEN"]
    base_url = app.config["BASE_URL"]

    pod_name = get_current_pod_name()
    pods = get_pods(token, base_url)
    nodes = get_nodes(token, base_url)

    return render_template("index.html",
        message=app.config["MESSAGE"],
        pod_name=pod_name,
        pods=pods,
        nodes=nodes
    )
