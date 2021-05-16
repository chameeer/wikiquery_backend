# WikiQuery (backend)
这里是 WikiQuery 项目的后端仓库, WikiQuery 是一款用于轻松查询和浏览维基百科资料的应用，主要面向移动端。

## 后端开发技术栈
- Flask
- Spark

## 如何加入
参与贡献前，请详细阅读 [Wiki页面](https://github.com/chameeer/wikiquery_backend/wiki) 中 “开发规约与建议” 和 “Commit 规范” 的内容。

### 前置需求
需要有 Python 或者 Anaconda 环境。

### 配置环境和依赖
在已经安装 Anaconda 的情况下，通过

```conda create -n wiki python=3.7``` 

创建全新环境

```conda activate wiki```

进入环境

```conda install flask flask-restful pyspark```

安装依赖

### 测试是否配置成功
进入项目根目录，在终端中执行

```python app.py```

打开浏览器，在地址栏中输入

```localhost:5000```

若看到以下显示，说明已经配置成功了。

```{hello: world}```




