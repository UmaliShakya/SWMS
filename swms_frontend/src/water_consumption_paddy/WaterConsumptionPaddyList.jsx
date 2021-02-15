import * as React from "react";
import {
    List,
    Datagrid,
    TextField,
    NumberField,
    downloadCSV,
    FunctionField,
} from "react-admin";
import jsonExport from "jsonexport/dist";

const exporter = (waterConsumptionPaddy) => {
    const waterConsumptionPaddyForExport = waterConsumptionPaddy.map((waterConsumptionPaddy) => {
        const { date, reservoir: { name }, water_consumption_paddy, rainfall, temperature, evaporation } = waterConsumptionPaddy;
        return {
            date,
            name,
            water_consumption_paddy,
            rainfall,
            temperature,
            evaporation,
        };
    });

    jsonExport(
        waterConsumptionPaddyForExport,
        {
            headers: [
                "date",
                "name",
                "water_consumption_paddy",
                "rainfall",
                "temperature",
                "evaporation",
            ], // Field order in exported file.
            rename: [
                "Date",
                "Reservoirs Name",
                "Water Consumption Paddy",
                "Rainfall",
                "Temperature",
                "Evaporation",
            ], // Rename headers in exported file.
        },
        (err, csv) => {
            downloadCSV(csv, "WaterConsumptionPaddy");
        }
    );
};

const WaterConsumptionPaddyList = (props) => (
    <List
        {...props}
        title="Water Consumption Paddy"
        exporter={exporter}
        perPage={25}
    >
        <Datagrid rowClick="show">
            <FunctionField label="Date" render={record => `${record.date.split('-')[0]} - ${record.date.split('-')[1]}`} />
            <TextField source="reservoir.name" label="Reservoir Name" />
            <NumberField source="water_consumption_paddy" />
            <NumberField source="rainfall" />
            <NumberField source="temperature" />
            <NumberField source="evaporation" />
        </Datagrid>
    </List>
);

export default WaterConsumptionPaddyList;
