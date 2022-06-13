# Selenium Actions project example

## Stack

* behave
* selenium-actions

## Python env and dependencies

```sh
# create env
> python -m venv env
# activate env mac/linux
>. ./env/bin/activate
# activate env windows
> env/Scripts/activate
# install dependencies inside env
(env) > pip install -r requirements.txt
```

## Run tests

Run tests with tag `@saskodzi` with HTML report in `reports/behave-report.html`

`behave --tags=saskodzi -f html -o reports/behave-report.html -f pretty`

## Configuration

Example configuration

```jsonc
// config.yours.json
// all timeouts are in seconds (float)
{
    /*
    webdriver - webdriver configuration
    */
    "webdriver": {
        "type": "chromedriver",  // only local chromedriver for now 👀
        "path": "/path/to/chromedriver"
    },
    /*
    timeouts - timeouts can be used fo overriding timeouts in actions
               see examples above
    ex:
      actions.click(locator, timeout="long")  # 10 sec
    */
    "timeouts": {
        "short": 3,
        "medium": 5,
        "long": 10,
        "absurd": 30
    },
    /*
    finder_default_timeout - default timeout variant for finder (when not using 'timeout' argument)
    ex:
      actions.click(locator)  # 3 sec
    */
    "finder_default_timeout": "short",
    /*
    actions_timeouts - specific for actions
    - wait_for_condition - default timeout for actions.wait_for(condition)  # 30 sec
    - sleep_between - sleep for certian actions
      ex: actions.click(locator)
    /*
    "actions_timeouts": {
        "wait_for_condition": 30,
        "sleep_between": 0.5
    }
}
```

You can set any desired configuration using `CONFIG_FILE` env variable.

```sh
export CONFIG_FILE=config.yours.json
```

When `CONFIG_FILE` is not set, environment.py is looking for `config.local.json` file.
