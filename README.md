# pytoodo

pytoodo is a Todo List CLI application written in Python.
It allows users to manage their daily tasks and
keep track of their progress in a terminal window.
This terminal CLI app is inspired by the [**Study Together**](https://discord.gg/study) discord server.

[![asciicast](https://github.com/domsalvador/pytoodo/raw/main/demo.gif)](https://asciinema.org/a/PBUJJsmfQP1JgD8Jqdl2dtim0)

- **Stay on track!** Add tasks as needed. Delete tasks when you're done.
- Your tasks are persistent **in-between** sessions! The app can remember past tasks even after you closed it!
- It **just works** and **respects your privacy**.
- **This CLI app** does not share data to 3rd-party companies. **All user data stays** on your device.
- **Free and Open Source**. As it should be.

## Requirements Installation and Usage

```bash
sudo apt-get update && sudo apt-get install python3 pip git -y
git clone https://github.com/Db-San/pytoodo
cd pytoodo
pip install -r requirements.txt
python3 pytoodo.py
```

## Sample Usage Output

```text
$ python3 pytoodo.py
pytoodo / your tasks (4)
-------------------------
1. water the plants (living room)
2. pay karl a visit at the bulding (2F, Unit 3)
3. dispose the garbage bin before going out
4. get ready for church (0430H)

Choices: 
[1] - Show all tasks
[2] - Add task
[3] - Delete task
[q] - Quit
Enter your choice [1-3, q(uit)]
> 2 <enter>
```
