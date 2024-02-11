#Libraries
import os
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import sys, subprocess
import time
from time import sleep
from rich.console import Console
from pygame import mixer

#ASCII Art and Text
gameMenuText = r"""
╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗║
║║                                                                                                                                 ║║
║║  ______     ______     __  __     __  __     ______        __  __     __     __   __     ______     ______     __     ______    ║║
║║ /\  ___\   /\  __ \   /\ \/ /    /\ \/ /    /\  __ \      /\ \/ /    /\ \   /\ "-.\ \   /\  ___\   /\  ___\   /\ \   /\  ___\   ║║
║║ \ \ \__ \  \ \  __ \  \ \  _"-.  \ \  _"-.  \ \ \/\ \     \ \  _"-.  \ \ \  \ \ \-.  \  \ \  __\   \ \___  \  \ \ \  \ \___  \  ║║
║║  \ \_____\  \ \_\ \_\  \ \_\ \_\  \ \_\ \_\  \ \_____\     \ \_\ \_\  \ \_\  \ \_\\"\_\  \ \_____\  \/\_____\  \ \_\  \/\_____\ ║║
║║   \/_____/   \/_/\/_/   \/_/\/_/   \/_/\/_/   \/_____/      \/_/\/_/   \/_/   \/_/ \/_/   \/_____/   \/_____/   \/_/   \/_____/ ║║
║║                                                                                                                                 ║║
║║                                                                                                                                 ║║
║╠═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣║
║║                                                                                                                                 ║║
║║                                                          1. Start Game                                                          ║║
║║                                                           2. Settings                                                           ║║
║║                                                             3. Exit                                                             ║║
║║                                                                                                                                 ║║
║╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝║
╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
"""
developerOptionsText = r"""
 ______  _______ _    _ _______         _____   _____  _______  ______       _____   _____  _______ _____  _____  __   _ _______
 |     \ |______  \  /  |______ |      |     | |_____] |______ |_____/      |     | |_____]    |      |   |     | | \  | |______
 |_____/ |______   \/   |______ |_____ |_____| |       |______ |    \_      |_____| |          |    __|__ |_____| |  \_| ______|                                                                                                                               
"""
loadingSplashScreen = r"""
⢐⢐⢐⢐⠔⡨⢐⢐⠔⡡⠢⡑⡌⡢⡱⡘⡌⢎⢢⠱⡊⡢⡑⢔⠡⢂⢂⢂⢂⠢⠡⡂⠢⡡⢂⠕⡨⠢⡑⡐⢅⠢⠡⡂⡢⠡⡂⠪⡐⠌⢔⢐⠅⡪⡐⡅⡪⡔⢕⠱⠡⡃⡕⣌⢶⣕⢷⢝⣵⡫⡇⡂⠪⡐⢅
⢐⠐⢔⢐⠡⡂⠢⡑⠬⡘⡌⢆⢣⠣⣑⠱⡘⢜⢌⢊⠢⡂⠪⡐⢌⢂⠢⡑⠄⠅⢕⠨⡨⠢⡑⢌⠢⡑⢌⢌⠢⡑⢅⠢⢊⢂⠪⠨⡂⢕⠡⡢⣕⠴⡱⡑⢕⢨⢰⡼⡨⣪⢯⡯⣗⣗⢯⣟⣮⡯⡇⢌⠪⠨⡂
⠠⢑⠐⠄⠅⢌⠌⡪⠨⠢⡑⢅⢅⠣⠢⡑⢅⢑⠄⢅⢑⠌⢌⢂⢆⠢⡑⠌⢌⢊⠢⡑⢌⠬⡨⠢⡑⢌⠢⠢⡑⢌⠢⢡⢑⢔⢑⢕⣜⠲⡙⢌⠢⣑⡴⣞⡾⣽⣫⢯⡂⣯⢷⣻⣗⣯⢿⣾⣟⣿⡇⡑⢌⠪⡨
⠨⢐⠨⠨⡈⠢⢑⠨⡘⢌⢊⠢⠢⡑⡑⠨⢐⢐⢈⠢⠢⡑⢅⢆⠢⡑⢌⠪⡂⢕⠨⡨⠢⡑⢌⠪⡨⠢⡑⡑⢌⠢⡡⠱⡔⡺⡨⡑⡤⣱⡌⢆⢿⢵⢯⣗⡯⣗⣯⢿⠨⡯⣿⡽⣞⣯⣿⣟⣿⡿⡇⡊⡢⡑⢌
⢐⠐⡨⢐⠨⡈⡂⢅⢂⠢⢂⠅⠅⢂⠂⠅⡂⡂⠢⡑⡱⡘⢔⠢⡑⡅⡣⡑⢌⠢⡑⢌⠪⡨⢢⢱⣨⡎⠔⢌⠢⡑⢌⠪⡢⣶⢾⣾⣻⣽⡏⡎⣯⢯⣗⡷⡯⣿⣾⣿⢑⣯⢷⣿⢯⣗⢿⡽⠿⡛⢇⠱⡐⡌⡢
⢐⠨⠐⠄⢅⠢⡈⡂⡢⠡⡑⠄⠅⡂⠌⡐⡐⢄⠑⠔⡌⢜⠰⡡⡃⢎⠢⡊⢆⠣⡊⡢⡱⠼⢞⢩⣰⢼⢘⢔⠡⡊⢲⣻⣺⣻⣿⢾⣯⣷⡯⡪⣯⢷⣳⣿⣻⣿⣟⣿⢐⠯⢟⢋⢭⣑⡵⣜⣾⣺⡇⡑⡌⡢⢊
⢀⠊⠌⢌⠢⡑⡨⠢⠨⡨⠂⠅⠅⠄⠅⡂⡂⠢⡑⡑⢌⠪⡨⡂⢎⢢⢱⠸⡐⠕⡌⡢⡪⡪⣾⣟⣯⣿⠢⡑⢌⢌⢺⢺⣺⣿⣽⣿⡷⣿⢯⢪⣾⢿⠿⡻⡹⡱⣩⣪⢂⢗⣿⢿⣿⣻⣟⣿⣽⡷⡇⡊⡢⡊⡢
⠠⠡⡡⡑⡰⡐⢌⢌⠪⠠⠡⠡⠡⠡⡑⡐⢌⢌⠢⡊⡂⢇⠧⡚⡌⣇⣷⣽⢌⠪⣂⠪⡇⡯⣾⣿⣟⣿⠨⡊⡢⠢⢪⢺⣽⣾⡿⢽⢟⡛⡍⡪⣢⣵⢷⡷⣿⣽⢿⣾⢨⣻⣿⢿⣿⢿⣿⣟⣷⡿⡇⡊⢆⠪⡐
⢘⢌⠢⠪⡰⡨⡢⡑⡅⡣⡡⡑⠅⢕⠰⣨⠢⡆⠕⢌⢪⣺⣴⡿⣿⣽⣾⢿⡐⢕⢔⢑⡧⣹⣻⣽⣿⢿⢘⢔⢘⢌⠪⡪⡪⣦⣧⡷⣷⣻⡇⣺⣿⣿⣿⣿⢿⣽⣿⣿⢰⢽⣾⣿⢿⡿⣟⣿⣿⣿⡇⢕⢅⠣⡊
⢔⠢⡩⡪⡢⡣⡪⣪⣪⡖⡌⢆⠑⠄⣇⣵⡵⣏⠪⡪⢸⢺⣯⣿⡿⣾⡿⣿⢨⠢⡣⡱⡓⡜⣭⣵⣼⣽⢰⢑⢌⢢⠱⡸⣺⡿⣷⣟⣯⣿⡇⣺⣯⣷⣿⡿⣟⣿⣷⣿⠸⣽⢾⣻⣟⣿⣻⣿⣻⣽⡇⢕⢅⢇⠪
⢂⢇⣣⢣⡷⣯⢯⢾⡯⣗⢕⢅⠅⢕⢽⣷⡟⣗⠕⡜⡸⣹⣯⠷⢿⢛⣛⣫⢊⢎⢪⢪⢸⢸⣿⣽⣯⣿⠰⡑⢔⠅⡕⣝⣵⣿⣯⣿⣯⣿⡇⣪⣿⣿⣻⣿⣿⡿⣷⡟⡕⣽⢽⣿⣽⣯⡿⣾⣻⢯⡇⢕⠕⡌⡪
⣏⢟⡮⢽⡽⣯⡗⣿⢽⣳⢱⢑⠌⡢⡻⡯⡗⡏⡪⡘⢜⢌⣶⣽⡦⣻⣟⣿⢨⠪⡢⡣⣗⣯⣷⣿⡷⣿⠡⡣⡡⡃⡪⣒⢷⣿⣿⣽⣷⢿⡇⡮⣿⣾⣿⣿⣽⣿⣿⣶⠪⣾⢿⣻⣾⡷⣿⢿⣾⣿⡇⢕⢱⢑⢌
⣗⢽⡪⣫⣯⢷⡯⣺⢯⢗⢕⢕⠨⡂⢧⣻⡧⣏⢎⠪⡪⣳⡿⣯⣗⣿⣻⣿⢐⢕⢕⢌⡧⡷⣿⣷⣿⣿⠱⡘⢔⢱⢨⢪⢽⣿⣾⣿⡾⠿⠳⢱⣿⣯⣷⣿⢿⣽⣿⣿⠸⣽⣿⢿⣯⣿⡿⣿⣿⣽⡇⢕⢱⠨⡂
⡳⡹⡕⣝⣞⣝⣞⢮⡷⣗⢕⠕⢌⠌⣾⢿⣳⣳⠅⡇⣝⢞⣿⣟⣷⢿⣽⣾⠌⡆⡇⡕⡽⣹⣿⣽⣾⣿⢸⢘⢌⢆⢇⢷⢯⣿⡞⠉⢂⠐⠈⠄⠹⣯⣿⣽⢿⣻⣯⣿⢪⢿⣾⣟⣯⣷⣿⣿⣯⣷⡇⡣⡱⡑⡌
⢎⣗⡝⡼⡾⡽⣇⢿⣽⡗⡕⡍⡢⠱⣸⣿⡇⡿⡸⡨⡪⡯⣿⣽⣯⣿⣿⣻⠌⡎⡪⡪⣺⢵⣟⣿⣻⣿⢸⢨⢪⢪⢪⡫⣯⣿⢀⠌⡀⢀⡈⠄⠡⣹⢿⣾⢿⣿⣻⣿⢘⣿⢷⣻⣽⢾⡯⣷⢿⡾⡇⢕⢕⢌⢪
⢕⡕⡇⣯⣻⣝⡧⣻⣺⣳⢱⢑⢌⠪⡪⣾⡗⡯⡪⡊⡎⣯⣿⣯⣷⣻⣽⣿⢘⢌⢎⠪⣟⣞⣿⣽⢿⣾⢸⢸⢨⢲⢱⣹⣺⣿⣿⢵⢑⠄⡂⠈⢀⠸⣟⣯⣿⢯⣿⢾⡑⣟⣿⣽⣯⣿⣻⣟⣯⡿⡇⡣⡣⡱⡑
⠕⡝⡜⣜⢮⡺⣪⢺⡳⡳⡱⡑⡰⡑⣝⣽⡯⣗⢕⢕⢕⢽⣾⣟⣿⣺⢿⣾⢸⢸⢸⢘⣗⢷⣻⣽⣟⣿⢸⢸⢸⢸⢰⣳⣳⡿⣟⣿⣦⣕⢔⠔⠄⠠⣸⣻⢺⣫⡝⡝⠼⢬⠭⡣⡒⢔⠢⡒⠔⢅⠕⠌⢜⠨⠨
⢊⠎⡎⢎⢞⢮⢪⢳⢹⢸⠨⡢⠒⢌⢖⣿⡇⣿⢨⢢⢳⢽⣯⢿⣾⣺⢿⣽⢸⢸⢸⠰⡗⣟⣯⣷⢿⣽⢜⢜⢜⢜⢜⣞⣾⣻⣿⢿⡛⠚⠢⢐⠈⢵⡱⡸⡨⡢⡪⢢⠣⣑⢔⢢⠪⡢⡱⡨⡊⡢⢊⠌⡂⠌⠌
⠡⡑⠌⡊⠢⡡⡑⢅⠣⡡⢑⠠⢑⠅⣟⣯⡗⡯⡊⡎⡺⡹⡯⡿⢾⢺⠿⣽⠸⡸⡸⣘⣏⢞⢟⢞⢻⢹⢸⡸⡸⣜⢎⣞⢗⢟⣝⠏⠄⠄⠈⠂⠉⠩⣻⢸⢸⠸⡸⡘⡜⡔⡕⢕⠕⡕⢜⠰⡑⢌⢂⠪⡠⠡⡡
⠨⡂⣕⡬⣞⡮⡞⢆⠕⡨⠂⢅⠂⠅⢅⢑⠩⡊⢜⠨⢪⢘⢌⢌⠢⡑⢌⢄⢕⠨⡐⠔⢄⢑⠄⢅⠢⡁⡢⡈⡢⢂⠕⡐⢅⠕⢔⠄⠈⠄⠐⠈⠄⠡⢈⢊⠢⡑⠌⠌⠌⢌⠪⠨⢊⠌⢌⠪⠨⡈⠢⠡⠨⠈⠄
⡕⡍⣎⢮⢑⠩⢈⠄⠅⡂⠅⡂⠅⢑⠠⠡⢑⢈⢂⠣⡑⡘⡐⡑⡑⢑⠑⠂⢅⠑⢌⢊⢂⠢⡑⡑⢌⢂⠢⡂⡪⢐⠌⡢⡑⢕⢑⠄⠁⠄⠁⠄⠄⠐⡸⢢⢑⠌⠌⢌⠪⡐⠡⠁⠆⢕⡐⡁⠅⠌⠌⠨⠈⠌⡐
⠯⠇⠣⢂⠢⠑⠔⠬⠴⢤⢥⢴⣨⢔⣈⣨⣐⡐⠠⡑⡘⡔⠒⢒⠘⡀⠅⠅⡡⡡⣁⢂⢅⢕⠨⡐⡐⢔⠐⠔⡒⡢⣱⣐⣌⠬⠄⠂⠁⠄⡠⠆⠌⠄⠌⠒⠑⠅⠧⠧⠣⠮⠬⠬⠨⡀⡂⡂⠅⢅⠁⡁⡁⠡⡐
⠨⡘⠜⢌⠪⡨⠂⡐⠨⡀⠠⠄⠄⠤⠤⠤⢤⣔⠥⠢⠢⠔⠥⠥⠮⠴⠥⠵⠤⠐⠠⠐⢈⢉⠁⠅⠨⢠⠡⢁⠢⠐⡀⢆⠄⡀⠄⠄⠄⠄⠂⢀⢂⠐⣀⣡⣈⣠⡑⡌⠂⢅⢊⢘⠒⠒⠒⠊⠚⠪⠧⠗⢜⠐⠐
⣀⣂⢡⡂⡅⠂⡑⡑⡙⠄⠄⠂⢐⠄⠄⠠⠄⠄⢀⠂⡐⢐⠐⢀⠂⠐⠐⠰⠼⠼⢲⢵⣲⡶⡿⠿⠿⠯⠯⠷⠯⠫⡉⢁⠠⠄⡀⠁⠈⠄⠐⠄⠄⠐⠄⡀⠠⠄⠄⠠⠈⡂⡂⠢⢡⢐⣈⣀⣐⡀⡄⡠⡁⠄⠂
⢈⡈⣈⢌⣂⡅⢂⢐⠨⠨⠨⢐⠠⢁⠂⠅⢂⢁⢀⢂⠈⠄⡐⡠⢠⣁⠄⡁⡀⡠⠄⠠⠄⢀⠠⠐⠄⢠⠢⠄⠄⠁⠄⠄⠄⠂⠠⠈⠄⠁⠄⡀⢢⢈⠄⡂⡒⠓⢒⠷⠶⠶⠻⢿⢿⡽⣟⣿⣾⢾⡼⠖⠷⠿⠓
⠕⠜⠜⠜⠜⠚⠓⢒⠨⡘⢌⠰⡈⠔⠨⡨⢂⠢⠨⠨⠉⢁⠂⡈⠄⡂⠅⠄⠠⠄⡈⠐⠄⠄⠠⠄⡁⢐⠌⠂⠈⢀⠈⠄⡀⠠⠄⠂⠁⠄⡀⠄⠄⡈⠄⡒⡌⠆⠠⠄⡐⠄⠄⠄⠠⠈⡈⢉⠁⡀⠄⠰⠈⠄⡀
⠄⠠⠐⠄⡂⢁⠐⠨⠪⡨⠢⢡⠡⡃⢸⢔⠅⢌⢪⢸⠈⡔⠄⡪⠨⡢⡁⠪⡨⡢⠠⡈⡲⠊⠢⠢⠢⠢⠡⢑⠈⠄⡀⠄⠄⡀⠄⠄⠄⢀⢀⢈⣠⡜⠄⡣⡊⡌⠄⢂⠠⠈⠠⠐⠄⠂⢐⠄⠠⢀⠄⠡⠄⠂⠄
⢀⠂⡠⠡⡀⠢⡨⣸⡺⡎⡜⡔⡕⣯⢳⣻⣯⡫⣟⣞⡶⡽⣔⢝⢗⢗⡇⡅⡧⢁⢲⠄⡢⢌⠌⡂⡢⠢⡑⡐⠄⡁⠄⢀⠄⢀⠄⡂⠡⠠⠠⢠⠠⠠⠄⢇⣕⣢⣡⣵⣴⢼⣶⣾⣺⡿⣿⡷⣞⣖⢖⢅⢆⢊⠄
⢐⠡⢂⠅⢌⢌⢢⢱⣟⡧⡣⡣⢪⢺⡪⣷⢗⢝⡞⡗⠯⠫⠚⠛⢋⠓⡅⠇⡓⢰⢡⠁⣎⢎⠪⢪⢨⢣⠢⠨⢸⡰⢄⠄⠠⢀⢒⠎⠓⠷⣳⣪⡺⣝⣿⣿⣿⣿⣺⢿⣿⢝⣯⣿⣺⣿⣟⣿⣷⣷⡗⡕⢕⠔⠅
⢢⡑⡕⠸⠴⠌⠖⠝⠘⠑⠑⠉⡁⠉⡉⠄⠄⠄⠄⠂⠐⠈⡐⡌⡆⡣⢊⠌⡪⢰⣱⠁⣗⣝⡝⣜⢮⣣⠡⠡⠙⡜⡜⡔⡢⢂⠪⡣⡣⡢⠄⠠⢀⠉⠉⠉⠚⠽⠞⢿⡿⣽⢿⡿⣯⣷⣿⢿⠷⣟⡏⡌⢆⠪⡨
⠄⠄⠐⠄⠂⠐⠄⠂⠁⡈⢀⠁⡀⠄⠄⠂⠂⠐⢀⠈⠄⠁⡇⡿⠾⠾⣗⢧⣻⢸⣞⠔⣝⢮⡫⣞⢯⢿⢈⠂⠅⡱⡱⢸⠸⠠⡃⡇⢎⢪⠨⢅⠄⡀⠁⠁⠐⡀⠄⠠⠄⡀⠉⠉⠘⠳⠿⠷⢿⣷⣿⢸⢘⢌⠢
⠄⠐⠈⠠⠈⠈⠠⠈⢀⠠⠄⡀⠠⠄⠄⠂⢈⠠⠄⠂⡈⠄⡃⡪⡘⠭⠩⢛⢛⢘⢍⢐⢍⠣⣃⠎⠊⠁⠠⠠⠁⠄⢎⠢⡣⢑⢕⢕⠥⡡⠣⡢⠄⠄⢈⠄⠂⠄⠂⠐⠠⠄⢁⠁⢈⠠⠄⠄⢀⠄⡈⠈⠈⠂⠑
⠄⠐⠄⠐⠄⠁⠐⢀⠂⠄⠄⠠⢀⠐⢀⠐⡀⠐⢈⠄⠙⡀⢇⢂⠪⡨⠨⡐⡐⡐⡐⢐⢔⢑⢀⠂⠁⠄⠄⠄⡂⣐⢸⢕⣧⢱⢱⢕⣕⢥⠱⡨⡂⢈⠠⠄⡁⢈⠄⠐⡀⠐⠄⠠⠄⠄⠁⠄⠄⢀⠄⠈⠄⠁⠄
⠄⠐⠈⢀⠈⡈⠠⢀⠐⢈⠄⢂⠄⡂⠄⠂⠠⢈⠠⠄⠡⠐⡕⠨⠨⡐⡁⡢⢐⢐⠌⡀⢆⢕⢐⠌⢌⣄⢕⠰⣬⣸⣻⣝⡼⣼⣻⢿⡽⡽⡜⠄⠠⢀⠐⡀⠄⠠⠄⢁⠄⠄⠈⢀⠠⠄⠄⠂⡁⠄⢀⠄⠁⡀⠄
⠄⠂⠁⠄⠂⢀⠂⡐⢀⠂⠈⠄⠂⠂⠬⠐⢃⠂⡊⠹⣐⠨⡪⠨⡈⡂⡪⠨⡂⢕⣨⣨⣢⣦⣥⡧⣵⢰⢘⡙⢗⠿⣞⣯⣿⣳⢯⡯⣯⢯⢪⢂⠠⢀⡦⠢⢐⠠⡈⠠⠄⠂⠈⠄⢀⠠⠄⢐⠄⠠⠄⠄⠄⠄⡀
⠄⢈⠄⠂⠈⢀⠠⠄⠄⠠⠡⠠⠑⠨⠐⠨⡐⠡⡂⠄⡣⠐⠅⠕⠬⢦⢗⢿⡻⣻⣫⡯⣷⣳⡷⣿⣻⣟⣯⣷⣧⣯⣪⢳⣛⢾⣟⣿⢽⣻⢸⡂⠄⢰⢋⠸⡸⡘⡀⢅⢊⠄⡁⡈⡀⠠⠐⠄⠂⢀⠐⠄⡐⡠⡐
⠄⡀⡀⠂⠌⠠⠠⠡⠈⢌⠨⠈⠄⠨⡀⠅⠌⠌⠄⠂⡐⠨⡈⢪⠨⡂⡣⠳⣟⣿⡽⣿⡽⣷⢿⣻⡽⣯⣻⢽⣺⡾⣾⢷⣵⣱⢸⢩⠫⢮⢪⠆⠐⢸⡂⢪⠢⡊⠔⡐⡑⢌⢪⢐⢔⢐⠐⢈⠄⠠⠢⡑⢅⠢⡊
"""
jailEndingText = r"""
     ██╗ █████╗ ██╗██╗         ███████╗███╗   ██╗██████╗ ██╗███╗   ██╗ ██████╗     
     ██║██╔══██╗██║██║         ██╔════╝████╗  ██║██╔══██╗██║████╗  ██║██╔════╝     
     ██║███████║██║██║         █████╗  ██╔██╗ ██║██║  ██║██║██╔██╗ ██║██║  ███╗    
██   ██║██╔══██║██║██║         ██╔══╝  ██║╚██╗██║██║  ██║██║██║╚██╗██║██║   ██║    
╚█████╔╝██║  ██║██║███████╗    ███████╗██║ ╚████║██████╔╝██║██║ ╚████║╚██████╔╝    
 ╚════╝ ╚═╝  ╚═╝╚═╝╚══════╝    ╚══════╝╚═╝  ╚═══╝╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝     
"""
shitEndingText = r"""
   .---. .-. .-.,-. _______   ,---.  .-. .-. ,'|"\   ,-..-. .-.  ,--,   
  ( .-._)| | | ||(||__   __|  | .-'  |  \| | | |\ \  |(||  \| |.' .'    
 (_) \   | `-' |(_)  )| |     | `-.  |   | | | | \ \ (_)|   | ||  |  __ 
 _  \ \  | .-. || | (_) |     | .-'  | |\  | | |  \ \| || |\  |\  \ ( _)
( `-'  ) | | |)|| |   | |     |  `--.| | |)| /(|`-' /| || | |)| \  `-) )
 `----'  /(  (_)`-'   `-'     /( __.'/(  (_)(__)`--' `-'/(  (_) )\____/ 
        (__)                 (__)   (__)               (__)    (__)     
"""
wastedEndingText = r"""
 █     █░ ▄▄▄        ██████ ▄▄▄█████▓▓█████ ▓█████▄    ▓█████  ███▄    █ ▓█████▄  ██▓ ███▄    █   ▄████ 
▓█░ █ ░█░▒████▄    ▒██    ▒ ▓  ██▒ ▓▒▓█   ▀ ▒██▀ ██▌   ▓█   ▀  ██ ▀█   █ ▒██▀ ██▌▓██▒ ██ ▀█   █  ██▒ ▀█▒
▒█░ █ ░█ ▒██  ▀█▄  ░ ▓██▄   ▒ ▓██░ ▒░▒███   ░██   █▌   ▒███   ▓██  ▀█ ██▒░██   █▌▒██▒▓██  ▀█ ██▒▒██░▄▄▄░
░█░ █ ░█ ░██▄▄▄▄██   ▒   ██▒░ ▓██▓ ░ ▒▓█  ▄ ░▓█▄   ▌   ▒▓█  ▄ ▓██▒  ▐▌██▒░▓█▄   ▌░██░▓██▒  ▐▌██▒░▓█  ██▓
░░██▒██▓  ▓█   ▓██▒▒██████▒▒  ▒██▒ ░ ░▒████▒░▒████▓    ░▒████▒▒██░   ▓██░░▒████▓ ░██░▒██░   ▓██░░▒▓███▀▒
░ ▓░▒ ▒   ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░  ▒ ░░   ░░ ▒░ ░ ▒▒▓  ▒    ░░ ▒░ ░░ ▒░   ▒ ▒  ▒▒▓  ▒ ░▓  ░ ▒░   ▒ ▒  ░▒   ▒ 
  ▒ ░ ░    ▒   ▒▒ ░░ ░▒  ░ ░    ░     ░ ░  ░ ░ ▒  ▒     ░ ░  ░░ ░░   ░ ▒░ ░ ▒  ▒  ▒ ░░ ░░   ░ ▒░  ░   ░ 
  ░   ░    ░   ▒   ░  ░  ░    ░         ░    ░ ░  ░       ░      ░   ░ ░  ░ ░  ░  ▒ ░   ░   ░ ░ ░ ░   ░ 
    ░          ░  ░      ░              ░  ░   ░          ░  ░         ░    ░     ░           ░       ░ 
                                             ░                            ░                             
"""
escapedEndingText = r'''
   ___                             _ __              _              ___               _      _              __ _  
  | __|    ___     __     __ _    | '_ \   ___    __| |     o O O  | __|   _ _     __| |    (_)    _ _     / _` | 
  | _|    (_-<    / _|   / _` |   | .__/  / -_)  / _` |    o       | _|   | ' \   / _` |    | |   | ' \    \__, | 
  |___|   /__/_   \__|_  \__,_|   |_|__   \___|  \__,_|   TS__[O]  |___|  |_||_|  \__,_|   _|_|_  |_||_|   |___/  
_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| {======|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| 
"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'./o--000'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-' 
'''
discordModEndingText = r"""
 (                               *                                                 
 )\ )                   (      (  `         (                 (                    
(()/( (            (    )\ )   )\))(        )\ )   (          )\ ) (        (  (   
 /(_)))\ (   (  (  )(  (()/(  ((_)()\  (   (()/(   )\   (    (()/( )\  (    )\))(  
(_))_((_))\  )\ )\(()\  ((_)) (_()((_) )\   ((_)) ((_)  )\ )  ((_)|(_) )\ )((_))\  
 |   \(_|(_)((_|(_)((_) _| |  |  \/  |((_)  _| |  | __|_(_/(  _| | (_)_(_/( (()(_) 
 | |) | (_-< _/ _ \ '_/ _` |  | |\/| / _ \/ _` |  | _|| ' \)) _` | | | ' \)) _` |  
 |___/|_/__|__\___/_| \__,_|  |_|  |_\___/\__,_|  |___|_||_|\__,_| |_|_||_|\__, |  
                                                                           |___/   
"""
safeEndingText = r"""
  ________            _____       ____        ______          ___            
 /_  __/ /_  ___     / ___/____ _/ __/__     / ____/___  ____/ (_)___  ____ _
  / / / __ \/ _ \    \__ \/ __ `/ /_/ _ \   / __/ / __ \/ __  / / __ \/ __ `/
 / / / / / /  __/   ___/ / /_/ / __/  __/  / /___/ / / / /_/ / / / / / /_/ / 
/_/ /_/ /_/\___/   /____/\__,_/_/  \___/  /_____/_/ /_/\__,_/_/_/ /_/\__, /  
                                                                    /____/   
"""
awkwardEndingText = r"""
 _____       _                   _       _____       _ _         
|  _  |_ _ _| |_ _ _ _ ___ ___ _| |     |   __|___ _| |_|___ ___ 
|     | | | | '_| | | | .'|  _| . |_ _ _|   __|   | . | |   | . |
|__|__|_____|_,_|_____|__,|_| |___|_|_|_|_____|_|_|___|_|_|_|_  |
                                                            |___|
"""
stupidEndingText = r"""
   _                               __ _               _     _ ___     __          _ _             
  /_\  _ __ ___  /\_/\___  _   _  / _\ |_ _   _ _ __ (_) __| / _ \   /__\ __   __| (_)_ __   __ _ 
 //_\\| '__/ _ \ \_ _/ _ \| | | | \ \| __| | | | '_ \| |/ _` \// /  /_\| '_ \ / _` | | '_ \ / _` |
/  _  \ | |  __/  / \ (_) | |_| | _\ \ |_| |_| | |_) | | (_| | \/  //__| | | | (_| | | | | | (_| |
\_/ \_/_|  \___|  \_/\___/ \__,_| \__/\__|\__,_| .__/|_|\__,_| ()  \__/|_| |_|\__,_|_|_| |_|\__, |
                                               |_|                                          |___/ 
"""

#Variables
script_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_dir)
mixer.init()
intro1 = "\nAs the final bell rings, you find yourself alone in the classroom with a girl who has chosen to stay behind."
intro2 = "\nThe room is filled with quiet anticipation, and the afternoon sunlight casts a warm glow."
intro3 = "\nIntrigued, you approach her, and she looks up, a smile of recognition crossing her face."
intro4 = "\nIn that moment, you sense the beginning of something where every choice you make will shape the narrative of your story.\n"
end = "\nThank you for playing Gakko Kinesis. Made by Matthew Raymundo and Inspired by the Goat. Goodbye\n"
name = ""
characterName = "Girl"
textSpeed = 0.05
console = Console()

#Effect Functions
def typeWriterEffect(textSpeed, word):
    for char in word:
        sleep(textSpeed)
        sys.stdout.write(char)
        sys.stdout.flush()
    return ""

#Settings
def settingsPage():
    global textSpeed
    typeWriterEffect("\n1. Text Speed\n")
    change = input(typeWriterEffect("\nWhich setting would you like to change? "))
    if change == "1":
        typeWriterEffect("\nWhat would you like to change it to?\n")
        print("\n1. Slow")
        time.sleep(0.5)
        print("\n2. Normal")
        time.sleep(0.5)
        print("\n3. Fast")
        time.sleep(0.5)
        print("\n4. Very Fast")
        time.sleep(0.5)
        print("\n5. Instant")
        time.sleep(0.5)
        textSpeedChoice = input(typeWriterEffect("\nChoose a number: "))
        if textSpeedChoice == "1":
            textSpeed = 0.1
        elif textSpeedChoice == "2":
            textSpeedChoice = 0.05
        elif textSpeedChoice == "3":
            textSpeedChoice = 0.03
        elif textSpeedChoice == "4":
            textSpeed = 0.01
        elif textSpeedChoice == "5":
            textSpeed = 0
        typeWriterEffect(f"\nText speed has been changed to {textSpeed}\n")
    settings = input(typeWriterEffect("\nWould you like to change any other settings? Yes or No? "))
    if settings.lower() == "yes":
        settingsPage()
    else:
        typeWriterEffect("\nSetting applied successfuly.\n")
        gameMenu()

def developerOptions():
    global textSpeed
    console.print(f"[bold green]{developerOptionsText}[/bold green]")
    print("\nText Speed will be set to instant.")
    textSpeed = 0
    time.sleep(1)
    print("\nWhich scene would you like to skip to?")
    time.sleep(0.3)
    print("\n1. Initial Conversation")
    time.sleep(0.3)
    print("\n2. Action Scene 1")
    time.sleep(0.3)
    print("\n3. Flustered Scene")
    time.sleep(0.3)
    print("\n4. Shouts for Help") 
    time.sleep(0.3)
    print("\n5. Run Away")
    time.sleep(0.3)
    print("\n6. Guard stops you")
    time.sleep(0.3)
    print("\n7. Guard doesn't believe you")
    time.sleep(0.3)
    print("\n8. Talk about hobbies")
    time.sleep(0.3)
    print("\n9. Talk about anime")
    time.sleep(0.3)
    skipChoice = input(typeWriterEffect(textSpeed, "\nChoose a number: "))
    print("\n")
    if skipChoice == "1":
        applyDeveloperOptions()
        introductoryConversation()
    elif skipChoice == "2":
        applyDeveloperOptions()
        actionScene1()
    elif skipChoice == "3":
        applyDeveloperOptions()
        flustered()
    elif skipChoice == "4":
        applyDeveloperOptions()
        shoutForHelp()
    elif skipChoice == "5":
        applyDeveloperOptions()
        runAway()
    elif skipChoice == "6":
        applyDeveloperOptions()
        smallTalk()
    elif skipChoice == "7":
        applyDeveloperOptions()
        return None
    elif skipChoice == "8":
        applyDeveloperOptions()
        hobbiesSmallTalk()
    elif skipChoice == "9":
        applyDeveloperOptions()
        animeSmallTalk()
        
def applyDeveloperOptions():
    with console.status("[bold green]Developer options being applied...[/bold green]", spinner="material") as status:
        time.sleep(3)
    console.print("[bold green]Developer options applied successfully.[bold green]\n")
    time.sleep(1)
    subprocess.run("cls", shell=True)

#Story Functions
def gameIntro():
    global name
    name = input("What is your name? ")
    time.sleep(1)
    print("\nHello, " + name + ".")
    time.sleep(1)
    print("\nYou have been given the gift of telekinesis, the ability to move objects with your mind. ")
    time.sleep(1)
    print("\nYou are about to embark on a journey that will test the limits of your power. ")
    time.sleep(1)
    print("\nYour choices will determine the outcome of your story.\n")
    time.sleep(1)
    readyPrompt()
        
def readyPrompt():
    ready = input(typeWriterEffect(textSpeed, "Are you ready to begin? "))
    if ready.lower() == "yes":
        print("\nLet's begin.")
        time.sleep(1)
        subprocess.run("cls", shell=True)
        typeWriterEffect(textSpeed, intro1 + intro2 + intro3 + intro4)
        introductoryConversation()
    elif ready.lower() == "no":
        typeWriterEffect(textSpeed, "\nWhy'd you even start the game then...")
        time.sleep(1)
        typeWriterEffect(0.5, "\nDumbass")
        time.sleep(1)
        exit()
    else:
        typeWriterEffect(textSpeed, "\nTf are you sayin bro?")
        time.sleep(1)
        typeWriterEffect(textSpeed, "\nLet's try that again shall we?")
        time.sleep(3)
        subprocess.run("cls", shell=True)
        readyPrompt()
        
def introductoryConversation():
    global characterName
    mixer.music.fadeout(1000)
    mixer.music.load("Music/Enchanting Serenade.mp3")
    mixer.music.play(-1)
    typeWriterEffect(textSpeed, "\nThe girl sits at her desk, her presence commanding attention in the otherwise empty classroom.")
    typeWriterEffect(textSpeed, "\nShe possesses an ethereal beauty that seems to defy description—a Japanese heritage evident in her delicate features and porcelain skin, as white as freshly fallen snow.")
    typeWriterEffect(textSpeed, "\nHer ebony hair is like a cascade of silk, flowing effortlessly down her back, contrasting beautifully against her fair complexion.")
    typeWriterEffect(textSpeed, "\nHer almond-shaped eyes, the color of onyx, hold a depth and radiance that seems to draw you in, leaving you mesmerized by their allure.\n")
    typeWriterEffect(textSpeed, "\n\n\nNow, as you stand before her, you have the opportunity to engage in conversation. The choices before you are:\n")
    time.sleep(1)
    print("\n1. Ask her how she is: Show genuine concern and ask her how she's doing, eager to engage in a deeper conversation and understand her current state of mind.")
    time.sleep(1)
    print("\n2. Ask her name: Curiously inquire about her name, eager to establish a personal connection and learn more about her identity.")
    time.sleep(1)
    print("\n3. Compliment her beauty: Unable to resist, you express your admiration for her stunning appearance, hoping to make a positive impression and potentially spark a deeper conversation.")
    time.sleep(1)
    choice = input(typeWriterEffect(textSpeed, "\nWhich will you choose? "))
    if choice == "1":
        typeWriterEffect(textSpeed, "\nYou: 'Hey, I noticed you stayed behind. How are you doing?'")
        typeWriterEffect(textSpeed, f"\n{characterName}: pauses, looking up from her book 'Oh, I'm doing alright, thank you'\n")
        actionScene1()
    elif choice == "2":
        typeWriterEffect(textSpeed, "\nYou: 'Hi there, I don't think we've officially met. What's your name?'")
        typeWriterEffect(textSpeed, f"\n{characterName}: 'I'm Yuki. It's nice to meet you. And you are?'")
        typeWriterEffect(textSpeed, "\nYou: 'I'm " + name + ". It's a pleasure to meet you, Yuki.'\n")
        characterName = "Yuki"
        actionScene1()
    elif choice == "3":
        typeWriterEffect(textSpeed, "\nYou: 'Excuse me, but I couldn't help but notice how stunning you look. Your beauty is truly captivating.'")
        typeWriterEffect(textSpeed, f"\n{characterName}: blushes, her smile widening 'Thank you, that's really kind of you to say. I appreciate it.'\n")
        actionScene1()

def actionScene1():
    mixer.music.fadeout(1000)
    mixer.music.load("Music/Serenade of the Sakura Blossoms.mp3")
    mixer.music.play(-1)
    if characterName == "Girl":
        typeWriterEffect(textSpeed, "\n\n\nAs you continue to converse with the girl, you decided on what lewd action to take next—whether to use your telekinesis powers or not.\n")
    else:
        typeWriterEffect(textSpeed, f"\n\n\nAs you continue to converse with {characterName}, you decided on what lewd action to take next—whether to use your telekinesis powers or not:\n")
    time.sleep(1)
    print("\n1. Use your telekinesis powers to masturbate her pussy\n")
    time.sleep(1)
    print("\n2. Approach her and kiss her\n")
    time.sleep(1)
    print("\n3. Grab her and hug her\n")
    time.sleep(1)
    print("\n4. Make small talk\n")
    time.sleep(1)
    choice = input(typeWriterEffect(textSpeed, "\nWhich will you choose? "))
    if choice == "1":
        flustered()
    elif choice == "2":
        return None
    elif choice == "3":
        shoutForHelp()
    elif choice == "4":
        smallTalk()

def flustered():
    typeWriterEffect(textSpeed, "\n\n\nAs you start to masturbate her using your telekinesis powers, she starts to get flustered.")
    typeWriterEffect(textSpeed, "\nHer face turns beet-red and sweat starts to form on the surface of her porcelain skin.\n")
    typeWriterEffect(textSpeed, "\nYou: 'Are you okay? Are you having any problems?'")
    typeWriterEffect(textSpeed, f"\n{characterName}: 'I-I'm okay, th-there's no problems'")
    typeWriterEffect(textSpeed, "\nYou: 'Are you sure? You don't seem fine?'")
    typeWriterEffect(textSpeed, f"\n{characterName}: 'N-no, I-I'm sure it n-nothing... Uugh...'")
    typeWriterEffect(textSpeed, "\nYou grab her by the hand and say: 'I'm here for you if you need anything...'")
    typeWriterEffect(textSpeed, "")
    
def shoutForHelp():
    typeWriterEffect(textSpeed, f"\n{characterName}: 'Hey! Get off me! What are you doing?!'")
    typeWriterEffect(textSpeed, "\nYou: 'Just stay quiet and behave yourself, I won't hurt you.'\n")
    typeWriterEffect(textSpeed, "\nYou continue to grip her, trying to stop her limbs from moving...")
    typeWriterEffect(textSpeed, f"\n{characterName}: 'Stop touching me!'")
    typeWriterEffect(textSpeed, "\nYou: 'Just stop moving, I'll make this quick.'")
    typeWriterEffect(textSpeed, f"\n{characterName}: 'STOP IT!!! SOMEONE HELP ME!!!'\n")
    typeWriterEffect(textSpeed, "\n\n\nAs she starts screaming, you have no choice but to make a decision:\n")
    time.sleep(1)
    print("\n1. Cover her mouth to stop her from screaming")
    time.sleep(1)
    print("\n2. Run away")
    time.sleep(1)
    shoutAction = input(typeWriterEffect(textSpeed, "\nWhich will you choose? "))
    if shoutAction == "1":
        coverHerMouth()
    elif shoutAction == "2":
        runAway()
    
def runAway():
    typeWriterEffect(textSpeed, "\nYou decide to escape while you still can.")
    typeWriterEffect(textSpeed, "\nAs you run out the classroom, you still hear her screams echoing through the empty hallways.")
    typeWriterEffect(textSpeed, "\nGuilt and fear consume you as you run away from the scene.")
    typeWriterEffect(textSpeed, "\n\n\nDespite this difficult mental situation, you must decide where to escape to: \n")
    time.sleep(1)
    print("\n1. Hide inside the school toilet and wait for the situation to calm down")
    time.sleep(1)
    print("\n2. Jump out of the window to make a quick escape")
    time.sleep(1)
    print("\n3. Run to the school's entrance and escape to another location")
    time.sleep(1)
    runAwayChoice = input(typeWriterEffect(textSpeed, "\nWhich will you choose? "))
    if runAwayChoice == "1":
        typeWriterEffect(textSpeed, "\nYou decide to run to a toilet stall and wait for the situation to calm down.")
        typeWriterEffect(textSpeed, "\nYou run towards one of the further school toilets and hide inside the stall, locking the door behind you.")
        typeWriterEffect(textSpeed, "\nYou hear footsteps fast approaching from the hallway, the door opens and multiple teachers come in.")
        typeWriterEffect(textSpeed, "\nYou are caught and taken to the principal's office while authorities are called.")
        shitEnding()
    elif runAwayChoice == "2":
        typeWriterEffect(textSpeed, "\nYou decide to jump out of the window to make a quick escape.")
        typeWriterEffect(textSpeed, "\nYou: 'Fuck it, I'll just have to jump out the fucking window.'")
        typeWriterEffect(textSpeed, "\nYou run towards one of the open windows inside the classroom and take a great leap.")
        typeWriterEffect(textSpeed, "\nThe air rushes past you as you freefall..")
        typeWriterEffect(textSpeed, "\nYou feel the adrenaline coursing through your veins until..")
        typeWriterEffect(textSpeed, "\nyou hit the ground... badly...")
        typeWriterEffect(textSpeed, "\nYou scream as a wave of pain and agony washes over you.")
        typeWriterEffect(textSpeed, "\nYou look down at your legs and you see them twisted and broken...")
        typeWriterEffect(textSpeed, "\nYour bones were snapped, blood seeping from your wounds...\n")
        wastedEnding()
    elif runAwayChoice == "3":
        guardStopsYou()
        
def guardStopsYou():
    typeWriterEffect(textSpeed, "\nYou decide to run to the school's entrance and escape to another location.")
    typeWriterEffect(textSpeed, "\nYou run out of the classroom, running through the hallways going past any students and teachers.")
    typeWriterEffect(textSpeed, "\nYou are finally approaching the school entrance, but you are stopped by the school's security guard.")
    typeWriterEffect(textSpeed, "\n\n\nHe doesn't know the situation yet so what excuse will you give him?\n")
    time.sleep(1)
    print("\n1. Tell him that you are feeling sick and need to go home")
    time.sleep(1)
    print("\n2. Tell him that there has been a terrorist attack in-campus")
    time.sleep(1)
    print("\n3. Tell him that you're late for a date with the principal's daughter")
    time.sleep(1)
    runAwayChoice = input(typeWriterEffect(textSpeed, "\nWhich will you choose? "))
    if runAwayChoice == "1":
        return None

def coverHerMouth():
    typeWriterEffect(textSpeed, "\nYou decide to cover her mouth to stop her from screaming.")
    typeWriterEffect(textSpeed, "\nShe struggled to scream, but it was now too late for you.")
    typeWriterEffect(textSpeed, "\nYou hear footsteps fast approaching from the hallway, the door opens and multiple teachers come in.")
    typeWriterEffect(textSpeed, "\nYou are caught and taken to the principal's office while authorities are called.")
    jailEnding()

def smallTalk():
    typeWriterEffect(textSpeed, "\n\n\nAs you decide to make small talk with her, you think of topics to talk about:\n")
    typeWriterEffect(textSpeed, "\n1. Talk about both of your hobbies\n")
    typeWriterEffect(textSpeed, "\n2. Talk about anime\n")
    typeWriterEffect(textSpeed, "\n3. Talk about how you are a racist\n")
    smallTalkTopic = input(typeWriterEffect(textSpeed, "\nWhich one will you choose? "))
    if smallTalkTopic == "1":
        mixer.music.fadeout(1000)
        mixer.music.load("Music/Shared Passions.mp3")
        mixer.music.play(-1)
        typeWriterEffect(textSpeed, "\n\n\nYou: 'So, what are your hobbies? You seem like the type of person who likes to read and draw. Am I right?'")
        typeWriterEffect(textSpeed, f"\n{characterName}: 'Haha, you're right. I do like to read and draw. What about you? What are your hobbies?\n")
        hobbiesSmallTalk()
        talkAboutMore()
    elif smallTalkTopic == "2":
        mixer.fadeout(1000)
        mixer.music.load("Music/Anime Love's Melody.mp3")
        mixer.music.play(-1)
        typeWriterEffect(textSpeed, "\n\n\nYou: 'Hey, I noticed that you have an anime keychain in your bag. Do you like anime?'")
        typeWriterEffect(textSpeed, f"\n{characterName}: 'Oh definitely! I love anime, I've been watching it since I was a kid. What about you?'")
        typeWriterEffect(textSpeed, "\nYou: 'I really like anime too. I've been watching it for a while now. Which one's your favorite?'")
        typeWriterEffect(textSpeed, f"\n{characterName}: 'Well, I recently finished Gintama and it made me laugh a lot so I guess that's my favorite for now. What about yours?'\n")
        animeSmallTalk()
    elif smallTalkTopic == "3":
        mixer.fadeout(1000)
        mixer.music.load("Music/You Gotta Move.mp3")
        mixer.music.play()
        typeWriterEffect(textSpeed, "\n\n\nYou: 'I'm a racist.'")
        typeWriterEffect(textSpeed, f"\n{characterName}: 'That is very concerning. I don't think we should talk anymore. Goodbye.")
        typeWriterEffect(textSpeed, "\nYou: 'Wait, I didn't mean it like that! I'm sorry!\n'")
        typeWriterEffect(textSpeed, "\nShe leaves the room and you are left alone, feeling a sense of regret and disappointment.\n")
        stupidEnding()
        
def talkAboutMore():
    typeWriterEffect(textSpeed, "\nWould you like to talk to her more or end the conversation?\n")
    typeWriterEffect(textSpeed, "\n1. Talk to her more about other topics\n")
    typeWriterEffect(textSpeed, "\n2. End the conversation\n")
    talkAboutMoreChoice = input(typeWriterEffect(textSpeed, "\nWhich one will you choose? "))
    if talkAboutMoreChoice == "1":
        smallTalk()
    elif talkAboutMoreChoice == "2":
        safeEnding()

def hobbiesSmallTalk():
    print("\n\n\nWhat are your hobbies?")
    time.sleep(1)
    print("\n1. Playing video games")
    time.sleep(1)
    print("\n2. Photography")
    time.sleep(1)
    print("\n3. Playing the piano")
    time.sleep(1)
    print("\n4. Moderating a Discord server")
    time.sleep(1)
    hobbiesChoice = input(typeWriterEffect(textSpeed, "\nWhich one will you choose? "))
    if hobbiesChoice == "1":
        typeWriterEffect(textSpeed, "\nYou: 'Right now, I really like playing video games, sometimes competitively, sometimes with friends.'")
        typeWriterEffect(textSpeed, "\nYou: 'I've even been able to play in some competitive esports tournaments.'")
        typeWriterEffect(textSpeed, f"\n{characterName}: 'Interesting, I rarely play video games because there's so much stuff to do for school.'")
        typeWriterEffect(textSpeed, "\nYou: 'Well I'm playing to get a potential profession out of it so I make time for gaming.'")
        typeWriterEffect(textSpeed, f"\n{characterName}: 'It's good that you are already thinking about your future.\n'")
        typeWriterEffect(textSpeed, "\nBoth of you continue to talk about your hobbies for a while...\n")
        talkAboutMore()
    elif hobbiesChoice == "2":
        typeWriterEffect(textSpeed, "\nYou: 'Photography is one of my main hobbies.'")
        typeWriterEffect(textSpeed, "\nYou: 'I really love preserving the beauty and the memories of this world.'")
        typeWriterEffect(textSpeed, f"\n{characterName}: 'Ooohhh, photography huh, you must be really creative for that.'")
        typeWriterEffect(textSpeed, f"\n{characterName}: 'Maybe you could take pictures of me next time for my Instagram posts hahaha.'")
        typeWriterEffect(textSpeed, "\nYou: 'Well sure, why not? It would be a good opportunity for me to practice while you get free pictures.\n'")
        typeWriterEffect(textSpeed, "\nBoth of you continue to talk about your hobbies for a while...\n")
        talkAboutMore()
    elif hobbiesChoice == "3":
        typeWriterEffect(textSpeed, "\nYou: 'I started learning how to play the piano a few years back, so that's probably one of my hobbies right now.'")
        typeWriterEffect(textSpeed, f"\n{characterName}: 'Ahh, so you're the musically inclined type. Music is definitely not my strength.'")
        typeWriterEffect(textSpeed, "\nYou: 'Don't be so negative, music can be learned. You just need a ton of practice for sure.'")
        typeWriterEffect(textSpeed, f"\n{characterName}: 'I'm really horrible at reading music notes, I gave up a long time ago hahaha.\n'")
        typeWriterEffect(textSpeed, "\nBoth of you continue to talk about your hobbies for a while...\n")
        talkAboutMore()
    elif hobbiesChoice == "4":
        typeWriterEffect(textSpeed, "\nYou: 'Uhhmm actually, I have a job already.'")
        typeWriterEffect(textSpeed, f"\n{characterName}: 'Okay wow, so what is it?'")
        typeWriterEffect(textSpeed, "\nYou: 'Well, I don't want to brag but I'm one of the moderators for the Roblox Discord server.'")
        typeWriterEffect(textSpeed, "\nShe suddenly bursts into laughter")
        typeWriterEffect(textSpeed, f"\nYou: 'Wait wait hold on, you're—a Discord mod???'")
        typeWriterEffect(textSpeed, "\nYou: 'Yeah? What's wrong about that?'")
        typeWriterEffect(textSpeed, "\nYou: 'That's actually disgusting, I bet you don't shower. Please don't talk to me ever again.'")
        discordModEnding()
    

def animeSmallTalk():
    print("\n\n\nWhich anime is your favorite?")
    time.sleep(1)
    print("\n1. One Piece")
    time.sleep(1)
    print("\n2. Jujutsu Kaisen")
    time.sleep(1)
    print("\n3. Gintama")
    time.sleep(1)
    print("\n4. I don't watch anime")
    time.sleep(1)
    animeChoice = input(typeWriterEffect(textSpeed, "\nWhich one will you choose? "))
    if animeChoice == "1":
        typeWriterEffect(textSpeed, "\nYou: 'One Piece is my favorite, I'm not only caught up to the anime but I also read the manga!")
        typeWriterEffect(textSpeed, f"\n{characterName}: 'Wow, that's impressive! I'm not caught up to the anime yet but so far, I'm really enjoying it.'")
        typeWriterEffect(textSpeed, "\nYou: 'Just keep watching, it gets wayyyy better when Luffy unlocks his next form!'")
        typeWriterEffect(textSpeed, f"\n{characterName}: 'Heyyyy, no spoilers! I'm only at the part where they're at Dressrosa.'")
        typeWriterEffect(textSpeed, "\nYou: 'HAHAHAHAHAHA, I'm sorry but just keep watching I promise it becomes so good!'\n")
        typeWriterEffect(textSpeed, "\nBoth of you continue to talk about your favorite anime as the sun starts to set...\n")
        talkAboutMore()
    elif animeChoice == "2":
        typeWriterEffect(textSpeed, "\nYou: 'Jujutsu Kaisen is my favorite, I was skeptical at first but it's really good.'")
        typeWriterEffect(textSpeed, "\nYou: 'I tried watching the first season first then I got so hooked that I'm now caught up to the manga.'")
        typeWriterEffect(textSpeed, f"\n{characterName}: 'By any chance, are you part of r/Jujutsufolk?'")
        typeWriterEffect(textSpeed, "\nYou: 'Yeah, I'm a part of that subreddit, it's too funny to not be a part of it.'")
        typeWriterEffect(textSpeed, f"\n{characterName}: 'Ahhh I see, you're a Jujutsufolker too. Well, I hope Gojo uses Lime Green when he comes back.'")
        typeWriterEffect(textSpeed, "\nYou: 'Yep, but will he stand proud because of Lime Green, or does he have Lime Green because he's standing proud?'")
        typeWriterEffect(textSpeed, f"\n{characterName}: 'Hahahaha, I think he's simply Him'")
        typeWriterEffect(textSpeed, "\nBoth of you continue to talk about your favorite anime as the sun starts to set...\n")
        talkAboutMore()
    elif animeChoice == "3":
        typeWriterEffect(textSpeed, "\nYou: 'Gintama is also my favorite, it's a really funny anime that I can't stop laughing at.'")
        typeWriterEffect(textSpeed, f"\n{characterName}: 'Mannn, Gintama is sooo good. It feels nostalgic thinking about it now.'")
        typeWriterEffect(textSpeed, "\nYou: 'It's like the first anime that really made me physically laugh out loud. It's definitely a hidden gem.'")
        typeWriterEffect(textSpeed, f"\n{characterName}: 'Yeah for sure, more people should watch it. I'm glad I found someone who also likes Gintama.'")
        typeWriterEffect(textSpeed, "\nYou: 'I never would've thought I'd meet someone who also likes Gintama, we're a rare breed.'")
        typeWriterEffect(textSpeed, f"\n{characterName}: 'Well, at least we know each other now, hahahaha.'\n")
        typeWriterEffect(textSpeed, "\nBoth of you continue to talk about your favorite anime as the sun starts to set...\n")
        talkAboutMore()
    elif animeChoice == "4":
        typeWriterEffect(textSpeed, "\nYou: 'I don't watch anime.'")
        typeWriterEffect(textSpeed, f"\n{characterName}: 'Oh, that's okay. I guess we can talk about something else.'")
        typeWriterEffect(textSpeed, "\nYou: 'Yeah, I'm sorry. I don't really like anime that much.'")
        typeWriterEffect(textSpeed, f"\n{characterName}: 'It's fine, I'm sure we can find something else to talk about.'")
        typeWriterEffect(textSpeed, "\nYou: 'Yeah, I'm sure we can...'\n")
        awkwardEnding()

def jailEnding():
    typeWriterEffect(textSpeed, "\nYou were arrested and taken to jail for your actions.")
    if characterName == "Girl":
        typeWriterEffect(textSpeed, "\nThe girl you assaulted was taken to the hospital and treated for her injuries.")
    else:
        typeWriterEffect(textSpeed, f"\n{characterName}, who you assaulted, was taken to the hospital and treated for her injuries.")
    typeWriterEffect(textSpeed, "\nHer parents pressed charges and you were sentenced to 10 years in prison.")
    typeWriterEffect(textSpeed, "\nYou are now a registered sex offender " + name + "...")
    typeWriterEffect(textSpeed, "\nTake some time to reflect on your actions and think about what you've done.\n")
    typeWriterEffect(0.01, jailEndingText)
    
def shitEnding():
    typeWriterEffect(textSpeed, "\nLMAO, what did you think would happen?")
    typeWriterEffect(textSpeed, "\nYou really thought they wouldn't find you? In the damn toilet?")
    typeWriterEffect(textSpeed, "\nYou deserve to not only go to jail but also to eat shit.\n")
    typeWriterEffect(0.01, shitEndingText)

def wastedEnding():
    typeWriterEffect(textSpeed, "\nAfter your fall, you were rushed to the hospital for emergency surgery.")
    if characterName == "Girl":
        typeWriterEffect(textSpeed, "\nThe girl you assaulted was taken to the hospital and treated for her injuries.")
    else:
        typeWriterEffect(textSpeed, f"\n{characterName}, who you assaulted, was taken to the hospital and treated for her injuries.")
    typeWriterEffect(textSpeed, "\nHer parents pressed charges and you were sentenced to 10 years in prison.")
    typeWriterEffect(textSpeed, "\nYou are now not only injured, but also registered sex offender " + name + "...")
    typeWriterEffect(textSpeed, "\nYou were really stupid to jump out of the window, did you think your legs could take 5 stories?")
    time.sleep(3)
    typeWriterEffect(textSpeed, "\nDumbass...\n")
    typeWriterEffect(0.01, wastedEndingText)

def escapedEnding():
    typeWriterEffect(0.01, escapedEndingText)

def discordModEnding():
    typeWriterEffect(textSpeed, "\nYour dumbass really told a girl that you were a Discord mod...")
    typeWriterEffect(textSpeed, "\nYou deserve no bitches for life.")
    typeWriterEffect(0.01, None)

def safeEnding():
    typeWriterEffect(textSpeed, "\nYou: 'Sorry, I have to get going now. It was nice meeting you.\n")
    if characterName == "Girl":
        typeWriterEffect(textSpeed, f"{characterName}: 'Likewise, take care.\n")
    else:
        typeWriterEffect(textSpeed, f"{characterName}: 'Likewise, take care {name}.\n")
    typeWriterEffect(textSpeed, "\nAs the conversation comes to an end, a sense of satisfaction fills the air.")
    typeWriterEffect(textSpeed, "\nWith a smile, you gather your belongings, ready to bid the girl farewell.")
    typeWriterEffect(textSpeed, "\nAs you walk away, you carry the memory of this meaningful encounter, cherishing the magic of connection and the potential for something more.\n")
    typeWriterEffect(0.01, safeEndingText)

def awkwardEnding():
    typeWriterEffect(textSpeed, "\nOops, that was kinda awkward...")
    typeWriterEffect(textSpeed, "\nYa'll didn't know what to talk about afterwards so you just left lmao...")
    typeWriterEffect(0.01, awkwardEndingText)
    
def stupidEnding():
    typeWriterEffect(textSpeed, f"\nWhy would you even do that {name}? You are a disgrace to humanity.\n")
    typeWriterEffect(0.01, stupidEndingText)

def replayOrQuit():
    typeWriterEffect(textSpeed, "\n\n\nWould you like to replay the game or quit?")
    time.sleep(1)
    print("\n1. Replay")
    time.sleep(1)
    print("\n2. Quit")
    replayOrQuitChoice = input(typeWriterEffect(textSpeed, "\nWhich one will you choose? "))
    if replayOrQuitChoice == "1":
        introductoryConversation()
    elif replayOrQuitChoice == "2":
        print("\nGoodbye.")
        time.sleep(1)
        exit()

#Game Menu
def gameMenu():
    mixer.music.load("Music/Whispers in the Hallway.mp3")
    mixer.music.play(loops=-1)
    typeWriterEffect(0.0005, gameMenuText)
    menuChoice = input("\nChoose a number: ")
    if menuChoice == "1":
        subprocess.run("cls", shell=True)
        print("\n")
        with console.status("[bold green]Loading game...\n"):
                time.sleep(3)
        console.print("[bold green]Loaded game successfully![/bold green]")
        time.sleep(1)
        subprocess.run("cls", shell=True)
        typeWriterEffect(0.001, loadingSplashScreen)
        time.sleep(1)
        subprocess.run("cls", shell=True)
        gameIntro()
    elif menuChoice == "2":
        subprocess.run("cls", shell=True)
        settingsPage()
        subprocess.run("cls", shell=True)
    elif menuChoice == "3":
        subprocess.run("cls", shell=True)
        typeWriterEffect(textSpeed, "Really?")
        typeWriterEffect(1, "\n...")
        typeWriterEffect(textSpeed, "\nI thought you wanted to play the game?")
        typeWriterEffect(1, "\n...")
        typeWriterEffect(textSpeed, "\nFine...")
        time.sleep(1)
        exit()
    elif menuChoice == "123":
        developerOptions()

#Game Structure
gameMenu()
typeWriterEffect(textSpeed, end)
replayOrQuit()