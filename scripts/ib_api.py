"""InstaBox API 调用。已适配 GitHub Actions，直接从环境变量读 key。"""
import json
import os
import sys
import urllib.error
import urllib.request
import uuid

BASE = "https://api.instabox.sh"
HOSTS = ["api.instabox.sh"]
LIFECYCLE = ("/suspend", "/resume", "/start", "/stop")

class ApiError(RuntimeError):
    pass

class DynamicCredentialError(RuntimeError):
    pass

# 替换原版的 add_surrogate_to_request，直接从环境变量读取 API_KEY
def add_surrogate_to_request(req, cred, allowed_hosts=None):
    api_key = os.environ.get("INSTABOX_API_KEY")
    if not api_key:
        raise DynamicCredentialError("环境变量中未找到 INSTABOX_API_KEY")
    req.add_header("X-API-Key", api_key)

def read_response_body(resp):
    return resp.read()

def call(method, path, cred, body=None, timeout=60):
    data = json.dumps(body).encode("utf-8") if body is not None else None
    req = urllib.request.Request(BASE + path, data=data, method=method,
                                 headers={"Content-Type": "application/json"})
    if path.endswith(LIFECYCLE):
        req.add_header("Idempotency-Key", str(uuid.uuid4()))
    add_surrogate_to_request(req, cred, allowed_hosts=HOSTS)
    try:
        with urllib.request.build_opener().open(req, timeout=timeout) as resp:
            return json.loads(read_response_body(resp).decode("utf-8", "replace") or "{}")
    except urllib.error.HTTPError as e:
        raise ApiError(f"HTTP {e.code}: {read_response_body(e).decode('utf-8', 'replace')}") from e
    except (urllib.error.URLError, TimeoutError) as e:
        raise ApiError(f"网络错误: {e}") from e
