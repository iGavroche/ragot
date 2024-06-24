import os

os.environ["OLLAMA_HOST"] = "http://localhost:11434"
from embedchain import App

# load llm configuration from config.yaml file
app = App.from_config(config_path="ollama_config.yaml")


# add embedchain documentation as a source
app.add("https://docs.embedchain.ai/sitemap.xml", "sitemap")

# test query
app.query("Summarize the features of EmbedChain")
