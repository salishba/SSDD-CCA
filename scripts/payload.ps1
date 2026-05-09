$headers = @{
    "x-access-token" = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE3NzgzNDQ3ODR9.Taszmkr7BUFvonYL46GgCaPW09O9-IEOLnzsMJcSUdE"
}

Invoke-WebRequest `
    -Uri "http://127.0.0.1:5000/api/post/1" `
    -Headers $headers