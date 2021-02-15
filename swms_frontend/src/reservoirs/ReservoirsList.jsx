import * as React from "react";
import {
  List,
  Datagrid,
  TextField,
  NumberField,
  downloadCSV,
  Filter,
  TextInput,
} from "react-admin";
import jsonExport from "jsonexport/dist";

const exporter = (reservoirs) => {
  const reservoirsForExport = reservoirs.map((reservoir) => {
    const { id, created_at, updated_at, ...reservoirForExport } = reservoir;
    return reservoirForExport;
  });

  jsonExport(
    reservoirsForExport,
    {
      headers: [
        "name",
        "division",
        "capacity",
        "catchment_area",
        "surface_area",
        "description",
      ], // Field order in exported file.
      rename: [
        "Name",
        "Division",
        "Capacity",
        "Catchment_area",
        "Surface_area",
        "Description",
      ], // Rename headers in exported file.
    },
    (err, csv) => {
      downloadCSV(csv, "Reservoirs");
    }
  );
};

const ReservoirsFilter = (props) => (
  <Filter {...props}>
    <TextInput label="Search" source="q" alwaysOn />
    {/* TODO : Add autocomplete. */}
    <TextInput label="Division" source="division" />
  </Filter>
);

const ReservoirsList = (props) => (
  <List
    {...props}
    title="List of Reservoirs"
    exporter={exporter}
    filters={<ReservoirsFilter />}
    perPage={25}
  >
    <Datagrid rowClick="show">
      <TextField source="name" />
      <TextField source="division" />
      <NumberField source="capacity" />
      <NumberField source="catchment_area" />
      <NumberField source="surface_area" />
    </Datagrid>
  </List>
);

export default ReservoirsList;
