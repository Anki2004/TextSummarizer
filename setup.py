import setuptools
with open("README.md",'r',encoding="utf-8") as fh:
    long_description = fh.read()


__version__ = "0.0.0"
REPO_NAME = "End-to-End-Text-Summarizer"
AUTHOR_NAME = "Anki2004"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "ankitsharma082004@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="end to end nlp project",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"http://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"http://github/{AUTHOR_NAME}/{REPO_NAME}/issues",

    },
    package_dir={"":"src"},
    packages= setuptools.find_packages(where="src"),
)