import yattag
from yattag import Doc
import markdown
import bs4
import os
import shutil

md = markdown.Markdown()

MAIN_SITE_URL = 'https://piaf-saclay.org'
BLOG_URL = 'https://blog.piaf-saclay.org'
YOUTUBE_CHANNEL = 'https://www.youtube.com/channel/UC3edW_hy2Ri_yilIiM3LTDA'
GITHUB_PAGE = 'https://github.com/ai-safety-saclay'
DISCORD_SERVER = 'https://discord.gg/zCyg7UWW2tZ'

KEYWORDS = 'IA, intelligence artificielle, fiable, association, école, étudiant, ingénieur, Saclay, conférence, Asimov, hackathon, recherche, numérique, dangers, sécurité, fiabilité, robustesse, sûreté, confiance, alignement, contrôle'
DESCRIPTION = 'Le PIAF est une association qui réunit des étudiants du plateau de Saclay autour de l\'intelligence artificielle fiable. Groupe de lecture, conférences, hackathons, et bien d\'autres projets.'

ASIMOV_VIDEO_IDS = [
    'sPyu_dTSma0?si=RGOFL9CJ8enPYmSX&t=509',
    'd9tjp4-xJG4?si=uj-flIbCPtmV5pkS&t=2461',
    'FhFxlZzptys?si=I-j6X3vFHZIwuKIi&amp;start=1318',
    'SYgsji_o3EE?si=8oUxvcOA1kUoL22d&amp;start=104',
    'g_smhWSbXFw?si=S067OMLP8v1VC0yP&t=398',
    'ofs-9_yzcvY?si=SFXXa6DMYhM52VWR&t=449s',
    'LZWr5OZyBWE?si=m-pkGXnDR_4pio73&t=849',
]

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

def write_html(path: str, doc: Doc):
    with open(path, 'w') as f:
        f.write(doc.getvalue())

def miniature_videos(builder: Doc):
    doc, tag, text = builder.tagtext()
    with tag('div', klass='video-container'):
        for id in ASIMOV_VIDEO_IDS:
            with tag('iframe', width='300', height='180', src=f'https://youtube.com/embed/{id}&origin={MAIN_SITE_URL}', loading='lazy'):
                pass

def navbar(builder: Doc):
    doc, tag, text = builder.tagtext()

    def item(title: str, url: str):
        with tag('li', klass='nav-item'):
            with tag('a', klass='nav-link', href=url):
                text(title)

    with tag('nav', klass='navbar', data_bs_theme='light'):
        with tag('a', klass='navbar-brand', href='/'):
            doc.stag('img', klass='piaf-icon', src='./piaf_gray.svg', width='60em', height='40em')
            with tag('b', klass='piaf-icon-title'):
                text('PIAF')
        with tag('ul', klass='navbar-nav'):
            item('Présentation', '/presentation.html')
            item('Asimov', '/asimov.html')
            item('Groupe de lecture', '/groupe-de-lecture.html')
            item('Blog', 'https://blog.piaf-saclay.org')
            item('Contact', '/contact.html')

def header(builder: Doc, page: str, title: str):
    doc, tag, text, line = builder.ttl()
    with tag('header', klass='site-header'):
        navbar(builder)
        with tag('div', klass='container'):
            with tag('h1', klass='page-title'):
                line('b', title)

def md_section(builder: Doc, path_to_md: str):
    content = read_md(path_to_md)

    doc, tag, text, line = builder.ttl()
    with tag('section', klass='container'):
        with tag('div', klass='md-row'):
            with tag('div', klass='md-content'):
                doc.asis(content)


def head(
    builder: Doc,
    page: str,
    title: str,
    keywords: str = KEYWORDS,
    description: str = DESCRIPTION,
):
    url = f'{MAIN_SITE_URL}/{page}'

    doc, tag, text = builder.tagtext()
    with tag('head'):
        with tag('title'):
            text(title)
        doc.stag('meta', charset='utf-8')
        doc.stag('meta', name='viewport', content='width=device-width, initial-scale=1.0')
        doc.stag('meta', name='title', property='og:title', content=title)
        doc.stag('meta', name='keywords', content=keywords)
        doc.stag('meta', name='description', content=description)
        doc.stag('meta', property='og:title', content=title)
        doc.stag('meta', property='og:url', content=url)
        doc.stag('meta', property='og:image', content=f'{MAIN_SITE_URL}/static/piaf_gray.png')
        doc.stag('meta', property='og:description', content=description)
        doc.stag('meta', property='og:type', content='website')
        # TODO: robots
        doc.stag('link', rel='canonical', href=url)
        # FIXME: /style.css
        doc.stag('link', rel='stylesheet', href='./style.css')
        # favicon
        doc.stag('link', rel='icon', type='image/svg', href='piaf.svg')



def footer(builder: Doc):
    doc, tag, text, line = builder.ttl()

    def item(name: str, link: str):
        with tag('li', klass='list-inline-item'):
            line('a', name, klass='nav-link', href=link)
    
    def social_icon(class_name: str, link: str):
        with tag('a', klass='icon-link', href=link):
            with tag('i', klass=class_name):
                pass
    
    with tag('footer'):
        with tag('div', klass='footer-nav'):
            with tag('ul', 'list-inline'):
                # TODO: information asso
                item('Mention légales', '/mentions-legales.html')
                # TODO: RAS
                item('Confidentialité', '/confidentialite.html')
                # TODO:
                item('Nous soutenir', '/nous-soutenir.html')
                # TODO:
                item('Liste des pages', '/liste-pages.html')
        #doc.stag('hr', klass='my-4 border-dark-subtle')
        
        with tag('div', klass='footer-social'):
            social_icon('bi bi-github h4', GITHUB_PAGE)
            social_icon('bi bi-youtube h4', YOUTUBE_CHANNEL)
            social_icon('bi bi-discord h4', DISCORD_SERVER)
        
        
        with tag('div', klass='footer-org'):
            with tag('div', klass='footer-piaf'):
                with tag('a', klass='navbar-brand', href='/'):
                    doc.stag('img', klass='piaf-icon', src='./piaf_gray.svg', width='60em', height='40em')
                    with tag('b', klass='piaf-icon-title'):
                        text('PIAF')
            with tag('div', klass='footer-copyright'):
                content = read_md('./home/copyright.md')
                doc.asis(content)

def card(builder: Doc, md_body_path: str, html_btn_path: str):
    body_content = read_md(md_body_path)
    btn_content = read_html(html_btn_path)
    
    doc, tag, text, line = builder.ttl()
    with tag('div', klass='col'): #klass='col-12 col-md-4'
        with tag('div', klass='card'):
            with tag('div', klass='card-body'):
                doc.asis(body_content)
                doc.asis(btn_content)



def centered_heading(builder: Doc, title: str):
    doc, tag, text, line = builder.ttl()
    line('h2', title, klass='centered-heading')

def generate_home():

    def header(builder: Doc, title: str, subtitle: str):
        doc, tag, text, line = builder.ttl()
        with tag('header', klass='site-header'):
            navbar(builder)
            with tag('div', klass='piaf-banner'):
                doc.stag('img', klass='piaf-logo-large', src='piaf_gray_with_text.svg', width='500em')
                line('h1', title, klass='page-title')
                line('p', subtitle, klass='motto')

    def whoarewe(builder: Doc):
        doc, tag, text, line = builder.ttl()
        with tag('div', klass='whoarewe'):
            with tag('div', klass='col'):
                line('h3', 'Qui sommes-nous ?', klass='smallcaps-heading')
                with tag('h2', klass='about-phrase'):
                    content = read_md('./home/about-phrase.md')
                    doc.asis(content)
    
    def cards_about(builder: Doc):
        doc, tag, text = builder.tagtext()
        with tag('div', klass='card-container'):
            with tag('div', klass='row'):
                card(builder, './home/cards/mission.md','./home/cards/mission-btn.html')
                card(builder, './home/cards/asimov.md', './home/cards/asimov-btn.html')
                card(builder, './home/cards/groupe-de-lecture.md', './home/cards/groupe-de-lecture-btn.html')
    
    def cards_social(builder: Doc):
        doc, tag, text = builder.tagtext()
        with tag('div', klass='card-container'):
            with tag('div', klass='row'):
                card(builder, './home/cards/discord.md', './home/cards/discord-btn.html')
                card(builder, './home/cards/github.md', './home/cards/github-btn.html')
                card(builder, './home/cards/contact.md', './home/cards/contact-btn.html')

    def news(builder: Doc):
        doc, tag, text, line = builder.ttl()

        def card(title: str, text: str, link: str, img_url: str):
            with tag('div', klass='card'):
                doc.stag('img', klass='card-img-top', src=img_url, alt=title, loading='lazy')
                with tag('div', klass='card-body'):
                    line('h5', title, klass='card-title')
                    line('p', text, klass='card-text')
                    line('a', 'Consulter', href=link, klass='btn')
        
        with tag('div', klass='container'):
            centered_heading(builder, 'À la une')
            # TODO: cards / carousel : Asimov #1
            # TODO: fetch RSS from https://blog.piaf-saclay.org/index.xml
            with tag('div', klass='row justify-content-center'):
                card(
                    title='Conférence Asimov n° 1 : (dés)information à l\'ère de l\'intelligence artificielle',
                    text='La première conférence du cycle Asimov avec Arthur Grimonpont a eu lieu le 14 octobre 2024 à Télécom Paris.',
                    link='https://lu.ma/5mbym8x1',
                    img_url='https://teletalks.fr/static/affiches/asimov%201.png',
                )

    builder = yattag.Doc()
    doc, tag, text, line = builder.ttl()

    with tag('html', lang='fr'):
        head(builder, page='', title='PIAF')            
        with tag('body'):
            # TODO: subtitle='Pour une Intelligence Artificielle Fiable' ?
            header(builder, 'PIAF', 'Former les étudiants aux risques et aux défis de l\'IA')
            with tag('main', klass='site-main', role='main'):
                with tag('section'):
                    whoarewe(builder)
                    cards_about(builder)
                with tag('section'):
                    centered_heading(builder, 'Rejoindre la communauté')
                    cards_social(builder)

                with tag('section', klass='events'):
                    news(builder)
            
        footer(builder)

    write_html('./build/index.html', doc)


def generate_presentation():
    TITLE = 'À propos du PIAF'
    PAGE = 'presentation.html'
    builder = yattag.Doc()
    doc, tag, text = builder.tagtext()

    with tag('html', lang='fr'):
        head(builder, page=PAGE, title=TITLE)
        with tag('body'):
            header(builder, page=PAGE, title=TITLE)
            with tag('main', klass='site-main', role='main'):
                md_section(builder, './presentation_piaf.md')
        footer(builder)

    write_html(f'build/{PAGE}', doc)


def generate_asimov():
    TITLE = 'Asimov : les dangers du numérique'
    PAGE = 'asimov.html'
    builder = yattag.Doc()
    doc, tag, text = builder.tagtext()

    with tag('html'):
        head(builder, page=PAGE, title=TITLE)
        with tag('body'):
            header(builder, page=PAGE, title=TITLE)
            with tag('main', klass='site-main', role='main'):
                md_section(builder, './presentation_asimov.md')
                miniature_videos(builder)
        footer(builder)

    write_html(f'build/{PAGE}', doc)

def generate_groupe_lecture():
    TITLE = 'Notre groupe de lecture'
    PAGE = 'groupe-de-lecture.html'
    builder = yattag.Doc()
    doc, tag, text = builder.tagtext()

    with tag('html'):
        head(builder, page=PAGE, title=TITLE)
        with tag('body'):
            header(builder, page=PAGE, title=TITLE)
            with tag('main', klass='site-main', role='main'):
                md_section(builder, './groupe_de_lecture.md')
                miniature_videos(builder)
        footer(builder)

    write_html(f'build/{PAGE}', doc)

def generate_contact():
    TITLE = 'Contact'
    PAGE = 'contact.html'
    builder = yattag.Doc()
    doc, tag, text = builder.tagtext()

    with tag('html'):
        head(builder, page=PAGE, title=TITLE)

        with tag('body'):
            header(builder, page=PAGE, title=TITLE)
            with tag('main', klass='site-main', role='main'):
                md_section(builder, './contact.md')
        footer(builder)

    write_html(f'build/{PAGE}', doc)

if __name__ == '__main__':
    # if 'build' folder does not exist, create it, copy content of 'static' folder to it
    # and generate html

    # if build folder exists, delete it
    if os.path.exists('./build'):
        shutil.rmtree('./build')
    shutil.copytree('./static', './build')

    shutil.copytree('./node_modules/bootstrap-icons/font/fonts', './build/fonts')

    generate_presentation()
    generate_asimov()
    generate_home()
    generate_groupe_lecture()
    generate_contact()
