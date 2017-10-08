# Homework 3 - SI 364 F17

### Deadline: October 8, 2017 at 11:59 PM

## Instructions

This homework consists of 2 parts, each worth 250 points.

### Part 1

Edit the `SI364_HW3.py` file inside the `HW3Part1` directory to add routes to the basic Flask application that will match the templates in the `templates` subdirectory inside the `HW3Part1` folder.

When you are done, you should have the following four routes which render each of the corresponding templates with reasonable data:

* `http://localhost:5000/artistform` -> `artistform.html`
* `http://localhost:5000/artistinfo` -> `artist_info.html`
* `http://localhost:5000/artistlinks` -> `artist_links.html`
* `http://localhost:5000/specific/song/<artist_name>` -> `specific_artist.html`

Each of the templates should be rendered with actual data when those routes are reached when the Flask application runs. 

Check out the action on forms and end-locations of links in order to ensure that you send the correct data to templates and that the templates get the correct data!

You may edit the templates (only slightly, you may not edit their structure), but you should not need to do so in any significant way.


### Part 2

Inside the provided directory `new_application`, there is an empty file `new_flask_app.py`, and an empty subdirectory `templates`. (The subdirectory has an HTML file in it, but that file is empty! You could replace it, fill it in with content, or rename it if you wanted. *[Note: if you delete a file, git will still need you to tell git, with the `git rm` command, that you've deleted it, to update that it isn't there! We can help you with this if you delete a file and have trouble dealing with it in git.]*)

To complete this part, write Flask application code in the empty file and add at least 2 HTML files to the `templates` subdirectory. 

The Flask application should have at least 2 routes (view functions). At least one of the routes should use a form to send data to the other one. (e.g. a form that, when submitted, sends the data input into the form to the other route)

The `templates` subdirectory here should contain at least 2 HTML files, which each get rendered when you access a different URL route while the Flask app is running.

For example, you could create a form that asks for your favorite English word. The other route could show *Your favorite word does not contain the letter 'z'* if there is no `z` character in the word you entered, and *Your favorite word contains the letter 'z'!* if there is.

That's a relatively simple data manipulation example, but that would completely fulfill the requirement! The only goal is to practice sending data and writing a template that will render dynamic data.

The only restriction is that you **may not get points for including view functions and/or routes that have been used in exercises/samples from lecture or section**. e.g. you should not submit a route `findcoolstuff` or `user/<name>`. It can be as minimal or as complicated as you want -- even if the data manipulation that your code does is simple (e.g. getting data about 1 word, and showing somethign different depending upon whether it includes the letter 'z'), the concepts you're dealing with here are quite challenging!


## To complete the assignment and submit it

Fork this repository. 

To work on it, clone the repository and make edits, additions, and commits per the directions. Push them to *your clone* of the repository.

Submit the link to YOUR repository clone to the assignment for **HW 3** on the SI 364 Canvas site. It should be a URL of the format: `https://github.com/`**Your-GitHub-Username**`/HW3.git`