import * as React from 'react';
import { Link } from 'react-router-dom';
import { useQueryWithStore, Loading, Error, Title as AdminTitle } from 'react-admin';
import { makeStyles } from '@material-ui/core/styles';
import { List, ListItem, ListItemIcon, ListItemText } from '@material-ui/core';
import FiberManualRecordIcon from '@material-ui/icons/FiberManualRecord';

const useStyles = makeStyles((theme) => ({
    root: {
        width: '100%',
        maxWidth: 360,
        backgroundColor: theme.palette.background.paper,
        margin: 3
    },
}));


const ReservoirsSelect = () => {
    const classes = useStyles();

    const { data, loading, error } = useQueryWithStore({
        type: 'getList',
        resource: 'reservoirs',
        payload: {
            pagination: {
                page: 1,
                perPage: 25,
            },
            sort: {
                field: "name",
                order: "ASC",
            },
            filter: {
                q: "",
            },
        }
    });

    if (loading) return <Loading loadingPrimary="Loading..." loadingSecondary="" />;
    if (error) return <Error />;
    if (!data) return null;

    return (
        <>
            <AdminTitle title="Water Consumption Prediction Domestic - Select Reservoir" />
            <div className={classes.root}>
                <List component="nav" >
                    {
                        data.map((n) =>
                            <ListItem button
                                key={n.id}
                                component={Link}
                                to={{
                                    pathname: `/water_consumption_prediction_domestic/${n.id}/`
                                }}
                            >
                                <ListItemIcon>
                                    <FiberManualRecordIcon color="secondary" />
                                </ListItemIcon>
                                <ListItemText primary={n.name} />
                            </ListItem>
                        )
                    }
                </List>
            </div>
        </>
    );
}

export default ReservoirsSelect;