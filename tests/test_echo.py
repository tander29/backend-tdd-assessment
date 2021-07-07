import unittest
import subprocess
from echo import create_argparser


class TestEcho(unittest.TestCase):
    def setUp(self):
        self.parser = create_argparser()

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

        namespace = self.parser.parse_args(['-u', 'hello'])
        namespace2 = self.parser.parse_args(['--upper', 'hello'])
        self.assertTrue(namespace.upper)
        self.assertTrue(namespace2.upper)

    def test_lower(self):
        my_inputs = ["-l", "--lower"]

        for item in my_inputs:
            process = subprocess.Popen(
                ["python", "./echo.py", item, "HELLO"],
                stdout=subprocess.PIPE)
            stdout, __ = process.communicate()
            namespace = self.parser.parse_args([item, 'HELLO'])
            self.assertEqual(stdout, "hello\n")
            self.assertTrue(namespace.lower)

    def test_title(self):
        process = subprocess.Popen(
            ["python", "./echo.py", "-t", "hello world"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        namespace = self.parser.parse_args(['-t', 'hello world'])
        namespace2 = self.parser.parse_args(['--title', 'hello world'])
        self.assertEqual(stdout, "Hello World\n")
        self.assertTrue(namespace)
        self.assertTrue(namespace2)

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
        namespace = self.parser.parse_args([text])
        self.assertEqual(stdout, text + '\n')
        self.assertFalse(namespace.upper)
        self.assertFalse(namespace.lower)
        self.assertFalse(namespace.title)


if __name__ == "__main__":
    unittest.main()
