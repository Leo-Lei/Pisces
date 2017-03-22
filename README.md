# Get started now!
在终端执行如下命令，该脚本会将一切都准备好，就是这么简单
```bash
curl -s "https://raw.githubusercontent.com/Leo-Lei/Pisces/master/.install.sh" | bash
```
脚本将会做以下事情：
1. 安装一些自定义python模块，包括一些工具类库
2. 安装docker engine
3. 配置docker registry
4. 安装run.py。该脚本支持以linux systemd服务启动spring-boot的JAR包，还支在tomcat的docker容器中运行WAR包。
5. 安装其他python脚本，有:
    * docker运行disconf
    * docker运行mysql
    * docker运行redis
    * docker运行mongodb
    * docker运行elk
    * 运行dubbo-monitor
    
