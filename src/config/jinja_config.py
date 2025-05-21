import os
from jinja2 import Environment, FileSystemLoader
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from pydantic import PrivateAttr

load_dotenv()

class JinjaSettings(BaseSettings):
   """
   Configuration for Jinja2 template rendering.
   """
   prompt_templates_folder: str = os.getenv('PROMPT_TEMPLATES_FOLDER', 'prompts')

   # Declare env as a private attribute
   _env: Environment = PrivateAttr()

   def __init__(self, **kwargs):
      super().__init__(**kwargs)
      
      # Automatically resolve the root directory of the project
      root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
      
      # Combine with your templates folder
      templates_dir = os.path.join(root_dir, self.prompt_templates_folder)
      
      # Normalize to absolute path
      templates_dir = os.path.abspath(templates_dir)
      
      # Set up Jinja2 environment
      self._env = Environment(loader=FileSystemLoader(templates_dir))
   
   def render_template(self, template_name: str, **kwargs) -> str:
      """
      Render a Jinja2 template with given parameters.
      """
      template = self._env.get_template(template_name)
      return template.render(**kwargs)
