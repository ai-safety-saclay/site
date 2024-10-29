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


def miniature_videos(builder: Doc):
    doc, tag, text = builder.tagtext()
    with tag('div', klass='container d-flex flex-wrap gap-2 my-5'):
        for id in ASIMOV_VIDEO_IDS:
            with tag('iframe', width='300', height='180', src=f'https://youtube.com/embed/{id}&origin={MAIN_SITE_URL}', loading='lazy'):
                pass

def navbar(builder: Doc):
    doc, tag, text = builder.tagtext()

    def item(title: str, url: str):
        with tag('li', klass='nav-item px-2 mx-2'):
            with tag('a', klass='nav-link rounded-3', href=url):
                text(title)

    with tag('nav', klass='navbar d-flex justify-content-start navbar-expand-lg bg-light shadow-sm', data_bs_theme='light'):
        with tag('a', klass='navbar-brand mx-5', href='/'):
            doc.stag('img', klass='piaf-icon icon-link icon-link-hover', src='./piaf_gray.svg', width='60em', height='40em')
            with tag('b', klass='piaf-icon-title'):
                text('Le PIAF')
        with tag('ul', klass='navbar-nav d-flex flex-row'):
            item('Présentation', '/presentation.html')
            item('Asimov', '/asimov.html')
            item('Blog', 'https://blog.piaf-saclay.org')
            item('Contact', '/contact.html')

def header(builder: Doc, page: str, title: str):
    doc, tag, text, line = builder.ttl()
    with tag('header', klass='site-header text-center'):
        navbar(builder)
        with tag('div', klass='container d-flex flex-column justify-content-center align-items-center'):
            # TODO: colored title
            # TODO: change font size: https://getbootstrap.com/docs/5.0/content/typography/#sass
            with tag('h1', klass='display-4 my-5'):
                line('b', title)

def md_section(builder: Doc, path_to_md: str):
    with open(path_to_md) as f:
        content = md.convert(f.read())
    
    # TODO: can I CSS or JS instead to apply class to every such tag?
    # Same for section py-5, btn, card...
    soup = bs4.BeautifulSoup(content, 'html.parser')
    for cls in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
        for h in soup.find_all(cls):
            h['class'] = ' display-5 my-4'
    content = str(soup)

    doc, tag, text, line = builder.ttl()
    with tag('section', klass='container'):
        with tag('div', klass='row justify-content-center'):
            with tag('div', klass='col-xxl-8 md-content'):
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
        doc.stag('link', rel='stylesheet', href='https://unpkg.com/bootstrap@5.3.3/dist/css/bootstrap.min.css')
        doc.stag('link', rel='stylesheet', href='https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css')
        # FIXME: /style.css
        doc.stag('link', rel='stylesheet', href='./style.css')
        # favicon
        doc.stag('link', rel='icon', type='image/svg', href='piaf.svg')



def footer(builder: Doc):
    doc, tag, text, line = builder.ttl()

    def item(name: str, link: str):
        with tag('li', klass='list-inline-item'):
            line('a', name, klass='nav-link p-2 mx-4 text-body-secondary rounded-3', href=link)
    
    def social_icon(class_name: str, link: str):
        with tag('a', klass='text-black me-5 icon-link icon-link-hover', href=link):
            with tag('i', klass=class_name):
                pass
    
    with tag('footer', klass='mt-5 text-center bg-body-tertiary'):
        with tag('section', klass='pt-3'):
            with tag('ul', 'list-inline'):
                # information asso
                item('Mention légales', '/mentions-legales.html')
                # RAS
                item('Confidentialité', '/confidentialite.html')
                item('Nous soutenir', '/nous-soutenir.html')
                item('Liste des pages', '/liste-pages.html')
        #doc.stag('hr', klass='my-4 border-dark-subtle')
        
        with tag('section', klass='py-2'):
            social_icon('bi bi-github h4', GITHUB_PAGE)
            social_icon('bi bi-youtube h4', YOUTUBE_CHANNEL)
            social_icon('bi bi-discord h4', DISCORD_SERVER)
                
        
        with tag('section', klass='mt-4'):
            with tag('div', klass='float-start mt-3'):
                with tag('a', klass='navbar-brand', href='/'):
                    doc.stag('img', klass='piaf-icon icon-link icon-link-hover', src='./piaf_gray.svg', width='60em', height='40em')
                    with tag('b', klass='piaf-icon-title'):
                        text('Le PIAF')
            # FIXME: le div flottant ne devrait pas décentrer celui-ci
            with tag('div', klass='text-center pt-4 pb-2 bg-body-secondary'):
                doc.asis('<p class="text-center text-body-secondary">&copy; 2024 <b>Pour une Intelligence Artificielle Fiable - PIAF</b></p>')

def card(builder: Doc, title: str, description: str, button_text: str, link: str):
    doc, tag, text, line = builder.ttl()
    with tag('div', klass='col-12 col-md-4'):
        with tag('div', klass='card bg-transparent shadow text-center h-100 rounded-3'):
            with tag('div', klass='card-body d-flex flex-column'):
                line('h2', title, klass='card-title mb-4')
                with tag('p', klass='card-text text-secondary'):
                    doc.asis(description)
                with tag('a', klass='btn btn-lg btn-block btn-primary mx-auto', href=link):
                    doc.asis(button_text)



def centered_heading(builder: Doc, title: str):
    doc, tag, text, line = builder.ttl()
    line('h2', title, klass='display-4 my-5 text-center') #text-primary

def generate_home():
    # TODO: gradient header with cool background effect

    def header(builder: Doc, title: str, subtitle: str):
        doc, tag, text, line = builder.ttl()
        with tag('header', klass='site-header text-center'):
            navbar(builder)
            with tag('div', klass='d-flex flex-column justify-content-center align-items-center piaf-banner'):
                # TODO: colored title
                doc.stag('img', klass='mt-5', src='piaf_gray_with_text.svg', width='500em')
                line('h1', title, klass='display-5 mt-3 mb-2')
                line('p', subtitle, klass='lead mb-3')

    def whoarewe(builder: Doc):
        doc, tag, text, line = builder.ttl()
        with tag('div', klass='container mb-5'):
            with tag('div', klass='col justify-content-md-center'):
                line('h3', 'Qui sommes-nous ?', klass='fs-6 mb-2 text-secondary text-center text-uppercase')
                with tag('h2', klass='display-5 mt-2 mb-5 text-center'):
                    # TODO: insert Markdown here
                    doc.asis('Nous sommes une association<br>d\'étudiants de ')
                    line('a', 'Paris-Saclay', href='https://fr.wikipedia.org/wiki/Paris-Saclay', klass='text-decoration-none link-primary')
                    doc.asis('<br>qui travaillent sur le sujet de<br>la ')
                    line('b', 'sûreté de l\'IA', klass='fw-bold')
                    text('.')
    
    # TODO: separate sections with borders or background
    def cards_about(builder: Doc):
        doc, tag, text = builder.tagtext()
        with tag('div', klass='container'):
            with tag('div', klass='row gy-4 gx-xxl-5'):
                card(
                    builder,
                    'Notre mission',
                    'Nous voulons sensibiliser les étudiants aux enjeux de la sûreté de l\'IA afin de démocratiser ce domaine dans les écoles d\'ingénieurs.',
                    'En savoir plus',
                    '/presentation.html',
                )
                card(
                    builder,
                    'Notre cycle de conférences',
                    'Nous organisons <b>Asimov</b>, un cycle de conférences dans les écoles du plateau de Saclay.',
                    'En savoir plus',
                    '/asimov.html',
                )
                card(
                    builder,
                    'Notre groupe de lecture',
                    'Assistez et participez à nos exposés sur la sûreté de l\'IA.',
                    'En savoir plus',
                    '/groupe-de-lecture.html',
                )
    
    def cards_social(builder: Doc):
        doc, tag, text = builder.tagtext()
        with tag('div', klass='container'):
            with tag('div', klass='row gy-4 gy-md-0 gx-xxl-5'):
                card(
                    builder,
                    'Discord',
                    'Rejoignez la communauté, discutez avec les membres de l\'association et tenez-vous au courant des activités du PIAF.',
                    '<i class="bi bi-discord me-2"></i> Rejoindre la discussion',
                    DISCORD_SERVER,
                )
                card(
                    builder,
                    'Github',
                    'Contribuez à notre projet sur la sécurité de l\'IA dans les écoles de Paris-Saclay.',
                    '<i class="bi bi-github me-2"></i> Notre organisation',
                    GITHUB_PAGE,
                )
                card(
                    builder,
                    'Nous contacter',
                    'Nous sommes ravis de collaborez avec vous et de répondre à vos questions.',
                    '<i class="bi bi-envelope-at me-2"></i> Contact',
                    '/contact.html',
                )

    def news(builder: Doc):
        doc, tag, text, line = builder.ttl()
        with tag('div', klass='container'):
            centered_heading(builder, 'À la une')
            # TODO: cards / carousel : Asimov #1
            # TODO: card content inside Markdown
            with tag('div', klass='row justify-content-center'):
                with tag('div', klass='card shadow'):
                    doc.stag('img', klass='card-img-top', src='https://teletalks.fr/static/affiches/asimov%201.png', alt='Affiche de la conférence Asimov n° 1')
                    with tag('div', klass='card-body'):
                        line('h5', 'Asimov n° 1 : (dés)information à l\'ère de l\'intelligence artificielle', klass='card-title text-center')
                        line('p', 'La première conférence du cycle Asimov avec Arthur Grimonpont a eu lieu le 14 octobre 2024 à Télécom Paris.', klass='card-text text-center')
                        line('a', 'Voir l\'événement', href='https://lu.ma/5mbym8x1', klass='btn btn-block btn-primary mx-auto')

    builder = yattag.Doc()
    doc, tag, text, line = builder.ttl()

    with tag('html', lang='fr'):
        head(builder, page='', title='Le PIAF')            
        with tag('body'):
            # TODO: subtitle='Pour une Intelligence Artificielle Fiable' ?
            header(builder, 'Le PIAF', 'Former les étudiants aux risques et aux défis de l\'IA')
            with tag('main', klass='site-main', role='main'):
                with tag('section', klass='py-5'):
                    whoarewe(builder)
                    cards_about(builder)
                with tag('section', klass='py-5'):
                    centered_heading(builder, 'Rejoindre la communauté')
                    cards_social(builder)

                with tag('section', klass='events py-5'):
                    news(builder)
            
        footer(builder)

    with open('build/index_test.html', 'w') as f:
        f.write(doc.getvalue())

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
                md_section(builder, 'presentation_piaf.md')
        footer(builder)

    with open(f'build/{PAGE}', 'w') as f:
        f.write(doc.getvalue())


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
                md_section(builder, 'presentation_asimov.md')
                miniature_videos(builder)
        footer(builder)

    with open(f'build/{PAGE}', 'w') as f:
        f.write(doc.getvalue())


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
                md_section(builder, 'contact.md')
        # FIXME: push footer down to bottom of the screen
        footer(builder)

    with open(f'build/{PAGE}', 'w') as f:
        f.write(doc.getvalue())

if __name__ == '__main__':
    # if 'build' folder does not exist, create it, copy content of 'static' folder to it
    # and generate html

    # if build folder exists, delete it
    if os.path.exists('./build'):
        shutil.rmtree('build')
    shutil.copytree('static', 'build')

    generate_presentation()
    generate_asimov()
    generate_home()
    generate_contact()
