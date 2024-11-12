import yattag
from yattag import Doc
import os
import shutil
import sass
from git import Repo
#from utils import *
from utils import *


MAIN_SITE_URL = 'https://piaf-saclay.org'
BLOG_URL = 'https://blog.piaf-saclay.org'
YOUTUBE_CHANNEL = 'https://www.youtube.com/channel/UC3edW_hy2Ri_yilIiM3LTDA'
GITHUB_PAGE = 'https://github.com/ai-safety-saclay'
DISCORD_SERVER = 'https://discord.gg/pWRjGuP4nE'

KEYWORDS = 'IA, intelligence artificielle, fiable, association, école, étudiant, ingénieur, Saclay, conférence, Asimov, hackathon, recherche, numérique, dangers, sécurité, fiabilité, robustesse, sûreté, confiance, alignement, contrôle'
DESCRIPTION = 'Le PIAF est une association qui réunit des étudiants du plateau de Saclay autour de l\'intelligence artificielle fiable. Groupe de lecture, conférences, hackathons, et bien d\'autres projets.'


# ON EVERY PAGE

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
            # TODO: dropdown 'Projets'
            item('Asimov', '/asimov.html')
            item('Groupe de lecture', '/groupe-de-lecture.html')
            item('Hackathons', '/hackathons.html')
            item('Blog', 'https://blog.piaf-saclay.org')
            item('Nous rejoindre', '/contact.html#nous-rejoindre')
            item('Contact', '/contact.html')


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
        doc.stag('link', rel='canonical', href=url)
        doc.stag('link', rel='stylesheet', href='/style.css')
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
                item('Mention légales', '/mentions-legales.html')
                item('Confidentialité', '/confidentialite.html')
                item('Nous aider', '/nous-aider.html')
                # TODO:
                #item('Liste des pages', '/liste-pages.html')

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
        with tag('div', klass='custom-card'):
            with tag('div', klass='card-body'):
                doc.asis(body_content)
                doc.asis(btn_content)




def header(builder: Doc, page: str, title: str):
    doc, tag, text, line = builder.ttl()
    with tag('header', klass='site-header'):
        navbar(builder)
        with tag('div', klass='container'):
            with tag('h1', klass='page-title'):
                line('b', title)





# PAGE GENERATION

def generate_home():

    def letters(builder: Doc):
        doc, tag, text = builder.tagtext()
        with tag('div', klass='d-flex justify-content-center'):
            with tag('div', klass='custom-word-container'):
                for word in ['Pour une', 'Intelligence', 'Artificielle', 'Fiable']:
                    letter = word[0]
                    remaining = word[1:]
                    line('span', letter, klass='custom-letter')
                    line('span', remaining, klass='custom-word-reveal')


    def header(builder: Doc):
        doc, tag, text, line = builder.ttl()
        with tag('header', klass='site-header'):
            navbar(builder)
            with tag('div', klass='piaf-banner'):
                doc.stag('img', klass='piaf-logo-large', src='piaf_gray_with_text.svg', width='500em')
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
            with tag('div', klass='custom-card'):
                doc.stag('img', klass='card-img-top', src=img_url, alt=title, loading='lazy')
                with tag('div', klass='card-body'):
                    line('h5', title, klass='card-title')
                    line('p', text, klass='card-text')
                    line('a', 'Consulter', href=link, klass='btn')

        with tag('div', klass='container'):
            centered_heading(builder, 'À la une')
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
            header(builder)
            with tag('main', klass='site-main', role='main'):
                letters(builder)
                with tag('section'):
                    content = read_md('./home/about-phrase.md')
                    doc.asis(content)
                    cards_about(builder)
                with tag('section'):
                    centered_heading(builder, 'Rejoindre la communauté')
                    cards_social(builder)

                with tag('section', klass='events'):
                    news(builder)

        footer(builder)

    write_html('./build/index.html', builder)


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

    write_html(f'build/{PAGE}', builder)


ASIMOV_VIDEO_IDS = [
    'd9tjp4-xJG4?start=2461', # Alexei Grinbaum
    'dp5Yga_WKng?start=337', # Asma Mhalla
    'c-MQPOoM6-E?start=2493', # Fabrice Epelboin
    'FhFxlZzptys?start=1318', # David Chavalarias
    'CoX5OZIbGl4?start=187', # Maxime Fournes
    'ofs-9_yzcvY?start=449', # Alain Damasio
    'LZWr5OZyBWE?start=849', # Raja Chatila
    'sPyu_dTSma0?start=509', # Caroline Jeanmaire
]


def miniature_videos(builder: Doc):
    doc, tag, text = builder.tagtext()
    with tag('div', klass='video-container'):
        for id in ASIMOV_VIDEO_IDS:
            src = f'https://www.youtube-nocookie.com/embed/{id}&origin={MAIN_SITE_URL}'
            with tag('iframe', width='300', height='180', src=src, loading='lazy'):
                pass

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

    write_html(f'build/{PAGE}', builder)


def generate_lecture(lecture, builder):
    doc, tag, text = builder.tagtext()
    with tag("div", klass="card my-2 p-3"):
        with tag('p', klass='text-muted small'):
            text(lecture["date"])
        
        with tag('h2', klass='card-title fs-3'):
            text(lecture["title"])
            
        with tag('h3', klass='card-subtitle mb-2 text-muted fs-5'):
            text(lecture["subtitle"])
            
        with tag('p', klass='card-text'):
            text('Papier: ')
            with tag('a', href=lecture["paper_link"], klass='fs-6'):
                text(lecture["paper_title"])
            if "blog_link" in lecture:
                doc.stag("br")
                text('Article récapitulatif: ')
                url = lecture["blog_link"]
                with tag('a', href=f"https://blog.piaf-saclay.org/{url}", klass='fs-6'):
                    text("ici")


def generate_groupe_lecture():
    PAGE='groupe-de-lecture.html'
    TITLE='Notre groupe de lecture'
    builder = yattag.Doc()
    doc, tag, text = builder.tagtext()

    lectures = read_yml('lectures.yml')
    
    with tag('html'):
        head(builder, page=PAGE, title=TITLE)
        with tag('body'):
            header(builder, page=PAGE, title=TITLE)
            with tag('main', klass='site-main', role='main'):
                md_section(builder, './groupe_de_lecture.md')
                with tag("section", klass="container"):
                    with tag("h2", klass="display-6 text-center"):
                        text("Nos exposés passés")
                    for l in lectures:
                        generate_lecture(l, builder)
    footer(builder)
        
    write_html(f'build/{PAGE}', builder)
    
    

def generate_md_page(page: str, title: str, md_path: str):
    """
    Generate a simple Markdown page.
    """
    builder = yattag.Doc()
    doc, tag, text = builder.tagtext()

    with tag('html'):
        head(builder, page=page, title=title)
        with tag('body'):
            header(builder, page=page, title=title)
            with tag('main', klass='site-main', role='main'):
                md_section(builder, md_path)
        footer(builder)

    write_html(f'build/{page}', builder)


if __name__ == '__main__':
    # if 'build' folder does not exist, create it, copy content of 'static' folder to it
    # and generate html

    # if build folder exists, delete it
    if os.path.exists('./build'):
        shutil.rmtree('./build')

    if not os.path.exists('./bootstrap'):
        Repo.clone_from(
            'https://github.com/twbs/bootstrap',
            'bootstrap',
            multi_options=['--depth=1', '--branch=v5.3.3'],
        )
        Repo.clone_from(
            'https://github.com/twbs/icons',
            'bootstrap-icons',
            multi_options=['--depth=1', '--branch=v1.11.3'],
        )

    shutil.copytree('./static', './build')
    sass.compile(dirname=('scss', 'build'))

    shutil.copytree('./bootstrap-icons/font/fonts', './build/fonts')

    generate_presentation()
    generate_asimov()
    generate_home()
    generate_groupe_lecture()
    generate_md_page(
        page='hackathons.html',
        title='Hackathons',
        md_path='./hackathons.md',
    )
    generate_md_page(
        page='contact.html',
        title='Contact',
        md_path='./contact.md',
    )
    generate_md_page(
        page='mentions-legales.html',
        title='Mentions légales',
        md_path='./mentions_legales.md',
    )
    generate_md_page(
        page='confidentialite.html',
        title='Politique de confidentialité',
        md_path='./confidentialite.md',
    )
    generate_md_page(
        page='nous-aider.html',
        title='Nous aider',
        md_path='./nous_aider.md',
    )
