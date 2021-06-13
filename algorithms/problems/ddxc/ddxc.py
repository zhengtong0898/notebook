import os
import requests


# https://developer.mozilla.org/en-US/docs/Web/HTTP/Range_requests
# https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.7
# https://blog.csdn.net/qq_35203425/article/details/80987880
def get_resource_size(url) -> int:
    with requests.get(url, stream=True, headers={"Range": "bytes=0-10"}) as resp:
        resp_header = dict(resp.headers)
        try:
            assert "Content-Range" in resp_header.keys()
            assert "Content-Length" in resp_header.keys()
        except AssertionError:
            return 0

        resource_bytes = resp_header["Content-Range"].split("/")[1]
        return int(resource_bytes)


def download(url, save_to):
    resource_bytes = get_resource_size(url)
    if resource_bytes <= 0: return

    current_bytes = os.path.getsize(save_to) if os.path.exists(save_to) else 0
    if current_bytes == resource_bytes: return
    headers = {"Range": f"bytes={current_bytes}-{resource_bytes}"}
    resp = requests.get(url, headers=headers, stream=True)

    loaded = current_bytes
    with open(save_to, "ab") as f:
        for content in resp.iter_content(chunk_size=1024):
            loaded += len(content)
            percentage = int(loaded / resource_bytes * 100)
            print(f"\r{percentage}%", end="")
            f.write(content)
            f.flush()


def main():
    url = "http://192.168.1.3/sss.jpg"
    download(url, "sss.jpg")


if __name__ == '__main__':
    main()
