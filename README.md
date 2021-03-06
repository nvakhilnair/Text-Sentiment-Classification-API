
# Text Sentiment Classification

API classifies textual data into positive, negative, and neutral based on the polarity score.
The model uses the Vader model for the classification which is a lexicon-based model.

## Installation

Installation of required python libraries

```bash
  pip install -r requirement.txt
```

## Run Locally

1. To run this project run the following command in downloaded directory
```bash
  python manage.py runserver 127.0.0.1:9000
```


## Usage(Locally)

- Using curl
    ```bash
    curl -X POST 127.0.0.1:9000 -H "Content-Type: text/plain" -d "I am happy"
    ```
- Using Python
    ```bash
    import requests
    URL = "http://127.0.0.1:9000"
    data = "I am happy"
    r = requests.post(url = URL, data = data,headers={'Content-Type': 'text/plain'})
    ```

## Deployment(Cloud)
The application is deployed on the cloud using heroku.  
link : https://text-classfication-api.herokuapp.com/

```bash
    import requests
    URL = "https://text-classfication-api.herokuapp.com"
    data = "I am sad"
    r = requests.post(url = URL, data = data,headers={'Content-Type': 'text/plain'})
```
## Features

- No credentials required
- Responsive and Fast
- Can be used for text containing emoji
- Can be easily integrated with any model or application

## Demo
https://text-classfication-api.herokuapp.com/


## Tech Stack

**Client:** HTML, CSS

**Server:** Python, Django, Django Rest Framework




## License

[MIT](https://choosealicense.com/licenses/mit/)


## Feedback

If you have any feedback, please reach out to us at madewithpy009@gmail.com

For support, email madewithpy009@gmail.com.## š About Me
- š Hi, Iām @nvakhilnair
- š Iām interested in Data Science,Machine learning, Data Mining, Data Visualization and Programing
- š± Iām currently open to work
- š« How to reach me https://www.linkedin.com/in/akhilnvnair
## Authors

- [@nvakhilnair](https://github.com/nvakhilnair)
