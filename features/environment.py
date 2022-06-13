import json, logging, os
from behave import use_fixture, fixture
from selenium.webdriver.chrome.webdriver import WebDriver as Chromedriver
from selenium.webdriver.chrome.service import Service as ChromeService
from seleniumactions import FluentFinder, Actions


logger = logging.getLogger(__name__)

LOCAL_CONFIG_FILE = 'config.local.json'
CONFIG_FILE = os.environ.get('CONFIG_FILE', LOCAL_CONFIG_FILE)

if CONFIG_FILE == LOCAL_CONFIG_FILE: print(f'[!!!]USING LOCAL CONFIG FILE: {LOCAL_CONFIG_FILE}[!!!]')


@fixture
def config(context):
    """
    Read configuration file
    """
    try:
        with open(CONFIG_FILE, 'r', encoding='utf-8') as conf:
            static_config = json.load(conf)
    except Exception as e:
        raise EnvironmentError(f'Failed to load config file {CONFIG_FILE}...\n{repr(e)}')

    confjson = json.dumps(static_config, indent=2)
    logger.info(f"[CONFIG] -> {confjson}")
    context.configuration = static_config
    return context.configuration


@fixture
def chromedriver(context):
    """
    Create chromedriver object
    """
    cfg = use_fixture(config, context)
    chromeservice = ChromeService(executable_path=cfg["webdriver"]["path"])
    chromedriver = Chromedriver(service=chromeservice)
    yield chromedriver

    chromedriver.quit()  # ! close after scenario is done


@fixture
def actions(context):
    """
    Create actions object
    """
    driver = use_fixture(chromedriver, context)
    cfg = context.configuration
    default_finder_timeout = cfg["timeouts"][cfg["finder_default_timeout"]]
    ffinder = FluentFinder(
        webdriver=driver,
        timeouts=cfg["timeouts"],
        default_timeout=default_finder_timeout
    )
    actions = Actions(
        finder=ffinder,
        wait_for_condition_timeout=cfg["actions_timeouts"]["wait_for_condition"],
        wait_between=cfg["actions_timeouts"]["sleep_between"]
    )
    context.actions = actions
    return context.actions



def before_tag(context, tag):
    # ! for each scenario taggerd with @web we do Dependency Injection with actions object
    if tag == "web":
        use_fixture(actions, context)
