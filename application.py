
class Application:
    def __init__(self, commands, user_interaction):
        self._commands = commands
        self._user_interaction = user_interaction
        self._in_process = True

    def run(self):
        while self._in_process:
            self._process()

    def _stop(self):
        self._in_process = False

    def _process(self):
        cmd_type = self._user_interaction.request_command()

        if cmd_type == "get_status":
            self._commands.get_status()

        if cmd_type == "status_up":
            self._commands.status_up()

        if cmd_type == "statistic":
            self._commands.calculate_statistic()

        if cmd_type == "stop":
            self._user_interaction.send_stop_application()
            self._stop()
