import os
import json
import requests


def main():
    # skydera_url = 'https://skydera-dev-api.cloudstart.co/infra/preview/deploy'
    skydera_url = 'https://api.skydera.com/infra/preview/deploy'

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    print('os.environ', os.environ)

    api_username = '__token__'
    api_key = os.environ["INPUT_SKYAPIKEY"]

    data = {
        'name': os.environ["INPUT_NAME"],
        'app_def_id': os.environ["INPUT_SKYAPPDEFID"],
        'namespace': os.environ["INPUT_SKYNAMESPACE"],
        'cert_id': os.environ["INPUT_SKYCERTID"],
        'git_intg_access_id': os.environ["INPUT_SKYGITINTGACCESSID"],
        'git_repo_slug': os.environ["INPUT_SKYGITREPOSLUG"],

        'gh_pr_number': os.environ["INPUT_PRNUMBER"],
        'gh_base_ref': os.environ["GITHUB_BASE_REF"],
        'gh_actor': os.environ["GITHUB_ACTOR"],
        'gh_event_name': os.environ["GITHUB_EVENT_NAME"],
        'gh_head_ref': os.environ["GITHUB_HEAD_REF"],
        'gh_repo': os.environ["GITHUB_REPOSITORY"],
        'gh_repo_owner': os.environ["GITHUB_REPOSITORY_OWNER"],
    }

    print('data', data)
    # for k, v in data.items():
    #     print(k, v)

    query_data = requests.post(
        skydera_url,
        data=json.dumps(data),
        headers=headers,
        auth=(api_username, api_key),
    )

    print(query_data.json())


if __name__ == "__main__":
    main()
