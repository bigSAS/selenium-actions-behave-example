
from seleniumactions import Using, Locator


class LinkByText(Locator):
    def __init__(self, variant: str = "exact") -> None:
        template = "//a[.='{text}']" if variant == "exact" \
            else "//a[contains(.='{text}')]"
        super().__init__(Using.XPATH, template)


class HeaderByText(Locator):
    def __init__(self, variant: str = "exact") -> None:
        template = "//*[self::h1 or self::h2 or self::h3 and .='{text}']" if variant == "exact" \
            else "//*[self::h1 or self::h2 or self::h3 and contains(.='{text}')]"
        super().__init__(Using.XPATH, template)


class ElementByClassName(Locator):
    def __init__(self) -> None:
        super().__init__(Using.CLASS, "{class_name}")


class Locators:
    link_by_text = LinkByText()
    link_contains_text = LinkByText(variant="contains")
    header_by_text = HeaderByText()
    header_contains_text = HeaderByText(variant="contains")
    element_by_class_name = ElementByClassName()
