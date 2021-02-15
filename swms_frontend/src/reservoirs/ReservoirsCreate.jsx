import * as React from "react";
import {
  Create,
  SimpleForm,
  TextInput, NumberInput,
  required,
  minValue,
  number,
} from "react-admin";

const ReservoirsCreate = (props) => (
  <Create title="Create Reservoir" {...props}>
    <SimpleForm variant="standard" margin="normal" redirect="list">
      <TextInput source="name" validate={required()} resettable />
      <TextInput source="division" validate={required()} resettable />
      <NumberInput source="capacity" validate={[required(), number(), minValue(1, "Should be grater than 0.")]} />
      <NumberInput source="catchment_area" validate={[required(), number(), minValue(1, "Should be grater than 0.")]} />
      <NumberInput source="surface_area" validate={[required(), number(), minValue(1, "Should be grater than 0.")]} />
      <TextInput multiline source="description" resettable />
    </SimpleForm>
  </Create>
);

export default ReservoirsCreate;
