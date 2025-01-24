# ReplyCommandAPI-MCDR
可替代`CommandSource.reply()`，支持自定义Logger插件（MCDR）和Skript插件FakePlayerCommand。

## 用法
### 前置条件
在服务端安装类似[FakePlayerCommand](https://github.com/Mooling0602/FakePlayerCommand-Skript/tree/main)的插件，或者直接使用游戏客户端进行测试。

使用服务端插件会更方便测试。

### API效果
如图所示，控制台将会同时输出发送给玩家的内容，且支持使用自定义的logger实例来显示相关日志：
![32225fc4e90ac439cae93a6a292c6613](https://github.com/user-attachments/assets/811044e2-9315-41f9-a291-8d8a8100ea4d)

### 如何导入并使用
```python
# 在此参考代码中，插件元数据需明确声明依赖rc_api >= 0.0.1
from rc_api import cmdReply
from mcdreforged.api.all import *

builder = SimpleCommandBuilder()

reply = cmdReply()

def on_load(server: PluginServerInterface, prev_module):
    builder.register(server)

@builder.command('!!your_cmd')
def on_command(src: CommandSource):
    # 若不需要输出到控制台，直接使用src.reply("message")或reply(src, "Message")
    reply.log(src, "message")
    # 若有自定义的logger实例例如your_logger = custom_logger()，使用reply.log(src, "Message", your_logger)
```
