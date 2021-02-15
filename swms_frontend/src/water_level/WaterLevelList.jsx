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

const exporter = (waterLevel) => {
    const waterLevelForExport = waterLevel.map((waterLevel) => {
        const { date, reservoir: { name }, water_level, rainfall, temperature, evaporation } = waterLevel;
        return {
            date,
            name,
            water_level,
            rainfall,
            temperature,
            evaporation,
        };
    });

    jsonExport(
        waterLevelForExport,
        {
            headers: [
                "date",
                "name",
                "water_level",
                "rainfall",
                "temperature",
                "evaporation",
            ], // Field order in exported file.
            rename: [
                "Date",
                "Reservoirs Name",
                "Water Level",
                "Rainfall",
                "Temperature",
                "Evaporation",
            ], // Rename headers in exported file.
        },
        (err, csv) => {
            downloadCSV(csv, "WaterLevel");
        }
    );
};

const WaterLevelList = (props) => (
    <List
        {...props}
        title="Water Level"
        exporter={exporter}
        perPage={25}
    >
        <Datagrid rowClick="show">
            <FunctionField label="Date" render={record => `${record.date.split('-')[0]} - ${record.date.split('-')[1]}`} />
            <TextField source="reservoir.name" label="Reservoir Name" />
            <NumberField source="water_level" />
            <NumberField source="rainfall" />
            <NumberField source="temperature" />
            <NumberField source="evaporation" />
        </Datagrid>
    </List>
);

export default WaterLevelList;
