# Machine-Learning-Projects

# API

`copy(text: string, options: object): boolean` &mdash; tries to copy text to clipboard. Returns `true` if no additional keystrokes were required from user (so, `execCommand`, IE's `clipboardData` worked) or `false`.

|Value |Default |Notes|
|------|--------|-----|
|options.debug  |false| `Boolean`. Optional. Enable output to console. |
|options.message|Copy to clipboard: `#{key}`, Enter| `String`. Optional. Prompt message. `*` |
|options.format|"text/html"| `String`. Optional. Set the MIME type of what you want to copy as. Use `text/html` to copy as HTML, `text/plain` to avoid inherited styles showing when pasted into rich text editor. |
|options.onCopy|null| `function onCopy(clipboardData: object): void`. Optional. Receives the clipboardData element for adding custom behavior such as additional formats |

Installation
1.Clone this repository

https://github.com/DipeshDhandha07/Machine-Learning-Projects.git

2.Python

pip install opencv-python\
pip install pandas\
pip install numpy

3.Anaconda

conda install -c anaconda opencv\
conda install -c anaconda numpy\
conda install -c anaconda pandas
