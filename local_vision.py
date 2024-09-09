import dashscope
import time
dashscope.api_key = 


def call_with_local_file(messages):
    messages = [{
        'role': 'system',
        'content': [{
            'text': '按用户对你提出的要求进行回答'
        }]
    }, {
        'role':
        'user',
        'content': messages
    }]
    response = dashscope.MultiModalConversation.call(model='qwen-vl-max-0809', messages=messages)
    print(response)



if __name__ == '__main__':
    now = time.time()
    local_path = "/Users/admin/Documents/vison_test/test_video/7.mp4"
    # local_path = '/Users/admin/Documents/vison_test/test_picture/test10.jpeg'
    video_ = [{"video": f"file://{local_path}"},
              {'text': '你是一名经验丰富的记者，对各类名人、新闻事件、名胜古迹十分熟悉。现在有一段视频，请利用你丰富的经验完成以下要求：1.如果视频里有人，提取可能涉及的名人；2.用简洁的句子概括视频中发生的事情；3.判断视频中的场景是否为著名地点，如果是给出地名。'},]

    image_ = [{"image": f"file://{local_path}"},
             {"text": "你是一名经验丰富的记者，对各类名人、新闻事件、名胜古迹十分熟悉。现在有一张图片，请利用你丰富的经验完成以下要求：1.如果照片里有人，提取可能涉及的名人；2.用简洁的句子概括照片中所描述的事物；3.判断照片中的场景是否为著名地点，如果是给出地名。"}]

    # call_with_local_file(image_)
    call_with_local_file(video_)

    print('time: ', time.time()-now)