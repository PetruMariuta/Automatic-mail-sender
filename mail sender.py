import webbrowser
import time
import win32com.client
import os

shell=win32com.client.Dispatch("WScript.Shell")

url = "gmail.com"
email_to ="example@mail.com"
subject = "mail"
message = "Hello there"

time.sleep(2)
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
webbrowser.get(chrome_path).open(url)

#webbrowser.open("url") if you want to use the default web browser


time.sleep(5)
shell.SendKeys("c", 0)
time.sleep(1)
shell.SendKeys(email_to, 0)
time.sleep(1)
shell.SendKeys("{TAB}", 0)
time.sleep(1)
shell.SendKeys("{TAB}", 0)
time.sleep(1)
shell.SendKeys(subject, 0)
time.sleep(1)
shell.SendKeys("{TAB}", 0)
time.sleep(1)
shell.SendKeys(message, 0)
time.sleep(1)
shell.SendKeys("{TAB}", 0)
time.sleep(1)
shell.SendKeys("{ENTER}", 0)