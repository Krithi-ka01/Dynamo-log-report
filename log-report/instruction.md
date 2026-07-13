You are given an Apache-style access log at /app/access.log.

Analyze the log and create a JSON report at /app/report.json.

Your report must satisfy the following requirements:

1. Count the total number of requests and store it as "total_requests".
2. Count the number of unique client IP addresses and store it as "unique_ips".
3. Determine the most frequently requested path and store it as "top_path".
4. Save the output as valid JSON at exactly /app/report.json.