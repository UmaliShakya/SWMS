import * as React from 'react';
import { Link, useParams } from 'react-router-dom';
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


const HouseSelect = () => {
    const classes = useStyles();

    let { id } = useParams();


    const { data, loading, error } = useQueryWithStore({
        type: 'getList',
        resource: 'homes',
        payload: {
            pagination: {
                page: 1,
                perPage: 25,
            },
            sort: {
                field: "home_name",
                order: "ASC",
            },
            filter: {
                q: '',
                reservoir_id: id
            },
        }
    });

    if (loading) return <Loading loadingPrimary="Loading..." loadingSecondary="" />;
    if (error) return <Error />;
    if (!data) return null;


    return (
        <>
            <AdminTitle title="Water Consumption Prediction - Select Home" />
            <div className={classes.root}>
                <List component="nav" >
                    {
                        data.map((n) =>
                            <ListItem button
                                key={n.id}
                                component={Link}
                                to={{
                                    pathname: `/domestic_water_consumption_prediction/${n.id}/`
                                }}
                            >
                                <ListItemIcon>
                                    <FiberManualRecordIcon color="secondary" />
                                </ListItemIcon>
                                <ListItemText primary={n.home_name} />
                            </ListItem>
                        )
                    }
                </List>
            </div>
        </>
    );
}

export default HouseSelect;