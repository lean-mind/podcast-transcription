# Docker support

If you need to change some of the commands, those are contained in the
[Makefile](../Makefile).

## Build image

This image is named as `podcast-transcription` and repository `audio_mp3_folder`
and `audio_text_folder` are mapped into the image. So the results of the
execution will be on the repository.

> Remember that the image should be builded again if you change the code.

```bash
make build-image
```

## Run docker

> Remember that you have the minimum requirements for the execution. Some clues
> are on the [usage document](./usage.md).

```bash
make run-image
```
