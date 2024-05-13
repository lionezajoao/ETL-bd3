import os
import logging
import pandas as pd
from logging.config import fileConfig
import pandas as pd
fileConfig('logging_config.ini')

class Utils:
    def __init__(self) -> None:
        self.path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        self.logger = logging.getLogger()

    def load_data(self, path):
        return pd.read_csv(path, na_values=['', ' ', 'nan'], keep_default_na=True)
    
    def handle_dim_customers(self):
        return self.load_data(f"{ self.path }/src/base_files/customers_export.csv")
        
    def handle_dim_dates(self) -> pd.DataFrame:
        df = self.load_data(f"{ self.path }/src/base_files/orders_export.csv")

        df['SALES_DATE'] = pd.to_datetime(df['ORDER_DATE'], format='%d-%b-%y')

        df['SALES_YEAR'] = df['SALES_DATE'].dt.year
        df['SALES_MONTH'] = df['SALES_DATE'].dt.month
        df['SALES_DAY'] = df['SALES_DATE'].dt.day
        df['SALES_QUARTER'] = df['SALES_DATE'].dt.quarter
        df['SALES_MONTH_NAME'] = df['SALES_DATE'].dt.strftime('%B')
        df['SALES_DAY_OF_YEAR'] = df['SALES_DATE'].dt.dayofyear
        df['SALES_DATE_ID'] = (df['SALES_DATE'] - pd.Timestamp("1970-01-01")) // pd.Timedelta('1ms')

        df = df[['SALES_YEAR', 'SALES_MONTH', 'SALES_DAY', 'SALES_QUARTER', 'SALES_MONTH_NAME', 'SALES_DAY_OF_YEAR', 'SALES_DATE_ID']]

        return df

    def handle_dim_products(self):
        return self.load_data(f"{ self.path }/src/base_files/products_export.csv")
    
    def handle_sales(self):

        df = self.load_data(f"{ self.path }/src/base_files/orders_export.csv")

        df.rename(columns={
            'CUSTOMER_ID': 'CUSTOMER_DIM_ID',
            'SALES_REP_ID': 'SALESREP_DIM_ID',
            'PROMO_ID': 'PROMO_DIM_ID',
            'PRODUCT_ID': 'PRODUCT_DIM_ID'
        }, inplace=True)

        df['ORDER_DATE'] = pd.to_datetime(df['ORDER_DATE'], format='%d-%b-%y')

        df['SALES_DATE_DIM_ID'] = (df['ORDER_DATE'] - pd.Timestamp("1970-01-01")) // pd.Timedelta('1ms')

        grouped_df = df.groupby(['CUSTOMER_DIM_ID', 'SALESREP_DIM_ID', 'PROMO_DIM_ID', 'PRODUCT_DIM_ID', 'SALES_DATE_DIM_ID']).agg({
            'UNIT_PRICE': 'sum',
            'QUANTITY': 'sum'
        }).rename(columns={
            'UNIT_PRICE': 'DOLLARS_SOLD',
            'QUANTITY': 'QUANTITY_SOLD'
        }).reset_index()

        return grouped_df
    
    def handle_fact_salesrep(self):
        return self.load_data(f"{ self.path }/src/base_files/salesrep_export.csv")

    def handle_promotions(self):
        return self.load_data(f"{ self.path }/src/base_files/promotions_export.csv")
    