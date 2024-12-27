import aws_cdk as core
import aws_cdk.assertions as assertions

from aisearch_cdk.aisearch_cdk_stack import AisearchCdkStack

# example tests. To run these tests, uncomment this file along with the example
# resource in aisearch_cdk/aisearch_cdk_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AisearchCdkStack(app, "aisearch-cdk")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
