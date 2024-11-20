
class Application:
    def __init__(self, commands, communication_with_user):
        self._commands = commands
        self._communication_with_user = communication_with_user
        self._in_process = True

    def run(self):
        while self._in_process:
            self._process()

    def _stop(self):
        self._in_process = False

    def _process(self):
        cmd = self._communication_with_user.request_command()

        if cmd == "get status":
            self._commands.get_status()

        if cmd == "status up":
            self._commands.status_up()

        if cmd == "стоп":
            self._communication_with_user.send_stop_application()
            self._stop()
