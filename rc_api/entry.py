from mcdreforged.api.all import *


def on_load(server: PluginServerInterface, prev_module):
    server.logger.info("ReplyCommandAPI loaded successfully!")