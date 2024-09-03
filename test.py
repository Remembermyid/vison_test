from openai import OpenAI
import os
import base64
import time
import multiprocessing


def get_response_online(image_url):
    client = OpenAI(
        # api_key=os.getenv("DASHSCOPE_API_KEY"),
        api_key= "",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )
    completion = client.chat.completions.create(
        model="qwen-vl-plus",
        messages=[
            {
              "role": "user",
              "content": [
                {
                  "type": "text",
                  "text": "你是一名经验丰富的记者，对各类名人、新闻事件、名胜古迹十分熟悉。现在有一张图片，请利用你丰富的经验完成以下要求：1.如果照片里有人，提取可能涉及的名人；2.用简洁的句子概括照片中所描述的事物；3.判断照片中的场景是否为著名地点，如果是给出地名。"
                },
                {
                  "type": "image_url",
                  "image_url": {
                    "url": image_url
                  }
                },
              ]
            }
          ]
        )
    print(completion.model_dump_json())



#  base 64 编码格式
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


def get_response(image_path):
    base64_image = encode_image(image_path)
    client = OpenAI(
        api_key= "sk-d4ec507cebcd42a28a5f719ebc5d70b7",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )
    completion = client.chat.completions.create(
        model="qwen-vl-plus",
        messages=[
            {
              "role": "user",
              "content": [
                {
                  "type": "text",
                  "text": "你是一名经验丰富的记者，对各类名人、新闻事件、名胜古迹十分熟悉。现在有一张图片，请利用你丰富的经验完成以下要求：1.如果照片里有人，提取可能涉及的名人；2.用简洁的句子概括照片中所描述的事物；3.判断照片中的场景是否为著名地点，如果是给出地名。"
                },
                {
                  "type": "image_url",
                  "image_url": {
                    "url": f"data:image/jpeg;base64,{base64_image}"
                  }
                }
              ]
            }
          ]
        )
    a = completion.model_dump_json()
    print(a)
    print(type(a))
    # a = eval(completion.model_dump_json())['choices'][0]["message"]["content"]
    # print(a)

if __name__=='__main__':
    now = time.time()
    picture_list = ["test1.jpeg",
                    "test2.jpeg",
                    "test3.jpeg",
                    "test4.png",
                    "test5.jpeg",]
    folder_dir = "E:\\GitLibrary\\vison_test-main\\test_picture\\"
    processes = []
    for i in range(5):  # 创建5个进程
        process = multiprocessing.Process(target=get_response, args=(folder_dir+picture_list[i],))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
    print(time.time()-now)
    # get_response(folder_dir + picture_list[1])