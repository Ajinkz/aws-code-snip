


### Using Redshift connector library

```python
import redshift_connector
import pandas as pd
import numpy as np
import json

conn = redshift_connector.connect(
    host='redshift-cluster-1.czaygp0m0n3j.us-east-1.redshift.amazonaws.com',
    port=5439,
    database='dev',
    user='username',
    password='xxxxxxxx'
 )
query="select * from category"
data= pd.read_sql_query(query,conn)
#indx = data.to_json(orient='index')
data.to_csv("export.csv",index=False)
```

### Using Sqlalchemy library

```python
from sqlalchemy import create_engine
import pandas as pd
engine = create_engine('postgresql://username:xxxxxxxxx@redshift-cluster-1.czaygp0m0n3j.us-east-1.redshift.amazonaws.com:5439/dev')
data_frame = pd.read_sql('SELECT * FROM category;', engine)
data_frame.to_csv("exported.csv",index=False)
```


Ref

- https://ayushbi.medium.com/import-aws-redshift-data-into-pandas-dataframe-ca3caace6df9
