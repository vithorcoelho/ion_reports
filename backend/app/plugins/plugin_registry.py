from app.plugins.base import ReportPlugin
from app.plugins.ionnutri_plugin import IonNutriPlugin
from app.plugins.prompts.ionnutri_prompts import IonNutriPrompts
from app.plugins.prompts.vidanova_prompts import VidaNovaPrompts
from app.plugins.vidanova_plugin import VidaNovaPlugin


def get_registered_plugins(llm_service) -> dict[str, ReportPlugin]:
    """Instancia e retorna todos os plugins disponíveis, já prontos para uso."""
    plugins: dict[str, ReportPlugin] = {}
    ionnutri_plugin = IonNutriPlugin(llm_service, IonNutriPrompts())
    plugins[ionnutri_plugin.get_plugin_name()] = ionnutri_plugin

    vidanova_plugin = VidaNovaPlugin(llm_service, VidaNovaPrompts())
    plugins[vidanova_plugin.get_plugin_name()] = vidanova_plugin

    return plugins
