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

```json
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


## Actions

Every gherkin test tagged `@web` gets actions available via `context` argument in `@step` implementation.

`context` is behave Context (see behave docs).

Example access to actions:

```python
from behave import step
from seleniumactions import Actions


@step('some cool gherkin step')
def mystep(context):
    actions: Actions = context.actions
```

From now on you can use actions everywhere 🚀

### Examples

```python
from seleniumactions import Actions, LocatorExists, XpathExists


actions: Actions = context.actions

# locators (tuples)
main_header = ('xpath', '//h1[.="Home"]')
menu = ('id', 'menu')
news_option = ('xpath', '//menu-option[.="News"]')
search_input = ('xpath', '//search-news//input')
form = ('xpath', '//form')

# take some actions 🚀
actions.goto('https://some.site.io')  # open site
actions.wait_for(LocatorExists(main_header))  # wait for condition to be met with default timeout from configuration applied
actions.click(menu)  # default timeout from configuration applied
actions.click(news_option, timeout='medium')  # 'medium' timeout from configuration applied
actions.type_text(search_input, text='python', explicit_timeout=3)  # explicit timeout in seconds (always overrides any timeout from configuration)
actions.submit()  # submit default form (//form) - works when theres only one form on page
# actions.submit(form)  # u can pass form locator also
actions.wait_for(XpathExists('//search-results'), timeout='long')  # wait for condition with 'long' timeout from configuration applied

# assert ect...
```

## Locators

Lest say we have HTML component (simplified for example 👀)


```html
<ul>
    <li class="menu"> Foo</li>
    <li class="menu"> Bar </li>
    <li class="menu">Baz </li>
</ul>
```

We want to  be able to click each one of them. So the xpath values for them will be:

```python
foo_xpath = "//ul/li[@class='menu' and contains(., 'Foo')]"
bar_xpath = "//ul/li[@class='menu' and contains(., 'Bar')]"
baz_xpath = "//ul/li[@class='menu' and contains(., 'Baz')]"
```

It can be painfull. Of course you can write a function and parametrize the string

```python
def get_menu_xpath(label: str):
    return f"//ul/li[@class='menu' and contains(., '{label}')]"
```

It's kind of frustrating...

We can use Locator class to solve that problem
```python
from seleniumactions import Locator

# You can define any parameters to a locator value template
menu_element = Locator(Using.XPATH, "//ul/li[@class='{class_name}' and contains(., '{label}')]")
menu_element.get_by(class_name='menu', label='Foo')
# >>> ("xpath", "//ul/li[@class='menu' and contains(., 'Foo')]")
menu_element.get_by(class_name='active-menu', label='Bar')
# >>> ("xpath", "//ul/li[@class='active-menu' and contains(., 'Bar')]")

# When you forget to pass values you'll get clear error
button = Locator(Using.NAME, '{action}-{foo}')
button.get_by()
# ValueError: get_by method is missing keyword arguments: ['action', 'foo']
button.get_by(action='goto')
# ValueError: get_by method is missing keyword argument: foo

# cool! 🕹 we can play with it!
```


### Examples (advanced)

We can go step further and implement our own custom locators 🚀
```python
# utils/locators.py
from seleniumactions import Using, Locator


class ButtonByLabel(Locator):
    def __init__(self) -> None:
        super().__init__(Using.XPATH, "//button[.='{label}']")


class ButtonSubmit(Locator):
    def __init__(self) -> None:
        super().__init__(Using.XPATH, "//button[@type='submit']")


class LinkByExactText(Locator):
    def __init__(self) -> None:
        super().__init__(Using.XPATH, "//a[.='{text}']")


class LinkByContainedText(Locator):
    def __init__(self) -> None:
        super().__init__(Using.XPATH, "//a[contains(.='{text}')]")


class HeaderByExactText(Locator):
    def __init__(self) -> None:
        super().__init__(Using.XPATH, "//h*[.='{text}']")

# You can easly match the composition of webapp you're testing with simple classes that inherit from Locator

class Locators:
    # for importing and better intellisence in other modules
    link = LinkByExactText()
    link_contains = LinkByContainedText()
    button = ButtonByLabel()
    submit_button = ButtonSubmit()
    header = HeaderByExactText()


###########################################
# test.py
from utlis.locators import Locators as Loc

# raw calling
actions.click(Loc.link.get_by(text='HOME'))
actions.wait_for(Loc.header.get_by(text='Welcome home!'))
actions.click(Loc.link_contains.get_by(text='see more...'))
actions.click(Loc.button.get_by(label='Next'))
actions.click(Loc.submit_button.get_by())

# or for more readability
home_link = Loc.link.get_by(text='HOME')
see_more_link = Loc.link_contains.get_by(text='see more...')
next_button = Loc.button.get_by(label='Next')
submit_button = Loc.submit_button.get_by()
home_header = Loc.header.get_by(text='Welcome home!')

actions.click(home_button)
actions.wait_for(home_header)
actions.click(see_more_link)
actions.click(next_button)
actions.click(submit_button)

# SUPER DRY!
```


## Real life examples

`features/saskodzi/blog.feature`

`features/steps/saskodzi_steps_*.py`
