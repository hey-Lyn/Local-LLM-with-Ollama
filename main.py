# This is just a simple code that will grow into something bigger. 
# Updates and documentation in progress.

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
    
