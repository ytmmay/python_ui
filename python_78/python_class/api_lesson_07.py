
#上节课：4.执行结果与预期结果对比====是否通过===最终结果  5.最终结果写入excel表格
#注意excel表格读取的数字===文本===字符串
#eval()从字符串里面获取到python表达式
from python_class import  api_lesson_06#导入
def execute_fun(filename,sheetname):
    cases = api_lesson_06.read_data(filename, sheetname)  # 调用读取数据的函数
    for i in cases:
        case_id = i.get("case_id")
        url = i.get("url")  # 取url
        data = i.get("data")  # 取测试参数
        data = eval(data)  # 从字符串里面获取到python表达式，转化成为一个字典（去引号）
        ret = i.get("ex_ret")
        ret = eval(ret)
        msg = ret.get("msg")
        real_ret = api_lesson_06.api_function(url_api=url, data_api=data)  # 调用接口发送的参数
        real_msg = real_ret.get("msg")
        print("预期执行结果：{}".format(msg))
        print("真实执行结果：{}".format(real_msg))
        if msg == real_msg:
            print("通过")
            final_ret = "passed"
        else:
            print("第{}不通过".format(case_id))
            final_ret = "failed"
        print("*" * 20)
        api_lesson_06.write_result(filename, sheetname, final_ret, case_id + 1, 8)  # 调用写入结果函数，进行回写




'''
在已有框架下实现的自动化的脚本
完整自动化框架：
1.基础代码
2.测试数据
3.报告、日志
'''


if __name__ == '__main__': #只会在当前文件里执行，其他不会执行

    execute_fun("test_case_api.xlsx", "login")
