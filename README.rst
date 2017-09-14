dotenvy
=======

dotenv handler for python


install
-------

 ::

  pip install dotenvy


sample usages
-------------

common usage ::

  from dotenvy import load_env, read_file
  from os import environ

  load_env(read_file('.env'))
  my_var = environ.get('MY_VAR')

loading dotenv file to a dict with type casting ::

  from dotenvy import read_file, truthy

  config = read_file('.env', schema={
    'HOSTNAME': str,
    'PORT': int,
    'IS_DEBUG': truthy,  # can be 1/true/on/yes
  })
