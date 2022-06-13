from behave import step
from seleniumactions import Actions, LocatorExists
from utils.assertions import assert_condition


@step('że blog zostanie odwiedzony używając domeny {url}')
def open_blog(context, url: str):
    actions: Actions = context.actions
    actions.goto(url)


@step('odwiedzający kliknie przycisk "Blog"')
def click_blog_button(context):
    actions: Actions = context.actions
    blog_button = ("xpath", "//a[.='Blog']")
    actions.click(blog_button, timeout="long")


@step('powinien zostać przekierowany do strony z blogiem')
def should_be_redirected_to_blog_posts(context):
    actions: Actions = context.actions
    wd = actions.webdriver  # ! RAW webdriver
    assert '/blog' in wd.current_url, "niepoprawny url!"


@step('powinien zostać wyświetlony nagłówek "Posty"')
def posts_header_should_be_present(context):
    header = ("xpath", "//h1[@class='blog-list-title' and .='Posty']")
    assert_condition(
        context.actions,
        LocatorExists(header),
        message="Nie znaleziono nagłówka 'Posty'!",
        timeout="absurd",
        explicit_timeout=3  # ! explicit allways overrides any timeout
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


@step('zostanie wybrany nagłówek posta {post_title}')
def goto_post(context, post_title: str):
    actions: Actions = context.actions
    post_tile = ("xpath", f"//a[.='{post_title}']")
    actions.click(post_tile)


@step('powinien zostać wyświetlony ekran z postem {post_title}')
def post_should_be_opened(context, post_title):
    post_header = ("xpath", f"//h1[@class='blog-title' and .='{post_title}']")
    assert_condition(
        context.actions,
        condition=LocatorExists(post_header),
        message="Nie wyświetlił się ekran z postem!"
    )
