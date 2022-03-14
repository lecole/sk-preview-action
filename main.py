import os
import json
import requests


def main():
    skydera_url = 'https://skydera-dev-api.cloudstart.co/infra/preview/deploy'

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    api_username = '__token__'
    api_key = os.environ["INPUT_SKYAPIKEY"]

    data = {
        'name': os.environ["INPUT_NAME"],
        'app_def_id': os.environ["INPUT_SKYAPPDEFID"],
        'namespace': os.environ["INPUT_SKYNAMESPACE"],
        'git_intg_access_id': os.environ["INPUT_SKYGITINTGACCESSID"],
        'git_repo_slug': os.environ["INPUT_SKYGITREPOSLUG"],
        'gh_pr_number': os.environ["INPUT_PRNUMBER"],


        'github_base_ref': os.environ["GITHUB_BASE_REF"],
        'github_pull_request_number': os.environ["GITHUB_REF"].split('/')[2],
        'github_actor': os.environ["GITHUB_ACTOR"],
        'github_event_name': os.environ["GITHUB_EVENT_NAME"],
        'github_head_ref': os.environ["GITHUB_HEAD_REF"],
        'gethub_repo_owner': os.environ["GITHUB_REPOSITORY_OWNER"],
    }

    query_data = requests.post(
        skydera_url,
        data=json.dumps(data),
        headers=headers,
        auth=(api_username, api_key),
    )

    print(query_data.json())


if __name__ == "__main__":
    main()
