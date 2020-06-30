<!--
https://readme42.com
-->



[![](https://img.shields.io/badge/OS-Unix-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/v/django-storages-s3-env.svg?maxAge=3600)](https://pypi.org/project/django-storages-s3-env/)
[![](https://img.shields.io/npm/v/django-storages-s3-env.svg?maxAge=3600)](https://www.npmjs.com/package/django-storages-s3-env)[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/django-storages-s3-env/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/django-storages-s3-env/actions)

### Installation
```bash
$ [sudo] pip install django-storages-s3-env
```

```bash
$ [sudo] npm i -g django-storages-s3-env
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
    <a href="https://readme42.com/">readme42.com</a>
</p>