import * as React from 'react';
import { useSelector } from 'react-redux';
import { DashboardMenuItem, MenuItemLink } from 'react-admin';
import OpacityIcon from "@material-ui/icons/Opacity";
import WavesIcon from '@material-ui/icons/Waves';
import TextureIcon from '@material-ui/icons/Texture';
import SpaIcon from '@material-ui/icons/Spa';
import AcUnitIcon from '@material-ui/icons/AcUnit';
import AllOutIcon from '@material-ui/icons/AllOut';
import BlurOnIcon from '@material-ui/icons/BlurOn';
import ContactlessIcon from '@material-ui/icons/Contactless';
import FlareIcon from '@material-ui/icons/Flare';

import Reservoirs from '../reservoirs'

const Menu = ({ onMenuClick, dense, logout }) => {

    const open = useSelector((state) => state.admin.ui.sidebarOpen);
    useSelector((state) => state.theme);

    return (
        <div>
           {/*  <DashboardMenuItem onClick={onMenuClick} sidebarIsOpen={open} /> */}

            <MenuItemLink
                to={`/reservoirs_select_water_level_prediction`}
                primaryText="Water Level Prediction"
                leftIcon={<WavesIcon />}
                onClick={onMenuClick}
                sidebarIsOpen={open}
                dense={dense}
            />

            <MenuItemLink
                to={`/reservoirs_select_water_consumption_prediction_domestic`}
                primaryText="Water Consumption Prediction Domestic"
                leftIcon={<TextureIcon />}
                onClick={onMenuClick}
                sidebarIsOpen={open}
                dense={dense}
            />

            <MenuItemLink
                to={`/reservoirs_select_water_consumption_prediction_paddy`}
                primaryText="Water Consumption Prediction Paddy"
                leftIcon={<BlurOnIcon />}
                onClick={onMenuClick}
                sidebarIsOpen={open}
                dense={dense}
            />

            <MenuItemLink
                to={`/reservoirs_select_domestic_water_consumption_prediction`}
                primaryText="Water Consumption Prediction per House"
                leftIcon={<AcUnitIcon />}
                onClick={onMenuClick}
                sidebarIsOpen={open}
                dense={dense}
            />

            <MenuItemLink
                to={`/reservoir_select_domestic_water_distribution_plan`}
                primaryText="Domestic Water Distribution Plan"
                leftIcon={<SpaIcon />}
                onClick={onMenuClick}
                sidebarIsOpen={open}
                dense={dense}
            />

            <MenuItemLink
                to={`/paddy_water_distribution_plan`}
                primaryText="Paddy Water Distribution Plan"
                leftIcon={<AllOutIcon />}
                onClick={onMenuClick}
                sidebarIsOpen={open}
                dense={dense}
            />

            <MenuItemLink
                to={`/reservoirs_select_water_level`}
                primaryText="Water Level"
                leftIcon={<OpacityIcon />}
                onClick={onMenuClick}
                sidebarIsOpen={open}
                dense={dense}
            />

            <MenuItemLink
                to={`/reservoirs_select_water_consumption_paddy`}
                primaryText="Water Consumption Paddy"
                leftIcon={<ContactlessIcon />}
                onClick={onMenuClick}
                sidebarIsOpen={open}
                dense={dense}
            />

            <MenuItemLink
                to={`/reservoirs_select_water_consumption_domestic`}
                primaryText="Water Consumption Domestic"
                leftIcon={<FlareIcon />}
                onClick={onMenuClick}
                sidebarIsOpen={open}
                dense={dense}
            />

            <MenuItemLink
                to={`/reservoirs`}
                primaryText="Reservoirs"
                leftIcon={<Reservoirs.icon />}
                onClick={onMenuClick}
                sidebarIsOpen={open}
                dense={dense}
            />
        </div>
    )
};

export default Menu;