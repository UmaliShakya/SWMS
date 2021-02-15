import * as React from 'react';
import { useQueryWithStore, Loading, Error, Title as AdminTitle } from 'react-admin';
import { makeStyles } from '@material-ui/core/styles';
import {
    Card,
    CardContent,
    Typography,
    Accordion,
    AccordionSummary,
    AccordionDetails,
    List, ListItem, ListItemIcon, ListItemText
} from '@material-ui/core';
import ExpandMoreIcon from '@material-ui/icons/ExpandMore';
import FiberManualRecordIcon from '@material-ui/icons/FiberManualRecord';
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


const PaddyWaterDistributionPlan = (props) => {
    const classes = useStyles();

    const { data, loading, error } = useQueryWithStore({
        type: 'getOne',
        resource: 'paddy_water_distribution_plan',
        payload: { id: 1 }
    });

    if (loading) return <Loading loadingPrimary="Loading..." loadingSecondary="" />;
    if (error) return <Error />;
    if (!data) return null;

    return (
        <Card>
            <AdminTitle title={`Paddy Water Distribution Plan`} />
            <CardContent>
                <Title>{`Paddy Water Distribution Plan`}</Title>
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
                                <div className={classes.accordionRoot}>
                                    {n.data.map(n =>
                                        <Accordion key={n.tank}>
                                            <AccordionSummary
                                                expandIcon={<ExpandMoreIcon />}
                                                id={n.tank}
                                            >
                                                <Typography className={classes.accordionHeading}>{n.tank}</Typography>
                                            </AccordionSummary>
                                            <AccordionDetails>
                                                <List >
                                                    <ListItem button>
                                                        <ListItemIcon>
                                                            <FiberManualRecordIcon />
                                                        </ListItemIcon>
                                                        <ListItemText primary={`Tank - ${n.tank}`} />
                                                    </ListItem>
                                                    <ListItem button>
                                                        <ListItemIcon>
                                                            <FiberManualRecordIcon />
                                                        </ListItemIcon>
                                                        <ListItemText primary={`Full Capacity - ${n.full_capacity}`} />
                                                    </ListItem>
                                                    <ListItem button>
                                                        <ListItemIcon>
                                                            <FiberManualRecordIcon />
                                                        </ListItemIcon>
                                                        <ListItemText primary={`Water Needed - ${n.schema_water_needed}`} />
                                                    </ListItem>
                                                    <ListItem button>
                                                        <ListItemIcon>
                                                            <FiberManualRecordIcon />
                                                        </ListItemIcon>
                                                        <ListItemText primary={`Current Capacity - ${n.current_capacity}`} />
                                                    </ListItem>
                                                    <ListItem button>
                                                        <ListItemIcon>
                                                            <FiberManualRecordIcon />
                                                        </ListItemIcon>
                                                        <ListItemText primary={`From Nachchiduwa - ${n.from_nachchiduwa}`} />
                                                    </ListItem>
                                                    <ListItem button>
                                                        <ListItemIcon>
                                                            <FiberManualRecordIcon />
                                                        </ListItemIcon>
                                                        <ListItemText primary={`From Nuwara Wewa - ${n.from_nuwarawewa}`} />
                                                    </ListItem>
                                                    <ListItem button>
                                                        <ListItemIcon>
                                                            <FiberManualRecordIcon />
                                                        </ListItemIcon>
                                                        <ListItemText primary={`From Thisa Wewa - ${n.from_thisawewa}`} />
                                                    </ListItem>
                                                    <ListItem button>
                                                        <ListItemIcon>
                                                            <FiberManualRecordIcon />
                                                        </ListItemIcon>
                                                        <ListItemText primary={`From Thuruwila - ${n.from_thuruwila}`} />
                                                    </ListItem>
                                                </List>
                                            </AccordionDetails>
                                        </Accordion>
                                    )}
                                </div>
                            </AccordionDetails>
                        </Accordion>
                    )}
                </div>
            </CardContent>
        </Card>
    );
}

export default PaddyWaterDistributionPlan;