import time
from http import HTTPStatus
import dashscope


dashscope.api_key = "sk-d4ec507cebcd42a28a5f719ebc5d70b7"
def simple_multimodal_conversation_call():
    """Simple single round multimodal conversation call.
    """
    messages = [
        {
            "role": "user",
            "content": [
                # 以视频文件传入
                {"video": "https://github.com/Remembermyid/vison_test/raw/main/test_video/11.mp4"},
                # 或以图片列表形式传入
                # {"video":[
                #     "https://dashscope.oss-cn-beijing.aliyuncs.com/images/dog_and_girl.jpeg",
                #     "https://dashscope.oss-cn-beijing.aliyuncs.com/images/tiger.png"
                #     ]},
                {"text": "你是一名经验丰富的记者，对各类名人、新闻事件、名胜古迹十分熟悉。现在有一段视频，请利用你丰富的经验完成以下要求：1.如果视频里有人，提取可能涉及的名人；2.用简洁的句子概括视频中发生的事情；3.判断视频中的场景是否为著名地点，如果是给出地名。"}
            ]
        }
    ]
    response = dashscope.MultiModalConversation.call(
        model='qwen-vl-max-0809',
        messages=messages
    )
    if response.status_code == HTTPStatus.OK:
        print(response)
    else:
        print(response)
        print(response.code)  # The error code.
        print(response.message)  # The error message.


if __name__ == '__main__':
    now = time.time()
    simple_multimodal_conversation_call()
    print(time.time()-now)
#
# 返回结果
#
# {
#     "status_code": 200,
#     "request_id": "157fab7e-b9ed-912c-8a8b-72495fbc3938",
#     "code": "",
#     "message": "",
#     "output": {
#         "text": null,
#         "finish_reason": null,
#         "choices": [
#             {
#                 "finish_reason": "stop",
#                 "message": {
#                     "role": "assistant",
#                     "content": [
#                         {
#                             "text": "视频的内容是演示如何使用阿里云的模型体验平台。"
#                         }
#                     ]
#                 }
#             }
#         ]
#     },
#     "usage": {
#         "input_tokens": 3725,
#         "output_tokens": 14,
#         "video_tokens": 3700
#     }
# }