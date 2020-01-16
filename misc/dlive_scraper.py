from time import sleep
import requests
import traceback
import re



END_POINT = "https://graphigo.prd.dlive.tv/"



def match_valid_user(text):

    if re.match('^[0-9A-Za-z_]+$', text):
        return text

    is_valid_url = re.search('https?\:\/\/.*\/([0-9A-Za-z_]+).*', text)
    if is_valid_url:
        return is_valid_url.group(1)

    remove_invalid = ""
    for char in text:
        if not re.match('[0-9A-Za-z_]', char):
            return False

    return False



def batch_queries(users, batch_size=8):
    output = ""
    queries = []
    ticker = 0
    num_users = len(users)

    for user in users:

        ticker += 1
        num_users -= 1
        output += f'{user}: userByDisplayName(displayname:"{user}")' + '''
        {
            id
            username
            displayname
            avatar
            offlineImage
            partnerStatus
            banStatus
            deactivated
            livestream {
                permlink
                title
                thumbnailUrl
                createdAt
                watchingCount
                view
                id
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
        '''
        if ticker == batch_size or num_users == 0:
            queries.append({'query': 'query{' + output + '}'})
            output = ""
            ticker = 0

    return queries



def parse_user(data):

    output = {}

    try:
        for chan in data['data']:

            data_user = data['data'][chan]

            if not data_user:
                continue

            data_live = data_user.get('livestream') if data_user.get('livestream') else {}

            platform = 'DLIVE'
            username = data_user.get('displayname')
            image_avatar = data_user.get('avatar')
            image_offline = data_user.get('offlineImage')
            partner = data_user.get('partnerStatus')
            num_followers = data_user.get('followers', {}).get('totalCount', 0)
            # is_banned: NO_BAN, BAN_FROM_STREAMING, ACCOUNT_SUSPENDED
            is_banned = False if data_user.get('banStatus') == "NO_BAN" else  data_user.get('banStatus')
            is_deactivated = data_user.get('deactivated')
            is_hosting = True if data_user.get('hostingLivestream') else False
            live = True if data_live else False
            live_id = data_live.get('id')
            live_title = data_live.get('title')
            live_viewers = data_live.get('watchingCount', 0)

            chan_formatted_data = {
                    username: {
                            'ch_platform': platform,
                            'ch_info_id': username,
                            'ch_info_name': username,
                            'ch_media_avatar': image_avatar,
                            'ch_media_offline': image_offline,
                            'ch_info_deactivated': is_deactivated,
                            'ch_info_banned': is_banned,
                            'ch_info_partner': partner,
                            'ch_info_num_broadcasts': 0,
                            'ch_info_num_videos': 0,
                            'ch_info_following': 0,
                            'ch_info_followers': num_followers,
                            'ch_live': live,
                            'ch_live_id': live_id,
                            'ch_live_title': live_title,
                            'ch_live_viewers': live_viewers,
                            'ch_live_hosting': is_hosting,
                        }
                    }
            output.update(chan_formatted_data)

    except Exception as e:
        print(traceback.format_exc())
        return False

    return output



def dlive_request(users, batch_size=8):
    """
        dlive_request(users=['user1', 'user2', 'user3'])

    :users: list|str
        Example:
            users = ['user1', 'user2', 'user3']
            or
            users = 'user1'

    :returns dict
        Example:
            {
                'user1': {...},
                'user2': {...}
            }
    """

    if isinstance(users, str):
        users = [users]

    dlive_users = {}

    # Only query valid usernames
    for u in users:
        valid_user = match_valid_user(u)
        if valid_user:
            dlive_users[valid_user] = {}

    query_batches = batch_queries(dlive_users.keys(), batch_size=batch_size)

    session = requests.session()

    for batch in query_batches:

        retries = 5
        dlive_user = {}

        while True:
            try:
                retries -= 1
                json_response = session.post(END_POINT, json=batch).json()
                dlive_user = parse_user(json_response)
            except Exception as e:
                print(e)
                if retries == 0:
                    break
                sleep(5)
                continue
            break

        if not dlive_user:
            continue

        dlive_users.update(dlive_user)
    return dlive_users



if __name__ == "__main__":
    from pprint import pprint as pp

    pp( dlive_request('hawkshredder42') )
    pp( dlive_request('https://dlive.tv/hawkshredder42') )
    pp( dlive_request(['https://dlive.tv/hawkshredder42', 'JuAsJaEn', 'ericwilson', 'MG_Live', 'RCG_WESKER', 'JiamitdemWesen', 'Millenay', 'RushkaGG', 'eaeNiko', 'MCJams', 'twiggy5000', 'Miroloji', 'Luthien', 'katzeMLBB', 'youlost']) )
