import * as React from "react";
import { Show, SimpleShowLayout, TextField, NumberField, FunctionField } from "react-admin";
import { Typography, Card, CardContent, Box } from '@material-ui/core';
import moment from 'moment';

const WaterConsumptionDomesticTitle = ({ record }) => {
    return <span>Water Consumption Domestic</span>;
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

const WaterConsumptionDomesticShow = (props) => (
    <Show title={<WaterConsumptionDomesticTitle />} aside={<Aside />}  {...props}>
        <SimpleShowLayout>
            <FunctionField label="Date" render={record => `${record.date.split('-')[0]} - ${record.date.split('-')[1]}`} />
            <TextField source="reservoir.name" label="Reservoir Name" />
            <NumberField source="water_consumption_domestic" />
            <NumberField source="population" />
            <NumberField source="no_of_families" />
            <NumberField source="no_of_housing_units" />
        </SimpleShowLayout>
    </Show>
);

export default WaterConsumptionDomesticShow;
