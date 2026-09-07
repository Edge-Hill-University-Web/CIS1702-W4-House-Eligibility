# House Eligibility Challenge -- Starter Files

The boilerplate function and the test file have already been written for
you. **You do not need to write or edit the test file.** Your job is only
to replace the `pass` statement inside the boilerplate function with real
logic, following the rules on Page 12.

This is its own standalone project, separate from the confidence challenge
on Page 11. Keep the two in separate folders.

## Folder structure

```
CIS1702-W4-House-Eligibility/
├── app/
│   └── gryffindor_eligibility.py
├── test/
│   └── test_gryffindor_eligibility.py
├── pytest.ini
└── requirements.txt
```

Application code lives in `app/`. Tests live in `test/`.

| File | What it is | Do you edit it? |
|---|---|---|
| `app/gryffindor_eligibility.py` | Boilerplate | Yes -- replace `pass` with your logic |
| `test/test_gryffindor_eligibility.py` | Tests | No |


## Running the tests

Always run pytest from inside the `gryffindor-challenge` folder (the one
containing `app/`, `test/` and `pytest.ini`):

```
cd gryffindor-challenge
pytest test/test_gryffindor_eligibility.py -v
```

Or simply:

```
pytest -v
```

Follow the instructions on Page 12 of the tutorial for the full Red,
Green, Refactor workflow, including when to commit and push at each
stage.
