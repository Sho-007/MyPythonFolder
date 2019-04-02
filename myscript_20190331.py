


# ターミナルでのPythonの環境構築及び起動
Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> Last login: Sun Mar 31 13:59:16 on ttys000
hiraimasayanoMacBook-Pro:~ hiraishoya$ pip freeze
-bash: pip: command not found
hiraimasayanoMacBook-Pro:~ hiraishoya$ which pip
hiraimasayanoMacBook-Pro:~ hiraishoya$ pip3

Usage:   
  pip3 <command> [options]

Commands:
  install                     Install packages.
  download                    Download packages.
  uninstall                   Uninstall packages.
  freeze                      Output installed packages in requirements format.
  list                        List installed packages.
  show                        Show information about installed packages.
  check                       Verify installed packages have compatible dependencies.
  config                      Manage local and global configuration.
  search                      Search PyPI for packages.
  wheel                       Build wheels from your requirements.
  hash                        Compute hashes of package archives.
  completion                  A helper command used for command completion.
  help                        Show help for commands.

General Options:
  -h, --help                  Show help.
  --isolated                  Run pip in an isolated mode, ignoring
                              environment variables and user configuration.
  -v, --verbose               Give more output. Option is additive, and can be
                              used up to 3 times.
  -V, --version               Show version and exit.
  -q, --quiet                 Give less output. Option is additive, and can be
                              used up to 3 times (corresponding to WARNING,
                              ERROR, and CRITICAL logging levels).
  --log <path>                Path to a verbose appending log.
  --proxy <proxy>             Specify a proxy in the form
                              [user:passwd@]proxy.server:port.
  --retries <retries>         Maximum number of retries each connection should
                              attempt (default 5 times).
  --timeout <sec>             Set the socket timeout (default 15 seconds).
  --exists-action <action>    Default action when a path already exists:
                              (s)witch, (i)gnore, (w)ipe, (b)ackup, (a)bort).
  --trusted-host <hostname>   Mark this host as trusted, even though it does
                              not have valid or any HTTPS.
  --cert <path>               Path to alternate CA bundle.
  --client-cert <path>        Path to SSL client certificate, a single file
                              containing the private key and the certificate
                              in PEM format.
  --cache-dir <dir>           Store the cache data in <dir>.
  --no-cache-dir              Disable the cache.
  --disable-pip-version-check
                              Don't periodically check PyPI to determine
                              whether a new version of pip is available for
                              download. Implied with --no-index.
  --no-color                  Suppress colored output
hiraimasayanoMacBook-Pro:~ hiraishoya$ pip -V
-bash: pip: command not found
hiraimasayanoMacBook-Pro:~ hiraishoya$ pip3 -V
pip 19.0.3 from /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pip (python 3.7)
hiraimasayanoMacBook-Pro:~ hiraishoya$ ipython -V
-bash: ipython: command not found
hiraimasayanoMacBook-Pro:~ hiraishoya$ python3 -m venv env
hiraimasayanoMacBook-Pro:~ hiraishoya$ source env/bin/activate
(env) hiraimasayanoMacBook-Pro:~ hiraishoya$ python -V
Python 3.7.3
(env) hiraimasayanoMacBook-Pro:~ hiraishoya$ ipython
Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
Type 'copyright', 'credits' or 'license' for more information
# Ipythonの起動
IPython 7.4.0 -- An enhanced Interactive Python. Type '?' for help.

# Pythonにおけるfor文の処理

In [1]: for year in [1950,2000.2020]: 
   ...:     if year < 1989: 
   ...:         print('昭和') 
   ...:         elif year < 2019: 
   ...:             print('平成')                                               
  File "<ipython-input-1-0335e2062be8>", line 4
    elif year < 2019:
       ^
SyntaxError: invalid syntax


In [2]: for year in [1950,2000.2020]:  
   ...:    ...:     if year < 1989:  
   ...:    ...:         print('昭和')  
   ...:    ...:         elif year < 2019:  
   ...:    ...:             print('平成')                                       
  File "<ipython-input-2-a850c974fab0>", line 4
    elif year < 2019:
       ^
SyntaxError: invalid syntax


In [3]: for year in [1950,2000,2020]                                            
  File "<ipython-input-3-0678c6fe0464>", line 1
    for year in [1950,2000,2020]
                                ^
SyntaxError: invalid syntax


In [4]: for year in [1950,2000.2020]                                            
  File "<ipython-input-4-87424acfb923>", line 1
    for year in [1950,2000.2020]
                                ^
SyntaxError: invalid syntax


In [5]: for year in [1950,2000,2020]                                            
  File "<ipython-input-5-0678c6fe0464>", line 1
    for year in [1950,2000,2020]
                                ^
SyntaxError: invalid syntax


In [6]: for year in [1950,2000,2020]: 
   ...:         if year < 1989: 
   ...:                 print('昭和') 
   ...:                     elif year < 2019: 
   ...:                             print('平成')                               
  File "<ipython-input-6-d474533d3d73>", line 4
    elif year < 2019:
    ^
IndentationError: unexpected indent


In [7]: for year in [1959,2000,2020]: 
   ...:     if year < 1989: 
   ...:         print('昭和') 
   ...:     elif year < 2019: 
   ...:         print('平成') 
   ...:     else : 
   ...:         pritn('新元号') 
   ...:                                                                         
昭和
平成
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-7-2f7902767972> in <module>
      5         print('平成')
      6     else :
----> 7         pritn('新元号')
      8 

NameError: name 'pritn' is not defined

In [8]: for year in [1959,2000,2020]:  
   ...:    ...:     if year < 1989:  
   ...:    ...:         print('昭和')  
   ...:    ...:     elif year < 2019:  
   ...:    ...:         print('平成')  
   ...:    ...:     else :  
   ...: print('新元号')                                                         
  File "<ipython-input-8-abfbe0094323>", line 7
    print('新元号')
                ^
IndentationError: expected an indented block


In [9]: for year in [1959,2000,2020]:  
   ...:    ...:     if year < 1989:  
   ...:    ...:         print('昭和')  
   ...:    ...:     elif year < 2019:  
   ...:    ...:         print('平成')  
   ...:    ...:     else :  
   ...:                 print('新元号') 
   ...:                                                                         
昭和
平成
新元号

# 例外処理
In [10]: try: 
    ...:     1/0 
    ...: except ZeroDivisionError: 
    ...:     pritn('0で割れません') 
    ...:                                                                        
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-10-538ec5d87182> in <module>
      1 try:
----> 2     1/0
      3 except ZeroDivisionError:

ZeroDivisionError: division by zero

During handling of the above exception, another exception occurred:

NameError                                 Traceback (most recent call last)
<ipython-input-10-538ec5d87182> in <module>
      2     1/0
      3 except ZeroDivisionError:
----> 4     pritn('0で割れません')
      5 

NameError: name 'pritn' is not defined

In [11]: 1/0                                                                    
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-11-9e1622b385b6> in <module>
----> 1 1/0

ZeroDivisionError: division by zero

In [12]: try: 
    ...:     1/0 
    ...: except ZeroDivisionError: 
    ...:     print('0で割れません') 
    ...:                                                                        
0で割れません

# 内包表記を使用せずに文字列の長さのリストを生成
In [13]: names = ['spam','ham','eggs']                                          

In [14]: lens = []                                                              

In [15]: for name in names: 
    ...:     lens.append(len(name)) 
    ...:                                                                        

In [16]: lens                                                                   
Out[16]: [4, 3, 4]

# 同じ処理のリスト内表記
In [17]: [len(name) for name in names]                                          
Out[17]: [4, 3, 4]

In [18]: names =['spam','ham','eggs']                                           

In [19]: lens = []                                                              

In [20]: [len(name) for name in names]                                          
Out[20]: [4, 3, 4]

# セット内包表記
In [21]: {len(name) for name in names}                                                                                                                                                                                                      
Out[21]: {3, 4}

# 辞書内包表記
In [22]: {name:len(name) for in names}                                                                                                                                                                                                      
  File "<ipython-input-22-517d42de75f9>", line 1
    {name:len(name) for in names}
                         ^
SyntaxError: invalid syntax


In [23]: {name: len(name) for name in names}                                                                                                                                                                                                
Out[23]: {'spam': 4, 'ham': 3, 'eggs': 4}

In [24]: [x*x for x in range(10) if x % 2 == 0]                                                                                                                                                                                             
Out[24]: [0, 4, 16, 36, 64]

In [25]: [[(y,x*x) for x in range(10) if x % 2 == 0]]                                                                                                                                                                                       
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-25-789102266902> in <module>
----> 1 [[(y,x*x) for x in range(10) if x % 2 == 0]]

<ipython-input-25-789102266902> in <listcomp>(.0)
----> 1 [[(y,x*x) for x in range(10) if x % 2 == 0]]

NameError: name 'y' is not defined

In [26]: [[(y,x*x) for x in range(10) if x % 2 == 0] for y in range(3)]                                                                                                                                                                     
Out[26]: 
[[(0, 0), (0, 4), (0, 16), (0, 36), (0, 64)],
 [(1, 0), (1, 4), (1, 16), (1, 36), (1, 64)],
 [(2, 0), (2, 4), (2, 16), (2, 36), (2, 64)]]

# ジェネレーター式 大量のデータ処理に大量のメモリを確保せずに負荷を軽減できる
# プログラミングとメモリの関係についてもまた深く学ぶ必要あり

In [27]: l = [x*x for x in range(10000)]                                                                                                                                                                                                    

In [28]: type(l),len(l)                                                                                                                                                                                                                     
Out[28]: (list, 10000)

In [29]: g = (x*x for x in range(10000))                                                                                                                                                                                                    

In [30]: type(g)                                                                                                                                                                                                                            
Out[30]: generator

In [31]: next(g),next(g),next(g)                                                                                                                                                                                                            
Out[31]: (0, 1, 4)

# ファイル入出力 
# with構文とopen関数を使う
In [32]: with open('sample.txt','w',encoding='utf-8') as f: 
    ...:     f.write('こんにちは')  
    ...:     f.write('Python\n') 
    ...:                                                                                                                                                                                                                                    

In [33]: f.closed                                                                                                                                                                                                                           
Out[33]: True

In [34]: with open('sample.txt',encoding='utf-8') as f: 
    ...:     data = f.read() 
    ...:                                                                                                                                                                                                                                    

In [35]: data                                                                                                                                                                                                                               
Out[35]: 'こんにちはPython\n'

# 文字列操作　
In [36]: s1 = 'hello Python'                                                                                                                                                                                                                

In [37]: s1.upper().s1.lower(),s1.title()                                                                                                                                                                                                   
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-37-09bc3996721c> in <module>
----> 1 s1.upper().s1.lower(),s1.title()

AttributeError: 'str' object has no attribute 's1'

In [38]: s1.upper(),s1.lower(),s1.title()     
# upperで全てを大文字、lowerで全てを小文字、titleで単語ごとに区切られた頭文字の大文字化                                                                                                                                                                                           
Out[38]: ('HELLO PYTHON', 'hello python', 'Hello Python')

In [39]: s1.replace('hello,Hi')                                                                                                                                                                                                             
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-39-efa652520fb5> in <module>
----> 1 s1.replace('hello,Hi')

TypeError: replace() takes at least 2 arguments (1 given)

In [40]: s1.replace('hello', 'Hi')                                                                                                                                                                                                          
Out[40]: 'Hi Python'

In [41]: s2 = ' spam ham eggs'                                                                                                                                                                                                              
# splitで分割
In [42]: s2.split()                                                                                                                                                                                                                         
Out[42]: ['spam', 'ham', 'eggs']

In [43]: import re                                                                                                                                                                                                                          

In [44]: prog = re.compile('(P(yth|l)|Z)o[pn]e?')                                                                                                                                                                                           

In [45]: prog.search('Python')                                                                                                                                                                                                              
Out[45]: <re.Match object; span=(0, 6), match='Python'>

In [46]: prog.search('Spam')                                                                                                                                                                                                                

In [47]:                                                                                                                                                                                                                                    

In [47]: import logging                                                                                                                                                                                                                     

In [48]: logging.basicConfig( 
    ...: filename ='example.log', 
    ...: level = logging,INFO, 
    ...: format = '%(asctime)s:%(levelname)s:%(message)s' 
    ...: )                                                                                                                                                                                                                                  
  File "<ipython-input-48-e7fa23118491>", line 3
    level = logging,INFO,
                   ^
SyntaxError: positional argument follows keyword argument


In [49]: logging.basicConfig( 
    ...: filename = 'example.log', 
    ...: level = logging.INFO, 
    ...: format = '%(asctime)s:%(levelname)s:%(message)s' 
    ...: )                                                                                                                                                                                                                                  

In [50]: logging.debug('デバッグレベル ')                                                                                                                                                                                                   

In [51]: logging.info('INFOレベル')                                                                                                                                                                                                         

In [52]: logging.warning('警告レベル ')                                                                                                                                                                                                     

In [53]: logging.error('エラーレベル')                                                                                                                                                                                                      

In [54]: logging.critical('重大なエラー')                                                                                                                                                                                                   

In [55]:                                                                                                                                                                                                                                    

In [55]:                                                                                                                                                                                                                                    

In [55]:                                                                                                                                                                                                                                    

In [55]:                                                                                                                                                                                                                                    

In [55]: vim                                                                                                                                                                                                                                
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-55-f45bf01bd8a7> in <module>
----> 1 vim

NameError: name 'vim' is not defined

In [56]: %save saved_session.py1-55                                                                                                                                                                                                         
'' was not found in history, as a file, url, nor in the user namespace.

In [57]: %save saved_hiraimasaya.py1-54                                                                                                                                                                                                     
'' was not found in history, as a file, url, nor in the user namespace.

In [58]: import pickle                                                                                                                                                                                                                      

In [59]: readline.write_history_file("history.py")                                                                                                                                                                                          
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-59-114728dfc9f0> in <module>
----> 1 readline.write_history_file("history.py")

NameError: name 'readline' is not defined

In [60]: readline.write_history_file("Pythonフォルダ")                                                                                                                                                                                      
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-60-5af2337c99f9> in <module>
----> 1 readline.write_history_file("Pythonフォルダ")

NameError: name 'readline' is not defined

In [61]: import readline                                                                                                                                                                                                                    

In [62]: readline.write_history_file("history.py")                                                                                                                                                                                          

In [63]:                                                                                                                                                                                                                                    

In [63]:
	
SyntaxError: invalid syntax
>>> 
>>> 
