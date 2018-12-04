# webonacci

[![Build Status](https://travis-ci.org/krigar1184/webonacci.svg?branch=master)](https://travis-ci.org/krigar1184/webonacci)
[![codecov](https://codecov.io/gh/krigar1184/webonacci/branch/master/graph/badge.svg)](https://codecov.io/gh/krigar1184/webonacci)

A simple web application calculating nth fibonacci number.

Built and tested using Docker-18.09.0 and Docker-compose 1.23.2.

Prerequisites:
- docker
- docker-compose

Usage:
- run `make test` to run the test suite.
- run `make run` to run a project locally.
- navigate to /fib/1/5 to get a fibonacci values from 1st to 5th;
- navigate to /health to health check services (currently Redis).
