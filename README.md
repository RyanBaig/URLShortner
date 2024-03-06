# URL Shortener Project

This is a simple URL Shortener application created by Ryan using Python and the Tkinter library for the user interface. It uses the Cutt.ly API to shorten long URLs.

## Getting Started

To get started with this project, you can follow the instructions below.

### Prerequisites

- Python installed on your system.
- The `requests` library for making HTTP requests.
- The `tkinter` library for the user interface.
- The `ttkbootstrap` library for styling the user interface.

### Installing Dependencies

You can install the required Python libraries using `pip`:

```shell
pip -r install requirements.txt
```
### Running the Application

1. Clone this repository:
```bash
git clone https://github.com/RyanBaig/URLShortner.git
```

2. Open the folder in the terminal:
```bash
cd URLShortner
```

3. Run the Python script url_shortener.py:
```bash
python url_shortener.py
```

1. The GUI application will open, allowing you to enter a long URL and convert it into a short URL.

2. Click the "Convert into Short URL" button to retrieve the shortened URL.
   You can also copy the Shortened URL in the Text Box/Widget.

### How it Works

1. The application makes use of the Cutt.ly API to shorten URLs.

2. It requests an API key, which you should replace with your own API key.

3. Enter the long URL in the input field and click the button to trigger the URL shortening process.

4. The shortened URL will be displayed in the application's window.
   
### Dependencies

- [requests](https://pypi.org/project/requests/): A library for making HTTP requests in Python.
- [ttkbootstrap](https://pypi.org/project/ttkbootstrap/): A theme for tkinter applications.

### License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.