# Write a Python program to display formatted text (width=50) as output.

import textwrap
sample_text = '''
    jsgfj aflakj agfka gjfask iufgja  fakgajk aigf af agfkf aak fakufg af aafkeglaieihf eig iwegw  iwilwll w   wiwwihiwhwhikshshsh fbf f f akf a af sghkjg  s sf ks s  ss ksghrig  ghirhgf  fg gf f r lsk js si shs ig ksg ksgksifd s gshgsbvi gihsig i shgs gisshg skgk gsiss gshgksdk g shgksh
  '''

print(textwrap.fill(sample_text, width=50))
