# 雪球app UI自动化

## PO设计分层

- basepage基础业务相关

  basepage.py 
    基础关键字find|click｜sedkeys的封装，异常弹窗黑名单的处理，steps测试步骤和测试数据的封装，通过yaml配置读取
      
  app.py 
    App的启动、停止、初始化cadesired_caps和driver的封装
      
  main.py 
    相当于主页APP的home跳转到不同的APP页签，例如goto_market跳转市场页，return到需要跳转到页面类
      
  search.py 
    自动化点击操作的业务类封装，search动作、reset动作、is_choose动作，通过读取对于yaml配置实现
  
- testcase测试用例相关

  conftest.py 
    前置条件数据处理、不同测试用例的数据共享，例如录屏
  test_search.py 
    查询的测试用例实现，通过链式调用组合基础关键字业务和业务关键子方法实现，其中其中包括断言
  asser.py 
    (待更新 通用断言)
  testbase.py 
    (待更新 所有测试用例继承testcase类，封装用例需需要初始化的方法等)
  test_search.yaml 
    测试用的测试数据配置提供给test_search.py读取
  
- report
  allure相关报告（待更新）
  
- util
  工具类扩展
 
