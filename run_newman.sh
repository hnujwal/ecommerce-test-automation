#!/bin/bash
# Newman script to run Postman collections

newman run postman/ecommerce_collection.json \
  --environment postman/environment.json \
  --reporters html,json \
  --reporter-html-export newman-report.html \
  --reporter-json-export newman-report.json