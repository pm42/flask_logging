"""This test the log file creation"""
import os


def test_info_log_file_creation():
    """This tests the info log creation"""
    # get root directory of project
    root = os.path.dirname(os.path.abspath(__file__))
    # set the name of the apps log folder to logs

    logdir = os.path.join(root, '../app/logs/info.log')
    assert os.path.exists(logdir)


def test_debug_log_file_creation():
    """This tests the debug log creation"""
    # get root directory of project
    root = os.path.dirname(os.path.abspath(__file__))
    # set the name of the apps log folder to logs

    logdir = os.path.join(root, '../app/logs/debug.log')
    assert os.path.exists(logdir)

