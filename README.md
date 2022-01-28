# Pyper
Pyper is powerful but simple pipeline tool 
```python 
nums = [1, 2, 3, 4]
fn = lambda x: x * 2

pipe = Pipe()
stage = (
    pipe.set_source(LocalSource(data=nums))
    .add_task(MapTask(fn=fn))
    .add_task(MapTask(fn=fn))
    .run()
)
stage.result # [4, 8, 12, 16] 
```

## Usage
### Interactive environment with Docker
```shell
> make run-interactive-docker

Python 3.7.12 (default, Jan 26 2022, 15:21:31) 
[GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import pyper
>>> ...

```