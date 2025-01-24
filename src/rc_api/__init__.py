from mcdreforged.api.types import CommandSource, ServerInterface


psi = ServerInterface.psi()

class psiLogger:

    def info(self, *args):
        psi.logger.info(args[0])

    def warning(self, *args):
        psi.logger.warning(args[0])
    
    def error(self, *args):
        psi.logger.error(args[0])

    def critical(self, *args):
        psi.logger.critical(args[0])

    def debug(self, *args):
        psi.logger.debug(args[0])

class cmdReply:
    def _send_message(self, src: CommandSource, message: str):
        if src.is_player:
            psi.tell(src.player, message)

    def __call__(self, src: CommandSource, message: str):
        self._send_message(src, message)

    def log(self, src: CommandSource, message: str, logger=psiLogger()):
        self._send_message(src, message)
        if src.is_player:
            try:
                logger.info(f"[-> {src.player}] {message}")
            except Exception:
                psi.logger.warning("Your logger instance is incompatible! Fallbacking to psi logger.")
                psi.logger.info(f"[-> {src.player}] {message}")
        else:
            psi.logger.warning("Command is not from any player or fake messages!")