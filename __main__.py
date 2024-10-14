import yattag
import markdown
import os
import shutil

md = markdown.Markdown()

asimov_video_ids = [
        "sPyu_dTSma0?si=RGOFL9CJ8enPYmSX&t=509",
        "d9tjp4-xJG4?si=uj-flIbCPtmV5pkS&t=2461",
        "FhFxlZzptys?si=I-j6X3vFHZIwuKIi&amp;start=1318",
        "SYgsji_o3EE?si=8oUxvcOA1kUoL22d&amp;start=104",
        "g_smhWSbXFw?si=S067OMLP8v1VC0yP&t=398",
        "ofs-9_yzcvY?si=SFXXa6DMYhM52VWR&t=449s",
        "LZWr5OZyBWE?si=m-pkGXnDR_4pio73&t=849",
        ]

def miniature_videos(builder):
    doc, tag, text = builder.tagtext()
    with tag("div", klass="d-flex flex-wrap gap-2"):
        for id in asimov_video_ids:
            with tag("iframe", width="330", height="180", klass="", src=f"https://youtube.com/embed/{id}&origin=https://piaf-saclay.org", loading="lazy"):
                pass


def home(builder):
    doc, tag, text = builder.tagtext()

    with open("home.md") as f:
        content = md.convert(f.read())

    with tag("section", klass="mx-4"):
        doc.stag("img", src="piaf_gray_with_text.svg", alt="le PIAF", width="500em")
        with tag("h1"):
            text("le PIAF")
        doc.asis(content)

def presentation_asimov(builder):
    doc, tag, text = builder.tagtext()
    with open("presentation_asimov.md") as f:
        content = md.convert(f.read())

    with tag("section", klass="mx-4"):
        with tag("h1"):
            text("Présentation Asimov")
        doc.asis(content)
    miniature_videos(builder)

def presentation_piaf(builder):
    doc, tag, text = builder.tagtext()
    with open("presentation_piaf.md") as f:
        content = md.convert(f.read())
    with tag("section", klass="mx-4"):
        with tag("h1"):
            text("Présentation PIAF")
        doc.asis(content)

def head(builder, title):
    doc, tag, text = builder.tagtext()
    with tag('head'):
        with tag("meta"):
            doc.stag('meta', charset="utf-8")
            doc.stag('meta', name="viewport", content="width=device-width, initial-scale=1.0")
            doc.stag('link', href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css", rel='stylesheet')

        with tag('title'):
            text(title)


def generate_home():
    builder = yattag.Doc()
    doc, tag, text = builder.tagtext()

    with tag('html'):
        head(builder, "le PIAF")

        with tag('body'):
            home(builder)

    with open("build/index.html", "w") as f:
        f.write(doc.getvalue())

def generate_presentation():
    builder = yattag.Doc()
    doc, tag, text = builder.tagtext()

    with tag('html'):
        head(builder, "à propos du PIAF")

        with tag('body'):
            presentation_piaf(builder)

    with open("build/presentation.html", "w") as f:
        f.write(doc.getvalue())


def generate_asimov():
    builder = yattag.Doc()
    doc, tag, text = builder.tagtext()

    with tag('html'):
        head(builder, "Asimov: les dangers du numérique")

        with tag('body'):
            presentation_asimov(builder)

    with open("build/asimov.html", "w") as f:
        f.write(doc.getvalue())

if __name__ == "__main__":
    # if "build" folder does not exist, create it, copy content of "static" folder to it
    # and generate html

    builder = yattag.Doc()
    doc, tag, text = builder.tagtext()


    shutil.rmtree("build")
    shutil.copytree("static", "build")

    generate_presentation()
    generate_asimov()
    generate_home()
