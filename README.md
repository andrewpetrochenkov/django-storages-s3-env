<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
https://pypi.org/project/django-readme-generator/
-->

[![](https://img.shields.io/badge/OS-Unix-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/v/django-storages-s3-env.svg?maxAge=3600)](https://pypi.org/project/django-storages-s3-env/)
[![](https://img.shields.io/npm/v/django-storages-s3-env.svg?maxAge=3600)](https://www.npmjs.com/package/django-storages-s3-env)
[![Travis](https://api.travis-ci.org/andrewp-as-is/django-storages-s3-env.svg?branch=master)](https://travis-ci.org/andrewp-as-is/django-storages-s3-env/)

#### Installation
```bash
$ [sudo] npm i -g django-storages-s3-env
```
```bash
$ [sudo] pip install django-storages-s3-env
```

#### Pros
+   compatible with [django-storages S3 settings](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html)
+   create env with one command

#### How it works
hard-coded environment variables names:
+   `AWS_STORAGE_BUCKET_NAME`
+   `AWS_STORAGE_USER`
+   `AWS_ACCESS_KEY_ID`
+   `AWS_SECRET_ACCESS_KEY`

#### Scripts usage
command|`usage`
-|-
`storages-s3-create-env` |`usage: storages-s3-create-env bucket`

#### Examples
`Makefile`, create env
```bash
MEDIA_BUCKET:=BUCKET_NAME
all:
    test -s .env.prod.media || storages-s3-create-env $(MEDIA_BUCKET) > .env.prod.media
```

#### Links
+   [django-storages](https://django-storages.readthedocs.io/en/latest/index.html)

<p align="center">
    <a href="https://pypi.org/project/django-readme-generator/">django-readme-generator</a>
</p>