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

const exporter = (waterConsumptionDomestic) => {
    const waterConsumptionDomesticForExport = waterConsumptionDomestic.map((waterConsumptionDomestic) => {
        const { date, reservoir: { name }, water_consumption_domestic, population, no_of_families, no_of_housing_units } = waterConsumptionDomestic;
        return {
            date,
            name,
            water_consumption_domestic,
            population,
            no_of_families,
            no_of_housing_units,
        };
    });

    jsonExport(
        waterConsumptionDomesticForExport,
        {
            headers: [
                "date",
                "name",
                "water_level",
                "water_consumption_domestic",
                "population",
                "no_of_families",
                "no_of_housing_units",
            ], // Field order in exported file.
            rename: [
                "Date",
                "Reservoirs Name",
                "Water Consumption Domestic",
                "Population",
                "No of Families",
                "No of Housing Units",
            ], // Rename headers in exported file.
        },
        (err, csv) => {
            downloadCSV(csv, "WaterConsumptionDomestic");
        }
    );
};

const WaterConsumptionDomesticList = (props) => (
    <List
        {...props}
        title="Water Consumption Domestic"
        exporter={exporter}
        perPage={25}
    >
        <Datagrid rowClick="show">
            <FunctionField label="Date" render={record => `${record.date.split('-')[0]} - ${record.date.split('-')[1]}`} />
            <TextField source="reservoir.name" label="Reservoir Name" />
            <NumberField source="water_consumption_domestic" />
            <NumberField source="population" />
            <NumberField source="no_of_families" />
            <NumberField source="no_of_housing_units" />
        </Datagrid>
    </List>
);

export default WaterConsumptionDomesticList;
