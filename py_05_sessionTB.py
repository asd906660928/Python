# 导入requests

import requests

# 定义请求的url

url = 'https://i.taobao.com/my_taobao.htm?nekot=YXNkOTA2NjYwOTI41580644908179'

# 定义登录请求的地址
login_url = 'https://login.taobao.com/member/login.jhtml?redirectURL=https%3A%2F%2Fi.taobao.com%2Fmy_taobao.htm%3Fnekot%3DYXNkOTA2NjYwOTI41580644908179'

# 定义请求头

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
    # 'cookie': 'thw=cn; t=bf7399115ab00bde256c0dc1bc4a97f6; cookie2=1af9080ad1ca4d9287606a50d770bc27; _tb_token_=eae713453e557; _samesite_flag_=true; ucn=center; cna=s3a9Fi1SMTsCAdzDQd0vpkJA; unb=859376533; uc3=nk2=AmJamjdnJrjdLXea&vt3=F8dBxdsQW6lgCWv%2FmkM%3D&lg2=URm48syIIVrSKA%3D%3D&id2=W8zC4T09oIi1; csg=66c9e43c; lgc=asd906660928; cookie17=W8zC4T09oIi1; dnk=asd906660928; skt=3906b59850971a5d; existShop=MTU4MDY0MTYwMA%3D%3D; uc4=nk4=0%40AImfrEko90sPd%2BXPD2RnA6mbue7l6jY%3D&id4=0%40We8xsj1qFrabSQQnOiZQYVKQxCU%3D; tracknick=asd906660928; _cc_=UtASsssmfA%3D%3D; tg=0; _l_g_=Ug%3D%3D; sg=837; _nk_=asd906660928; cookie1=Uone%2BXVv72kPu3HsaDCdlvmhigxrQ6COJiSPYxr9xpw%3D; mt=ci=37_1; v=0; uc1=cookie16=VT5L2FSpNgq6fDudInPRgavC%2BQ%3D%3D&cookie21=U%2BGCWk%2F7owY3j65jYmjW9Q%3D%3D&cookie15=WqG3DMC9VAQiUQ%3D%3D&existShop=true&pas=0&cookie14=UoTUOqbGI6VT4Q%3D%3D&tag=8&lng=zh_CN; isg=BJGRzl3zq5ayaMeCa2RsQRFVoJQr_gVwVMfMF3Mni9h3GrBsu022QAI4vO78Ep2o; l=cBx2XPOlQMBEJCZCBOfalurza779mIOb8sPzaNbMiICPOg1H5VLhWZ0PIQYMCnGVK65WR35rozS8BJLwIz1gEM5_YQPpHPf..'
}

# 如果需要爬虫程序主动记录cookie并且携带cookie，那么使用requests之前先调用session方法
# 并且使用session方法对返回的对象发送请求即可

req = requests.session()

# 定义登录Data数据

data = {
        'TPL_username': 'asd906660928',
        'TPL_password': '',
        'ncoSig': '',
        'ncoSessionid': '',
        'ncoToken': '60babe4ca27d504ff2acf7575b24cdca61265b75',
        'slideCodeShow': 'false',
        'useMobile': 'false',
        'lang': 'zh_CN',
        'loginsite': '0',
        'newlogin': '0',
        'TPL_redirect_url': 'https://i.taobao.com/my_taobao.htm?nekot=YXNkOTA2NjYwOTI41580644908179',
        'from': 'tb',
        'fc': 'default',
        'style': 'default',
        'css_style': '',
        'keyLogin': 'false',
        'qrLogin': 'true',
        'newMini': 'false',
        'newMini2': 'false',
        'tid': '',
        'loginType': '3',
        'minititle': '',
        'minipara': '',
        'pstrong':' ',
        'sign':' ',
        'need_sign':' ',
        'isIgnore':' ',
        'full_redirect':' ',
        'sub_jump':' ',
        'popid':' ',
        'callback':' ',
        'guf':' ',
        'not_duplite_str':' ',
        'need_user_id':' ',
        'poy':' ',
        'gvfdcname': '10',
        'gvfdcre': '68747470733A2F2F6C6F67696E2E74616F62616F2E636F6D2F6D656D6265722F6C6F676F75742E6A68746D6C3F73706D3D61317A30322E312E3735343839343433372E372E36336434373832644D4A6545433126663D746F70266F75743D7472756526726564697265637455524C3D6874747073253341253246253246692E74616F62616F2E636F6D2532466D795F74616F62616F2E68746D2533466E656B6F7425334459584E6B4F5441324E6A59774F54493431353830363434393038313739',
        'from_encoding':' ',
        'sub':' ',
        'TPL_password_2': '07a826b9e39d78d02763c3bd6f5a6f5510fa1e8eaefd30358ba1033b2dc1e5d9f54aa29fecd689e75e4043a295679146fea66c429dd88bc6366145f3e339667039320edd78d61842b9dfec0c089a253dcd2c8fee559c3da40c8c0a9813ea72300e2343c92ec465cfe54a8db74e0ef02c7bcbdd45ee0d022c8fc90926c986f73f',
        'loginASR': '1',
        'loginASRSuc': '1',
        'allp':' ',
        'oslanguage': 'zh-CN',
        'sr': '1920*1080',
        'osVer':' ',
        'naviVer': 'chrome|79.03945117',
        'osACN': 'Mozilla',
        'osAV': '5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
        'osPF': 'Linux x86_64',
        'miserHardInfo':' ',
        'appkey': '00000000',
        'nickLoginLink':' ',
        'mobileLoginLink': 'https://login.taobao.com/member/login.jhtml?redirectURL=https://i.taobao.com/my_taobao.htm?nekot=YXNkOTA2NjYwOTI41580644908179&useMobile=true',
        'showAssistantLink':' ',
        'um_token': 'TFF401B6355D05371DEFCE2DB924D39287F52D89D6C233135A9460259E3',
        'ua': '122#geDeEJJAEEaYNDpZMEpaEJponDJE7SNEEP7rEJ+/5s8S4oQLpo7iEDpWnDEeK51HpyGZp9hBuDEEJFOPpC76EJponDJL7gNpEPXZpJRgu4Ep+FQLpoGUEJLWn4yP7SQEEyuLpERmIaf/prZCnaRx9kb/BsZk2SZXx+zx21jMUuYJlJIp/UVgkrfjPEAsIgEGZAQUz1t/qCtOrd5g3uy/KOIlHai+iY0PlHMrt2gYX9P6j6EzmrnuGQsWTlshhwN+y2yznTs/088p0EVDqMfW8seccM2/KyXGqRXr8CpwDUGJzCwkOgU4q8pxdgL1ulIEDLGrG2w7GPjEyF3D7MtbEEpCGGTCLPqEELjX8oLUJDIpyBfDqMfbDEpxnSp1uOIbELVZ8CpUJ4bEyF3mqWf2E5pangL4ul0EHhXZ8ohSJNEpyFffn9RbufyQVq8a8lwlpewTuJff/JmFbb5ZCOvRqa0T7b3kNZnHW0zL2GvPXCQ+revZFNsi2u9CI2bbnO9MgWNebAOzpAOx9dStW8IjWGl5AnQogTozUWBj8x6ao+Ttpb9nP3wdNlFHIBtp43AODz5kzJq7WU60Vta8WAyKN/ySDHFZFHQGQ3OEDtrvfO4NgAGQ3YGBm+BUUx0+HBc0Js090iQdo9J0ZdwejR3Gp1f8KQe2+qcPJP/cE+t09cImsVuy28D5H6TJEFYEO/oAkTKBHAjndJ4YNwvaNzaUXQQorl2hLuAgvaM71VwWdiavGffx3YeSb4HoOIwyQv25Jhp3bmfQpU+Clqai7kPwsWKHbRcYUGpc+N03tAUnAg7d4ao7sEbLkdFbrZ8pgD7b84mQod6uUFUtIAdBVboUclcC3RA61eELpNb7+tOV+mJGbcNlGEBtyeA6Lp51HpGUqhZPWex+dIaNKgjZDa4aX4ysJ08nY4sjaVLNb65Nl50zz049KXlwpfVr85MYudOr/y6zLg8hGPyQZ/AOBBNEZYuplP7CJxz7TmDD+XrCbhHjhDqteKlGc0x/uWNUSq6NxN9xNP9WW4iofYFrLGASfREMJMWSCLoXO5BRZWAkeGkfP+WWiokmcDxQy1FXFGijC20+H+woh/txsgtF9RiQDW/R+d6jeyCYijSzdb1tbAFTztWMsi/R/igOZKmqCPze5RzoFdURw8VE1eIdjk01uMVaCFqSPRCjhNxhQPq48KhcMdU2UAhCGTLL96qvLV5JNcvR45BTs7O7SSZtyxDIz5Cw8VLSKRJE/n+1vnDbrbavLTJdGe7o3ohboUS/lq0nrIOANub6BsUiaX5jts0r7a3KHpkeQZCFhUakmdkT4crbxR/sg1Z87zyU9hV3Mf/grjx7qQZ8jxY/NxXtc/cisFytgMQNoaZx4ADFiSCuGCCSwR97H+srjBTcW+bVZ/qrW8O4BX9KYMovCPTTu8F5S+3tu1ApUA/S2InotUtviEytIuSFMD==',
}

# 发起登录请求
res = req.post(url=login_url, headers=headers, data=data)

# 获取响应状态码判断状态
code = res.status_code
print(code)
if code == 200:
    # 发起新的请求，去获取目标数据
    res = req.get(url=url, headers=headers)
    # 把获取的数据写入一个文件
    with open('./tb.html', 'w') as fp:
        fp.write(res.text)
