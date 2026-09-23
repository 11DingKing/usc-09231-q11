# 独立基础项目

这是从上游真实项目父版本整理出的独立 Python 基础快照，保留复现缺陷所需的源码、测试和配置。

准备环境（快照仅包含 `beets/metadata_plugins.py`，其余 beets 模块由已安装的 beets 包提供）：

```bash
python3 -m venv .venv
.venv/bin/pip install beets==2.14.1 pytest
```

运行测试：

```bash
.venv/bin/python -m pytest
```

检查构建：

```bash
.venv/bin/python -m compileall .
```
