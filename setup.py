import setuptools

setuptools.setup(
    name='django-storages-s3-env',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages(),
    scripts=['scripts/storages-s3-create-env']
)
