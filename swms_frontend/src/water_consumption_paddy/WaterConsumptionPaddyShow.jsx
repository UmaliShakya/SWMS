import * as React from "react";
import { Show, SimpleShowLayout, TextField, NumberField, FunctionField } from "react-admin";
import { Typography, Card, CardContent, Box } from '@material-ui/core';
import moment from 'moment';

const WaterConsumptionPaddyTitle = ({ record }) => {
    return <span>Water Consumption Paddy</span>;
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

const WaterConsumptionPaddyShow = (props) => (
    <Show title={<WaterConsumptionPaddyTitle />} aside={<Aside />}  {...props}>
        <SimpleShowLayout>
            <FunctionField label="Date" render={record => `${record.date.split('-')[0]} - ${record.date.split('-')[1]}`} />
            <TextField source="reservoir.name" label="Reservoir Name" />
            <NumberField source="water_consumption_paddy" />
            <NumberField source="rainfall" />
            <NumberField source="temperature" />
            <NumberField source="evaporation" />
        </SimpleShowLayout>
    </Show>
);

export default WaterConsumptionPaddyShow;
