from behave import step
from seleniumactions import Actions, LocatorExists, assert_condition
# ! todo: cooler - locator , custom locator, custom condition

@step('że blog zostanie odwiedzony używając domeny {url}')
def open_blog(context, url: str):
    actions: Actions = context.actions
    actions.goto(url)


@step('odwiedzający kliknie przycisk "Blog"')
def click_blog_button(context):
    actions: Actions = context.actions
    blog_button = ("xpath", "//a[.='Blog']")
    actions.click(blog_button)


@step('powinien zostać przekierowany do strony z blogiem')
def should_be_redirected_to_blog_posts(context):
    actions: Actions = context.actions
    url = actions.webdriver.current_url  # ! <- access raw WebDriver
    assert '/blog' in url, "niepoprawny url!"


@step('powinien zostać wyświetlony nagłówek "Posty"')
def posts_header_should_be_present(context):
    header = ("xpath", "//h1[@class='blog-list-title' and .='Posty']")
    assert_condition(
        context.actions,
        LocatorExists(header),
        message="Nie znaleziono nagłówka 'Posty'!"
    )


@step('posty powinny zostać wylistowane')
def posts_should_be_listed(context):
    actions: Actions = context.actions
    container = ("class name", "blog-list__container")
    assert_condition(
        context.actions,
        LocatorExists(container),
        message="Brak kontenera z postami!"
    )
    post_link = ("css selector", ".blog-post__link")
    posts = actions.finder.find_elements(post_link)
    assert len(posts) > 0, "Brak postów !"
