create table if not exists dim_customers (
    CUSTOMER_ID INTEGER PRIMARY KEY,
    CUST_FIRST_NAME VARCHAR,
    CUST_LAST_NAME VARCHAR,
    STREET_ADDRESS VARCHAR,
    POSTAL_CODE INTEGER,
    CITY VARCHAR,
    STATE_PROVINCE VARCHAR,
    COUNTRY_ID VARCHAR,
    COUNTRY_NAME VARCHAR,
    REGION_ID INTEGER,
    NLS_LANGUAGE VARCHAR,
    NLS_TERRITORY VARCHAR,
    CREDIT_LIMIT INTEGER,
    CUST_EMAIL VARCHAR,
    PRIMARY_PHONE_NUMBER VARCHAR,
    PHONE_NUMBER_2 VARCHAR,
    ACCOUNT_MGR_ID INTEGER,
    LOCATION_GTYPE INTEGER,
    LOCATION_SRID INTEGER,
    LOCATION_X FLOAT,
    LOCATION_Y FLOAT
);

create table if not exists dim_promotions (
    PROMO_ID INTEGER PRIMARY KEY,
    PROMO_NAME VARCHAR
);

create table if not exists dim_products (
    PRODUCT_ID INTEGER PRIMARY KEY,
    PRODUCT_NAME VARCHAR,
    LANGUAGE_ID VARCHAR,
    MIN_PRICE FLOAT,
    LIST_PRICE FLOAT,
    PRODUCT_STATUS VARCHAR,
    SUPPLIER_ID INTEGER,
    WARRANTY_PERIOD INTEGER,
    WEIGHT_CLASS INTEGER,
    PRODUCT_DESCRIPTION VARCHAR,
    CATEGORY_ID INTEGER,
    CATALOG_URL VARCHAR,
    SUB_CATEGORY_NAME VARCHAR,
    SUB_CATEGORY_DESCRIPTION VARCHAR,
    PARENT_CATEGORY_ID INTEGER,
    CATEGORY_NAME VARCHAR
);

create table if not exists dim_date(
    SALES_DATE_ID BIGINT PRIMARY KEY,
    SALES_DATE DATE,
    SALES_YEAR INTEGER,
    SALES_MONTH INTEGER,
    SALES_DAY INTEGER,
    SALES_QUARTER INTEGER,
    SALES_MONTH_NAME VARCHAR,
    SALES_DAY_OF_YEAR INTEGER
);

create table if not exists dim_salesrep(
    EMPLOYEE_ID INTEGER PRIMARY KEY,
    FIRST_NAME VARCHAR,
    LAST_NAME VARCHAR,
    EMAIL VARCHAR,
    PHONE_NUMBER VARCHAR,
    HIRE_DATE VARCHAR,
    JOB_ID VARCHAR,
    SALARY INTEGER, 
    COMMISSION_PCT FLOAT,
    MANAGER_ID INTEGER,
    DEPARTMENT_ID INTEGER
);

create table if not exists sales(
    SALES_ID SERIAL PRIMARY KEY,
    CUSTOMER_DIM_ID INTEGER,
    PROMO_DIM_ID INTEGER,
    PRODUCT_DIM_ID INTEGER,
    SALES_DATE_DIM_ID BIGINT,
    SALESREP_DIM_ID INTEGER,
    DOLLARS_SOLD FLOAT,
    QUANTITY_SOLD INTEGER,
    FOREIGN KEY (CUSTOMER_DIM_ID) REFERENCES dim_customers(CUSTOMER_ID),
    FOREIGN KEY (PROMO_DIM_ID) REFERENCES dim_promotions(PROMO_ID),
    FOREIGN KEY (PRODUCT_DIM_ID) REFERENCES dim_products(PRODUCT_ID),
    FOREIGN KEY (SALES_DATE_DIM_ID) REFERENCES dim_date(SALES_DATE_ID),
    FOREIGN KEY (SALESREP_DIM_ID) REFERENCES dim_salesrep(EMPLOYEE_ID)
);

create sequence if not exists sales_id;

create table if not exists sales(
    SALES_ID INTEGER PRIMARY KEY DEFAULT nextval('sales_id'),
    CUSTOMER_DIM_ID INTEGER,
    PROMO_DIM_ID INTEGER,
    PRODUCT_DIM_ID INTEGER,
    SALES_DATE_DIM_ID BIGINT,
    SALESREP_DIM_ID INTEGER,
    DOLLARS_SOLD FLOAT,
    QUANTITY_SOLD INTEGER,
    FOREIGN KEY (CUSTOMER_DIM_ID) REFERENCES dim_customers(CUSTOMER_ID),
    FOREIGN KEY (PROMO_DIM_ID) REFERENCES dim_promotions(PROMO_ID),
    FOREIGN KEY (PRODUCT_DIM_ID) REFERENCES dim_products(PRODUCT_ID),
    FOREIGN KEY (SALES_DATE_DIM_ID) REFERENCES dim_date(SALES_DATE_ID),
    FOREIGN KEY (SALESREP_DIM_ID) REFERENCES dim_salesrep(EMPLOYEE_ID)
);