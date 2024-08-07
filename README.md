# Install

1. Set Replicate API token in .env file.
2. Run docker-compose.

```docker-compose up```

# API
## POST /api/v1/video
Returns description of video.
### Body
|   |   |
|---|---|
|video|\<string\> (Required) URL path to a video.|
|prompt|\<string\> An additional text prompt.|

### Response
|   |   |
|---|---|
|output|\<string\> Model output.|
