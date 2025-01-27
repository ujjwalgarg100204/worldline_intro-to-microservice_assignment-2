#!/bin/bash

conda activate microsvc__order_management_sys__order_sys
uvicorn app:app --reload --host 0.0.0.0 --port 8000
