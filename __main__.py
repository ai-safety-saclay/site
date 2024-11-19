import os
import sass
from git import Repo
from jinja2 import Environment, FileSystemLoader
import yaml
from markdown import Markdown
from markupsafe import Markup
from mdx_math import MathExtension
import setuptools
dir_util = setuptools.distutils.dir_util


MAIN_SITE_URL = "https://piaf-saclay.org"
BLOG_URL = "https://blog.piaf-saclay.org"
YOUTUBE_CHANNEL = "https://www.youtube.com/@GROUPE-PIAF"
GITHUB_PAGE = "https://github.com/ai-safety-saclay"
DISCORD_SERVER = "https://discord.gg/pWRjGuP4nE"

KEYWORDS = "IA, intelligence artificielle, fiable, association, école, étudiant, ingénieur, Saclay, conférence, Asimov, hackathon, recherche, numérique, dangers, sécurité, fiabilité, robustesse, sûreté, confiance, alignement, contrôle"
DESCRIPTION = "Le PIAF est une association qui réunit des étudiants du plateau de Saclay autour de l'intelligence artificielle fiable. Groupe de lecture, conférences, hackathons, et bien d'autres projets."

GLOBALS = {
    "MAIN_SITE_URL": MAIN_SITE_URL,
    "BLOG_URL": BLOG_URL,
    "YOUTUBE_CHANNEL" : YOUTUBE_CHANNEL,
    "GITHUB_PAGE" : GITHUB_PAGE,
    "DISCORD_SERVER" : DISCORD_SERVER,
    "KEYWORDS": KEYWORDS,
    "DESCRIPTION": DESCRIPTION,
}

env = Environment(
    loader= FileSystemLoader(["pages", "components"]),
    extensions=["jinja_markdown.MarkdownExtension"]
)


def read_yml(path: str) -> dict:
    with open(path, "r") as f:
        return yaml.safe_load(f)

def write_html(path: str, template):
    with open(f"build/{path}", "w") as f:
        f.write(template.render())

def generate_home():
    page="index.html"
    title="PIAF"

    globals = dict(GLOBALS, page=page, title=title)
    template = env.get_template("home.html", globals=globals)

    write_html("index.html", template)


def generate_page(title, template_path, **globals):
    page = template_path.split(".")[0] + ".html"

    globals = dict(GLOBALS, title=title, page=page, **globals)

    template = env.get_template(template_path, globals=globals)

    write_html(page, template)


ASIMOV_VIDEO_IDS = [
    "d9tjp4-xJG4?start=2461", # Alexei Grinbaum
    "dp5Yga_WKng?start=337", # Asma Mhalla
    "c-MQPOoM6-E?start=2493", # Fabrice Epelboin
    "FhFxlZzptys?start=1318", # David Chavalarias
    "CoX5OZIbGl4?start=187", # Maxime Fournes
    "ofs-9_yzcvY?start=449", # Alain Damasio
    "LZWr5OZyBWE?start=849", # Raja Chatila
    "sPyu_dTSma0?start=509", # Caroline Jeanmaire
]

md_configs = {
    "mdx_wikilink_plus": {
        "url_whitespace": "%20",
    },
    "mdx_math": {
        "enable_dollar_delimiter": True
    }
}

md = Markdown(extensions=["mdx_math", "fenced_code", "tables", "full_yaml_metadata", "mdx_wikilink_plus", "markdown_gfm_admonition", "nl2br"], extension_configs=md_configs)

def generate_blog():
    for filename in os.listdir("blog"):
        if filename.endswith(".md"):
            with open("blog/"+filename, "r") as f:
                text_content = f.read()
                #content = Markup(md.convert(text_content))
                content = md.convert(text_content)

                title = md.Meta["title"]
                article_id = filename.split(".")[0]
                page = f"blog/{article_id}.html"

                arguments = dict(GLOBALS, title=title, page=page, content=content)

                template = env.get_template("blog_page.html", globals=arguments)
                write_html(page, template)




if __name__ == "__main__":
    # if "build" folder does not exist, create it, copy content of "static" folder to it
    # and generate html

    # if build folder exists, delete it
    if os.path.exists("./build"):
        dir_util.remove_tree("./build")

    if not os.path.exists("./bootstrap"):
        Repo.clone_from(
            "https://github.com/twbs/bootstrap",
            "bootstrap",
            multi_options=["--depth=1", "--branch=v5.3.3"],
        )
        Repo.clone_from(
            "https://github.com/twbs/icons",
            "bootstrap-icons",
            multi_options=["--depth=1", "--branch=v1.11.3"],
        )

    dir_util.copy_tree("./static", "./build")
    dir_util.copy_tree("blog/documents", "build/blog")

    sass.compile(dirname=("scss", "build"))

    dir_util.copy_tree("./bootstrap-icons/font/fonts", "./build/fonts")

    generate_home()
    generate_page("Asimov : les dangers du numérique", "asimov.html", video_ids=ASIMOV_VIDEO_IDS)
    
    lectures = read_yml("lectures.yml")
    past_lectures = reversed([l for l in lectures if l["past"]])
    future_lectures = [l for l in lectures if not l["past"]]
    generate_page("Notre groupe de lecture", "groupe-de-lecture.html", past_lectures=past_lectures, future_lectures=future_lectures)

    generate_page("Politique de confidentialité", "confidentialite.md")
    generate_page("Mentions légales", "mentions-legales.md")
    generate_page("Nous aider", "nous-aider.md")
    generate_page("À propos du PIAF", "presentation.md")
    generate_page("Hackathons", "hackathons.md")
    generate_page("Contact", "contact.md")

    generate_blog()