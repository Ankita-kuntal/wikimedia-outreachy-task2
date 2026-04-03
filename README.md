# Wikimedia-outreachy-task2 - URL Status Checker

This script reads a list of URLs from a CSV file and checks their HTTP status.

## Approach
- Read URLs from the CSV file
- Send a request to each URL
- Print the status code if successful
- Print "(ERROR)" if the request fails

## Example Output
(200) https://example.com  
(404) https://example.com/page  
(ERROR) https://invalid-url  

## What this shows
- Basic handling of HTTP requests
- Error handling using try-except
- Working with CSV input data
