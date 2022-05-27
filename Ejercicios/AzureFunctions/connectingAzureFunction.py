import requests 

def get_AzureFunction(name,url = 'https://<name_of_azure_function>.azurewebsites.net/api/HttpTrigger1', code=0):
    args = {
        'code': code,
        'name': name
    } if code else {} 
    

    response = requests.get(url, params=args)

    if response.status_code == 200:

        print(response.text)

    
if __name__ == '__main__':
    url = ''

    name_to_pass = input('Enter name:')

    get_AzureFunction(code='<code_of_azure_function>',name=name_to_pass)
