import json

import allure
import requests


class BaseClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json; charset=UTF-8"})

    def request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        with allure.step(f"{method.upper()} {url}"):
            response = self.session.request(method=method, url=url, timeout=20, **kwargs)
            self._attach_request_and_response(method=method, url=url, response=response, kwargs=kwargs)
            return response

    @staticmethod
    def _attach_request_and_response(method: str, url: str, response: requests.Response, kwargs: dict):
        request_payload = {
            "method": method.upper(),
            "url": url,
            "params": kwargs.get("params"),
            "json": kwargs.get("json"),
            "data": kwargs.get("data"),
        }
        allure.attach(
            json.dumps(request_payload, ensure_ascii=False, indent=2),
            name="request",
            attachment_type=allure.attachment_type.JSON,
        )
        try:
            response_body = response.json()
        except ValueError:
            response_body = response.text

        response_payload = {
            "status_code": response.status_code,
            "headers": dict(response.headers),
            "body": response_body,
        }
        allure.attach(
            json.dumps(response_payload, ensure_ascii=False, indent=2),
            name="response",
            attachment_type=allure.attachment_type.JSON,
        )

    def get(self, endpoint: str, **kwargs) -> requests.Response:
        return self.request("GET", endpoint, **kwargs)

    def post(self, endpoint: str, **kwargs) -> requests.Response:
        return self.request("POST", endpoint, **kwargs)

    def put(self, endpoint: str, **kwargs) -> requests.Response:
        return self.request("PUT", endpoint, **kwargs)

    def patch(self, endpoint: str, **kwargs) -> requests.Response:
        return self.request("PATCH", endpoint, **kwargs)

    def delete(self, endpoint: str, **kwargs) -> requests.Response:
        return self.request("DELETE", endpoint, **kwargs)
