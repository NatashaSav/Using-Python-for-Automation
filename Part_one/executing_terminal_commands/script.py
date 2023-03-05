import subprocess


class RunProcess:
    def __init__(self, script_path: str):
        self.script_path = script_path

    def run(self):
        subprocess.check_call(['python', self.script_path])


if __name__ == "__main__":
    process = RunProcess('example.py')
    for i in range(0, 5):
        process.run()
