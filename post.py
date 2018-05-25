#-*- coding:utf-8 -*-

import requests
import json

############################################################
#SlackでWebhookAPIを作って、表示されたURLを記入して下さい
API_URL = 'https://hooks.slack.com/services/ランダム文字列'

############################################################



def post(postText):
    print(API_URL)
    print(postText)
    requests.post(API_URL, data = json.dumps({
        'text': postText
    }))


if __name__ == '__main__':
    import sys
    post(sys.argv[1])
