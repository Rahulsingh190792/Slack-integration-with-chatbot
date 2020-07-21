# # # from gensim.test.utils import datapath, get_tmpfile
# # # from gensim.models import KeyedVectors
# # # from gensim.scripts.glove2word2vec import glove2word2vec
# # # from DocSim import DocSim
# # #
# import os, xlsxwriter, pandas as pd,numpy as np
# # # glove_file = datapath('test_glove.txt')
# # # tmp_file = get_tmpfile("test_word2vec.txt")
# # # stopwords_path = "./data/stopwords_en.txt"
# # # _ = glove2word2vec(glove_file, tmp_file)
# # # import joblib
# # # model = KeyedVectors.load_word2vec_format(tmp_file)
# # #
# # # with open(stopwords_path, 'r') as fh:
# # #     stopwords = fh.read().split(",")
# # # ds1 = DocSim(model, stopwords=stopwords)
# # #
# # from slackclient import SlackClient
# # from slackeventsapi import SlackEventAdapter
# #
# # separator = "="
# # keys = {}
# # with open('property.config') as f:
# #     for line in f:
# #         if separator in line:
# #             # Find the name and value by splitting the string
# #             name, value = line.split(separator, 1)
# #             # Assign key value pair to dict
# #             # strip() removes white space from the ends of strings
# #             keys[name.strip()] = value.strip()
# # print(keys)
# # print(keys['slack_signing_secret'])
# # # Our app's Slack Event Adapter for receiving actions via the Events API
# # slack_signing_secret = keys['slack_signing_secret']
# # print(slack_signing_secret)
# # slack_events_adapter = SlackEventAdapter(slack_signing_secret, keys['slack_events_adapter_url_extension'])
# # print(keys['slack_events_adapter_url_extension'])
# # # Create a SlackClient for your bot to use for Web API requests
# # slack_bot_token = keys['slack_bot_token']
# # slack_client = SlackClient(slack_bot_token)
# #
# #
# # import requests
# # payload = {'token': 'xoxb-1037685824519-1028785981763-OKF297psbGniXHw0hVpSpRK3', 'user': 'U0111HP31PF'}
# # r = requests.get('https://slack.com/api/users.info', params=payload)
# # user_id = message.get('user')
# # sam = slack_client.api_call('users.info', user=user_id)
# # real_name = sam['user'].get('real_name')
# # print("real name of the user", real_name)
# #
# # sam = slack_client.api_call('users.info', user='U0111HP31PF')
# # print(sam['user'].get('real_name'))
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# # # joblib.dump(ds1, './data/test_model.pkl')
# # # import requests
# # # separator = "="
# # # keys = {}
# # # with open('property.config') as f:
# # #
# # #     for line in f:
# # #         if separator in line:
# # #             # Find the name and value by splitting the string
# # #             name, value = line.split(separator, 1)
# # #             # Assign key value pair to dict
# # #             # strip() removes white space from the ends of strings
# # #             keys[name.strip()] = value.strip()
# # # headers = {'Authorization': 'xoxb-1037685824519-1028785981763-OKF297psbGniXHw0hVpSpRK3', 'Content-Type': 'text/xml', 'charset': 'utf-8'}
# # # print(headers)
# # # files = {'file': ('./data/result.csv', open('./data/result.csv', 'rb')), 'initial_comment': (None, 'I am Iron Man'), 'channels': (None, 'C010NS3JT3L')}
# # # print(files)
# # # url = 'https://slack.com/api/files.upload'
# # # testing = requests.request("POST", url, headers=headers, files=files)
# # # print(testing)
# # # print("Status code: ", testing.status_code)
# #
# # # I named your file conf and stored it
# # # in the same directory as the script
# # #
# # # # with open('property.config') as f:
# # #
# # # with open('./data/result.csv', 'rb') as f:
# # #     headerss = {'Authorization': 'xoxb-1037685824519-1028785981763-OKF297psbGniXHw0hVpSpRK3', 'Content-Type': 'text/xml',
# # #                'charset': 'utf-8'}
# # #     filess = {'file': f}
# # #     r = requests.post(url, headers=headerss, files=filess)
# # #     print(r)
# # # #
# # # #     for line in f:
# # # #         if separator in line:
# # # import shlex, subprocess
# # # command_line = 'curl -F file=@"./data/result.pdf" -F channels=C010NS3JT3L -H "Authorization: Bearer xoxb-1037685824519-1028785981763-OKF297psbGniXHw0hVpSpRK3" https://slack.com/api/files.upload'
# # # args = shlex.split(command_line)
# # # subprocess.Popen(args)
# # # print(args)
# #
# # from datetime import date
# #
# # today = date.today()
# # print(today)
# # # dd/mm/YY
# # d1 = today.strftime("%d/%m/%Y")
# # print("d1 =", d1)
# #
# # # Textual month, day and year
# # d2 = today.strftime("%B %d, %Y")
# # print("d2 =", d2)
# #
# # # mm/dd/y
# # d3 = today.strftime("%m/%d/%y")
# # print("d3 =", d3)
# #
# # # Month abbreviation, day and year
# # d4 = today.strftime("%b-%d-%Y")
# # print("d4 =", d4)
# # #
# # #             # Find the name and value by splitting the string
# # #             name, value = line.split(separator, 1)
# # #
# # #             # Assign key value pair to dict
# # #             # strip() removes white space from the ends of strings
# # #             keys[name.strip()] = value.strip()
# # #
# # # print(keys['slack_signing_secret'])
# workbook = xlsxwriter.Workbook('./data/Tubclass_Report.xlsx')
# #Cell Formating to bold
# # bold = workbook.add_format({'bold': True, 'border': 1, 'text_wrap':1})
# # size = workbook.add_format({'font_size': 12, 'border': 1, 'text_wrap':1})
# # border = workbook.add_format({'border': 1, 'text_wrap':1,})
# # dtype_num = workbook.add_format({'border': 1,'num_format':'###'})
# # align_center = workbook.add_format({'align': 'center', 'border': 1, 'text_wrap':1})
# # white_cell = workbook.add_format({'bold': True, 'font_color': 'colour'})
# # #Merge Format For Merging cells
# # merge_format_header = workbook.add_format({'bold': 0,'border': 1,'align': 'center','valign': 'vcenter','fg_color': 'yellow', 'font_size': 18})
# # merge_format_date = workbook.add_format({'bold': 0,'border': 1,'valign': 'vcenter','font_size': 12})
# # from overall_report import date_filter, UWQS, QSR, QSRlog
# #
# # TSS = "17-04-2020"
# # TSE = "15-04-2020"
# #
# # date_filter(TSS, TSE)
# # UWQS(TSS, TSE)
# # QSR(TSS, TSE)
# # QSRlog(TSS, TSE)
# from slackclient import SlackClient
# from slackeventsapi import SlackEventAdapter
# separator = "="
# keys = {}
# with open('property.config') as f:
#     for line in f:
#         if separator in line:
#             # Find the name and value by splitting the string
#             name, value = line.split(separator, 1)
#             # Assign key value pair to dict
#             # strip() removes white space from the ends of strings
#             keys[name.strip()] = value.strip()
# print(keys)
# channel = "sam"
# user= "ramu"
# import threading
# slack_client=SlackClient(slack_bot_token)
# import logging.handlers
# sam=slack_client.api_call('users.info', user=user)
#     real_name=sam['user'].get('real_name')
#     channel=message["channel"]
#     print("channel source:", channel)
# if channel == keys['channel']:
#     if real_name == keys['app_name']:
#         print("app cannot send the data to input channel")
#     else:
#         x=threading.Thread(
#             target=some_processing,
#             args=(username, event_ts, real_name,)
#         )
#         x.start()
#
# elif channel == keys['channel_report']:
#     if real_name == keys['app_name']:
#         print("app cannot send the data to report channel")
#         # sys.exit()
#     elif '@report' in username:
#         x=threading.Thread(
#             target=todays_report,
#             args=(event_ts, keys, real_name,)
#         )
#         x.start()
#     else:
#         slack_client.api_call("chat.postMessage", channel=keys['channel_report'],
#                               text='This message is not supported in this channel, it should be used only for generating report.')
#         logger.warning(
#             'This message is outside the scope of this Channel!. Please contact the system administrator of this application')  # will print a message to the console
# else:
#     print("not a valid channel")# print(args)