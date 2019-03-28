import re
from robot.api import logger    # noqa: F401 #pylint: disable=unused-import
from robot.libraries.BuiltIn import BuiltIn
from Castle.Core.Logging import LoggerLevel    # noqa: E402
from System import Console     # noqa: E402
from System.IO import StringWriter    # noqa: E402
from TestStack.White.Configuration import CoreAppXmlConfiguration, WhiteDefaultLoggerFactory    # noqa: E402


class LogWriter(object):
    def __init__(self):
        self.log_writer = StringWriter()
        # Redirect White's output to a StringWriter
        Console.SetOut(self.log_writer)

    def log_white_messages(self):
        messages = self.log_writer.ToString()
        for line in re.findall(r"(\[\w+\s-\s.+?\].*)", messages):
            if line.startswith("[Debug"):
                logger.debug(line)
            else:
                logger.info(line)
        # Empty the StringBuilder containing White's output
        string_builder = self.log_writer.GetStringBuilder()
        string_builder.Remove(0, string_builder.Length)


def update_white_log_level():
    log_lvl = BuiltIn().get_variable_value("${LOG_LEVEL}")
    if log_lvl in ("DEBUG", "TRACE"):
        CoreAppXmlConfiguration.Instance.LoggerFactory = WhiteDefaultLoggerFactory(LoggerLevel.Debug)
    else:
        CoreAppXmlConfiguration.Instance.LoggerFactory = WhiteDefaultLoggerFactory(LoggerLevel.Info)
