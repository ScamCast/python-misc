import requests
from time import sleep
from pprint import pprint as pp
END_POINT = "https://graphigo.prd.dlive.tv/"
dlive_users = {}

def query_user(user):
    output = '''query{
    userByDisplayName(displayname:"''' + user + '''") {
        id
        username
        displayname
        avatar
        partnerStatus
        livestream {
            permlink
            title
            thumbnailUrl
            createdAt
            watchingCount
            view
        }
        hostingLivestream {
            creator {
                id
            }
        }
        followers {
            totalCount
        }
    }
}'''
    return {'query': output}


def parse_user(data):



    ######## NOTES: Values are returning NONE, need to set values before 'try'
    try:
        user = data['data']['userByDisplayName']
        username = user.get('displayname')
        output = {
                username: {
                        'ch_platform': 'DLIVE',
                        'ch_info_id': username,
                        'ch_info_name': username,
                        'ch_media_avatar': user.get('avatar'),
                        # 'ch_media_offline': None,
                        # 'ch_info_deactivated': False,
                        # 'ch_info_banned': False,
                        'ch_info_partner': user.get('partnerStatus'),
                        # 'ch_info_num_broadcasts': 0,
                        # 'ch_info_num_videos': 0,
                        # 'ch_info_following': 0,
                        'ch_info_followers': user.get('followers', {}).get('totalCount', 0),
                        'ch_live': True if user.get('livestream') else False,
                        'ch_live_title': user.get('livestream', {}).get('title'),
                        'ch_live_viewers': user.get('livestream', {}).get('watchingCount', 0),
                        'ch_live_hosting': True if user.get('hostingLivestream') else False,
                    }
                }
    except Exception as e:
        print(e)
        return False
    return output


def dlive_request(users):
    global dlive_users
    if isinstance(users, str):
        users = [users]

    session = requests.session()
    retries = 3

    for user in users:
        dlive_user = {}
        while True:
            try:
                retries -= 1
                response = session.post(END_POINT, json=query_user(user)).json()
                pp(response)
                dlive_user = parse_user(response)
            except Exception as e:
                print(e)
                if retries == 0:
                    return False
                sleep(5)
                continue
            break
        if not dlive_user:
            dlive_users.update({user: {}})
            continue
        dlive_users.update(dlive_user)
    return dlive_users


pp(dlive_request(['Grimoire', 'hawkshredder42', 'JuAsJaEn']))
