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
    api_key = os.environ["INPUT_SKYAPIKEY"]

    data = {
        'name': os.environ["INPUT_NAME"],
        'app_def_id': os.environ["INPUT_SKYAPPDEFID"],
        'namespace': os.environ["INPUT_SKYNAMESPACE"],
        'git_intg_access_id': os.environ["INPUT_SKYGITINTGACCESSID"],
        'git_repo_slug': os.environ["INPUT_SKYGITREPOSLUG"],


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

data = {'version': '2.0', 'routeKey': 'POST /infra/deploy/preview', 'rawPath': '/dev/infra/deploy/preview',
        'rawQueryString': '', 'headers': {'accept': 'application/json', 'accept-encoding': 'gzip, deflate',
                                          'authorization': 'Basic X190b2tlbl9fOnVkcmp3Zmt0amYycnFqenM4MDZuYXY0eW96bXpnY3lv',
                                          'content-length': '265', 'content-type': 'application/json',
                                          'host': 'skydera-dev-api.cloudstart.co',
                                          'user-agent': 'python-requests/2.27.1',
                                          'x-amzn-trace-id': 'Root=1-622d771f-1e33afaf0118bcbe6259ba26',
                                          'x-forwarded-for': '20.106.90.153', 'x-forwarded-port': '443',
                                          'x-forwarded-proto': 'https'},
        'requestContext': {'accountId': '974366620082', 'apiId': 'e5lhgjpuw2',
                           'domainName': 'skydera-dev-api.cloudstart.co', 'domainPrefix': 'skydera-dev-api',
                           'http': {'method': 'POST', 'path': '/dev/infra/deploy/preview', 'protocol': 'HTTP/1.1',
                                    'sourceIp': '20.106.90.153', 'userAgent': 'python-requests/2.27.1'},
                           'requestId': 'O5-M5h03CYcEPrQ=', 'routeKey': 'POST /infra/deploy/preview', 'stage': 'dev',
                           'time': '13/Mar/2022:04:46:23 +0000', 'timeEpoch': 1647146783152},
        'body': '',
        'isBase64Encoded': False}

data2 = {
    "my_input": "world hello hello hello",
    "github_base_ref": "main",
    "github_ref_path": "refs/pull/3/merge",
    "github_pull_request_number": "3",
    "github_actor": "lecole",
    "github_event_name": "pull_request",
    "github_head_ref": "preview",
    "gethub_repo_owner": "lecole"
}

data3 = {'version': '2.0', 'routeKey': 'POST /infra/deploy/preview', 'rawPath': '/dev/infra/deploy/preview',
         'rawQueryString': '', 'headers': {'accept': 'application/json', 'accept-encoding': 'gzip, deflate',
                                           'authorization': 'Basic X190b2tlbl9fOnVkcmp3Zmt0amYycnFqenM4MDZuYXY0eW96bXpnY3lv',
                                           'content-length': '271', 'content-type': 'application/json',
                                           'host': 'skydera-dev-api.cloudstart.co',
                                           'user-agent': 'python-requests/2.27.1',
                                           'x-amzn-trace-id': 'Root=1-622d78e0-1a6cc63727973d892578bb85',
                                           'x-forwarded-for': '20.106.90.123', 'x-forwarded-port': '443',
                                           'x-forwarded-proto': 'https'},
         'requestContext': {
             'accountId': '974366620082',
             'apiId': 'e5lhgjpuw2',
             'authorizer': {
                 'lambda': {
                     'account': 'da0tbtlojyizz8wolqgmitxwc6ez8i',
                     'company_id': 'olqgmitxwc6ez8i',
                     'is_active': True,
                     'pk': 'da0tbtlojyizz8wolqgmitxwc6ez8i:api_key',
                     'user_key': 'abf04ef1-9e0c-4077-805c-9f542e19b0a4'
                 }
             },
             'domainName': 'skydera-dev-api.cloudstart.co',
             'domainPrefix': 'skydera-dev-api',
             'http': {'method': 'POST', 'path': '/dev/infra/deploy/preview', 'protocol': 'HTTP/1.1',
                      'sourceIp': '20.106.90.123', 'userAgent': 'python-requests/2.27.1'},
             'requestId': 'O5_TCilUCYcEPXw=', 'routeKey': 'POST /infra/deploy/preview', 'stage': 'dev',
             'time': '13/Mar/2022:04:53:52 +0000', 'timeEpoch': 1647147232043},
         'body': '{"my_input": "world hello hello hello hello", "github_base_ref": "main", "github_ref_path": "refs/pull/3/merge", "github_pull_request_number": "3", "github_actor": "lecole", "github_event_name": "pull_request", "github_head_ref": "preview", "gethub_repo_owner": "lecole"}',
         'isBase64Encoded': False}

data4 = {'version': '2.0',
         'routeKey': 'POST /infra/deploy/preview',
         'rawPath': '/dev/infra/deploy/preview',
         'rawQueryString': '',
         'headers': {'accept': 'application/json', 'accept-encoding': 'gzip, deflate',
                     'authorization': 'Basic X190b2tlbl9fOnVkcmp3Zmt0amYycnFqenM4MDZuYXY0eW96bXpnY3lv',
                     'content-length': '310', 'content-type': 'application/json',
                     'host': 'skydera-dev-api.cloudstart.co',
                     'user-agent': 'python-requests/2.27.1',
                     'x-amzn-trace-id': 'Root=1-622d8efd-4e0acd7f08d085c32ce12de0',
                     'x-forwarded-for': '104.42.109.102', 'x-forwarded-port': '443',
                     'x-forwarded-proto': 'https'},
         'requestContext': {
             'accountId': '974366620082',
             'apiId': 'e5lhgjpuw2',
             'authorizer': {
                 'lambda': {
                     'account': 'da0tbtlojyizz8wolqgmitxwc6ez8i',
                     'company_id': 'olqgmitxwc6ez8i',
                     'is_active': True,
                     'pk': 'da0tbtlojyizz8wolqgmitxwc6ez8i:api_key',
                     'user_key': 'abf04ef1-9e0c-4077-805c-9f542e19b0a4'
                 }
             },
             'domainName': 'skydera-dev-api.cloudstart.co',
             'domainPrefix': 'skydera-dev-api',
             'http': {'method': 'POST', 'path': '/dev/infra/deploy/preview', 'protocol': 'HTTP/1.1',
                      'sourceIp': '104.42.109.102', 'userAgent': 'python-requests/2.27.1'},
             'requestId': 'O6NHlgoSiYcEPCw=', 'routeKey': 'POST /infra/deploy/preview', 'stage': 'dev',
             'time': '13/Mar/2022:06:28:13 +0000', 'timeEpoch': 1647152893139},
         'body': '',
         'isBase64Encoded': False}

data5 = {
    "my_input": "world hello hello hello hello hello",
    "deploy_name": "deploy-preview",
    "github_base_ref": "main",
    "github_ref_path": "refs/pull/3/merge",
    "github_pull_request_number": "3",
    "github_actor": "lecole",
    "github_event_name": "pull_request",
    "github_head_ref": "preview",
    "gethub_repo_owner": "lecole"
}
