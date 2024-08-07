# Install

1. Set Replicate API token in .env file.
2. Run docker-compose.

```docker-compose up```

# API
## GET /api/v1/video
Returns description of video.
### Query Params
|   |   |
|---|---|
|video|\<string\> (Required) URL path to a video.|
|prompt|\<string\> An additional text prompt.|

### Response
|   |   |
|---|---|
|output|\<string\> Model output.|

### Sample
```
curl --get --location 'http://localhost:8000/api/v1/video/' \
--data-urlencode 'video=https://j-static.oss-cn-hangzhou.aliyuncs.com/pstatic/aivideo/c10ceba0b5a807c87c98ede52ec5667c.mp4' \
--data-urlencode 'prompt=Write a poem about what is happening.'
```

```
{"output": "The laptop screen glows,\nAs the person types away,\nTheir fingers moving swiftly,\nCreating words that flow.\n\nThe coffee cup sits nearby,\nAs the person sips and types,\nTheir thoughts flowing freely,\nInto the laptop's pages.\n\nThe sound of the keyboard,\nAs the person types away,\nTheir mind racing with ideas,\nAs they work through the day.\n\nThe coffee cup, a symbol,\nOf the energy that flows,\nAs the person works diligently,\nCreating something new and bold.\n\nThe laptop screen, a window,\nTo the world beyond,\nAs the person types and thinks,\nTheir ideas taking flight."}
```
