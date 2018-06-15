runserver:
	python manage.py runserver --settings=issue_tracker.local_settings

run_linter:
	black --config pyproject.toml .

run_isort:
	isort

full_lint: run_linter run_isort

createsuperuser:
	 python manage.py createsuperuser --settings=issue_tracker.local_settings

shell:
	python manage.py shell --settings=issue_tracker.local_settings

migrate:
	python manage.py migrate --settings=issue_tracker.local_settings

makemigrations:
	python manage.py makemigrations --settings=issue_tracker.local_settings
