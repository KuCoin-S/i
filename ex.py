# Import module
import asyncio
import random
import re
import subprocess
import sys
import time
import tkinter as tk
from time import sleep
from tkinter import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from urllib.parse import urljoin

import aiohttp
from aiohttp.client import ClientSession


class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    lightgrey = '\033[37m'
    darkgrey = '\033[90m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


import requests
#
# response = requests.get("https://ipgeolocation.abstractapi.com/v1/?api_key=a172e77c9dc4438597857fbacb538008")
# print(response.status_code)
# print(response.content)

# print("Cleaning mode is in progress")
# bad_words = ['blog', 'terms', 'themes', 'slide', 'google', 'wp-json', '.json', 'CSS', 'shop', 'purchase']
# with open('hitscleanedup.txt') as oldfile, open('better.txt', 'a') as newfile:
#     for line in oldfile:
#         if not any(bad_word in line for bad_word in bad_words):
#             newfile.write(line)
# print("what a messy house stage 2 activated")
#
# print("House KEeping is Completed")
# # Create object
root = tk.Tk()

# Adjust size
root.geometry("615x400")

# Add image file
bg = PhotoImage(file="new.png")

# Create Canvas
canvas1 = Canvas(root, width=400,
                 height=400)

canvas1.pack(fill="both", expand=True)

# Display image
canvas1.create_image(0, 0, image=bg,
                     anchor="nw")

word = "Hello Luna, Just a moment while we make sure its Not you.."


def write(write):
    # Repeats for each letter.
    for i in write:
        # sys.stdout.write doesn't create a new line for each print
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(.05)
    # Do you want to continue to the next text?


text = tk.Text(root, height=12)


def giftedtouch():
    global waybacks
    count = 0
    target = print(colors.HEADER + colors.BOLD + "Scanning for Target: " + colors.ENDC)
    sleep(3)
    print(colors.OKGREEN + colors.BOLD + "Target Found! " + colors.ENDC)
    sleep(3)
    scopey = ['https://giftcard.eigendev.com', 'https://gift.wegift.io' 'https://vanillaprepaid.com',
              'https://www.superex.com', 'vanillaprepaid.com', 'https://givex.com;', 'https://bitrefill.com',
              'https://homedepot.cashstar.com', 'https://redeem.tangocard.com', 'https://www.bitrefill.com',
              'https://cashstar.com', 'https://buyatab.com', 'https://jnrcard.com', 'https://cardswap.ca',
              'https://cashstar.com', 'https://shop.giftofchoice.ca', 'https://www.giftcertificates.ca',
              'https://wyndhamca.eyrewardshq.com', 'https://coincards.ca', 'https://one.ngcecodes.com',
              'https://starbucks.cashstar.com', 'https://cashstar.com', 'https://dev.ngcrewards.com',
              'https://stores.xoxoday.com', 'https://www.prepaiddigitalsolutions.com', 'https://egift.amexgiftcard.com',
              'https://supercert.rewardlink.io', 'https://www.rewardsgenius.com', 'https://wwws-canada2.givex.com',
              'https://buyatab.com', 'https://carswap.com', 'https://giftcash.com', 'https://www.vcdelivery.com/',
              'https://www.giftcardmall.com/', 'https://www.giftcards.com', 'https://www.giftcardgranny.com',
              'https://www.giftcardrescue.com/', 'https://www.giftcardzen.com', 'https://www.giftcards.com/',
              'https://www.giftcardrescue.com/', 'https://www.giftcardzen.com/', 'https://www.giftcardgranny.com/',
              'https://www.giftcardmall.com/', 'https://www.corporateboxoffice.com/', 'https://www.vcdelivery.com/',
              'https://starbucks.cashstar.com', 'https://www.buyatab.com', 'https://egift.thegiftcardshop.com']
    target = random.choice(scopey)
    if not target.startswith("http://") and not target.startswith("https://"):
        target = "http://" + target

    if target.endswith("/"):
        target = target[:-1]
    print(colors.OKCYAN + colors.BOLD + "[+] Target: " + target + colors.ENDC)

    try:
        requests.get(target)
    except Exception as e:
        print(colors.FAIL + colors.BOLD + "Please Enter A Valid URL ex:https://example.com")
        sys.exit()

    x = target.split("/")
    y = x[2]
    subprocess.call("mkdir " + y, shell=True)

    invalid = True

    while invalid:
        externals = print(colors.WARNING + colors.BOLD + "Deep Injection has begun. : ")
        externals = "Y"
        if externals == "Y" or externals == "y" or externals == "N" or externals == "n":
            invalid = False
        else:
            print(colors.FAIL + colors.BOLD + "Please Get help ")

    wayinvalid = True

    while wayinvalid:
        waybacks = print(colors.WARNING + colors.BOLD + "You should see results raining in now")
        waybacks = "Y"
        if waybacks == "Y" or waybacks == "y" or waybacks == "N" or waybacks == "n":
            wayinvalid = False
        else:
            print(colors.FAIL + colors.BOLD + "Please get help")

    target_url = []
    target_links = []
    temp_links = []
    target_js = []
    target_form = []
    target_robo = []
    target_sitemaps = []
    ginti = []
    target_url.append(target)
    target_url.append(target + "/sitemap.xml")
    target_url.append(target + "/robots.txt")

    async def link_extractor(url, session: ClientSession):
        async with session.get(url) as response:
            result = await response.text()
            href_links = re.findall('(?:href=")(.*?)"', str(result)) + re.findall("(?:href=')(.*?)'", str(result))
            js_links = re.findall('(?:src=")(.*?)"', str(result)) + re.findall("(?:src=')(.*?)'", str(result))
            form_links = re.findall('(?:action=")(.*?)"', str(result)) + re.findall("(?:action=')(.*?)'", str(result))
            xml_links = re.findall('(?:<loc>)(.*?)</loc>', str(result))
            robo_links = re.findall('(?:Disallow: )(.*?)\n', str(result)) + re.findall('(?:Allow: )(.*?)\n',
                                                                                       str(result)) + re.findall(
                '(?:sitemap: )(.*?)\n', str(result))

            for link in href_links:
                link = urljoin(url, link)
                # if "#" in link:
                #     link = link.split("#")[0]

                if target in link and link not in target_links:
                    temp_links.append(link)

                if externals == "y" or externals == "Y":

                    if link not in target_links:
                        print(colors.OKGREEN + colors.BOLD + "[+] Link: " + link + colors.ENDC)
                        target_links.append(link)
                        ginti.append("[+] Link: " + link)

                elif externals == "n" or externals == "N":

                    if target in link and link not in target_links:
                        print(colors.OKGREEN + colors.BOLD + "[+] Link: " + link + colors.ENDC)
                        target_links.append(link)
                        ginti.append("[+] Link: " + link)

            for limk in js_links:

                limk = urljoin(url, limk)

                if target in limk and limk not in target_js and limk.endswith(".json"):
                    temp_links.append(limk)

                if externals == "Y" or externals == "y":
                    if limk not in target_js and limk.endswith(".js"):
                        target_js.append(limk)
                        print(colors.OKBLUE + colors.BOLD + "[+] JS file: " + limk + colors.ENDC)
                        ginti.append("[+] JS file: " + limk)
                    elif limk not in target_js and limk not in target_form and limk not in target_links:
                        target_js.append(limk)
                        print(colors.OKGREEN + colors.BOLD + "[+] Link: " + limk + colors.ENDC)
                        ginti.append("[+] Link: " + limk)


                elif externals == "N" or externals == "n":
                    if target in limk and limk not in target_js and limk.endswith(".js"):
                        target_js.append(limk)
                        print(colors.OKBLUE + colors.BOLD + "[+] JS file: " + limk + colors.ENDC)
                        ginti.append("[+] JS file: " + limk)
                    elif target in limk and limk not in target_js and limk not in target_form and limk not in target_links:
                        target_js.append(limk)
                        print(colors.OKGREEN + colors.BOLD + "[+] Link: " + limk + colors.ENDC)
                        ginti.append("[+] Link: " + limk)

            for limk in form_links:

                limk = urljoin(url, limk)

                if target in limk and limk not in target_form:
                    temp_links.append(limk)

                if externals == "Y" or externals == "y":
                    if limk not in target_form:
                        target_form.append(limk)
                        print(colors.HEADER + colors.BOLD + "[+] Form: " + limk + colors.ENDC)
                        ginti.append("[+] Form: " + limk)

                elif externals == "N" or externals == "n":
                    if target in limk and limk not in target_form:
                        target_form.append(limk)
                        print(colors.HEADER + colors.BOLD + "[+] Form: " + limk + colors.ENDC)
                        ginti.append("[+] Form: " + limk)

            for limk in xml_links:

                limk = urljoin(url, limk)

                if externals == "Y" or externals == "y":
                    if limk not in target_form:
                        target_form.append(limk)
                        print(colors.WARNING + colors.BOLD + "[+] Sitemap-Results: " + limk + colors.ENDC)
                        ginti.append("[+] Sitemap-Results: " + limk)

                elif externals == "N" or externals == "n":
                    if target in limk and limk not in target_form:
                        target_form.append(limk)
                        print(colors.WARNING + colors.BOLD + "[+] Sitemap-Results: " + limk + colors.ENDC)
                        ginti.append("[+] Sitemap-Results: " + limk)

            for limk in robo_links:

                limk = urljoin(url, limk)

                if externals == "Y" or externals == "y":
                    if limk not in target_robo:
                        target_robo.append(limk)
                        print(colors.OKCYAN + colors.BOLD + "[+] ROBOTS.TXT-Results: " + limk + colors.ENDC)
                        ginti.append("[+] ROBOTS.TXT-Results: " + limk)

                elif externals == "N" or externals == "n":
                    if target in limk and limk not in target_robo:
                        target_robo.append(limk)
                        print(colors.OKCYAN + colors.BOLD + "[+] ROBOTS.TXT-Results: " + limk + colors.ENDC)
                        ginti.append("[+] ROBOTS.TXT-Results: " + limk)

    async def crawl(urls):
        rocky = []
        for i in urls:
            rocky.append(i)
        temp_links.clear()
        my_conn = aiohttp.TCPConnector(limit=10)
        async with aiohttp.ClientSession(connector=my_conn) as session:
            tasks = []
            for url in rocky:
                task = asyncio.ensure_future(link_extractor(url=url, session=session))
                tasks.append(task)
            await asyncio.gather(*tasks, return_exceptions=True)  # the await must be nest inside of the session

    asyncio.run(crawl(target_url))

    while True:
        try:
            asyncio.run(crawl(temp_links))
            if len(temp_links) <= 0:
                print(colors.HEADER + colors.BOLD + "Gift Card files Downloading now ...")
                with open('barcode.txt', 'a') as the_file:

                    for link in ginti:
                        if "barcode" in link:
                            the_file.write(link + '\n')

                if waybacks == "Y" or waybacks == "y":
                    url = 'http://web.archive.org/cdx/search/cdx?url=*.' + target + '/*&output=txt&fl=original&collapse=urlkey'
                    r = requests.get(url)
                    results = r.text
                    print(colors.OKBLUE + colors.BOLD + "------------- [+] Injection Result ------------")
                    print(results)
                    with open('hits.txt', 'a') as the_file:
                        the_file.write(results)
                        the_file.close()
                    print(colors.HEADER + colors.BOLD + "[+] Stage Completed")
                    print(colors.OKCYAN + colors.BOLD + "[+] Total Discoveries: " + (str(len(ginti))))

                    import hashlib

                    # 1
                    output_file_path = "hitscleanedup.txt"
                    input_file_path = "hits.txt"

                    # 2
                    completed_lines_hash = set()

                    # 3
                    output_file = open(output_file_path, "w")

                    # 4
                    for line in open(input_file_path, "r"):
                        # 5
                        hashValue = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()
                        # 6
                        if hashValue not in completed_lines_hash:
                            output_file.write(line)
                            completed_lines_hash.add(hashValue)
                    # 7
                    # output_file.close()

                    count = count + 1
                    target = random.choice(scopey)
                # sys.exit()
        except KeyboardInterrupt:
            print(colors.HEADER + colors.BOLD + "Attacking with SQL.. DORKS ....XSS  ....INJECTION")
            with open('hits.txt', 'a') as the_file:
                for link in ginti:
                    if "cert" in link:
                        the_file.write(link + '\n')
            if waybacks == "Y" or waybacks == "y":
                url = 'http://web.archive.org/cdx/search/cdx?url=*.' + target + '/*&output=txt&fl=original&collapse=urlkey'
                r = requests.get(url)
                results = r.text
                if "cert" in r.text:
                    with open('cert.txt', 'a') as the_file:
                        the_file.write(results)
                        the_file.close()
                if "barcode" in r.text:
                    with open('barcode.txt', 'a') as the_file:
                        the_file.write(results)
                        the_file.close()
                if "testtttt" in r.text:
                    with open('cert.txt', 'a') as the_file:
                        the_file.write(results)
                        the_file.close()

                print(
                    colors.OKBLUE + colors.BOLD + "------------- [+] GiftCard Revolver By t.me/MoreSaves ------------")
                print(results)
                with open('hits.txt', 'a') as the_file:
                    the_file.write(results)
                    the_file.close()
            print(colors.FAIL + colors.BOLD + "[!] Scan Aborted By User.")


def select_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='',
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=filename
    )


def open_text_file():
    # file type
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    # show the open file dialog
    f = fd.askopenfile(filetypes=filetypes)
    # read the text file and show its content on the Text
    text.insert('1.0', f.readlines())


canvas1.create_text(100, 270, text=write(word))

# Create Buttons
button1 = Button(root, text="Exit")
button1["bg"] = "#c71545"
button3 = tk.Button(root, text="Start", command=giftedtouch)
button3["bg"] = "#c71585"

button2 = Button(root, text="Hits", command=open_text_file)
button2["bg"] = "#c71583"
# Display Buttons
button1_canvas = canvas1.create_window(100, 100,
                                       anchor="nw",
                                       window=button1)

button2_canvas = canvas1.create_window(150, 100,
                                       anchor="nw",
                                       window=button2)

button3_canvas = canvas1.create_window(200, 100, anchor="nw",
                                       window=button3)

# Execute tkinter
root.mainloop()
