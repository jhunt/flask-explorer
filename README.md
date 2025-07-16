flask-explorer
==============

A small Flask app for exploring containerized environments,
troubleshooting deployments, debugging secrets propagation, etc.

Often I find myself in need of a way to simply determine if an
environment variable is being set properly, if a volume mount into
a container took, or if a container bind mount is wired
appropriately.  This application is my attempt to build a small
application that can be run strictly from a browser to inspect the
state of a configured container.

Note: you do need to be able to modify the deployment to use this
image for the container; this is _not_ a general purpose attach-to
debugger by any stretch!

## Deployment

Build the image with the included Dockerfile and put it somewhere
that your container deployment runtime can get to.

Then, deploy it via your normal methodology; `kubectl`, `docker`,
(in my case, at least) Snowflake's [Snowpark Container
Services][1], etc.

[1]: https://docs.snowflake.com/en/developer-guide/snowpark-container-services/specification-reference

The container will listen on TCP port 80 for standard HTTP
traffic; wire up services and networking bits accordingly.

## Usage

The `/` endpoint dumps the current environment variables in a
table, so that you can inspect them.

The `/file/*` endpoint reads and returns the contents of the file
starting from the root of the container filesystem.  This means
that if you ask for `/file/etc/passwd`, you will get the contents
of `/etc/passwd` – debugging and security are odd bedfellows,
indeed.

The `/ls/*` endpoint performs an `ls -la` on the given directory
or file (again, starting from the container filesystem root) and
returns that output as a text dump.  With no arguments (i.e.
`/ls`), the root directory is listed.
