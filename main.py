import os
import json
import requests  # noqa We are just importing this to prove the dependency installed correctly


def main():
    skydera_url = 'https://skydera-dev-api.cloudstart.co/infra/deploy/preview'

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    api_username = '__token__'
    api_key = os.environ["INPUT_SKYDERAAPIKEY"]

    data = {}
    for k, v in sorted(os.environ.items()):
        print(k + ':', v)
        data[k] = v

    my_output = f"Hello {api_key}"

    print(f"::set-output name=myOutput::{my_output}")

    query_data = requests.post(
        skydera_url,
        data=json.dumps(data),
        headers=headers,
        auth=(api_username, api_key),
    )

    print(query_data.json())


if __name__ == "__main__":
    main()
