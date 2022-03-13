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

    github_ref_path = os.environ["GITHUB_REF"]

    data = {
        'my_input': os.environ["INPUT_MYINPUT"],
        'github_base_ref': os.environ["GITHUB_BASE_REF"],
        'github_ref_path': os.environ["GITHUB_REF"],
        'github_pull_request_number': github_ref_path.split('/')[2],
        'github_actor': os.environ["GITHUB_ACTOR"],
        'github_event_name': os.environ["GITHUB_EVENT_NAME"],
        'github_head_ref': os.environ["GITHUB_HEAD_REF"],
        'gethub_repo_owner': os.environ["GITHUB_REPOSITORY_OWNER"],
    }

    # for k, v in sorted(os.environ.items()):
    #     print(k + ':', v)
    #     data[k] = v

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
