import * as React from "react";
import { Show, SimpleShowLayout, TextField, NumberField } from "react-admin";
import { Typography, Card, CardContent, Box } from '@material-ui/core';
import moment from 'moment';

const ReservoirTitle = ({ record }) => {
  return <span>Reservoir {record ? `"${record.name}"` : ""}</span>;
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

const ReservoirsShow = (props) => (
  <Show title={<ReservoirTitle />} aside={<Aside />}  {...props}>
    <SimpleShowLayout>
      <TextField source="id" />
      <TextField source="name" />
      <TextField source="division" />
      <NumberField source="capacity" />
      <NumberField source="catchment_area" />
      <NumberField source="surface_area" />
      <TextField source="description" />
    </SimpleShowLayout>
  </Show>
);

export default ReservoirsShow;
