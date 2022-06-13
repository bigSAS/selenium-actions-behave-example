
from seleniumactions import Using, Locator


class LinkByExactText(Locator):
    """
    Example:

    home_link = LinkByExactText('HOME')
    actions.click(home_link.get_by())
    """
    def __init__(self, text: str) -> None:
        super().__init__(Using.XPATH, "//a[.='{text}']")

# todo: from readme
