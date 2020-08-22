# PocLibrary - 定制界面版个人POC/EXP脚本仓库

<p align="center">
  <a href="https://github.com/Coldwave96/PocLibrary">
    <img src="https://raw.githubusercontent.com/Coldwave96/PocLibrary/master/logo.ico" alt="PocLibrary">
  </a>
<p>

<p align="center">
  <a><img src="https://img.shields.io/badge/Python-3-blue"></a>
  <a><img src="https://img.shields.io/github/license/Coldwave96/PocLibrary"></a>
  <a><img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Mac-orange"></a>
  <a><img src="https://img.shields.io/github/issues/Coldwave96/PocLibrary?color=lightgreen"></a>
  <a><img src="https://img.shields.io/github/forks/Coldwave96/PocLibrary?color=lightred"></a>
  <a><img src="https://img.shields.io/github/stars/Coldwave96/PocLibrary?color=red"></a>
  <a><img src="https://img.shields.io/github/v/release/coldwave96/PocLibrary?color=lightblue"></a>
  <a><img src="https://img.shields.io/github/contributors/Coldwave96/PocLibrary?color=yellow"></a>
</p>

<p align="center">
  <a href="https://coldwave96.github.io/">Welcome to my personal blog（＾◇＾）</a>
</p>

<hr>

## 项目起源

* 是否觉得到处收集的POC/EXP脚本临乱无章？

* 是否觉得到处fork的POC/EXP仓库难以管理？

* 感谢[@zhzyker的exphub项目](https://github.com/zhzyker/exphub)给的灵感

* 设计归类了这样一个可视化POC/EXP仓库

## 数据格式

* Library中存放着POC/EXP脚本文件以及对应脚本和漏洞介绍

    * script_name，POC/EXP脚本
    
    * script_name.txt，POC/EXP脚本及用法介绍
    
    * script_name_vul.txt，POC/EXP脚本对应漏洞介绍

* 脚本类型可以大致分为[漏洞验证脚本]、[漏洞利用脚本]、[远程命令执行脚本]、[shell交互脚本]、[Webshell上传脚本]

    * cve-xxxx-xxxx_poc [漏洞验证脚本] 仅检测验证漏洞是否存在
    
    * cve-xxxx-xxxx_exp [漏洞利用脚本] 例如文件包含、任意文件读取等常规漏洞
    
    * cve-xxxx-xxxx_rce [远程命令执行脚本] 命令执行漏洞利用脚本，无法交互
    
    * cve-xxxx-xxxx_cmd [远程命令执行脚本] 命令执行漏洞利用脚本，无法交互
    
    * cve-xxxx-xxxx_shell [远程命令执行脚本] 直接反弹Shell，或者提供简单的交互Shell以传递命令,基础交互
    
    * cve-xxxx-xxxx_webshell [Webshell上传脚本] 自动或手动上传Webshell

## 脚本数量

* 脚本名称单独放在data.py文件中，v1.0版本总共有14个模块，59个POC/EXP脚本

* 后续版本增加脚本将在Reease中说明

## v1.0版本模块

* Apache-Solr

* Drupal

* F5

* Fastjson

* IIS

* Jboss

* Linux-local：Linux本地提权脚本

* Nexus

* Shiro

* Spring

* Struts2

* Tomcat

* Weblogic

* Webmin

## 文件说明

* PocLibrary.py：入口脚本

* Poclibrary.spec：pyinstaller配置文件

* data.py：数据仓库

* gui.py：wxpython创建的GUI + 功能函数

* logo.icns：Mac下APP的logo文件

* logo.ico：Win下exe的logo文件

* setup.py：py2app配置文件

## 依赖库

* 程序运行依赖库

    * wxpython

    * pyperclip

* 程序打包依赖库

    * py2app
    
    * pyinstaller

## 使用方法

* 运行

    * 根据操作系统（Win or Mac）直接下载Release中对应版本
    
    * 双击运行即可

* 改造

    * 根据需要自行改造源码
    
* 打包

    * Mac：`python3 setup.py py2app`（建议在项目文件夹中建立虚拟环境，否则可能会出错）
    
    * Win：`pyinstaller -F PocLibrary.spec`
    
## To Do List

* 调整现有脚本及漏洞描述文件的内容，增加更多模块和脚本

* 界面美化（如果有时间）

* 解决现有Bug，详见Release说明