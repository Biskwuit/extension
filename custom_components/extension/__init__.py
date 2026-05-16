from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.typing import ConfigType

DOMAIN = "extension"

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    hass.states.async_set("extension.hello", "world")
    return True