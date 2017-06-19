"""Example use of jupyter_kernel_test, with tests for IPython."""

import os
import unittest

import jupyter_kernel_test

from spylon_kernel.scala_interpreter import init_spark
from textwrap import dedent

coverage_rc = os.path.abspath(os.path.join(os.path.dirname(__file__), ".coveragerc"))
os.environ["COVERAGE_PROCESS_START"] = coverage_rc


class SpylonKernelTests(jupyter_kernel_test.KernelTests):
    kernel_name = "spylon-kernel"
    language_name = "scala"
    # code_hello_world = "disp('hello, world')"
    completion_samples = [
        {'text': 'val x = 8; x.toL',
         'matches': {'x.toLong'}},
    ]
    code_page_something = "x?"

    code_hello_world = '''
        println("hello, world")
        // Sleep for a bit since the process for getting text output is asynchronous
        Thread.sleep(1000)
        '''

    code_stderr = '''
        Console.err.println("oh noes!")
        // Sleep for a bit since the process for getting text output is asynchronous
        Thread.sleep(1000)
        '''

    complete_code_samples = ['val y = 8']
    incomplete_code_samples = ['{ val foo = 9 ']
    invalid_code_samples = ['val {}']

    code_generate_error = "4 / 0"

    spark_configured = False

    def setUp(self):
        """Set up to capture stderr for testing purposes."""
        super(SpylonKernelTests, self).setUp()
        self.flush_channels()
        if not self.spark_configured:
            self.execute_helper(code='%%init_spark --stderr')
            self.spark_configured = True


if __name__ == '__main__':
    unittest.main()