- 启动app
```shell
python3 manage.py startapp [app路径]
```
- 启动项目
```shell
python3 manage.py runserver
```
- 生成model配置文件
```shell
 python3 manage.py makemigrations
```

- 生成数据库表（根据model配置文件）
```shell
python3 manage.py migrate
```
- 导出依赖到配置文件
```shell
pip3 freeze > requirements.txt
```
- 安装依赖
```shell
pip3 install -r requirements.txt
```