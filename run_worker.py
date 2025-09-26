import asyncio

from temporalio.client import Client
from temporalio.worker import Worker

from activities import ApiActivities
from workflows import OpenApiCall


async def main() -> None:
    print("Worker starting...")
    client: Client = await Client.connect("localhost:7233", namespace="default")
    activities=ApiActivities()
    worker: Worker = Worker(
        client,
        task_queue="OPENAPI_TASK_QUEUE",
        workflows=[OpenApiCall],
        activities=[activities.OpenApiCall],
    )
    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
# @@@SNIPEND
