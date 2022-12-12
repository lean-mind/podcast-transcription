# Usage

- Add our audios files into `x_folder/` at the root of the project.
- We can use [Docker](./docker-support.md) to execute the transformation or we
  can use `make run-<module-name>` to execute in the local machine (needs
  installation).
- The final result it's a text file in `x_folder/` at the `data/` folder in the
  root of the project.
- I have an example of the output using
  [Carlos Ble podcast episode 30](./ep30-podcast-carlos-ble.txt)

> The format of the audios files should be `.mp3` for now the code it's blocked
> just only to use those kind of format.

## Performance (Tested on local machine)

Take in consideration the performance implications of the transformation. For
those examples I used 23 minutes of podcast and CPU not GPU.

> Make sure your audio it's not corrupted.
