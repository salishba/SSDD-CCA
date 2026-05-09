$headers = @{
    "x-access-token" = "=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE3NzgxNjcyNDB9.QC36LfDB6vz7Bodhb8QQDHq6cNMsqjzKOLPzXyhMgRM"
}

Invoke-WebRequest `
    -Uri "http://127.0.0.1:5000/api/post/3" `
    -Headers $headers