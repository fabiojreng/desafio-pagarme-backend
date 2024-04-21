from flask import Flask, jsonify, request, json, Response
from src.Infra.Http.interface_server_http import HttpServer


class FlaskAdapter(HttpServer):
    def __init__(self) -> None:
        self.__app = Flask(__name__)
        self.__app.config["JSON_SORT_KEYS"] = False

    def register(self, method, url, callback):
        if not callable(callback):
            raise ValueError("Callback must be a callable function")
        if not isinstance(url, str):
            raise ValueError("URL must be a string")

        view_name = f"{method.lower()}_{url.replace('/', '_')}_callback"

        def flask_callback(*args, **kwargs):
            try:
                if request.method == "GET":
                    output = callback(*args, **kwargs)
                    return jsonify(output)
                else:
                    data = request.json
                    output = callback(data)
                    return Response(
                        json.dumps(output, sort_keys=False), mimetype="application/json"
                    )
            except Exception as e:
                return jsonify({"error": str(e)}), 400

        flask_callback.__name__ = view_name

        return self.__app.add_url_rule(
            rule=url, view_func=flask_callback, methods=[method.upper()]
        )

    def listen(self, port):
        print(f"SERVER RUNNING IN PORT {port}")
        return self.__app.run(port=port, debug=True)
