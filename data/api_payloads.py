POST_PAYLOADS = {
    "posts": {"title": "autotest title", "body": "autotest body", "userId": 1},
    "comments": {
        "name": "autotest comment",
        "email": "autotest@example.com",
        "body": "comment body",
        "postId": 1,
    },
    "albums": {"title": "autotest album", "userId": 1},
    "todos": {"title": "autotest todo", "completed": False, "userId": 1},
}

PUT_POST_PAYLOAD = {"id": 1, "title": "updated title", "body": "updated body", "userId": 7}
PATCH_POST_PAYLOAD = {"title": "patched title"}

RESOURCE_SCHEMAS = {
    "posts": {"required_keys": {"userId", "id", "title", "body"}},
    "comments": {"required_keys": {"postId", "id", "name", "email", "body"}},
    "albums": {"required_keys": {"userId", "id", "title"}},
    "photos": {"required_keys": {"albumId", "id", "title", "url", "thumbnailUrl"}},
    "todos": {"required_keys": {"userId", "id", "title", "completed"}},
    "users": {"required_keys": {"id", "name", "username", "email", "address", "phone", "website", "company"}},
}
