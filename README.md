# py-memz
Python implementation of the popular MEMZ trojan

## Notes
Doesn't rewrite the boot sector (yet) (its never going to)

Instead, it puts a silly little python file in your startup that emulates the nyan cat part

The Death trojan triggers after 4 minutes of the Puzzle payload (final payload) and is the only way to trigger it, as i couldn't actually detect if one of the processes got killed

No external modules or files needed! Only python (with Tkinter for the nyan cat payload)

## Credits
Reverse Text, Create Windows, Invert, Tunnel and Icons created by doot (dootw on discord)

Everything else by me (puzzl3d on discord)

Original trojan by Leurak

Idea to make in python by doot
