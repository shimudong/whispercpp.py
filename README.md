Python bindings for whisper.cpp
===============================

<a href="https://www.buymeacoffee.com/lukeFxC" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>

Change the lang from 'en' to 'zh' and add an api script. 

---
`pip install git+https://github.com/shimudong/whispercpp.py`

```python
from whispercpp import Whisper

w = Whisper('tiny')

result = w.transcribe("./wav_file/get.wav")
text = w.extract_text(result)
```

### Use the api 

##### First

```
python python_api.py
```
##### Then get a request
```
python api_res.py
```

Note: default parameters might need to be tweaked.
See Whispercpp.pyx.
