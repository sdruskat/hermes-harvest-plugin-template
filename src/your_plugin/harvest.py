"""A hermes harvest plugin that harvests your_source"""

from os import chdir, getcwd

from pydantic import BaseModel
# from hermes.model import SoftwareMetadata
from hermes.commands.harvest.base import HermesHarvestCommand, HermesHarvestPlugin


class YourHarvestSettings(BaseModel):
    """
    Settings class for this plugin
    """

    your_parameter = ''


class YourHarvestPlugin(HermesHarvestPlugin):
    """
    Base class for the hermes plugin that harvests your_source
    """

    def __call__(self, command: HermesHarvestCommand):
        """
        start of the process of harvesting your_source
        invoked when hermes harvest is run and this module is registered as a harvester
        """

        # set the working directory temporary to the correct location
        old_dir = getcwd()
        chdir(command.args.path)

        data = {} # SoftwareMetadata()
        # harvest data and store it in data

        chdir(old_dir)

        # returning the harvested data and metadata
        return data, {}
