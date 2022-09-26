# Usage

- Add our audios files into `audio_mp3_folder/` at the root of the project.
- We can use Docker to execute the transformation or we can use `make run local` to execute in the local machine (needs installation).
- The final result it's a text file in `audio_text_folder/` at the root of the project.
- I have an example of the output using [Carlos Ble podcast episode 30](./ep30-podcast-carlos-ble.txt)

> The format of the audios files should be `.mp3` for now the code it's blocked just only to use those kind of format.

## Performance (Tested on local machine)

Take in consideration the performance implications of the transformation.

- Base: (4GB RAM) 8 minutes of execution time. There are some small mistakes in the transformation process.
- Large: (12GB RAM) 3h 43 minutes of execution time. There are some small mistakes in the transformation process but with more quality than base.
