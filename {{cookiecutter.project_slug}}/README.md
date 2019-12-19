# {{cookiecutter.project_name}}

Context
-------

{{cookiecutter.description}}

Install
-------

Make sure you have Python >=3.7, create a [virtualenv](https://virtualenv.pypa.io/en/latest/)
and execute:

```
make requirements-dev
```

Run
---

Execute:

```
make run
```


Unit Tests
----------

Execute:

```
make test
```

Coverage
----------

Execute:

```
make test-coverage
```


Release
-------
Before generating a release you must create a env-var like the following:

```
export SIMPLE_SETTINGS={{cookiecutter.project_slug}}.settings.development 
```

This project uses [Semantic Versioning](http://semver.org/)
To make a release use one of the following commads:

```
make release-patch
make release-minor
make release-major
```

After running the command, you can simply push the tags to github with the command `git push && git push --tags`
