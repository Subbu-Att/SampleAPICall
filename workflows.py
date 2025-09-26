# @@@SNIPSTART python-money-transfer-project-template-workflows
from datetime import timedelta

from temporalio import workflow
from temporalio.common import RetryPolicy
from temporalio.exceptions import ActivityError

with workflow.unsafe.imports_passed_through():
    from activities import ApiActivities
    


@workflow.defn
class OpenApiCall:
    @workflow.run
    async def run(self ) -> str:
        print("Workflow started")
        try:
            retry_policy = RetryPolicy(
                maximum_attempts=3,
                maximum_interval=timedelta(seconds=2),
                non_retryable_error_types=["InvalidAccountError", "InsufficientFundsError"],
            )
        # Withdraw money
            api_output = await workflow.execute_activity_method(
                ApiActivities.OpenApiCall,
                start_to_close_timeout=timedelta(seconds=5),
                retry_policy=retry_policy,
            ) 
            print("workflow api output:", api_output)
            return api_output
        
        except ActivityError as deposit_err:
            # Handle deposit error
            workflow.logger.error(f"call failed: {deposit_err}")

            # Re-raise deposit error if refund was successful
            raise deposit_err