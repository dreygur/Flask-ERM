#!/usr/bin/env python3

import os

# Third Party
from flask import Blueprint
from flask import request, jsonify
from flask import render_template

# main
from . import routes

main = Blueprint('main', __name__)

# Routes
main.add_url_rule("/", 'root', view_func=routes.root)
main.add_url_rule("/api/", 'api', view_func=routes.api)
main.add_url_rule("/form/", 'form', view_func=routes.form)


if __name__ == "__main__":
    main.debug = True
    main.port = int(os.getenv("PORT", 5000))
    main.run()


