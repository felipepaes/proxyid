import secrets
import pprint


def generate_config() -> None:
    config = {
        "hashids": {
            "salt": secrets.token_urlsafe(),
            "min_length": 14
        }
    }
    print("\n\033[1m\033[92mProxyid configuration generated:\033[0m")
    print("PROXYID =", config, end="\n\n")
