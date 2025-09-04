"""A hermes harvest plugin that harvests your_source"""

from pydantic import BaseModel

from hermes.commands.harvest.base import HermesHarvestCommand, HermesHarvestPlugin


class YourHarvestSettings(BaseModel):  # TODO: Rename
    """
    Settings class for this plugin, inherits from pydantic.BaseModel.
    
    For using pydantic models, see https://docs.pydantic.dev/latest/concepts/models/.
    """

    your_parameter: str = "foobar"  # TODO: Remove or adapt


class YourHarvestPlugin(HermesHarvestPlugin):  # TODO: Rename
    """
    Base class for the hermes plugin that harvests <your_source>  # TODO: Replace placeholder
    """
    settings_class = YourHarvestSettings

    def __call__(self, command: HermesHarvestCommand):
        """
        Start of the process of harvesting <your_source>.
        
        This function is invoked when `hermes harvest` is run
        and this module is registered as a harvester.
        """

        data = {}  # FIXME: Replace with hermes.model.SoftwareMetadata()
        
        # TODO: Implement metadata harvesting here
        try:
            raise NotImplementedError("Metadata harvesting is not implemented.")
        except:
            pass

        # Return the harvested metadata and provenance information  # FIXME: Update on fix of https://github.com/softwarepub/hermes/issues/363
        return data, {}
