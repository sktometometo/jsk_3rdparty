import openai
import rospy

from openai_api_ros.srv import Completion
from openai_api_ros.srv import CompletionRequest
from openai_api_ros.srv import CompletionResponse


class OpenAIAPIInterface:

    def __init__(self, api_key: str = None):

        rospy.loginfo('api_key: {}'.format(api_key))
        openai.api_key = api_key
        self.srv = rospy.Service('~completion', Completion, self.handler)
        rospy.loginfo('Initialized')

    def complete(self, prompt: str):

        # For options, please see https://beta.openai.com/docs/api-reference/completions/create
        response = openai.Completion.create(
            prompt=prompt,
            model='text-davinci-003',
            max_tokens=1000,
            temperature=1.5,
        )

        rospy.logdebug('Get response: {} from prompt {}'.format(response, prompt))

        return response

    def handler(self, req: CompletionRequest) -> CompletionResponse:

        response = self.complete(req.prompt)
        return response['choices'][0]['text']
