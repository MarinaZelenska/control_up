import requests
from typing import Any, Dict, Optional


class BaseApiClient:
    def __init__(self, base_url: str, session: requests.Session, timeout: int = 15):
        self.base_url = base_url
        self.session = session
        self.timeout = timeout

    def _url(self, path: str) -> str:
        return f"{self.base_url}{path}"

    def get_json(self, path: str, **kwargs) -> Dict[str, Any]:
        response = self.session.get(self._url(path), timeout=self.timeout, **kwargs)
        response.raise_for_status()
        return response.json()

    def post_json(self, path: str, json: Optional[Dict[str, Any]] = None, **kwargs) -> Dict[str, Any]:
        response = self.session.post(self._url(path), json=json, timeout=self.timeout, **kwargs)
        response.raise_for_status()
        return response.json()
