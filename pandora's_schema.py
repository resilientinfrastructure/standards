# class-based API
class DemoSchema(pa.DataFrameModel):
    item: Series[str] = pa.Field(isin=["apple", "orange"], coerce=True)
    price: Series[float] = pa.Field(gt=0, coerce=True)
