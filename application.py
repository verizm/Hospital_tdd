
class Application:
    def __init__(self, commands, io_helper):
        self._commands = commands
        self._io_helper = io_helper
        self._in_process = True

    def run(self):
        while self._in_process:
            self._process()

    def _stop(self):
        self._in_process = False

    def _process(self):
        cmd = self._io_helper.request_command()

        if cmd == "get status":
            self._commands.get_status()

        if cmd == "status up":
            self._commands.status_up()

        if cmd == "стоп":
            self._io_helper.send_stop_application()
            self._stop()
