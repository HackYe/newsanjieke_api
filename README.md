一、项目描述：

        newsanjieke_api 接口自动化测试框架
        
        该项目主要是针对已经通过测试接口进行回归，保证已经通过测试的接口不会因为升级或者迭代而出现问题
引言
        
        部署环境时，首先执行requirements.txt，命令如下:
        导出环境中的第三方库：pip freeze > requirements.txt
        新的服务器导入第三方库：pip -r install requirements.txt
    
二、各个模块简介

    1、Base封装Request方法
    
        base_request 操作接口，其中封装了get和post方法(如后期有需要可以增加请求方式)
    
    2、Case测试用例维护目录
    
        sanjieke_auto.xlsx 维护测试用例

    3、Common封装的常用的方法
        
        dir_config 方法为定义路径方法，获取文件路径和其他参数的路径
        get_data 方法为获取替换变量的数据
        html_read 读取html报告中的文本数据，用于发送邮件的正文
        HTMLTestRunner_cn 生成测试报告的文件
        Send_email 发送邮件的方法
        
    4、Config配置文件存储目录
    
        header.ini 存储header的配置文件
        mysql.in 存储数据库的配置文件
        server.in 存储测试环境的文件 (Online、pre、Beta)

    5、image图片存储目录
    
        image.png 上传头像接口用到的图片
        
    6、Outputs测试报告输出目录
    
        html 此文件夹存储测试报告(html的方式)
        
    7、TestCases测试用例存放目录
    
        Run 使用unittest，调用defaultTestLoader方法，加载discover，用来查询某个文件夹下以test_开头的.py结尾的文件，用来执行所有的测试用例，并生成测试报告
        Run_Email 在Run的基础上加入发送邮件的功能
        stencil 测试用例的模版
        test_001_universal_interface 通用接口的测试用例
        test_002_buy_self_study_course 购买自学课并学习的测试用例
        test_003_buy_training_camp_course 购买训练营并学习的测试用例
        test_004_redeem_coupons 兑换优惠券的测试用例
        test_005_login_and_register 登录和注册的测试用例
        test_006_change_phone_number 更换手机号的测试用例
        test_007_change_password 更换密码的测试用例
       
    8、Tools
    
        handle_excel 读取和写入excel的方法
        handle_init 读取配置文件的方法
        handle_mysql 读取mysql的方法
        handle_replace 替换数据的方法
        handle_result json格式比对的方法