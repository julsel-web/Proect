from clients.base_client import BaseClient


class JSONPlaceholderClient(BaseClient):
    def get_collection(self, resource: str):
        return self.get(resource)

    def get_by_id(self, resource: str, item_id: int):
        return self.get(f"{resource}/{item_id}")

    def create(self, resource: str, payload: dict):
        return self.post(resource, json=payload)

    def update(self, resource: str, item_id: int, payload: dict):
        return self.put(f"{resource}/{item_id}", json=payload)

    def partial_update(self, resource: str, item_id: int, payload: dict):
        return self.patch(f"{resource}/{item_id}", json=payload)

    def remove(self, resource: str, item_id: int):
        return self.delete(f"{resource}/{item_id}")
