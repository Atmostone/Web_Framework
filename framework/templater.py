from jinja2 import Template


def render(template_name, **kwargs):
    """
    open required template file with Jinja
    :param template_name:
    :param kwargs:
    :return:
    """
    with open(template_name, encoding='utf-8') as f:
        template = Template(f.read())
    return template.render(**kwargs)
