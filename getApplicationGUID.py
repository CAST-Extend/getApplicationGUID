import json
from argparse import ArgumentParser
import requests

def get_application_guid(console_url, console_api_key, app_name):
    url=f"{console_url}api/applications"
    headers = {
        "x-api-key": console_api_key
    }

    try:
        #fetching the Application list and details.
        rsp = requests.get(url, headers=headers)
        # print(rsp.status_code)
        if rsp.status_code == 200:
            apps = json.loads(rsp.text) 
            for app in apps['applications']:
                if app["name"] == app_name:
                    return app["guid"] 
            print(f'{app_name} application not present in AIP Console')

        else:
            print("Some error has occured! While retriving ApplicationGUID...")
            # print(rsp.text)

    except Exception as e:
        print('some exception has occured! \n Please resolve them or contact developers')
        print(e)




if __name__ == "__main__":

    parser = ArgumentParser()
 
    parser.add_argument('-app_name','--app_name',required=True,help='Application Name')
    parser.add_argument('-console_url', '--console_url', required=True, help='AIP Console URL')
    parser.add_argument('-console_api_key', '--console_api_key', required=True, help='AIP Console API KEY')

    args=parser.parse_args()

    if not args.console_url.endswith('/'):
        args.console_url = args.console_url + '/'

    print(f'Getting the Application GUID for the Application -> {args.app_name}.............')

    guid = get_application_guid(args.console_url, args.console_api_key, args.app_name)
    
    name = 'ApplicationGUID'    
    # set variable
    print(f'##vso[task.setvariable variable={name};]{guid}')
