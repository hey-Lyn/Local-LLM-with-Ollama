import ollama

if __name__ == '__main__':
    while True:
        content = str(input('>: '))
        response = ollama.chat(
            model = 'qwen:0.5b',
            messages=[{'role': 'user', 'content': content},
                      ],
        )
        print(response['message']['content'])
    
