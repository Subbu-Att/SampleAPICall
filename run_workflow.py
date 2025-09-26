# @@@SNIPSTART python-project-template-run-workflow
import asyncio
import traceback

from temporalio.client import Client, WorkflowFailureError

from workflows import OpenApiCall


async def main() -> None:
    # Create client connected to server at the given address
    client: Client = await Client.connect("localhost:7233")
    print("Client connected")
    try:
        result1 = await client.execute_workflow(
            OpenApiCall.run,          
            id="OpenAPiCall-001",
            task_queue="OPENAPI_TASK_QUEUE",
        )
        print("Workflow started")

        print(f"Transaction Result: {result1}")

    except WorkflowFailureError:
        print("Got expected exception: ", traceback.format_exc())

if __name__ == "__main__":
    asyncio.run(main())
# @@@SNIPEND