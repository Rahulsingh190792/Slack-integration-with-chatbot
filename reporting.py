import shlex
import pandas as pd
import subprocess
import requests
from reportlab.pdfgen import canvas
from expiry_testing import program_expired
import logging

# create logger
logger = logging.getLogger('basic_report')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

def generateReport(event_ts, keys):
    program_expired(event_ts)
    logger.info('event triggered')
    directory = "./data/"
    csv_name = "result.csv"
    csvpath = directory + csv_name
    csv = pd.read_csv(csvpath)
    # Querry Classification Summary Report
    Querry_Classification_Summary_Report = keys['report_header']
    # COunting Total No. of Querries
    total_querry_count = csv.count()
    total_querry_count = str(total_querry_count[0])
    all_product_count = csv["Category"].value_counts().rename_axis('products').reset_index(name='counts')
    total_products = all_product_count.count()
    total_products = total_products[0]
    indent = 100
    indent_next = 250
    pdf_name = "result.pdf"
    pdfpath = directory + pdf_name
    c = canvas.Canvas(pdfpath)
    c.drawString(indent, 800, Querry_Classification_Summary_Report)
    c.drawString(indent, 750, "Total No. Of querries = ")
    c.drawString(indent_next, 750, total_querry_count)
    c.drawString(indent, 725, "Product")
    c.drawString(indent_next, 725, "Count")
    height = 700
    for i in range(total_products):
        c.drawString(indent, height, str(all_product_count["products"][i]))
        c.drawString(indent_next, height, str(all_product_count["counts"][i]))
        height = height - 25
    c.save()
    logger.info('pdf generated')
    cha = keys['channel_report']
    chai = keys['slack_bot_token']
    chaii = 'Please find the report attached'
    try:
        command_line = 'curl -F file=@"./data/result.pdf" -F "initial_comment=%s" -F channels=%s -H "Authorization: Bearer %s" https://slack.com/api/files.upload --ssl-no-revoke' % (
        chaii, cha, chai)
        args = shlex.split(command_line)
        subprocess.Popen(args)
        logger.info('pdf uploaded')
    except (
    AssertionError, AttributeError, EOFError, FloatingPointError, GeneratorExit, ImportError, IndexError, KeyError,
    KeyboardInterrupt, MemoryError, NameError, NotImplementedError, OSError, OverflowError, ReferenceError,
    RuntimeError, StopIteration, SyntaxError, IndentationError, TabError, SystemError, SystemExit, TypeError,
    UnboundLocalError, UnicodeError, UnicodeEncodeError, UnicodeDecodeError, UnicodeTranslateError, ValueError,
    ZeroDivisionError):
        logger.info('pdf uploaded method two')
        headers = {
            'Authorization': keys['slack_bot_token']
        }
        print(headers)
        files = {
            'file': ('C:\\Users\\z003ww7c.AD001\\PycharmProjects\\SlackIntegration\\data\\result.csv',
                     open('C:\\Users\\z003ww7c.AD001\\PycharmProjects\\SlackIntegration\\data\\result.csv', 'rb')),
            'initial_comment': 'Please find the report attached',
            'channels': keys['channel'],
        }
        url = 'https://slack.com/api/files.upload'
        requests.post(url, headers=headers, files=files)
