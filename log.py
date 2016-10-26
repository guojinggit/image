import sys
import datetime


def info(context):

    """Return the frame object for the caller's stack frame."""
    try:
        raise Exception
    except:
        f = sys.exc_info()[2].tb_frame.f_back
    time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    text = "{} function:{}() lineNum:{}    {}".format(
        time_now, f.f_code.co_name, f.f_lineno, context)
    print text
