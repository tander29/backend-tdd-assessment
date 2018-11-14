import unittest
import subprocess


class TestEcho(unittest.TestCase):
    def test_help(self):
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()

        self.assertEquals(stdout, usage)

    def test_upper(self):
        process = subprocess.Popen(
            ["python", "./echo.py", "--upper", "hello"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()

        self.assertEqual(stdout, "HELLO\n")

    def test_lower(self):
        my_inputs = ["-l", "--lower"]

        for item in my_inputs:
            process = subprocess.Popen(
                ["python", "./echo.py", item, "HELLO"],
                stdout=subprocess.PIPE)
            stdout, _ = process.communicate()
            self.assertEqual(stdout, "hello\n")

    def test_title(self):
        process = subprocess.Popen(
            ["python", "./echo.py", "-t", "hello world"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()

        self.assertEqual(stdout, "Hello World\n")

    def test_multi_option(self):
        multi_options = ["-tul", "-ul", "-ltu", "-tu", "-tl", "-l", "-u"]

        for option in multi_options:
            process = subprocess.Popen(
                ['python', './echo.py', option, "hElLO!"],
                stdout=subprocess.PIPE)
            stdout, _ = process.communicate()

            if 't' in option:
                self.assertEqual(stdout, "Hello!\n")
            elif 'l' in option:
                self.assertEqual(stdout, "hello!\n")
            elif 'u' in option:
                self.assertEqual(stdout, "HELLO!\n")

    def test_no_options(self):
        text = "heLlo"
        process = subprocess.Popen(
            ['python', './echo.py', text],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()

        self.assertEqual(stdout, text + '\n')


if __name__ == "__main__":
    unittest.main()
