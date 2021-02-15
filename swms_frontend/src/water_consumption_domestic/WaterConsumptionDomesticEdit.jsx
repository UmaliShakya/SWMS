import * as React from "react";
import {
    Edit,
    SimpleForm,
    TextInput,
    NumberInput,
    DateInput,
    required,
    minValue,
    number,
} from "react-admin";
import { Typography, Card, CardContent, Box } from '@material-ui/core';
import moment from 'moment';

const WaterConsumptionDomesticTitle = ({ record }) => {
    return <span>Edit Water Consumption Domestic</span>;
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

const WaterConsumptionDomesticEdit = (props) => (
    <Edit title={<WaterConsumptionDomesticTitle />} aside={<Aside />} {...props}>
        <SimpleForm variant="standard" margin="normal">
            <TextInput disabled label="Id" source="id" />
            <DateInput disabled label="Date" source="date" />
            <TextInput disabled label="Reservoir Name" source="reservoir.name" />
            <NumberInput source="water_consumption_domestic" validate={[required(), number(), minValue(1, "Should be grater than 0.")]} />
            <NumberInput source="population" validate={[required(), number(), minValue(1, "Should be grater than 0.")]} />
            <NumberInput source="no_of_families" validate={[required(), number(), minValue(1, "Should be grater than 0.")]} />
            <NumberInput source="no_of_housing_units" validate={[required(), number(), minValue(1, "Should be grater than 0.")]} />
        </SimpleForm>
    </Edit>
);

export default WaterConsumptionDomesticEdit;
