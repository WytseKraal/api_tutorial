#!/usr/bin/env python3

import connexion
import logging

from swagger_server import encoder


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.logger.setLevel(logging.DEBUG)
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Simple student API'}, pythonic_params=True)
    app.run(port=8080)


if __name__ == '__main__':
    main()
