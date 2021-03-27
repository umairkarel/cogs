from enum import auto

from PyDrocsid.permission import BasePermission
from PyDrocsid.translations import t


class VoiceChannelPermission(BasePermission):
    @property
    def description(self) -> str:
        return t.voice_channel.permissions[self.name]

    private_owner = auto()
    dyn_read = auto()
    dyn_write = auto()
    link_read = auto()
    link_write = auto()
