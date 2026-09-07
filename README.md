# Gryffindor Challenge -- Starter Files

Starter project for Page 12 (Final Challenge, Part 2: Combining Comparisons
with `and` / `or`).

The boilerplate function and the test file have already been written for
you. **You do not need to write or edit the test file.** Your job is only
to replace the `pass` statement inside the boilerplate function with real
logic, following the rules on Page 12.

This is its own standalone project, separate from the confidence challenge
on Page 11. Keep the two in separate folders.

## Folder structure

```
gryffindor-challenge/
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

## Setup

1. Copy this whole `gryffindor-challenge` folder into your
   `hogwarts-sorting-hat` repository, as a top-level folder alongside your
   existing `sorting_hat.py` (and the `confidence-challenge` folder, if you
   have already completed Page 11).
2. Install pytest if you haven't already:

   ```
   cd gryffindor-challenge
   pip install -r requirements.txt
   ```

   (or simply `pip install pytest`)

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

### Why the imports still work

The test file still says `from gryffindor_eligibility import ...`, even
though `gryffindor_eligibility.py` now lives in a different folder
(`app/`) to the test file (`test/`). That works because of `pytest.ini`:
it tells pytest to add `app/` to Python's import path before the tests
run. You don't need to understand this file in detail, and you don't need
to change it -- just keep it inside `gryffindor-challenge`, alongside
`app` and `test`.

Follow the instructions on Page 12 of the tutorial for the full Red,
Green, Refactor workflow, including when to commit and push at each
stage.
