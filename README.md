# Flask Server

Flask 服务框架项目

## 快速开始

### 1. 环境安装

```bash
conda create -n flask python=3.12
conda activate flask
pip install -r requirements.txt
```

### 2. 启动服务

```bash
python run.py
```

默认监听端口：`8080`

## 配置说明

| 配置项 | 文件位置 | 说明 |
|--------|--------|------|
| 端口、常见配置 | `setting.py` | 修改服务端口和其他基础配置 |
| 接口开发 | `app.py` | 在此文件中开发新接口 |
| 日志配置 | `logger.py` | 配置日志级别和输出方式 |

## 访问服务

### 本地访问

```
http://localhost:8080
http://localhost:8080/call_back
```

### 远程访问

将 `localhost` 替换为：
- 机器的外网 IP 地址
- 域名（需要已配置解析）

## 测试

确保服务已启动，然后在新终端中运行：

```bash
python test_api.py
```