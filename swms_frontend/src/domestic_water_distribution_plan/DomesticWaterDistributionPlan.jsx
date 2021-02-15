import * as React from 'react';
import { useParams } from 'react-router-dom';
import { useQueryWithStore, Loading, Error, Title as AdminTitle } from 'react-admin';
import { makeStyles } from '@material-ui/core/styles';
import {
    Card,
    CardContent,
    Typography,
    TableContainer,
    Table,
    TableBody,
    TableCell,
    TableHead,
    TableRow,
    Accordion,
    AccordionSummary,
    AccordionDetails
} from '@material-ui/core';
import ExpandMoreIcon from '@material-ui/icons/ExpandMore';
import moment from 'moment'

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
    },
    accordionRoot: {
        width: '100%',
    },
    accordionHeading: {
        fontSize: theme.typography.pxToRem(15),
        fontWeight: theme.typography.fontWeightRegular,
    },
}));

const Title = (props) => {
    const classes = useStyles();

    return (
        <Typography component="h2" variant="h6" color="primary" className={classes.titleSpacing} gutterBottom>
            {props.children}
        </Typography>
    );
};

const DataTable = ({ data }) => {

    return (
        <>
            <TableContainer >
                <Table size="small">
                    <TableHead>
                        <TableRow>
                            <TableCell>House</TableCell>
                            <TableCell>Recommended Value</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {data.map((row) => (
                            <TableRow key={row.home.id}>
                                <TableCell>{row.home.home_name}</TableCell>
                                <TableCell>{row.value}</TableCell>
                            </TableRow>
                        ))}
                    </TableBody>
                </Table>
            </TableContainer>
        </>
    );
};


const DomesticWaterDistributionPlan = (props) => {
    const classes = useStyles();

    let { id } = useParams();

    const { data, loading, error } = useQueryWithStore({
        type: 'getOne',
        resource: 'domestic_water_distribution_plan',
        payload: { id: id }
    });

    if (loading) return <Loading loadingPrimary="Loading..." loadingSecondary="" />;
    if (error) return <Error />;
    if (!data) return null;

    return (
        <Card>
            <AdminTitle title={`Domestic Water Distribution Plan`} />
            <CardContent>
                <Title>{`Domestic Water Distribution Plan`}</Title>
                <div className={classes.accordionRoot}>
                    {data.map(n =>
                        <Accordion key={n.date}>
                            <AccordionSummary
                                expandIcon={<ExpandMoreIcon />}
                                id={n.date}
                            >
                                <Typography className={classes.accordionHeading}>{moment(n.date).format('YYYY MMMM')}</Typography>
                            </AccordionSummary>
                            <AccordionDetails>
                                <DataTable data={n.data} />
                            </AccordionDetails>
                        </Accordion>
                    )}
                </div>
            </CardContent>
        </Card>
    );
}

export default DomesticWaterDistributionPlan;