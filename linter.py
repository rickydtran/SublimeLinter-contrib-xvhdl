#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by BrunoJJE 
# Updated by Ricky Tran

"""This module exports the Xvhdl plugin class."""

from SublimeLinter.lint import Linter


class Xvhdl(Linter):

    """Provides an interface to xvhdl (from Xilinx Vivado Simulator)."""

    # cmd = 'xvhdl $file'
    cmd = 'xvhdl @'
    tempfile_suffix = 'vhd'

    regex = (
        r"^(?P<error>ERROR: )(?P<message>\[.*\].*)"
        r"\[(?P<path>.*):(?P<line>[0-9]+)\]"
    )

    defaults = {
        'working_dir': '$project_path',
        'args' : "-nolog -2008",
        'selector': 'source.vhdl'
    }

    def split_match(self, match):
        """
        Extract and return values from match.
        We override this method to prefix the error message with the
        linter name.
        """

        match, line, col, error, warning, message, near = super().split_match(match)

        if match:
            message = '[xvhdl] ' + message

        return match, line, col, error, warning, message, near