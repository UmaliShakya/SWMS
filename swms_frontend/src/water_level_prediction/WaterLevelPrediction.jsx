import * as React from 'react';
import { useParams } from 'react-router-dom';
import { useQueryWithStore, Loading, Error, Title as AdminTitle } from 'react-admin';
import { makeStyles } from '@material-ui/core/styles';
import {
    Card,
    CardContent,
    Typography,
    Container,
    Grid,
    Paper,
    TableContainer,
    Table,
    TableBody,
    TableCell,
    TableHead,
    TableRow,
} from '@material-ui/core';
import moment from 'moment'
import {
    LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend,
    ResponsiveContainer,
} from "recharts";

const useStyles = makeStyles((theme) => ({
    root: {
        display: "flex",
    },
    title: {
        flexGrow: 1,
    },
    content: {
        flexGrow: 1,
    },
    container: {
        paddingTop: theme.spacing(4),
        paddingBottom: theme.spacing(4),
    },
    paper: {
        padding: theme.spacing(2),
        display: "flex",
        overflow: "auto",
        flexDirection: "column",
    },
    fixedHeight: {
        height: 240,
    },
    depositContext: {
        flex: 1,
    },
    table: {
        minWidth: 650,
    },
    tableRow: {
        backgroundColor: '#d1ff33'
    },
    titleSpacing: {
        margin: "20px"
    }
}));

const Title = (props) => {
    const classes = useStyles();

    return (
        <Typography component="h2" variant="h6" color="primary" className={classes.titleSpacing} gutterBottom>
            {props.children}
        </Typography>
    );
};

const Chart = ({ data_real, data_predicted, reservoir }) => {
    let series = []

    let data = []

    data_real.forEach((n) => {
        data.push({
            date: moment(n.date, 'YYYY MM DD').format('X'),
            value: n.water_level,
        })
    })

    series.push({
        name: "Real",
        data: data
    })

    data = []

    data_predicted.forEach((n) => {
        data.push({
            date: moment(n.date, 'YYYY MM DD').format('X'),
            value: n.water_level,
        })
    })

    series.push({
        name: "Predicted",
        data: data
    })

    return (
        <>
            <Title>{`Water Level Prediction - ${reservoir.name}`}</Title>
            <ResponsiveContainer width='95%' height={500}>
                <LineChart
                    margin={{
                        top: 16,
                        right: 16,
                        bottom: 0,
                        left: 24,
                    }}
                >
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis
                        dataKey="date"
                        domain={['auto', 'auto']}
                        name='Time'
                        tickFormatter={(unixTime) => moment.unix(unixTime).format('YYYY MMM')}
                        type="number"
                        allowDuplicatedCategory={false} />
                    <YAxis dataKey="value" name='Water Level' />
                    <Tooltip labelFormatter={(label) => moment.unix(label).format('YYYY MMM')} />
                    <Legend />
                    {series.map((s, i) => (
                        <Line
                            dataKey="value"
                            data={s.data}
                            name={s.name}
                            key={s.name}
                            strokeWidth={2}
                            stroke={(i === 0) ? '#00ff00' : '#ff0000'}
                            dot={i === 0 ? { stroke: '#00ff00', strokeWidth: 2 } : { stroke: '#ff0000', strokeWidth: 2 }}
                        />
                    ))}
                </LineChart>
            </ResponsiveContainer>
        </>
    );
};

const DataTable = ({ rows_real, rows_predicted, reservoir }) => {
    const classes = useStyles();

    return (
        <>
            <Title>{`Water Level Prediction - ${reservoir.name}`}</Title>
            <TableContainer >
                <Table size="small">
                    <TableHead>
                        <TableRow>
                            <TableCell>Date</TableCell>
                            <TableCell>Water Level</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {rows_real.map((row) => (
                            <TableRow key={row.id}>
                                <TableCell>{row.date}</TableCell>
                                <TableCell>{row.water_level}</TableCell>
                            </TableRow>
                        ))}
                        {rows_predicted.map((row) => (
                            <TableRow key={row.id} className={classes.tableRow}>
                                <TableCell>{row.date}</TableCell>
                                <TableCell>{row.water_level}</TableCell>
                            </TableRow>
                        ))}
                    </TableBody>
                </Table>
            </TableContainer>
        </>
    );
};


const WaterLevelPrediction = (props) => {
    const classes = useStyles();

    let { id } = useParams();

    const { data, loading, error } = useQueryWithStore({
        type: 'getOne',
        resource: 'water_level_prediction',
        payload: { id: id }
    });

    if (loading) return <Loading loadingPrimary="Loading..." loadingSecondary="" />;
    if (error) return <Error />;
    if (!data) return null;

    return (
        <Card>
            <AdminTitle title={`Water Level Prediction - ${data.reservoir.name}`} />
            <CardContent>
                <main className={classes.content}>
                    <div className={classes.appBarSpacer} />
                    <Container maxWidth="lg" className={classes.container}>
                        <Grid container spacing={3}>
                            <Grid item xs={12}>
                                <Paper >
                                    <Chart data_real={data.real} data_predicted={data.predicted} reservoir={data.reservoir} />
                                </Paper>
                            </Grid>
                            <Grid item xs={12}>
                                <Paper className={classes.paper}>
                                    <DataTable rows_real={data.real} rows_predicted={data.predicted} reservoir={data.reservoir} />
                                </Paper>
                            </Grid>
                        </Grid>
                    </Container>
                </main>
            </CardContent>
        </Card>
    );
}

export default WaterLevelPrediction;