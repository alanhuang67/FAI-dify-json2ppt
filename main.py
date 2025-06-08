import logging
import sys

from dify_plugin.plugin import Plugin
from dify_plugin.config.config import DifyPluginEnv

# 配置日志输出到标准错误流，用于早期调试
logging.basicConfig(level=logging.INFO, stream=sys.stderr, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

logger.info("main.py: 插件入口点已达到")

# Plugin is the entry point for the plugin, the environment parameters come from Dify.
# Default parameters can be set when initializing Plugin.
plugin = Plugin(DifyPluginEnv(MAX_REQUEST_TIMEOUT=30))

if __name__ == "__main__":
    logger.info("main.py: 准备启动插件服务")
    plugin.run()
    logger.info("main.py: 插件服务已启动 (或已结束)")
