import aws_cdk as core
import aws_cdk.assertions as assertions

from py_cdk_poc.py_cdk_poc_stack import PyCdkPocStack

# example tests. To run these tests, uncomment this file along with the example
# resource in py_cdk_poc/py_cdk_poc_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = PyCdkPocStack(app, "py-cdk-poc")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
