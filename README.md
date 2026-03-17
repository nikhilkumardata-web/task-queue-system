# Distributed Task Queue System

## Overview
This project implements a basic distributed task queue system using Python.

It demonstrates how backend systems process asynchronous jobs using queues and worker processes.

## Architecture
Client → FastAPI → Queue → Worker → Result

## Features
- Task submission via API
- Queue-based processing
- Background worker execution
- Unique task tracking

## Tech Stack
Python, FastAPI

## How it works
1. API receives task request
2. Task is pushed to queue
3. Worker processes tasks asynchronously
