import os
import sass
from git import Repo
from urllib.request import urlretrieve
from jinja2 import Environment, FileSystemLoader
import yaml
import setuptools

dir_util = setuptools.distutils.dir_util
file_util = setuptools.distutils.file_util

MAIN_SITE_URL = "https://piaf-saclay.org"
YOUTUBE_CHANNEL = "https://www.youtube.com/@GROUPE-PIAF"
GITHUB_PAGE = "https://github.com/ai-safety-saclay"
DISCORD_SERVER = "https://discord.gg/pWRjGuP4nE"
WHATSAPP_GROUP = "https://chat.whatsapp.com/Jt5NdWFuUexFPFtyosDxGD"
LINKEDIN_PAGE = "https://www.linkedin.com/company/piaf-saclay"

KEYWORDS = "IA, intelligence artificielle, fiable, association, école, étudiant, ingénieur, Saclay, conférence, Asimov, recherche, numérique, dangers, sécurité, fiabilité, robustesse, sûreté, confiance, alignement, contrôle"
DESCRIPTION = "Le PIAF est une association qui réunit des étudiants du plateau de Saclay autour de l'intelligence artificielle fiable. Groupe de lecture, conférences, et bien d'autres projets."

GLOBALS = {
    "MAIN_SITE_URL": MAIN_SITE_URL,
    "YOUTUBE_CHANNEL": YOUTUBE_CHANNEL,
    "GITHUB_PAGE": GITHUB_PAGE,
    "DISCORD_SERVER": DISCORD_SERVER,
    "WHATSAPP_GROUP": WHATSAPP_GROUP,
    "LINKEDIN_PAGE": LINKEDIN_PAGE,
    "KEYWORDS": KEYWORDS,
    "DESCRIPTION": DESCRIPTION,
}

env = Environment(
    loader=FileSystemLoader(["pages", "components"]),
    extensions=["jinja_markdown.MarkdownExtension"],
)


def read_yml(path: str) -> dict:
    with open(path, "r") as f:
        return yaml.safe_load(f)


def write_html(path: str, template):
    with open(f"build/{path}", "w") as f:
        f.write(template.render())


def read_event_file(yml_file):
    # TODO: méthode plus robuste
    events = read_yml(yml_file)
    past = list(reversed([l for l in events if l["past"]]))
    future = [l for l in events if not l["past"]]
    return past, future


def generate_home(title):
    page = "index.html"
    globals = dict(GLOBALS, title=title, page=page)
    template = env.get_template("home.html", globals=globals)

    write_html("index.html", template)


def generate_page(title, template_path, **globals):
    page = template_path.split(".")[0] + ".html"

    globals = dict(GLOBALS, title=title, page=page, **globals)

    # Un fichier .md ne contient que son texte, md_page.html l'habille
    if template_path.endswith(".md"):
        globals["content"] = template_path
        template_path = "md_page.html"

    template = env.get_template(template_path, globals=globals)

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

    sass.compile(dirname=("scss", "build"))

    urlretrieve(
        "https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js",
        "./build/popper.min.js",
    )

    file_util.copy_file("./bootstrap/dist/js/bootstrap.min.js", "./build")
    dir_util.copy_tree("./bootstrap-icons/font/fonts", "./build/fonts")

    generate_home("PIAF")

    past_asimov, _ = read_event_file("asimov.yml")
    past_lectures, _ = read_event_file("lectures.yml")
    past_jeudia, _ = read_event_file("jeudia.yml")
    generate_page(
        "Événements passés",
        "evenements-passes.html",
        past_asimov=past_asimov,
        past_jeudia=past_jeudia,
        past_lectures=past_lectures,
    )

    generate_page("Piailleries", "piailleries.md")

    generate_page("Politique de confidentialité", "confidentialite.md")
    generate_page("Mentions légales", "mentions-legales.md")
    generate_page("Nous aider", "nous-aider.md")
    generate_page("À propos du PIAF", "presentation.md")
    generate_page("Contact", "contact.md")
