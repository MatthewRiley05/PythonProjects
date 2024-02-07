#Libraries
import sys, subprocess
import time
from time import sleep
from rich.console import Console

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
safeEndingText = r"""
  ________            _____       ____        ______          ___            
 /_  __/ /_  ___     / ___/____ _/ __/__     / ____/___  ____/ (_)___  ____ _
  / / / __ \/ _ \    \__ \/ __ `/ /_/ _ \   / __/ / __ \/ __  / / __ \/ __ `/
 / / / / / /  __/   ___/ / /_/ / __/  __/  / /___/ / / / /_/ / / / / / /_/ / 
/_/ /_/ /_/\___/   /____/\__,_/_/  \___/  /_____/_/ /_/\__,_/_/_/ /_/\__, /  
                                                                    /____/   
"""
jailEndingText = r"""
     ██╗ █████╗ ██╗██╗         ███████╗███╗   ██╗██████╗ ██╗███╗   ██╗ ██████╗     
     ██║██╔══██╗██║██║         ██╔════╝████╗  ██║██╔══██╗██║████╗  ██║██╔════╝     
     ██║███████║██║██║         █████╗  ██╔██╗ ██║██║  ██║██║██╔██╗ ██║██║  ███╗    
██   ██║██╔══██║██║██║         ██╔══╝  ██║╚██╗██║██║  ██║██║██║╚██╗██║██║   ██║    
╚█████╔╝██║  ██║██║███████╗    ███████╗██║ ╚████║██████╔╝██║██║ ╚████║╚██████╔╝    
 ╚════╝ ╚═╝  ╚═╝╚═╝╚══════╝    ╚══════╝╚═╝  ╚═══╝╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝     
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
stupidEndingText = r"""
   _                               __ _               _     _ ___     __          _ _             
  /_\  _ __ ___  /\_/\___  _   _  / _\ |_ _   _ _ __ (_) __| / _ \   /__\ __   __| (_)_ __   __ _ 
 //_\\| '__/ _ \ \_ _/ _ \| | | | \ \| __| | | | '_ \| |/ _` \// /  /_\| '_ \ / _` | | '_ \ / _` |
/  _  \ | |  __/  / \ (_) | |_| | _\ \ |_| |_| | |_) | | (_| | \/  //__| | | | (_| | | | | | (_| |
\_/ \_/_|  \___|  \_/\___/ \__,_| \__/\__|\__,_| .__/|_|\__,_| ()  \__/|_| |_|\__,_|_|_| |_|\__, |
                                               |_|                                          |___/ 
"""

#Variables
intro1 = "\nAs the final bell rings, you find yourself alone in the classroom with a girl who has chosen to stay behind."
intro2 = "\nThe room is filled with quiet anticipation, and the afternoon sunlight casts a warm glow."
intro3 = "\nIntrigued, you approach her, and she looks up, a smile of recognition crossing her face."
intro4 = "\nIn that moment, you sense the beginning of something where every choice you make will shape the narrative of your story.\n"
end = "\nThank you for playing Gakko Kinesis. Goodbye.\n"
name = ""
characterName = "Girl"
textSpeed = 0.05

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

#Story Functions
def gameStart():
    global name
    name = input("What is your name? ")
    time.sleep(1)
    print("\nHello, " + name + ".")
    time.sleep(1)
    print("\nYou have been given the gift of telekinesis, the ability to move objects with your mind. ")
    time.sleep(3)
    print("\nYou are about to embark on a journey that will test the limits of your power. ")
    time.sleep(3)
    print("\nYour choices will determine the outcome of your story.\n")
    time.sleep(3)
    ready = input(typeWriterEffect(textSpeed, "Are you ready to begin? "))
    if ready.lower() == "yes":
        print("\nLet's begin.")
        time.sleep(1)
        subprocess.run("cls", shell=True)
        typeWriterEffect(textSpeed, intro1 + intro2 + intro3 + intro4)
        introductoryConversation()
    else:
        print("\nGoodbye.")
        time.sleep(1)
        exit()
        
def introductoryConversation():
    global characterName
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
        typeWriterEffect(textSpeed, "\nYou: 'So, what are your hobbies? You seem like the type of person who likes to read and draw. Am I right?'")
        typeWriterEffect(textSpeed, f"\n{characterName}: 'Haha, you're right. I do like to read and draw. What about you? What are your hobbies?")
        typeWriterEffect(textSpeed, "\nYou: 'I love writing and playing video games. I'm currently writing a romance novel. I also like to play the piano when I have time.'")
        typeWriterEffect(textSpeed, f"\n{characterName}: Wow, we have Mr. Talented over here.\n")
        typeWriterEffect(textSpeed, "\nBoth of you continue to talk about your hobbies for a while...\n")
        talkAboutMore()
    elif smallTalkTopic == "2":
        typeWriterEffect(textSpeed, "\nYou: 'Hey, I noticed that you have an anime keychain. Do you like anime?'")
        typeWriterEffect(textSpeed, f"\n{characterName}: 'Oh definitely! I love anime, I've been watching it since I was a kid. What about you?'")
        typeWriterEffect(textSpeed, "\nYou: 'I like anime too. I've been watching it for a while now. Which one's your favorite?'")
        typeWriterEffect(textSpeed, f"\n{characterName}: 'Well, I recently finished Gintama and it made me laugh a lot so I guess that's my favorite for now. What about you?'\n")
        animeSmallTalk()
        talkAboutMore()
    elif smallTalkTopic == "3":
        typeWriterEffect(textSpeed, "\nYou: 'I'm a racist.'")
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
        typeWriterEffect(textSpeed, "\nBoth of you continue to talk about One Piece as the sun starts to set...\n")
    
def jailEnding():
    typeWriterEffect(textSpeed, "\nYou were arrested and taken to jail for your actions.")
    if name == "Girl":
        typeWriterEffect(textSpeed, "\nThe girl you assaulted was taken to the hospital and treated for her injuries.")
    else:
        typeWriterEffect(textSpeed, f"\n{characterName}, who you assaulted, was taken to the hospital and treated for her injuries.")
    typeWriterEffect(textSpeed, "\nHer parents pressed charges and you were sentenced to 10 years in prison.")
    typeWriterEffect(textSpeed, "\nYou are now a registered sex offender " + name + "...")
    typeWriterEffect(textSpeed, "\nTake some time to reflect on your actions and think about what you've done.\n")
    typeWriterEffect(0.01, jailEndingText)

def safeEnding():
    typeWriterEffect(textSpeed, "\nYou: 'Sorry, I have to get going now. It was nice meeting you.\n")
    if characterName == "Yuki":
        typeWriterEffect(textSpeed, f"{characterName}: 'Likewise, take care {name}.\n")
    else:
        typeWriterEffect(textSpeed, f"{characterName}: 'Likewise, take care.\n")
    typeWriterEffect(textSpeed, "\nAs the conversation comes to an end, a sense of satisfaction fills the air.")
    typeWriterEffect(textSpeed, "\nWith a smile, you gather your belongings, ready to bid the girl farewell.")
    typeWriterEffect(textSpeed, "\nAs you walk away, you carry the memory of this meaningful encounter, cherishing the magic of connection and the potential for something more.\n")
    typeWriterEffect(0.01, safeEndingText)
    
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
    typeWriterEffect(0.0005, gameMenuText)
    menuChoice = input("\nChoose a number: ")
    if menuChoice == "1":
        subprocess.run("cls", shell=True)
        console = Console()
        print("\n")
        with console.status("[bold green]Loading game...\n"):
                time.sleep(3)
        console.print("[bold green]Loaded game successfully![/bold green]")
        time.sleep(1)
        subprocess.run("cls", shell=True)
        typeWriterEffect(0.001, loadingSplashScreen)
        time.sleep(1)
        subprocess.run("cls", shell=True)
        gameStart()
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

#Game Structure
gameMenu()
typeWriterEffect(textSpeed, end)
replayOrQuit()