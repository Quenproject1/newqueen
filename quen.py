#coding: utf-8
# module
import os,sys,time,getpass

# username
x = "QUEN PROJECT"
# password
y = "QUEN"


# mengetik otomatis cepat
def sp(a):
  for e in a + "\n":
    sys.stdout.write(e)
    sys.stdout.flush()
    time.sleep(0.002)


# login
def login():
  os.system("clear")
  sp("\033[1;96m      <div><span style="color: #ff0000">�</span><span style="color: #ff2000">�</span><span style="color: #ff4000">�</span><span style="color: #ff5f00">�</span><span style="color: #ff7f00">�</span><span style="color: #ff9900">�</span><span style="color: #ffb200">�</span><span style="color: #ffcc00">�</span><span style="color: #ffe500"> </span><span style="color: #ffff00">�</span><span style="color: #bfff00">�</span><span style="color: #80ff00">�</span><span style="color: #40ff00">�</span><span style="color: #00ff00">�</span><span style="color: #00ff33">�</span><span style="color: #00ff66">�</span><span style="color: #00ff99">�</span><span style="color: #00ffcc">�</span><span style="color: #00ffff">�</span><span style="color: #00bfff">�</span><span style="color: #0080ff">�</span><span style="color: #0040ff">�</span><span style="color: #0000ff">�</span></div>
  sp("\033[1;96m+\033[1;90m========================================\033[1;96m+")
  sp(" \033[1;97m{\033[1;95m•\033[1;97m} \033[1;93mAuthor   \033[1;91m: \033[1;95mQUEN PROJECT")
  sp(" \033[1;97m{\033[1;95m•\033[1;97m} \033[1;93mFacebook \033[1;91m: \033[1;95mQUEN PROJECT1")
  sp(" \033[1;97m{\033[1;95m•\033[1;97m} \033[1;93mYouTube  \033[1;91m: \033[1;95mQUEN PROJECT")
  sp(" \033[1;97m{\033[1;95m•\033[1;97m} \033[1;93mGithub   \033[1;91m: \033[4;92mhttps://github.com/Rendi-ID\033[1;0m")
  sp("\033[1;96m+\033[1;90m========================================\033[1;96m+")
  username = raw_input(" \033[1;97m{\033[1;93m+\033[1;97m} \033[1;96mUsername:\033[1;92m ")
  password = getpass.getpass(" \033[1;97m{\033[1;93m+\033[1;97m} \033[1;96mPassword: ")
  if username == x and password == y:
    print(" \033[1;92mAccess Grented")
    time.sleep(1)
  else:
    print(" \033[1;91mAccess Denied")
    time.sleep(1)
    login()

login()
