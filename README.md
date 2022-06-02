# Quantium starter repo
This repo contains everything you need to get started on the program! Good luck!

> 1. Create a virtual environment:

```bash
$ python3 -m venv venv
```

> 2. Activate the virtual environment:

```bash
$ source venv/bin/activate
(venv) $
```

> 3. Install Packages Into It (install any external dependencies )

```bash
(venv) $ python -m pip install <package-name>
pip install pandas
pip install dash
pip install dash[testing]
```

> 4. Deactivate It

```bash
(venv) $ deactivate
$
```

> 5. Run dash app

```bash
(venv) $ python app.py
```

> 5. test dash app

```bash
(venv) $ python -m pytest --remote -k bsly001 task5.py
(venv) $ pytest --remote -k bsly001 task5.py
```

These CSV files contain transaction data for Soul Foods’s entire morsel line. 

Each row indicates the quantity of a given type of morsel sold in a given region at a given price on a given day. 

These CSV files contain transaction data for Soul Foods’s entire morsel line. Each row indicates the quantity of a given type of morsel sold in a given region at a given price on a given day. 

![Screen Shot 2022-06-02 at 2.11.13 PM](/Users/chy/Library/Application Support/typora-user-images/Screen Shot 2022-06-02 at 2.11.13 PM.png)