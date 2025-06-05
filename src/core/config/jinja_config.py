import os
from core.config.base import AppBaseSettings
from jinja2 import Environment, FileSystemLoader
from pydantic import PrivateAttr, Field

class JinjaSettings(AppBaseSettings):
    prompt_templates_folder: str = Field("src/core/prompt_templates", env="PROMPT_TEMPLATES_FOLDER")

    _env: Environment = PrivateAttr()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Dynamically resolve the root directory (2 levels up from this file: /src/config/)
        root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "../.."))
        
        # Normalize and join path to the templates
        templates_dir = os.path.normpath(os.path.join(root_dir, self.prompt_templates_folder))

        self._env = Environment(loader=FileSystemLoader(templates_dir))

    def render_template(self, template_name: str, **kwargs) -> str:
        return self._env.get_template(template_name).render(**kwargs)
