"""
@file: 密码验证合格程序
@AUTHOR : brooks
@time: 2025/7/26 21:07
@desc:

描述：
你需要书写一个程序验证给定的密码是否合格。

合格的密码要求：
长度不少于8位
必须包含大写字母、小写字母、数字、特殊字符中的至少三种
不能分割出两个独立的、长度大于2的连续子串，使得这个两个子串完全相同；更具体地，如果存在两个长度大于2的独立子串s1,s2，使得s1=s2, 那么密码不合法。

子串为从原字符串中，连续的选择一段字符（可以全选、可以不选）得到的新字符串。

可见字符集为ASCII码在33到126范围内的可见字符。您可以参阅下表获得其详细信息（您可能关注的内容是，这其中不包含空格、换行）。

输入描述：
本题将会给出1≤T≤10组测试数据，确切数字未知，您需要一直读入知道文件结尾；每组测试数据描述如下：

在一行上输入一个长度为1≤length(s)≤100，由可见字符构成的字符串s, 代表待判断的密码。

输出描述：
对于每一组测试数据，新起一行。若密码合格，输出OK， 否则输出NG。


"""
import sys

def has_repeated_substring(s_password):
    # 检查是否存在两个独立的、长度大于2的相同子串
    length = len(s_password)
    # sub_length 是子串的长度，从3开始，最大到 length // 2（因为两个相同子串的总长度不能超过原字符串长度）。
    #
    # 例如，如果 s_password 长度为10，则 sub_length 的可能值为3、4、5。
    for sub_length in range(3, length // 2 + 1):
        # 对于每个可能的子串长度 sub_length，遍历字符串中的所有起始位置 i。
        #
        # s_password[i:i+sub_length] 是从位置 i 开始、长度为 sub_length 的子串。
        for i in range(length - sub_length + 1):
            substirng = s_password[i:i+sub_length]
            remaining = s_password[i+sub_length:]
            if substirng in remaining:
                return True
    return False


def check_password(s_password):
    # 条件1: 长度不少于8位
    if len(s_password) < 8:
        return "NG"

    # 条件2: 检查字符类型
    has_upper = any(c.isupper() for c in s_password)
    has_lower = any(c.islower() for c in s_password)
    has_digit = any(c.isdigit() for c in s_password)
    has_special = any(not c.isalnum() for c in s_password)

    # 统计满足的字符类型数量
    type_count = sum([has_upper, has_lower, has_digit, has_special])
    if type_count < 3:
        return "NG"

    # 条件3: 检查是否存在重复子串
    if has_repeated_substring(s_password):
        return "NG"

    return "OK"

if __name__ == '__main__':
    for line in sys.stdin:
        password = line.strip()
        if password:  # 确保不是空行
            print(check_password(password))