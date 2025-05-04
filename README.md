

 _               _      _   _ _   _ _     
| |             (_)    | | | | | (_) |    
| |__   __ _ ___ _  ___| | | | |_ _| |___ 
| '_ \ / _` / __| |/ __| | | | __| | / __|
| |_) | (_| \__ \ | (__| |_| | |_| | \__ \
|_.__/ \__,_|___/_|\___|\___/ \__|_|_|___/
                                          
                                          


# BasicUtils V.0.0.3

A collection of basic utility functions that can be used for various tasks. The `basicUtils.py` script provides several commands to make daily operations easier.

## REQUIRED

* Colorama is required for colouring the outputs
  ```bash
  pip install colorama
  ```

## Features

* Basic math operations
* Date and time utilities
* String manipulation functions
* Random number generation and hexadecimal conversion

## Installation

To use **basicUtils**, you can easily download the script from GitHub or use `curl` to fetch it directly. Here's how to set it up:

### Quick Install
```bash
python3 -m pip install --user --quiet colorama && curl -s https://raw.githubusercontent.com/wizardstream/basicUtils/master/basicUtils.py | sudo tee /usr/local/bin/basicUtils > /dev/null && sudo chmod +x /usr/local/bin/basicUtils
```


### 1. Download via GitHub

Clone the repository with Git and access the `basicUtils.py` file:

```bash
git clone https://github.com/wizardstream/basicUtils.git
cd basicUtils
```

### 2. Download via `curl`

Alternatively, you can download the script directly with `curl`. Run the following command to save the script:

```bash
curl -o basicUtils.py https://raw.githubusercontent.com/wizardstream/basicUtils/master/basicUtils.py
```

### 3. Make the Script Executable

To make the `basicUtils.py` script executable directly from your terminal without needing to type `python3` every time, follow these steps:

* Change the script’s permissions to make it executable:

  ```bash
  chmod +x basicUtils.py
  ```

* Move it to a directory that is already in your system's `PATH` (like `/usr/local/bin`), or leave it in its current directory. For simplicity, you can move it like this:

  ```bash
  sudo mv basicUtils.py /usr/local/bin/basicUtils
  ```

  Now, you can run the script directly from anywhere by simply typing:

  ```bash
  basicUtils
  ```
**Note:** The `.py` extension will be removed when you move the script to a directory in your `PATH`. This allows you to run the script directly by typing `basicUtils` (without the `.py` suffix) from anywhere in the terminal.

## Usage

Once the script is installed, you can run it from the terminal. Here's how to use some of the basic commands:

### Run the Script

Simply type the following command to execute the script:

```bash
basicUtils
```

Once the script is running, you can call different functions based on the available commands in the script.

### Example Functionality

Here are a few examples of what the script can do:

#### Math Operations:

```bash
$ basicUtils -calc add 5 10
# Output: 15

$ basicUtils -calc subtract 15 5
# Output: 10
```

#### Date and Time:

```bash
$ basicUtils -dateTime
# Output: Current date and time (formatted)
```

#### Random Hexadecimal:

```bash
$ basicUtils -random 4
# Output: A random hexadecimal value (e.g., 1a3f4b) 4 bytes big

```
### Other Commands

Use `--help` or `--h` for a list of commands and how to use them.
```bash
basicUtils --h
```
or
```bash
basicUtils --help
```

## License

This work is licensed under **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License**.

* You can use, share, and modify this script as long as it is for non-commercial purposes.
* If you redistribute or modify the script, you must do so under the same license.
* You must provide appropriate credit and give a link to the license.

See the full [license text here](https://creativecommons.org/licenses/by-nc-sa/4.0/).


