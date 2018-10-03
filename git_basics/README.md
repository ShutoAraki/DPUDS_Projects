# `git` Practice Session
Author: Shuto Araki

Date: 10/01/2018

## First, fork this repository from the upper right button.
This allows you to copy this repository that you own and play around with!

## Clone this repository
1. Create a folder named `git_practice` on your Desktop (or wherever you like).

2. Open Terminal (Mac) or Command Prompt (Windows). This application helps you navigate through files in your computer without GUI (Graphical User Interface). Back in the day before Windows or Mac OS came out, this is how people used to operate computers!

3. Here's a good command for ya: `cd [directory-name]` will <strong>c</strong>hange <strong>d</strong>irectory. From your default current working directory, type `cd Desktop`. Try navigating to your `git_practice` folder.

4. Go back to your repository that you just forked. You see the green button that says "Clone or Download"? Click on it and copy the address you see. In my case, it is `git@github.com:ShutoAraki/PracticeSession.git`.

5. On Terminal, type `git clone [whatever address that you just copied]`. So in my case, I would type `git clone git@github.com:ShutoAraki/PracticeSession.git`. This should create a copy of your <strong>remote repository</strong> on the folder `git_practice`. This folder is now your <strong>local repository</strong>!

## Try add, commit, and push to your repository!
Remember `git add .`, `git commit -m "Message"`, and `git push`? Try those commands on your Terminal or Command Prompt.

1. Create a new text file and type whatever you like and add it to your `git_practice` folder.

2. Go back to Terminal on the folder and type `git status`. It tells you what file you haven't committed or staged.

3. Stage the new text file by typing `git add .`. The last dot means "Add every unstaged file to the stage." You can also specify which file to stage by typing its name. (Tip: You can start typing the file name and hit the tab key. It will automatically fills in what you were trying to type! You don't have to type a whole name, this is great!!)

4. Commit the staged file into your local repository by typing `git commit -m "This is my first git practice"`. You can type whatever message you want, but don't forget `-m`, which signifies a flag for message.

5. Push the committed file onto your remote repository by typing `git push`. Check your GitHub repository page now and see if the new file is pushed!

Refer to [the official documentation/guide](https://git-scm.com/book/en/v2) for more!

## Try creating pull request to MY repository for suggestion/changes in the code.
I should be able to see your changes and decide whether I accept your change or not!

### THIS IS HOW OPEN SOURCE CONTRIBUTIONS WORK! WOW! IT'S AWESOME!!

