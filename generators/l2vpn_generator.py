from typing import Dict

from infrahub_sdk.generator import InfrahubGenerator

from utils import create_and_save, populate_local_store


class L2VPNServiceGenerator(InfrahubGenerator):
    """Generate L2VPN services."""

    async def generate(self, data: Dict) -> None:
        """Method to generate L2VPN Services in a fabric."""
        # try:
        #     # CoreAccount
        #     accounts = await self.client.all("CoreAccount")
        #     # Organizations
        #     tenants = await self.client.all("OrganizationTenant")
        #     # Topologies + Related informations
        #     topologies = await self.client.all(
        #         "TopologyTopology", populate_store=True, prefetch_relationships=True
        #     )
        #     # VRF
        #     vrfs = await self.client.all("InfraVRF")
        #     # TopologyNetworkService
        #     services = await self.client.all(
        #         "TopologyNetworkService", populate_store=True
        #     )

        # except Exception:
        #     exit(1)

        # service_id = 0
        # service_type = "Layer2"
        # vrf_name = "staging"

        print(data)
