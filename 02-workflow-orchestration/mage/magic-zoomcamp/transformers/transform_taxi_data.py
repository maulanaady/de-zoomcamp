import re
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


def change_case(str):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', str)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


@transformer
def transform(data, *args, **kwargs):
    ######### tutorial ###################
    # print("Rows with zero pasenggers and zero trip distance:", data['passenger_count'].isin([0]).sum())
    # return data[data['passenger_count'] > 0]

    ########### task ##############
    # first transformation : filter passenger count and trip distance greather than 0
    print(f'Original row count = {data.shape[0]}')
    filter = (data['passenger_count'] > 0) & (data['trip_distance'] > 0)
    data = data[filter]

    # second transformation: tpep_pickup_date based on tpep_pickup_datetime column
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date

    # third transformation: convert column name from camel case to snake case
    mapping = {}
    for cols in data.columns:
        
        mapping.update({cols : change_case(cols)})
    data.rename(columns=mapping, inplace=True)

    print(f'Final row count = {data.shape[0]}')
    return data
    


@test
def test_passenger_count(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output['passenger_count'].isin([0]).sum() == 0, 'There are rides with zero passengers'

@test
def test_trip_distance(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output['trip_distance'].isin([0]).sum() == 0, 'There are rides with zero trip distance'    

@test
def test_vendor_id_column(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output.columns.isin(['vendor_id']).any() == True, 'vendor_id column does not exist in results'    
