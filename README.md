# date_correction

日付をフォーマットを統一する('yyyy/mm/dd'型もしくは'yyyy/mm'型にする)

# version
0.0.3

# install

```shell
pip install -U date_correction
```

# usage

```python
correction = date_correction()
date_ymd = correction.jap_to_west("令和元年5月1日")
print(date_ymd) # '2019/05/01'
date_ym = correction.jap_to_west("令和元年5月1日", remove_day=True)
print(date_ym) # '2019/05'
```

