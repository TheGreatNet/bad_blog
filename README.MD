# 简介

本项目预期实现一个简单的博客系统，仅用于自身学习Django框架所用，不准备投入实际使用。

# 预期功能

+ 自动将特定文件夹下按照特定格式书写的Markdown文件渲染为博客展示所用的HTML页面（使用第三方库实现）。
+ 允许用户使用Github账号登录（使用Github OAuth API）。
+ 允许指定管理用Github账号，能够登录后台管理界面，对现有评论进行管理。
+ 后台管理界面可以新增、删除、编辑博客，管理现有评论。
+ RSS支持。

# TODO LIST

+ [ ] 配置Travis-CI，配置集成测试（待摸索）。
+ [ ] Markdown渲染至HTML。
+ [ ] 使用Github账号登录。
+ [ ] 从配置文件中读取博客所有者的Github账号，并提供管理者权限。
+ [ ] 登录后评论功能（此时只能在后台中查看评论）。
+ [ ] 服务端渲染评论至博客页面（此时不允许对评论进行回复）。
+ [ ] 为评论提供回复功能，仿[阮一峰的博客](http://www.ruanyifeng.com/blog/)。
+ [ ] 提供RSS服务。

# 杂项

+ 为简化部署，使用SQLite作为项目数据库。
+ Gitmoji使用规范:<https://gitmoji.carloscuesta.me/>

# 开发环境

+ Python 3.6(64bit)
+ Django(2.0)