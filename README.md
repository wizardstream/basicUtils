
# BasicUtils

A collection of basic utility functions that can be used for various tasks. The `basicUtils` script provides several commands to make daily operations easier.

## Features

* Basic math operations
* Date and time utilities
* String manipulation functions
* Random number generation and hexadecimal conversion

## Installation

To use **basicUtils**, you can easily download the script from GitHub or use `curl` to fetch it directly. Here's how to set it up:

### 1. Download via GitHub

You can clone the repository with Git and access the `basicUtils.py` file:

```bash
git clone https://github.com/yourusername/basicUtils.git
cd basicUtils
```

### 2. Download via `curl`

Alternatively, you can download the script directly with `curl`. Run the following command to save the script:

```bash
curl -o basicUtils.py https://raw.githubusercontent.com/yourusername/basicUtils/master/basicUtils.py
```

### 3. Make the Script Executable (Optional)

If you want to execute the script directly from your terminal without typing `.py`:

* Add the directory containing `basicUtils.py` to your PATH or place the script in a directory that is already in your PATH (like `/usr/local/bin`).

* Change the script’s permissions to make it executable:

```bash
chmod +x basicUtils.py
```

* Now you can run it directly from the terminal using:

```bash
basicUtils.py
```

## Usage

### Run the Script

To run the `basicUtils.py` script, simply execute it:

```bash
python3 basicUtils.py
```

Once the script is running, you can call different functions based on the available commands in the script.

### Example Functionality

Here are a few examples of what the script can do:

#### Math Operations:

```bash
$ python3 basicUtils.py add 5 10
# Output: 15

$ python3 basicUtils.py subtract 15 5
# Output: 10
```

#### Date and Time:

```bash
$ python3 basicUtils.py date
# Output: Current date and time (formatted)

$ python3 basicUtils.py time
# Output: Current time
```

#### Random Hexadecimal:

```bash
$ python3 basicUtils.py random-hex
# Output: A random hexadecimal value (e.g., 1a3f4b)
```

## License

This work is licensed under **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License**.

* You can use, share, and modify this script as long as it is for non-commercial purposes.
* If you redistribute or modify the script, you must do so under the same license.
* You must provide appropriate credit and give a link to the license.

See the full [license text here](https://creativecommons.org/licenses/by-nc-sa/4.0/).

