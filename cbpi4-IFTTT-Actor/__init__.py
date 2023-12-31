# -*- coding: utf-8 -*-
# pylint: disable=invalid-name
"""cbpi4-IFTTT-Actor is a plugin for CraftBeerPi 4
"""
import requests
from cbpi.craftbeerpi import CraftBeerPi
from cbpi.api import *

_EVENT_NAME = "Event Name"
_IFTTT_KEY = "IFTTT Key"
_INDICATOR = "%s"


@parameters(
    [
        Property.Text(
            label=_IFTTT_KEY, configurable=True, description="Your IFTTT Key"
        ),
        Property.Text(
            label=_EVENT_NAME,
            configurable=True,
            description="Event Name with optional '%s' for 'on' or 'off'",
        ),
    ]
)
class IFTTTActor(CBPiActor):
    """IFTTTActor is a CraftBeerPi 4 Actor using IFTTT Maker Webhooks"""
    def __init__(
        self, cbpi: CraftBeerPi, _id, props
    ):  # pylint: disable=redefined-builtin
        super().__init__(cbpi, _id, props)
        self.name = [a.name for a in cbpi.actor.data if a.id == _id][0]
        self.power = None

    @action(
        "Set Power",
        parameters=[
            Property.Number(
                label="Power", configurable=True, description="Power Setting [0-100]"
            )
        ],
    )
    async def setpower(self, Power=100):
        """setpower is a CraftBeerPi action"""
        self.logger.debug("%s.setpower(Power=%d)", self.name, Power)
        Power = int(Power)
        if Power < 0:
            Power = 0
        elif Power > 100:
            Power = 100
        await self.on(Power)

    async def on_start(self):
        self.logger.debug("%s.on_start()", self.name)
        await self.off()

    async def on_stop(self):
        self.logger.debug("%s.on_stop()", self.name)
        await self.off()  # it is better to lose a batch than burn down a house

    async def on(self, power=0):
        self.logger.debug("%s.on(power=%d)", self.name, power)
        self.state = True
        self.power = power
        self.trigger()

    async def off(self):
        self.logger.debug("%s.off()", self.name)
        self.state = False
        self.power = 0
        self.trigger()

    def trigger(self):
        """trigger the IFTTT Maker Webhook"""
        event = self.props.get(_EVENT_NAME)
        partial = f"https://maker.ifttt.com/trigger/{event}".replace(
            _INDICATOR, "on" if self.power else "off"
        )
        url = partial + f"/with/key/{self.props.get(_IFTTT_KEY)}"
        power = {"power": self.power} if _INDICATOR in event else None
        res = requests.post(url, json=power, timeout=10)
        log = self.logger.info if res.ok else self.logger.warning
        log("%s.trigger(): POST %s status=%d", self.name, partial, res.status_code)


def setup(cbpi4):
    """register the plugin"""
    cbpi4.plugin.register("IFTTT-Actor", IFTTTActor)
