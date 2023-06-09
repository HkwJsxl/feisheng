

## 飞升项目后台



### 介绍

~~~python
Django3.2.18项目
~~~

### 技术栈

~~~python
1.项目搭建和基本配置
日志配置，自定义response对象，自定义异常处理，mysql数据库连接池配置，redis缓存配置，解决跨域问题
2.站点首页功能完善
自定义basemodels模型类，导航栏模型类，自定义mixins，自定义返回状态码，轮播图模型类开放静态文件的url，缓存导航与轮播图数据
3.登录和注册功能实现
扩展Django用户模型类字段，JWT的认证流程，集成JWT登录认证，多方式登录，更新异常处理函数，手机号短信平台接入(容联云)，短信验证码做缓存，客户端实现多功能登录和注册
4.Redis&Celery异步任务
redis高级操作，celery异步框架的集成
5.课程管理模块实现
课程列表api实现，simpleui美化admin站点，添加富文本编辑器，给图片字段生成缩略图（小中大），分页排序...
虚拟化技术：docker/podman的使用
elasticsearch/elasticsearch-head/kibana安装和使用，elasticsearch集成到服务端项目中(haystack)，课程全文搜索，热门关键字搜索
课程详情页/课程章节api实现
6.价格优惠策略&购物车的实现（优惠券、积分）
7.下单并支付（使用优惠券和积分），supervisor管理celery异步处理订单
8.课程学习相关实现，集成视频（第三方保利威平台）
9.项目部署（linux/docker/docker-compose/ssh/nginx）
~~~

