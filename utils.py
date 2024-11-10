from yattag import Doc
import markdown
import yaml
md = markdown.Markdown(extensions=['bs4md', 'md_in_html'])

def read_md(path: str) -> str:
    """
    Read a Markdown file and convert it to HTML.
    """
    # TODO: add extension to parse HTML include directive (for buttons)
    with open(path, 'r') as f:
        return md.convert(f.read())

def read_html(path: str) -> str:
    with open(path, 'r') as f:
        return f.read()
    
def read_yml(path: str) -> dict:
    with open(path, 'r') as f:
        return yaml.safe_load(f)

def write_html(path: str, doc: Doc):
    with open(path, 'w') as f:
        f.write(doc.getvalue())



def md_section(builder: Doc, path_to_md: str):
    content = read_md(path_to_md)

    doc, tag, text, line = builder.ttl()
    with tag('section', klass='container'):
        with tag('div', klass='md-row'):
            with tag('div', klass='md-content'):
                doc.asis(content)


def centered_heading(builder: Doc, title: str):
    doc, tag, text, line = builder.ttl()
    line('h2', title, klass='centered-heading')