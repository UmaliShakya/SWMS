import * as React from "react";
import {
    Create,
    SimpleForm,
    ReferenceInput,
    SelectInput,
    NumberInput,
    DateInput,
    required,
    minValue,
    number,
} from "react-admin";

const WaterConsumptionDomesticCreate = (props) => (
    <Create title="Create Water Consumption Domestic" {...props}>
        <SimpleForm variant="standard" margin="normal" redirect="list">
            <DateInput label="Date" source="date" />
            <ReferenceInput label="Reservoir Name" source="id" reference="reservoirs">
                <SelectInput optionText="name" />
            </ReferenceInput>
            {/* <TextInput disabled label="Reservoir Name" source="reservoir.name" /> */}
            <NumberInput source="water_consumption_domestic" validate={[required(), number(), minValue(1, "Should be grater than 0.")]} />
            <NumberInput source="population" validate={[required(), number(), minValue(1, "Should be grater than 0.")]} />
            <NumberInput source="no_of_families" validate={[required(), number(), minValue(1, "Should be grater than 0.")]} />
            <NumberInput source="no_of_housing_units" validate={[required(), number(), minValue(1, "Should be grater than 0.")]} />
        </SimpleForm>
    </Create>
);

export default WaterConsumptionDomesticCreate;
