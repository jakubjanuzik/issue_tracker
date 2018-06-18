# Setting up local instance


## Virtualenv and virtualenvwrapper (optional, highly recommended)

Installing virtualenvwrapper can be found [here](http://virtualenvwrapper.readthedocs.io/en/latest/install.html)

* `mkvirtualenv issue_tracker --python=$(which python3.6)`
* `cd /path/to/project` and `setvirtualenvproject` - thanks to that everytime you use `workon issue_tracker` your current directory will be changed to `/path/to/project`

## Installing necessary packages

* `pip install -r requirements.pip`

## Running development server

In order to use local_settings file, running application commands from `manage.py` should include `--settings=issue_tracker.local_settings` at the end. Example: `python manage.py runserver --settings=issue_tracker.local_settings`

## Makefile commands
There's a makefile available to run specific commandsm e.g. running local server or running migrations. To run it simply use `make command_name`, for example: `make runserver` to run local server.

## Permissions
There are three permissions defining what use can or cannot do.
To add/edit/remove them login as admin and go to "/admin/auth/permission/"
    * codename: can_add_issue - Determines whether or not user can add new issue
    * codename: can_edit_issue - Determines whether or not user can edit existing issue
    * codename: can_delete_issue - Determines whether or not user can delete issue
