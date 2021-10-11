# cloodle

A Moodle command-line tool for students that streamlines assignment retrieval and submissions.

It makes use of Moodle's mobile web services API, and consequently requires appropriate settings to be enabled by the site admin.

Currently only has support on Linux.

## Installation

### Prerequisite installations
* [python3](https://www.python.org/downloads/)
* [curl](https://curl.se/download.html)

### Clone repository from github
```
git clone https://github.com/sriramun/cloodle.git
cd cloodle
```

### Create alias
If you wish to use the tool from anywhere on your system
```
echo alias lms="\"$(pwd)/lms\"" >> ~/.bash_aliases
. ~/.bashrc
```

## Usage
Execute `./lms help` to get started.

## Contribute
Useful Moodle sites for testing and debugging: 
* [sandbox.moodledemo.net](https://sandbox.moodledemo.net/)
* [school.moodledemo.net](https://school.moodledemo.net/)
