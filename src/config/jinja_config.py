import os
from jinja2 import Environment, FileSystemLoader
from pydantic import PrivateAttr
from config.base import AppBaseSettings  # Use shared base

class JinjaSettings(AppBaseSettings):
    prompt_templates_folder: str = "prompts"

    _env: Environment = PrivateAttr()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
        templates_dir = os.path.abspath(os.path.join(root_dir, self.prompt_templates_folder))

        self._env = Environment(loader=FileSystemLoader(templates_dir))

    def render_template(self, template_name: str, **kwargs) -> str:
        return self._env.get_template(template_name).render(**kwargs)
