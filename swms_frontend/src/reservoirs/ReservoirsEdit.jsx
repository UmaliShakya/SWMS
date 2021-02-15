import * as React from "react";
import {
  Edit,
  SimpleForm,
  TextInput, NumberInput,
  required,
  minValue,
  number,
  maxLength
} from "react-admin";
import { Typography, Card, CardContent, Box } from '@material-ui/core';
import moment from 'moment';

const ReservoirTitle = ({ record }) => {
  return <span>Edit Reservoir {record ? `"${record.name}"` : ""}</span>;
};

const Aside = ({ record }) => (
  <Card p={1} m={1}>
    <CardContent>
      <Typography variant="h6">
        History
        </Typography>
      <Typography component="div">
        <Box fontWeight="fontWeightMedium" m={1}>
          Created At
        </Box>
        <Box fontWeight="fontWeightLight" m={1}>
          {record ? `${moment(record.created_at).format("YYYY D MMM, H:m")}` : ""}
        </Box>
        <Box fontWeight="fontWeightMedium" m={1}>
          Updated At
        </Box>
        <Box fontWeight="fontWeightLight" m={1}>
          {record ? `${moment(record.updated_at).format("YYYY D MMM, H:m")}` : ""}
        </Box>
      </Typography>
    </CardContent>
  </Card>
);

const ReservoirsEdit = (props) => (
  <Edit title={<ReservoirTitle />} aside={<Aside />} {...props}>
    <SimpleForm variant="standard" margin="normal">
      <TextInput disabled label="Id" source="id" />
      <TextInput source="name" validate={[required(), maxLength(99, "Too Long")]} resettable />
      <TextInput source="division" validate={[required(), maxLength(99, "Too Long")]} resettable />
      <NumberInput source="capacity" validate={[required(), number(), minValue(1, "Should be grater than 0.")]} />
      <NumberInput source="catchment_area" validate={[required(), number(), minValue(1, "Should be grater than 0.")]} />
      <NumberInput source="surface_area" validate={[required(), number(), minValue(1, "Should be grater than 0.")]} />
      <TextInput multiline source="description" validate={[required(), maxLength(199, "Too Long")]} resettable />
    </SimpleForm>
  </Edit>
);

export default ReservoirsEdit;
