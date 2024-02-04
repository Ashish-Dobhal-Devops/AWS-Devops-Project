from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    # Updated HTML content with visual styling
    html_content = """
    <html>
    <head>
        <title>Ashish Dobhal's AWS DevOps Project</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                background-color: #f0f2f5;
            }
            .message {
                text-align: center;
                font-weight: bold; /* Making the text bold */
                color: #333;
            }
            .highlight {
                color: #2a9d8f;
                font-size: 24px; /* Larger font size for emphasis */
            }
        </style>
    </head>
    <body>
        <div class="message">
            <p>Welcome to Ashish Dobhal's AWS Devops Project!</p>
            <p>You have successfully created an AWS Devops project using Code Commit, Code Build, Code Deploy and Code Pipeline with full automation.</p>
            <p class="highlight">@@@Congratulations@@@</p>
        </div>
    </body>
    </html>
    """
    return html_content

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7777)  # Listen on all network interfaces and on port 7777
