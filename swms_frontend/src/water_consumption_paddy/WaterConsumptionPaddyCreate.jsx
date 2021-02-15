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

const WaterConsumptionPaddyCreate = (props) => (
    <Create title="Create Water Consumption Paddy" {...props}>
        <SimpleForm variant="standard" margin="normal" redirect="list">
            <DateInput label="Date" source="date" />
            <ReferenceInput label="Reservoir Name" source="id" reference="reservoirs">
                <SelectInput optionText="name" />
            </ReferenceInput>
            {/* <TextInput disabled label="Reservoir Name" source="reservoir.name" /> */}
            <NumberInput source="water_consumption_paddy" validate={[required(), number(), minValue(1, "Should be grater than 0.")]} />
            <NumberInput source="rainfall" validate={[required(), number(), minValue(1, "Should be grater than 0.")]} />
            <NumberInput source="temperature" validate={[required(), number(), minValue(1, "Should be grater than 0.")]} />
            <NumberInput source="evaporation" validate={[required(), number(), minValue(1, "Should be grater than 0.")]} />
        </SimpleForm>
    </Create>
);

export default WaterConsumptionPaddyCreate;
