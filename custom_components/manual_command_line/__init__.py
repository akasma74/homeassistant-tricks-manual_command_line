DOMAIN = "manual_command_line"

import homeassistant.components.command_line.sensor as sensor

@property
def should_poll(self) -> bool:
    return False

sensor.CommandSensor.should_poll = should_poll

async def async_setup(hass, config):
    return True
