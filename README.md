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