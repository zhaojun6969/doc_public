# pyarmor gen <options> <SCRIPT or PATH>
# 选项

# -i
# 保存运行辅助文件到加密包的内部 ...

# -O PATH, --output PATH
# 设置输出目录 ...

# -r, --recursive
# 递归搜索目录中的脚本...

# --exclude PATTERN
# 排除脚本或者子目录。这个选项可以使用多次  ...


# --period N
# 周期性检查运行密钥 ...
# pyarmor gen --period 60m foo.py


# -e DATE, --expired DATE
# 设置脚本有效期，YYYY-MM-DD ...
# 默认情况是检查本地时间，使用下面的命令查看默认的时间服务器
# pyarmor cfg nts
# 如果需要检查网络时间，那么需要指定 NTP 服务器。例如:
# pyarmor cfg nts=pool.ntp.org


# -b DEV, --bind-device DEV
# 绑定脚本到设备 ...


# --obf-module <0,1>
# 指定模块加密模式，默认是 1 ...

# --obf-code <0,1,2>
# 指定代码加密模式，默认是 1 ...
# 模式 2 是 Pyarmor 8.2 中新增加的，它能增加从 Bytecode 进行反编译的难度，同时会降低一点性能。
# 它可以把部分表达式中的属性名称混淆，例如:
# obj.attr          ==> getattr(obj, 'xxxx')
# obj.attr = value  ==> setattr(obj, 'xxxx', value)


# --no-wrap
# 禁用包裹加密模式 ...
# 使用包裹模式加密函数是指在调用函数的时候解密函数，调用完成重新加密函数。
# 禁用之后第一次调用函数的解密函数，但是调用完成之后不在加密，以后调用的时候也无需重新解密。
# 禁用包裹模式，对于多次执行的函数可以提高性能。

# --enable <jit,rft,bcc,themida>
# 启用不同的保护特征 ...

# --enable-jit
# 使用 JIT 来处理一些敏感数据以增强安全性

# --enable-rft
# 启用 RFT 模式 pro

# --enable-bcc
# 启用 BCC 模式 pro



# --mix-str
# 混淆字符串常量 ...
# 混淆所有的字符串,用于保护字符串常（如密码，增加破解难度）


# --private
# 启用私有模块加密脚本 ...
# 启用私有模式之后，模块的属性和方法不允许外部脚本或者 Python 解释器直接访问
# 现在加密脚本可以导入加密模块，但是不能访问其属性

# --restrict
# 启用约束模式加密包 ...
# 主要应用于保护加密包，保护包里面的模块，只能在包内部使用，不能被外部模块调用
# 这个选项隐含启用 --private
# 当约束模式启用之后，除了 __init__.py 输出的名称之外，其他模块都不能被外部脚本导入和使用。



# --assert-import
# 确保导入的脚本是经过加密的 ...
# 启用自动检查模块功能，确保加密的模块没有被替换
# 这个选项隐含启用 --private

# --assert-call
# 确保调用的函数是经过加密的 ...
# 启用自动检查函数功能，确保加密函数没有被替换
# 这个选项隐含启用 --private


# --bind-data 12345 
# 绑定自定义数据到运行密钥 ...
# 自定义数据可以是任何字符串，例如时间戳，设备 ID 等。
# 这个选项可以存储任何数据到 运行密钥 中，但是有长度限制，一般不超过 4096 个字节。
# 主要用于用户扩展验证运行密钥的方式，在加密脚本中读取运行密钥中存放的数据，
# 使用自己的算法进行校验和检查。




# --pack <onefile,onedir,FC,DC,NAME.spec>
# 加密脚本然后在打包成为单文件或者单目录 ...
# pyarmor gen --pack onefile -r foo.py
# 而是直接删除输出目录，可以使用 FC 或者 DC 进行打包， 
# F 表示 onefile ， D 表示 onedir ， C 表示无需确认清空输出目录。例如:
# pyarmor gen --pack --output=packed_script.exe FC foo.py



#%%
# pip install PyInstaller
# !python -m pip install pyarmor -i https://mirror.baidu.com/pypi/simple

# 打包单个文件
# pyarmor gen --output dist 代码加密.py

# 加密所有符合条件的文件
# pyarmor gen -r main.py src/*.py libs/utils.py libs/dbpkg

# （打包目录中的所有文件，文件还是可被引用，和正常python文件一样），可以新加未加密的文件，引用加密文件
# pyarmor gen -r -O dist ./
# INFO     Python 3.10.10
# INFO     Pyarmor 9.2.3 (trial), 000000, non-profits
# INFO     Platform windows.x86_64


# 只列出所有符合条件的文件，不加密
# pyarmor gen -r @filelist --exclude "*/test.py" ./


# python -m pyarmor.cli.hdinfo 
# 直接得到:term:客户设备 的硬件信息如下:
# Machine ID: 'mc92c9f22c732b482fb485aad31d789f1'
# Default Harddisk Serial Number: 'HXS2000CN2A'
# Default Mac address: '00:16:3e:35:19:3d'
# Default IPv4 address: '128.16.4.10'
# Multiple Mac addresses: <68:7a:64:bd:27:9c,68:7a:64:bd:27:98,68:7a:64:bd:27:99,6a:7a:64:bd:27:98>
# Domain: 'dashingsoft.com'

# from pyarmor.cli import hdinfo
# print(hdinfo.get_hd_info(hdinfo.HT_IPV4))

# 指定一个设备的多个硬件信息，使用空格分开各项
# pyarmor gen -b "128.16.4.10 00:16:3e:35:19:3d HXS2000CN2A" foo.py





## 购买pyarmor版权
# pyarmor reg
# pyarmor-regcode-xxxx.txt 激活文件，一般在购买许可证之后会发送到注册邮箱
# pyarmor-regfile-xxxx.zip 注册文件，初始登记之后自动生成

# 检查当前设备的注册信息:
# pyarmor -v


# 初始登记
# 初始登记使用下面的命令，产品名称必须输入，使用实际产品名称替换 NAME ，用于非商业化产品的使用名称 non-profits:
# pyarmor reg -p NAME pyarmor-regcode-xxxx.txt
# 初始登记完成之后会生成相应的 注册文件 pyarmor-regfile-xxxx.zip ，在其他设备以及后续的注册均使用这个文件，并且不需要输入产品名称:
# pyarmor reg pyarmor-regfile-xxxx.zip





# 一般的脚本补丁是嵌入到了加密脚本中，如果需要在运行加密脚本之前就进行一些定制或者额外的检查，那么就需要使用到特殊的脚本补丁 .pyarmor/hooks/pyarmor_runtime.py ，这个脚本补丁可以定义在加密脚本执行之前就被调用的函数。
# 首先创建脚本 .pyarmor/hooks/pyarmor_runtime.py ，然后定义一个函数 bootstrap() ，这个函数在扩展模块 pyarmor_runtime 初始化的过程中被调用，其他代码都会被忽略。
# bootstrap(user_data)
# 参数
# user_data (bytes) -- 运行密钥里面的用户自定义数据
# 返回
# 如果返回 False ，那么扩展模块 pyarmor_runtime 初始化失败，并且抛出保护异常 返回其他任何值，继续执行加密脚本

# 抛出
# SystemExit -- 直接退出，不显示调用堆栈
# ohter Exception -- 退出并且显示调用堆栈


# .pyarmor/hooks/pyarmor_runtime.py
# def bootstrap(user_data):
#     # 必须在函数内容导入需要的名称，不要在模块级别导入
#     import sys
#     import time
#     from struct import calcsize

#     print('user data is', user_data)

#     # 检查平台，不支持 32 位
#     if sys.platform == 'win32' and calcsize('P'.encode()) * 8 == 32:
#         raise SystemExit('no support for 32-bit windows')

#     # 在 Windows 平台下面检查是否有调试器存在
#     if sys.platform == 'win32':
#         from ctypes import windll
#         if windll.kernel32.IsDebuggerPresent():
#             print('found debugger')
#             return False

#     # 在这个例子中，传入的自定义数据是时间戳
#     if time.time() > int(user_data.decode()):
#         return False

# pyarmor gen --bind-data 12345 foo.py
# $ pyarmor gen --bind-data 12345 foo.py
# $ python dist/foo.py

# user data is b'12345'
# Traceback (most recent call last):
#   File "dist/foo.py", line 2, in <module>
#   ...
# RuntimeError: unauthorized use of script (1:10325)

print(123)