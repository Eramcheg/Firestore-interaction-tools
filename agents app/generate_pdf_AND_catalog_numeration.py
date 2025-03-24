# import concurrent
# import csv
# from reportlab.lib import colors
# import ast
# import random
# from datetime import datetime
# from random import randint
# from reportlab.platypus import Image
# import concurrent.futures
# import os
# import json
# import firebase_admin
# import os
# import json
# import time
# import logging
# import tempfile
# from datetime import datetime, timedelta
# from subprocess import run
# from io import BytesIO, StringIO
# import urllib.request
# import ftplib
#
# # Third-party imports
#
# import firebase_admin
# from firebase_admin import credentials, firestore
# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import A4
# from reportlab.lib.units import inch, cm
# from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
# from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
# orders = [{"order-id": 40576720, "description": "Ring Joker STE GP", "quantity": 1, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/NewImages/41219GL.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/NewImages/41219GL.jpg", "price": 12.6, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "41219GL"}, {"order-id": 40576720, "description": "FussNecklace Love STE GP CZ CRY", "quantity": 4, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/39104G.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/39104G.jpg", "price": 11.6, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "39104G"}, {"order-id": 40576720, "description": "Pendant Unique GP CRY", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/NewImages/12428G.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/NewImages/12428G.jpg", "price": 22.4, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "12428G"}, {"order-id": 40576720, "description": "Orrechini Crab GP CRY RED", "quantity": 1, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/NewImages/23172G.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/NewImages/23172G.jpg", "price": 16.3, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "23172G"}, {"order-id": 40576720, "description": "Ring Distinct 925AG CZ RH L/XL", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/63251LXL.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/63251LXL.jpg", "price": 17.7, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "63251LXL"}, {"order-id": 40576720, "description": "Earrings Twice RH CRY", "quantity": 4, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/NewImages/22572R.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/NewImages/22572R.jpg", "price": 9.9, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "22572R"}, {"order-id": 40576720, "description": "Ring Character STE GP L", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/41198GL.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/41198GL.jpg", "price": 10.5, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "41198GL"}, {"order-id": 40576720, "description": "Ring Links STE L/XL", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/41161LXL.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/41161LXL.jpg", "price": 8.2, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "41161LXL"}, {"order-id": 40576720, "description": "Pendant Pace 925 AG CZ RH CRY", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/61141.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/61141.jpg", "price": 19.7, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "61141"}, {"order-id": 40576720, "description": "Ring Real GP CRY M", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/41036GM.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/41036GM.jpg", "price": 13.3, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "41036GM"}, {"order-id": 40576720, "description": "Earrings 004 cal.", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/21004.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/21004.jpg", "price": 6.5, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "21004"}, {"order-id": 40576720, "description": "Earrings Dual RH CRY", "quantity": 4, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/22417R.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/22417R.jpg", "price": 15.0, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "22417R"}, {"order-id": 40576720, "description": "Earrings Twisty STE", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/23035.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/23035.jpg", "price": 13.3, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "23035"}, {"order-id": 40576720, "description": "Bracelet Tane STE CZ", "quantity": 4, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/32332.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/32332.jpg", "price": 14.3, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "32332"}, {"order-id": 40576720, "description": "Ring Solitaire GP CRY M", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/41001M.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/41001M.jpg", "price": 13.9, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "41001M"}, {"order-id": 40576720, "description": "Earrings Sense RH CZ", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/22982R.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/22982R.jpg", "price": 10.5, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "22982R"}, {"order-id": 40576720, "description": "Earrings Double klein RH CRY", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/22156R.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/22156R.jpg", "price": 18.4, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "22156R"}, {"order-id": 40576720, "description": "Necklace Rings 3-tone CRY", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/11062.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/11062.jpg", "price": 21.1, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "11062"}, {"order-id": 40576720, "description": "Pendant Just RH CRY", "quantity": 4, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/11685R.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/11685R.jpg", "price": 12.9, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "11685R"}, {"order-id": 40576720, "description": "Bangle Choice GP CRY", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/32008G.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/32008G.jpg", "price": 29.9, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "32008G"}, {"order-id": 40576720, "description": "Necklace Volition STE RG Pearl", "quantity": 4, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12400RG.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12400RG.jpg", "price": 11.9, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "12400RG"}, {"order-id": 40576720, "description": "Pendant Lucina STE CRY", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12287.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12287.jpg", "price": 11.9, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "12287"}, {"order-id": 40576720, "description": "Bracelet Love STE RG CRY", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/32224RG.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/32224RG.jpg", "price": 12.9, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "32224RG"}, {"order-id": 40576720, "description": "Necklace You STE RG CRY", "quantity": 1, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12292RG.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12292RG.jpg", "price": 16.0, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "12292RG"}, {"order-id": 40576720, "description": "Bangle Local RH CRY", "quantity": 4, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/32164R.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/32164R.jpg", "price": 19.0, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "32164R"}, {"order-id": 40576720, "description": "Ring Distinct 925AG CZ RH S/M", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/63251SM.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/63251SM.jpg", "price": 17.7, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "63251SM"}, {"order-id": 40576720, "description": "FussNecklace Butterfly STE CZ CRY", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/39102.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/39102.jpg", "price": 9.9, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "39102"}, {"order-id": 40576720, "description": "Bracelet Change STE CRY", "quantity": 4, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/32316.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/32316.jpg", "price": 9.2, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "32316"}, {"order-id": 40576720, "description": "Pendant Open STE CZ WHI", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/11861.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/11861.jpg", "price": 12.2, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "11861"}, {"order-id": 40576720, "description": "Ring Ariel GP CZ", "quantity": 4, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/41215G.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/41215G.jpg", "price": 5.4, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "41215G"}, {"order-id": 40576720, "description": "Earrings Soriso STE GP", "quantity": 1, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/23069G.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/23069G.jpg", "price": 12.6, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "23069G"}, {"order-id": 40576720, "description": "Ring Fortune 925AG CZ RH White", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/63288M.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/63288M.jpg", "price": 21.1, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "63288M"}, {"order-id": 40576720, "description": "Collier Viridios STE CZ", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12305.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12305.jpg", "price": 13.3, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "12305"}, {"order-id": 40576720, "description": "Collier Entitlement STE GP Pearl", "quantity": 4, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12378G.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12378G.jpg", "price": 9.9, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "12378G"}, {"order-id": 40576720, "description": "Pendant Moon STE", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/11945.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/11945.jpg", "price": 14.6, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "11945"}, {"order-id": 40576720, "description": "Pendant Pik STE GP CRY green", "quantity": 1, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/NewImages/12427G%20GRE.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/NewImages/12427G%20GRE.jpg", "price": 13.3, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "12427G GRE"}, {"order-id": 40576720, "description": "Necklace Accept STE GP CRY", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12240G.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12240G.jpg", "price": 14.6, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "12240G"}, {"order-id": 40576720, "description": "Bracelet Hearty RH CRY", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/32089.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/32089.jpg", "price": 15.0, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "32089"}, {"order-id": 40576720, "description": "Ring Austras 925AG CZ RH White", "quantity": 1, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/63289L.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/63289L.jpg", "price": 22.4, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "63289L"}, {"order-id": 40576720, "description": "Pendant Under FS STE RG CZ WHI", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12195RG.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12195RG.jpg", "price": 17.7, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "12195RG"}, {"order-id": 40576720, "description": "Bracelet Pleasure STE GP", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/32402G.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/32402G.jpg", "price": 9.9, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "32402G"}, {"order-id": 40576720, "description": "Pendant Heely RG silver night", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12044RG.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12044RG.jpg", "price": 27.5, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "12044RG"}, {"order-id": 40576720, "description": "Necklace Felicity 925AG RH  CZ", "quantity": 1, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/NewImages/61270%20WHI.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/NewImages/61270%20WHI.jpg", "price": 19.0, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "61270 WHI"}, {"order-id": 40576720, "description": "Pendant Trust RH CRY", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/11273.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/11273.jpg", "price": 17.3, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "11273"}, {"order-id": 40576720, "description": "Ring Private RH CRY M", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/41134M.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/41134M.jpg", "price": 15.6, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "41134M"}, {"order-id": 40576720, "description": "Pendant Class GP CRY", "quantity": 4, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/11548G.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/11548G.jpg", "price": 15.0, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "11548G"}, {"order-id": 40576720, "description": "Necklace Fond RG CRY", "quantity": 4, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/11615RG.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/11615RG.jpg", "price": 16.3, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "11615RG"}, {"order-id": 40576720, "description": "Earrings 036 CAL.", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/21013.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/21013.jpg", "price": 5.8, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "21013"}, {"order-id": 40576720, "description": "Pendant Favour RH CRY", "quantity": 4, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/11534.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/11534.jpg", "price": 9.9, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "11534"}, {"order-id": 40576720, "description": "Earrings Levity GP", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/23128G.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/23128G.jpg", "price": 17.7, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "23128G"}, {"order-id": 40576720, "description": "Earrings Sense GP CZ", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/22982G.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/22982G.jpg", "price": 10.9, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "22982G"}, {"order-id": 40576720, "description": "Ohrring Sound STE GP CZ WHI", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/22965G.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/22965G.jpg", "price": 13.3, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "22965G"}, {"order-id": 40576720, "description": "Earrings Ladybug mini RH CRY", "quantity": 4, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/22186.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/22186.jpg", "price": 10.5, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "22186"}, {"order-id": 40576720, "description": "Necklace TwoCats FS CZ RG WHI", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12194RG.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12194RG.jpg", "price": 14.6, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "12194RG"}, {"order-id": 40576720, "description": "Pendant Safe 925AG RH CRY", "quantity": 1, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/61060%20001.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/61060%20001.jpg", "price": 17.3, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "61060 001"}, {"order-id": 40576720, "description": "Bangle Base RH CRY", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/32163R.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/32163R.jpg", "price": 22.1, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "32163R"}, {"order-id": 40576720, "description": "Earrings Diamond GP CRY", "quantity": 4, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/22066G.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/22066G.jpg", "price": 7.8, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "22066G"}, {"order-id": 40576720, "description": "Collier Tane STE CZ", "quantity": 4, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12277.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12277.jpg", "price": 19.7, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "12277"}, {"order-id": 40576720, "description": "Necklace Change STE RG CRY", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12254RG.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12254RG.jpg", "price": 11.2, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "12254RG"}, {"order-id": 40576720, "description": "Earrings Pik STE GP CRY gre", "quantity": 1, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/NewImages/23148G%20GRE.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/NewImages/23148G%20GRE.jpg", "price": 13.3, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "23148G GRE"}, {"order-id": 40576720, "description": "Ring Links STE GP S/M", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/41162SM.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/41162SM.jpg", "price": 8.2, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "41162SM"}, {"order-id": 40576720, "description": "Pendant Mummy 925AG RH CZ", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/61265.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/61265.jpg", "price": 33.7, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "61265"}, {"order-id": 40576720, "description": "Ring Horizon GP CRY L", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/41004L.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/41004L.jpg", "price": 13.9, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "41004L"}, {"order-id": 40576720, "description": "Pendant Pearl simple RH CRY", "quantity": 4, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12066.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12066.jpg", "price": 12.2, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "12066"}, {"order-id": 40576720, "description": "Ring Pearly RH CRY L", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/41051L.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/41051L.jpg", "price": 15.3, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "41051L"}, {"order-id": 40576720, "description": "Earrings Just RH CRY", "quantity": 6, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/22604R.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/22604R.jpg", "price": 9.9, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "22604R"}, {"order-id": 40576720, "description": "Pendant Pursue STE CZ GP", "quantity": 4, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12402G.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12402G.jpg", "price": 12.9, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "12402G"}, {"order-id": 40576720, "description": "Pendant Corazina RG light silk", "quantity": 6, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/11982RG%20261.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/11982RG%20261.jpg", "price": 9.2, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "11982RG 261"}, {"order-id": 40576720, "description": "Earrings Excuse STE RG Pearl RG", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/23130RG.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/23130RG.jpg", "price": 9.2, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "23130RG"}, {"order-id": 40576720, "description": "Ring Rapunzel GP CZ", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/41214G.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/41214G.jpg", "price": 6.5, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "41214G"}, {"order-id": 40576720, "description": "Pendant Upside RH CRY", "quantity": 4, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12077.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12077.jpg", "price": 18.4, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "12077"}, {"order-id": 40576720, "description": "Earrings Chance RH CRY", "quantity": 1, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/NewImages/23145.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/NewImages/23145.jpg", "price": 23.5, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "23145"}, {"order-id": 40576720, "description": "Pendant Uno RH emerald", "quantity": 4, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/11740%20205.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/11740%20205.jpg", "price": 10.5, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "11740 205"}, {"order-id": 40576720, "description": "Earrings Horae STE CZ", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/23046.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/23046.jpg", "price": 9.9, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "23046"}, {"order-id": 40576720, "description": "Pendant Aloha RH CRY", "quantity": 4, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/11318.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/11318.jpg", "price": 18.4, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "11318"}, {"order-id": 40576720, "description": "Ohrring Sound STE CZ WHI", "quantity": 1, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/22965.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/22965.jpg", "price": 13.3, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "22965"}, {"order-id": 40576720, "description": "Pendant Estar  STE RG CZ WHI", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12069RG.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12069RG.jpg", "price": 11.9, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "12069RG"}, {"order-id": 40576720, "description": "Bangle Serial RH CRY", "quantity": 3, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/32165R.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/32165R.jpg", "price": 18.7, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "32165R"}, {"order-id": 40576720, "description": "Ring Links STE GP L/XL", "quantity": 1, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/41162LXL.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/41162LXL.jpg", "price": 8.2, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "41162LXL"}, {"order-id": 40576720, "description": "Collier Idea STE GP CZ", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12406G.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12406G.jpg", "price": 11.9, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "12406G"}, {"order-id": 40576720, "description": "Pendant Giant GP silver night", "quantity": 4, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/11512G.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/11512G.jpg", "price": 18.7, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "11512G"}, {"order-id": 40576720, "description": "Ring Private RH CRY L", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/41134L.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/41134L.jpg", "price": 15.6, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "41134L"}, {"order-id": 40576720, "description": "Pendant Point Pearl RH CRY", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12160.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12160.jpg", "price": 15.0, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "12160"}, {"order-id": 40576720, "description": "Pendant Cornetto RH Siam", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12145.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12145.jpg", "price": 17.3, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "12145"}, {"order-id": 40576720, "description": "Ring Austras 925AG CZ RH White", "quantity": 1, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/63289M.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/63289M.jpg", "price": 22.4, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "63289M"}, {"order-id": 40576720, "description": "Pendant ZigZag STE RG CRY", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12319RG.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12319RG.jpg", "price": 12.6, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "12319RG"}, {"order-id": 40576720, "description": "Earrings Belief STE GP CRY green", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/NewImages/23163G%20GRE.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/NewImages/23163G%20GRE.jpg", "price": 13.3, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "23163G GRE"}, {"order-id": 40576720, "description": "Bracelet Gracious STE GP CRY white", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/NewImages/32413G%20WHI.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/NewImages/32413G%20WHI.jpg", "price": 7.8, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "32413G WHI"}, {"order-id": 40576720, "description": "Bracelet Connected STE RG CZ", "quantity": 4, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/32296RG.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/32296RG.jpg", "price": 12.9, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "32296RG"}, {"order-id": 40576720, "description": "Earrings Lucent creme RH CRY", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/22559%20CRE.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/22559%20CRE.jpg", "price": 15.0, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "22559 CRE"}, {"order-id": 40576720, "description": "Necklace Arista STE", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12320.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12320.jpg", "price": 12.9, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "12320"}, {"order-id": 40576720, "description": "Earrings Suadela STE RG CZ", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/23089RG.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/23089RG.jpg", "price": 8.8, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "23089RG"}, {"order-id": 40576720, "description": "Ring Horizon GP CRY M", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/41004M.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/41004M.jpg", "price": 13.9, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "41004M"}, {"order-id": 40576720, "description": "Ohrklemme Create GP CRY one piece", "quantity": 4, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/22937G.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/22937G.jpg", "price": 9.2, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "22937G"}, {"order-id": 40576720, "description": "Earrings Doggy RH CRY", "quantity": 4, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/22699.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/22699.jpg", "price": 10.9, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "22699"}, {"order-id": 40576720, "description": "Ring Solitaire GP CRY L", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/41001L.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/41001L.jpg", "price": 13.9, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "41001L"}, {"order-id": 40576720, "description": "Earrings Flower pearl RH CRY", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/22774.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/22774.jpg", "price": 10.5, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "22774"}, {"order-id": 40576720, "description": "Ring Eternita 925AG CZ RH White", "quantity": 1, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/63290M.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/63290M.jpg", "price": 28.6, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "63290M"}, {"order-id": 40576720, "description": "FussNecklace Love STE CZ CRY", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/39104.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/39104.jpg", "price": 9.9, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "39104"}, {"order-id": 40576720, "description": "Necklace Diamond RH CRY", "quantity": 4, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/11025R.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/11025R.jpg", "price": 10.9, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "11025R"}, {"order-id": 40576720, "description": "Earrings Volition STE GP Pearl", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/23105G.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/23105G.jpg", "price": 9.5, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "23105G"}, {"order-id": 40576720, "description": "Ring Caroline 925AG GP CZ L", "quantity": 1, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/NewImages/63340GL%20WHI.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/NewImages/63340GL%20WHI.jpg", "price": 19.4, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "63340GL WHI"}, {"order-id": 40576720, "description": "Necklace Keylove STE RG CRY", "quantity": 4, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12171RG.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12171RG.jpg", "price": 8.2, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "12171RG"}, {"order-id": 40576720, "description": "Necklace Aranyani STE GP pearl", "quantity": 4, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12314G.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12314G.jpg", "price": 12.9, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "12314G"}, {"order-id": 40576720, "description": "Bracelet Gracious STE GP CRY green", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/NewImages/32413G%20GRE.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/NewImages/32413G%20GRE.jpg", "price": 7.8, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "32413G GRE"}, {"order-id": 40576720, "description": "Earrings Utopia GP CRY", "quantity": 1, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/23096G.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/23096G.jpg", "price": 17.7, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "23096G"}, {"order-id": 40576720, "description": "Necklace Keylove STE CRY (a)", "quantity": 6, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12171.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12171.jpg", "price": 8.2, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "12171"}, {"order-id": 40576720, "description": "Pendant Flower Pearl RH CRY", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/11947.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/11947.jpg", "price": 12.9, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "11947"}, {"order-id": 40576720, "description": "Pendant Ladybug mini RH CRY", "quantity": 6, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/11182.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/11182.jpg", "price": 11.6, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "11182"}, {"order-id": 40576720, "description": "Ring Links STE S/M", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/41161SM.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/41161SM.jpg", "price": 8.2, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "41161SM"}, {"order-id": 40576720, "description": "Ring Joker STE GP", "quantity": 1, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/NewImages/41219GM.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/NewImages/41219GM.jpg", "price": 12.6, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "41219GM"}, {"order-id": 40576720, "description": "Necklace Accept STE CRY", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12240.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12240.jpg", "price": 14.6, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "12240"}, {"order-id": 40576720, "description": "Necklace River RH pearl", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12248.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12248.jpg", "price": 19.0, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "12248"}, {"order-id": 40576720, "description": "Pendant Uno RHamethyst", "quantity": 4, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/11740%20204.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/11740%20204.jpg", "price": 10.5, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "11740 204"}, {"order-id": 40576720, "description": "Earrings Belief STE GP CRY white", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/NewImages/23163G%20WHI.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/NewImages/23163G%20WHI.jpg", "price": 13.3, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "23163G WHI"}, {"order-id": 40576720, "description": "Bangle Plain STE CZ", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/32222.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/32222.jpg", "price": 27.5, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "32222"}, {"order-id": 40576720, "description": "Bracelet Loco RH CRY (a)", "quantity": 1, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/32252R%20001.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/32252R%20001.jpg", "price": 25.8, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "32252R 001"}, {"order-id": 40576720, "description": "Pendant Cat RH CRY", "quantity": 6, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/11362.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/11362.jpg", "price": 12.2, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "11362"}, {"order-id": 40576720, "description": "Earrings Vibe STE GP CRY white", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/NewImages/23164G.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/NewImages/23164G.jpg", "price": 13.3, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "23164G"}, {"order-id": 40576720, "description": "Earrings Upside RH CRY", "quantity": 4, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/22861.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/22861.jpg", "price": 16.7, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "22861"}, {"order-id": 40576720, "description": "Pendant Courage RH CZ", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12253R.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12253R.jpg", "price": 19.7, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "12253R"}, {"order-id": 40576720, "description": "Earrings Würfel CRY.", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/21015%20001.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/21015%20001.jpg", "price": 6.5, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "21015 001"}, {"order-id": 40576720, "description": "Pendant Sound STE CZ", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12243.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12243.jpg", "price": 14.6, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "12243"}, {"order-id": 40576720, "description": "Pendant Blue eye RH aquamarine", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/11028.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/11028.jpg", "price": 14.6, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "11028"}, {"order-id": 40576720, "description": "Pendant Family 925AG RH CZ", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/61266.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/61266.jpg", "price": 33.7, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "61266"}, {"order-id": 40576720, "description": "Bracelet Tane STE GP CZ", "quantity": 4, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/32332G.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/32332G.jpg", "price": 14.3, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "32332G"}, {"order-id": 40576720, "description": "Earrings Way GP CZ", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/22983G.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/22983G.jpg", "price": 11.2, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "22983G"}, {"order-id": 40576720, "description": "Earrings Double RH lt. amethyst", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/22815%20212.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/22815%20212.jpg", "price": 12.9, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "22815 212"}, {"order-id": 40576720, "description": "Pendant Mom 925AG CZ WHI", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/61165.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/61165.jpg", "price": 24.8, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "61165"}, {"order-id": 40576720, "description": "Earrings Perk STE GP CZ", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/23135G.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/23135G.jpg", "price": 13.3, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "23135G"}, {"order-id": 40576720, "description": "Ring Tiana GP CZ", "quantity": 4, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/41213G.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/41213G.jpg", "price": 7.1, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "41213G"}, {"order-id": 40576720, "description": "Ring Eternita 925AG CZ RH White", "quantity": 1, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/63290L.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/63290L.jpg", "price": 28.6, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "63290L"}, {"order-id": 40576720, "description": "Ring Fortune 925AG CZ RH White", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/63288L.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/63288L.jpg", "price": 21.1, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "63288L"}, {"order-id": 40576720, "description": "Earrings Twisty STE GP", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/23035G.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/23035G.jpg", "price": 13.3, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "23035G"}, {"order-id": 40576720, "description": "Ring Caroline 925AG GP CZ M", "quantity": 1, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/NewImages/63340GM%20WHI.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/NewImages/63340GM%20WHI.jpg", "price": 19.4, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "63340GM WHI"}, {"order-id": 40576720, "description": "Necklace Sinann STE GP pearl", "quantity": 6, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12309G.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12309G.jpg", "price": 15.6, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "12309G"}, {"order-id": 40576720, "description": "Pendant Class RH CRY", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/11548R.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/11548R.jpg", "price": 15.0, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "11548R"}, {"order-id": 40576720, "description": "Pendant Amo STE CZ CRY RG", "quantity": 4, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/11772RG.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/11772RG.jpg", "price": 19.0, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "11772RG"}, {"order-id": 40576720, "description": "Ohrringe Delight STE RG CZ", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/NewImages/23102RG.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/NewImages/23102RG.jpg", "price": 13.9, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "23102RG"}, {"order-id": 40576720, "description": "Ring Jasmine GP CZ", "quantity": 4, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/41212G.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/41212G.jpg", "price": 9.2, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "41212G"}, {"order-id": 40576720, "description": "Bracelet Connected STE CZ", "quantity": 4, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/32296.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/32296.jpg", "price": 12.9, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "32296"}, {"order-id": 40576720, "description": "Pendant FS Loving STE RG (a)", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12187RG.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12187RG.jpg", "price": 9.9, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "12187RG"}, {"order-id": 40576720, "description": "Earrings Luminary GP CRY", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/NewImages/23150G.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/NewImages/23150G.jpg", "price": 14.3, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "23150G"}, {"order-id": 40576720, "description": "Necklace Arista STE", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12320G.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12320G.jpg", "price": 12.9, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "12320G"}, {"order-id": 40576720, "description": "Collier Damu STE GP", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12289G.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12289G.jpg", "price": 12.6, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "12289G"}, {"order-id": 40576720, "description": "Necklace TwoCats FS CZ WHI", "quantity": 4, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12194.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/12194.jpg", "price": 14.6, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "12194"}, {"order-id": 40576720, "description": "Ring Links STE L/XL", "quantity": 2, "image_url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/41161LXL.jpg", "image-url": "https://storage.googleapis.com/flutterapp-fd5c3.appspot.com/Images/41161LXL.jpg", "price": 8.2, "order_id": 40576720, "emailOwner": "aida.suljevic@nall.me", "name": "41161LXL"}]
# order = {"order-id": 40576720, "date": str(datetime.now()), "Status": "Awaiting", "list": ["Order/44vFx3T3AcKU3SbbV9dF", "Order/IG7EWbWlcY3jxzeoStME", "Order/UfhRBe7yiBVx7TRo751U", "Order/QmhKyBTLop2X9fwe1yn9", "Order/2VBfeE0trLQ0w0yI4ksz", "Order/ZYXm51I8SqvkY2cY1ixw", "Order/SGV899ynqqIJkBjcEIZ6", "Order/6bQ7iRhXeu8LSnkeIJHm", "Order/IC1RjjdOjLCCP80BSJl0", "Order/YpvYJOQRXyQf2RxPzkE0", "Order/UvF3YR8HKYniPkGh7dob", "Order/HimPIAHuFJS2no9quVpT", "Order/y1MjJCUKZiCXANl94DlU", "Order/Tzt4xZUSHNG8EE5XAFWD", "Order/4vt7OmEzY1QybKW8rbpp", "Order/cl0UnIEP2XQ8GAEBXNte", "Order/Y9Rrn8ahkis2yNsy70Lq", "Order/BYyW4yQQKJMIsfJTk4bx", "Order/dgRGlJtZTbOrXOmc45Yx", "Order/m8SZC5bOGLqQSqWs1N6Q", "Order/slIpCjlEXsCpKQv1Gtel", "Order/5IwouNeHyGDkNMmGOrWw", "Order/mrUI6dRmyObLRvWG7EMg", "Order/Au8DLAv4HtDNAkX7UjEl", "Order/0H2Ad2TgmCD4FvLv3AFD", "Order/UeolDrto0DbkPJkN5UB5", "Order/N84f5H8KxON6PyaTcGoD", "Order/5sWaL5sHZvPH0sGXMBRk", "Order/c14LyHqfu0AKmEWqxprr", "Order/DRc6xbGZwwg9Oe3txJDK", "Order/smd6Ph8aq9a0zMaDsIyW", "Order/0W5qXdOkoGpAdDMtrF9m", "Order/g0glutakUOBNU6rFP7Kc", "Order/3g2IICg9YW66dAVU73ou", "Order/1oVt1uLZF6z8MSwZXfhE", "Order/fZrhHQuO45oUp2oK0cO8", "Order/7UwH4R8HcCMFE0kahWWg", "Order/mLpGlVy8rRK1Eth1DPad", "Order/2rB3rub6EHQ0PnJVff9B", "Order/NTkH3EmcYSPS61Q8cpP6", "Order/fzQHnJM7Zhl8Q0ZiOMGK", "Order/h0aASiBe2m2JllpWb8ML", "Order/ArBGEx02eGhdXDw42TaA", "Order/GPHcsGFIrn6y3zZ5MwYr", "Order/rx64T1JHK9ZGr0t6m3Jo", "Order/h8bzlOOKmPnEQyuC4Q6g", "Order/NnovmRN9yRDLMFIrhw0b", "Order/3grDuMpQTuh82RNxMfrB", "Order/FQz1K0S9Ttl0Eug6N2B0", "Order/jKgow1cQASxYfGIcg98l", "Order/7Uo4yiIx2uzXnJusH4l5", "Order/VnHZJFtNJUTOxcVboknl", "Order/2MPr0CsMqVrZgFU4Nuun", "Order/XIzZGTXOSvmlrwmKM0He", "Order/TFYCCqAUH9dMTmbTibW2", "Order/jjGsoq6D012HNyD1Chbx", "Order/H8nsRLMJauJL71ChJxC7", "Order/v0EPxj4s4pJcWbpQ9wxF", "Order/PmJe0KnzUUTpVatERc0c", "Order/Duns41FJjPKcWf0zsxpy", "Order/eHFWDFGnlDSJDrSaFzWw", "Order/4HNkMxrVtDNYgQOeGQuL", "Order/hM4KPyJpvEr2cfADjSSv", "Order/rgYvyiW0oA5eN49FZ4qq", "Order/E2VnH6Pp1jm9brdkfdDT", "Order/ZDLiW3240IYG0fSeGgJA", "Order/EdXz6ZYVQYJ59ZGpQeLV", "Order/AZAjHIf2dvb7R9qZMYwZ", "Order/me4TF94jnB6y7UbD4MO8", "Order/r7KMwrDBqEZs7ORiRJ2o", "Order/QpB4twQQaV6n8QuPlm0B", "Order/X0CxkE1Hnd5aiLOmMkoG", "Order/Lft5vY7bC6P0Oj0kLDAB", "Order/MYSg9uAJwAyFr6N0tL1H", "Order/vPOehIivNS4YUVeRIADn", "Order/MYGPXzEgwEXTGPln50QF", "Order/vuwhoKAPAAxqyaWHdhPu", "Order/cewQRt46FbNHCaRyt0h0", "Order/rhxjY1ky9EDlnApY4utf", "Order/8zA7xxmW9aLieHeIK3Rc", "Order/MfwJ5hlkAfmvE6BcJECS", "Order/kxZozngRNkrXxWLEGfl0", "Order/jEc7iIALexpADDkdpWVT", "Order/zBONzoeXHsGrHExkEZZ8", "Order/YWGl9U0qXXPtxxni59iP", "Order/ZOOuhaMsj8xhwzEZ5ThT", "Order/uk2gvWi5o8U9XRdVPn8Z", "Order/gzRAp7Y2T9fUDQjUU1xJ", "Order/LPoqkWIfQCLGQFZCvIMD", "Order/5IExK6xVlfVKALvaId2C", "Order/u1QnUPCkawtDNVcPqzmj", "Order/T5PXWJdRmulMPRW38Zuc", "Order/m2KG0l8clqxoGZtYSUYN", "Order/dyFTz4Mc1Dz7PHwQg5E0", "Order/jgdVrUef8d3Fw5beXWk4", "Order/JZUNWIePGV2Fe2SNinlq", "Order/ReR29Z5ny2SDLApQu26g", "Order/KZeIvnByqaz9ozNCvHau", "Order/l9bGKcK9ey61wcQlqsvE", "Order/1C1eitIIRZEsvkjzBYLs", "Order/FQevGKMlWx1uc2MHmnuU", "Order/01OcCBAxWFSNYEEtNEtQ", "Order/xG5YNMIJV1e4RvJHqao2", "Order/elvT1V0T4LooFaVj3iOQ", "Order/8YOkRabc5bTHYggImgpw", "Order/fTAzofZRwMLB0K5uNaXA", "Order/B8OVXYBIvayD2rHjPjeQ", "Order/S7mJRNzypkvnt4gYSh2t", "Order/ZKOFvgF8WPUgEbmbvcJa", "Order/KQnFvTU5H4NcvOz8opkX", "Order/AVTcY1PBgrlvWbO3RMXQ", "Order/YmdJd8GtG3JXsxV28gis", "Order/uD7U2fp5vRdaduo55HwR", "Order/H5GAwIAIVlLEsb0NwZ50", "Order/IsoXXDt1D0IvOFk3ClqJ", "Order/uGryXJFf810ySiS9zN2L", "Order/aP1FXSjuJ6QPXmmffT2g", "Order/4cPPra7jG6GgpEYMhAUd", "Order/oBn3NvoN3Jg2p1nY607h", "Order/QkvGfableqGMWnfPdDH3", "Order/LqHLxxmwBcZZ2YfHNgOX", "Order/54m1uSJAeXbzbBjtiC5X", "Order/oiPi2NlQGL0fg9kKp934", "Order/N4jMES3id8j47pa5tIjG", "Order/qbR0bapFIEXyKlTVIxhl", "Order/beszaQzrgmVqLM1uK8qY", "Order/86YeAr4XqKEItHIHNbz0", "Order/Lez7BGeu0BLOX4cIhJFV", "Order/KAMXqfvrVfxrf1SbAv30", "Order/0piqOphXLPqLRzlWtEne", "Order/zf7s35tuZ9nCuX25S3nU", "Order/441yFuXGrAivkOm3Uvbr", "Order/uRRlZeDnfSWUwK15L6cA", "Order/gIjnI92nfp8yrqS2D2d1", "Order/9bCM9lbdFK0tTbxqsMou", "Order/5uGA0GpMFzattKHK0me7", "Order/6SsNDEs3aKBk7E98hMhg", "Order/TVbSwG8ZXlY4SMYdjYRd", "Order/IDY1xr5nodhUOdrIDBP1", "Order/DHw4KQ4ofFOvzXBJ14WY", "Order/8XzbySqecZNiewabotia", "Order/hvUfRVgcJu4GKdBmgoUe", "Order/UJ7HhTWy0gRsnEEgzQd2", "Order/hs4dwItzMeADz04JbjFU", "Order/3HomREOnKayMBlFstsmT", "Order/mNdTC5B4IJxnt8CXxiV3", "Order/hL9DYRjq8fRmfoDk562q"], "price": 5089.0, "currency": "Euro", "order_id": 40576720, "email": "aida.suljevic@nall.me"}
#
# currency = "€"
# name = "Nall International D.O.O. Montenegro"
# buffer = BytesIO()
# file = "output.pdf"
# # Basic setup
# styles = getSampleStyleSheet()
#
# center_bold_style = ParagraphStyle("CenterBold", parent=styles["Normal"], fontSize=12, alignment=1,
#                                    fontName="Times-Bold")
# bold_style = ParagraphStyle("Bold", parent=styles["Normal"], fontSize=12, fontName="Times-Bold")
# doc = SimpleDocTemplate(file, pagesize=A4, rightMargin=30, leftMargin=30, topMargin=30, bottomMargin=18)
# content = []
# title_style = styles["Heading1"]
# content.append(Paragraph("OLIVER WEBER COLLECTION", title_style))
# content.append(Spacer(1, 0.3 * inch))
# content.append(Paragraph(f"Client name: {name}", bold_style))
#
# table_data = [["Product", "Image", "Quantity", "Price per item", "Total"]]
# for item_order in orders:
#     image_path = item_order["image-url"]  # Adjust this line to get the actual image path or object
#     image = Image(image_path)
#     image.drawHeight = 50  # Example height in points
#     image.drawWidth = 50
#     row = [item_order["name"], image, item_order["quantity"], currency + str(item_order["price"]), currency + str(round(item_order["price"] * item_order["quantity"], 2))]
#     table_data.append(row)
#
# table = Table(table_data, colWidths=[1.7 * inch, 1.0 * inch, 1.0 * inch, 1.7 * inch, 1.3 * inch])
#
# table_style = TableStyle([
#     ("BACKGROUND", (0, 0), (-1, 0), "#f0f0f0"),
#     ("TEXTCOLOR", (0, 0), (-1, 0), "#000000"),
#     ("ALIGN", (0, 0), (-1, -1), "CENTER"),
#     ("VALIGN", (0, 1), (-1, -1), "MIDDLE"),
#     ("FONTNAME", (0, 0), (-1, 0), "Times-Bold"),
#     ("FONTSIZE", (0, 0), (-1, 0), 14),
#     ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
#     ("BACKGROUND", (0, 1), (-1, -1), "#ffffff"),
#     ("GRID", (0, 0), (-1, -1), 1, "#000000")
# ])
# table.setStyle(table_style)
# content.append(Spacer(1, 1 * cm))
#
# content.append(table)
#
# # Order details
# email = order.get("email", "No email provided")
# date_str = order["date"]
# date_obj = datetime.fromisoformat(date_str)
#
# # Теперь применяем форматирование
# formatted_date = date_obj.strftime("%Y-%m-%d %H:%M:%S")
# total_price = round(order.get("price", 0), 2)
# content.append(Spacer(1, 0.5 * inch))
# content.append(Paragraph(f"Total to pay(incl. VAT): {currency}{total_price}", bold_style))
# # content.append(Paragraph(f"Included VAT: {currency}{round(order["price"] * vat,2)}", bold_style))
# content.append(Spacer(1, 0.3 * inch))
# content.append(Paragraph(f"Date: {formatted_date}", center_bold_style))
# content.append(Spacer(1, 10))
# content.append(Paragraph(f"E-mail: {email}", center_bold_style))
# content.append(Spacer(1, 10))
# content.append(Paragraph(f"DOCUMENT N.: {10036}", center_bold_style))
# content.append(Spacer(1, 10))
# content.append(Paragraph("Thank you for your purchase!", center_bold_style))
#
# doc.build(content)
#
#
# # Preparing response
# # pdf = buffer.getvalue()
# # buffer.close()
# # response = HttpResponse(content_type="application/pdf")
# # response["Content-Disposition"] = f"attachment; filename="order_{order.get("order_id", "unknown")}.pdf""
# # response.write(pdf)
import re


def update_numbers_in_string(input_str):
    # Define a regex pattern to match // followed by a 3-digit number
    pattern = r'//(\\d{3})'

    # Function to decrement the number by 50 and replace in the string
    def decrement_number(match):
        number = int(match.group(1))
        new_number = number - 50
        return f'//{new_number:03}'

    # Use re.sub() with a callback function to replace matched patterns
    updated_str = re.sub(pattern, decrement_number, input_str)

    return updated_str
dic = """//178
    ["61268", "61267", "63336", "62237", "63540"],
    //179
    [
      '61270 WHI',
      '61272 WHI',
      '61272G WHI',
      '62252',
      '62239 WHI',
      '62242 WHI',
      '62242G WHI',
      '63337G WHI',
      '63338G WHI',
      '62241',
      '63338 WHI',
      '63541'
    ],
    //180
    [
      '61271G WHI',
      '61272RG PIN',
      '61270G PIN',
      '62240G WHI',
      '62242RG PIN',
      '62239G PIN',
      '62337G PIN',
      '63542 WHI',
      '63542G WHI',
      '63338RG PIN',
      '63542RG PIN'
    ],
    //181
    [
      '61275',
      '61274',
      '62244',
      '63340 WHI',
      '63543',
      '62246',
      '63340G WHI',
      '63543G WHI',
      '62247',
      '63544',
      '62245'
    ],
    //182
    [
      '63339 WHI',
      '63339G WHI',
      '62243 WHI',
      '61273 WHI',
      '62243G WHI',
      '61273G WHI'
    ],
    //183
    [
      '61277',
      '61278',
      '61280',
      '61281',
      '62249',
      '62250',
      '62254',
      '62253',
      '63311',
      '63289',
      '63286'
    ],
    //184
    ['61279', '61269', '61276', '62251', '62238', '62248', '63545', '63341'],
    //185
    [
      '23165G',
      '23164G',
      '23163G WHI',
      '23163G GRE',
      '41222G GRE',
      '41222G WHI',
      '41220G'
    ],
    //186
    [],
    //187
    [
      '12427G GRE',
      '23148G GRE',
      '23162G GRE',
      '23162G WHI',
      '32413G WHI',
      '32413G GRE'
    ],
    //188
    ['41221G GRE', '23160G', '41221G WHI', '41219G', '23161G', '41065G'],
    //189
    ['31003 WHI', '12440', '22572R', '21020 621'],
    //190
    ['22628R', '22813R', '12442', '12441', '31003 GOL', '31003 GRY'],
    //191
    ['12421', '12420', '12423', '12422', '12424', '23145'],
    //192
    ['12439', '12439G', '23159', '23159G', '12419', '12418', '23144', '23143'],
    //193
    ['12432RG', '12431G', '12431RG', '23152RG', '23151G', '23151RG'],
    //194
    ['12429G', '12428G', '12430G', '32414G', '23149G', '23150G', '22968G'],
    //195
    [],
    //196
    ['12435', '12435G', '23155', '23155G', '32417', '32417G'],
    //197
    ['12434', '12434G', '23154', '23154G', '32416', '32416G'],
    //198
    ['12433G', '12433', '23153', '23153G', '41179', '32415', '32415G'],
    //199
    [],
    //200
    ['12426', '12425', '23146', '23147', '31003 LTUR', '31003 TUR'],
    //201
    ['12438', '12438G', '23158', '23158G', '58050', '58050G'],
    //202
    [
      '12436',
      '12436G',
      '12437',
      '12437G',
      '23156',
      '23156G',
      '23157',
      '23157G',
      '41191RG'
    ],
    //203
    [
      '1275RG',
      '12375',
      '32391G',
      '32391RG',
      '32391',
      '12375G',
      '23100RG',
      '23100G',
      '23100'
    ],
    //204
    ['12376', '12376G', '32392', '32392G', '23101', '23101RG', '23101G'],
    //205
    [],
    //206
    ['12377', '23102G', '32393', '23102', '32393G', '23102RG'],
    //207
    [],
    //208
    [],
    //209
    ['12444G', '23167G', '12445G', '12447G', '32421G', '23168G'],
    //210
    ['23169G', '12446G', '23170G', '32422G', '23172G', '23171G', '23173G'],
    //211
    [
      '11022 209',
      '11022 214',
      '11022 001',
      '32418 IND',
      '32418 VIO',
      '32420S BLA',
      '32420M BLA',
      '32419 AQUA',
      '32419 SAP',
      '32420S JET',
      '32420M JET'
    ],
    //212
    ['12448G', '12443G', '23174G', '23166G', '12449 202', '12449 GSHA'],
    //213
    [],
    //214
    ['61282', '61283', '61284', '62168', '62255', '62256', '63302', '63343'],
    //215
    [
      '61290G VIO',
      '61290G YEL',
      '61290G TUR',
      '62258G VIO',
      '62258G YEL',
      '62258G TUR',
      '62259G VIO',
      '62259G YEL',
      '62259G TUR'
    ],
    //216
    [
      '61290 RED',
      '61290 PIN',
      '61290 GRE',
      '61289 BLA',
      '62258 RED',
      '62258 PIN',
      '62258 GRE',
      '62258 BLA',
      '62259 RED',
      '62259 PIN',
      '62259 GRE'
    ],
    //217
    [
      '61285',
      '61286',
      '61287',
      '62257',
      '61288',
      '63344',
      '61241G GRE',
      '62173G GRE',
      '63342'
    ],
    //218
    ['62225', '61252', '63345', '63548', '63547', '63546'],
    //219
    [],
    //220
    [],
    //221
    [],
    //222
    [],
    //223
    ['FUR0027'],
    //224
    ['FUR0002', 'FUR0030'],
    //225
    ['FUR0001'],
    //226
    ['FUR0011', 'FUR0008'],
    //227
    ['FUR0006', 'FUR0028'],
    //228
    ['FUR0031', 'FUR0010'],
    //229
    ['FUR0026'],
    //230
    ['FUR0007', 'FUR0005'],
    //231
    ['FUR0025'],
    //232
    ['FUR0022'],
    //233
    ['FUR0021'],
    //234
    [
      '2610 BLU',
      '2610 WHI',
      '2609 BLU',
      '2609 WHI',
      '2612 BLU',
      '2612 WHI',
      '2613 BLU',
      '2613 WHI'
    ],
    //235
    ['2632', '2606', '2605', '2604', '2681', '2682', '2683', '2655'],
    //236
    ['V311'],
    //237
    ['2615', 'V310', '2679', '2652', '2651'],
    //238
    ['2608', '2668', '2660', '2678', '2670', '2607'],
    //239
    ['2635', '2637', '2656', '2640', '2669', '2667', '2680', '2603'],
    //240
    ['2624', '2623', '2625', '2621', '2622', '2626', '2620'],
    //241
    ['2700', '2701', '2702', '2703', '2704', '2705', '2706', '2707'],
    //242
    [
      'V107',
      'REPFOR',
      'V113',
      'REPKIT',
      '9983',
      'V218',
      'V223',
      '2691',
      '2692'
    ],
    //243
    [
      'R900311023',
      'R900311024',
      'R900311020',
      'R900311025',
      'R900311027',
      'R900311022',
      'R900311028'
    ],
    //244
    [
      'R900300044',
      'R900300022',
      'R900300040',
      'R900300039',
      'R900311012',
      '9976',
      'D003',
      'D103',
      'D102'
    ],
    //245
    [
      'CAT_WINTER',
      'CAT_MAIN',
      'CAT_WEDDING',
      'CAT_SILVER',
      'CAT_WINTER',
      'CAT_GAUDI',
      'CAT_SUMMER'
    ],
    //246
    ['V220', 'V221', 'V222', 'V101', 'V114', 'V225'],
    //247
    ['00000'],
    //248
    ['00000'],
    //249
    [
      'BANNER_1',
      'BANNER_2',
      'BANNER_GAUDI',
      'BANNER_PL',
      'BANNER_FREEDOM',
      'BANNER_WEDDING'
    ],
    //250
    ['FOILS_OPTIONAL'],
    //251
    ['DISPLAYS_CARDBOARD'],
    //252
    ['DISPLAYS_CARDBOARD'],
    //253
    ['00000'],
    //254
    ['00000'],
    //255
    ['00000'], """
def subtract_50(match):
    number = int(match.group(1))
    return "//" + str(number - 50)

# Use regular expression to find and replace the numbers
updated_dic = re.sub(r"//(\d{3})", subtract_50, dic)

print(updated_dic)