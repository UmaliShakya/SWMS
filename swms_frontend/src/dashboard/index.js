import * as React from "react";
import { Title as AdminTitle } from "react-admin";
import { Card, CardContent, Typography } from "@material-ui/core";

const Title = (props) => {
  return (
    <Typography component="h2" variant="h6" color="primary" gutterBottom>
      {props.children}
    </Typography>
  );
};

export default () => (
  <Card>
    <AdminTitle title="SWMS" />
    <CardContent>
      <Title>Dashboard</Title>
    </CardContent>
  </Card>
);
