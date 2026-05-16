from homeassistant.components.sensor import SensorEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.config_entries import ConfigEntry

from . import DOMAIN

async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    async_add_entities([HelloWorldSensor()])


class HelloWorldSensor(SensorEntity):

    _attr_name = "Hello World"
    _attr_unique_id = "hello_world_sensor"
    _attr_native_value = "Hello World"
    _attr_icon = "mdi:hand-wave"

    @property
    def suggested_display_precision(self) -> int | None:
        return None