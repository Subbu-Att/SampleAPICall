# @@@SNIPSTART python-money-transfer-project-template-withdraw
import asyncio
#Test Push
from temporalio import activity
from api_service import ApiService

class ApiActivities:
    def __init__(self):
        self.api = ApiService("bank-api.example.com")

    @activity.defn
    async def OpenApiCall(self) -> str:
        try:
            confirmation = await asyncio.to_thread(
                self.api.call,
            )
            return confirmation
        except Exception:
            activity.logger.exception("Withdrawal failed")
            raise

