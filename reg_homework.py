import re
s = """
为了让大家练习正则表达式，我写了以下一篇短文章（有可能逻辑不是特别好，但主要不是为了写文章，而是想让大家练习正则啊，煞费苦心）正文开始：
做个自我介绍吧，我叫周景阳，现在我在贪心学院任职教学副院长.
2018年3月1日，我们在北京注册了贪心学院，我们的官网是http://www.greedyai.com/,我的手机号码是13888886666，如果是真的该有多好。
我的邮箱是42197393@qq.com,我还有另外一个邮箱zjingyang@sina.com，邮箱可是真的，但邮件我不常看，我的qq是:42197393。
在2014-04-01，这个时间时，我第一次接触了AI。
当时我还在苦练编码能力，当时做了一套分布式系统，用了3台服务器，IP分别是：192.168.1.107,236.142.271.23和142.168.122.1。
搭建了一套kafka + storm 分布式流式实时计算引擎，当时用这套架构搞big data实时计算，还是非常流行的。
但突然间就搞起来了知识图谱、聊天机器人等AI相关的项目，对于当时的我来说，来一句发自肺腑的话，真的挺难的，中间踩了很多坑。
基于这些想法，我们出来创办了贪心学院，我们的目标是以项目式学习的方式，让大家能够在实战中掌握知识点,快速转型AI。
"""

# 按照以下格式进行代码开发

def get_skypegmwcn(s):
    result = re.findall(r'\w{4}://\w{3}\.\w{8}.\w{3}',s)
    # 匹配出贪心科技的官网

    return result



def get_email(s):
    result = re.findall(r'([a-zA-Z0-9]{1,}@(?:qq|sina)\.com)',s)#正则中？：代表非捕获
    # 匹配出邮箱

    return result


def get_telphone(s):
    result = re.findall(r'(?:138|137)\d{1,}',s)
    # 匹配出手机号码

    return result
print(get_telphone(s))


def get_time(s):
    result = re.findall(r'\d{4}-\d{2}-\d{2}|\d{4}年\d{1,2}月\d{1,2}日',s)
    # 匹配出时间


    return result



def get_qq(s):
    result = re.findall(r'我的qq是:(.*)。',s)
    # 匹配出qq号码

    return result



def get_ai_count(s):
    result =len(re.findall(r'AI',s))
    # 匹配出AI一共出现了多少次
    return result


def get_IP(s):
    result = re.findall(r'\d{3}\.\d+\.\d+\.\d+',s)
    # 匹配出所有的ip

    return result




