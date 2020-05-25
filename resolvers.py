import requests
# import requests.auth 

def resolve_apigithub_search_user(_, info, _username):
    response = requests.get('https://api.github.com/users/{}' .format(_username))
    try: 
        resolve = response.json()['html_url']
        return resolve
    except Exception as e:
        return "Usuario não encontrado"
    

def resolve_apigithub_list_repos(_, info, _username):
    response = requests.get('https://api.github.com/users/{}/repos' .format(_username))
    name_repos = []
    try:
        for repositorio in response.json():
            if repositorio['private'] == False:
                name_repos.append(repositorio['name'])
        return name_repos
    except Exception as e:
        name_repos.append('Não encontrado')
        return name_repos

def resolve_apigithub_repos_info(_, info, _username, _repos):
    response = requests.get('https://api.github.com/users/{}/repos' .format(_username))
    try:
        for repositorio in response.json():
            list_options = repositorio.keys()
            return list_options
    except Exception as e:
        return "repositório não encontrado"

def resolve_apigithub_repos_info_options(_, info, _username, _repos, _options):
    response = requests.get('https://api.github.com/users/{}/repos' .format(_username))
    try:
        for repositorio in response.json():
            if repositorio['name'] == _repos:
                repos_options = repositorio[_options]
                return repos_options
    except Exception as e:
        print(e)
        return "options não encontrada"