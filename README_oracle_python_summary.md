## Work Process

I created an Oracle Cloud Database (Free Tier), used SQL Developer to create tables, insert dummy data, and build a view.

I saved the SQL scripts to a GitHub repository.

The repository was initialized using `git init`, connected to GitHub, and pushed via the CLI.

I also created a Python script to connect to the database using the `oracledb` library.

---

## Problem

- The thin client didn’t work (it doesn't support the wallet – the authentication package).
- I had to switch to the thick client (Oracle Instant Client).
- However, when using the thick mode, Oracle ignored my wallet folder and looked for `tnsnames.ora` in the default `network/admin` directory.
- I solved this by setting:

  ```python
  os.environ["TNS_ADMIN"] = wallet_location

###  Key Point
> The `cursor` object showed the **specific error**, which helped me resolve the issue in **5 minutes** — something I couldn't figure out for over an hour without it.  
> The cursor *“knows the context”* and displays the **actual database response**.


## Result

-  The Python script works with the wallet in **thick mode**
-  **Connection**, **SQL query**, and **data output** are all functioning correctly
-  The entire process is **reproducible** and can be easily **shared** or **reused**
