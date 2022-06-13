import logging
from seleniumactions.actions import Actions

log = logging.getLogger('ASSERTIONS')


def assert_condition(actions: Actions, condition: object,
                     timeout: str = None, explicit_timeout: int = None, message: str = None):
    """
    Opakowuje actions.wait_for w try/except + fail msg
    """
    try:
        actions.wait_for(condition=condition, timeout=timeout, explicit_timeout=explicit_timeout)
        log.info(f"met condition :) {condition}")
    except Exception as e:
        msg = f"condition not met :( {condition}\nException: {repr(e)}"
        log.error(msg)
        assert False, f"{message}\n{msg}"
