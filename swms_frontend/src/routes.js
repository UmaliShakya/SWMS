import * as React from "react";
import { Route } from "react-router-dom";

import ReservoirsSelectWaterLevel from "./water_level/ReservoirsSelect";
import ReservoirsSelectWaterConsumptionPaddy from "./water_consumption_paddy/ReservoirsSelect";
import ReservoirsSelectWaterConsumptionDomestic from "./water_consumption_domestic/ReservoirsSelect";
import ReservoirsSelectWaterLevelPrediction from "./water_level_prediction/ReservoirsSelect";
import WaterLevelPrediction from "./water_level_prediction/WaterLevelPrediction";
import ReservoirsSelectWaterConsumptionPredictionDomestic from "./water_consumption_prediction_domestic/ReservoirsSelect";
import WaterConsumptionPredictionDomestic from "./water_consumption_prediction_domestic/WaterConsumptionPredictionDomestic";
import ReservoirsSelectWaterConsumptionPredictionPaddy from "./water_consumption_prediction_paddy/ReservoirsSelect";
import WaterConsumptionPredictionPaddy from "./water_consumption_prediction_paddy/WaterConsumptionPredictionPaddy";
import ReservoirsSelectDomesticWaterConsumptionPrediction from "./domestic_water_consumption_prediction/ReservoirsSelect";
import HouseSelectDomesticWaterConsumptionPrediction from "./domestic_water_consumption_prediction/HouseSelect";
import DomesticWaterConsumptionPrediction from "./domestic_water_consumption_prediction/DomesticWaterConsumptionPrediction";
import ReservoirsSelectDomesticWaterDistributionPlan from "./domestic_water_distribution_plan/ReservoirsSelect";
import DomesticWaterDistributionPlan from "./domestic_water_distribution_plan/DomesticWaterDistributionPlan";
import PaddyWaterDistributionPlan from "./paddy_water_distribution_plan/PaddyWaterDistributionPlan";

export default [
  <Route
    exact
    path="/reservoirs_select_water_level_prediction"
    component={ReservoirsSelectWaterLevelPrediction}
  />,
  <Route
    exact
    path="/water_level_prediction/:id"
    component={WaterLevelPrediction}
  />,
  <Route
    exact
    path="/reservoirs_select_water_consumption_prediction_domestic"
    component={ReservoirsSelectWaterConsumptionPredictionDomestic}
  />,
  <Route
    exact
    path="/water_consumption_prediction_domestic/:id"
    component={WaterConsumptionPredictionDomestic}
  />,
  <Route
    exact
    path="/reservoirs_select_water_consumption_prediction_paddy"
    component={ReservoirsSelectWaterConsumptionPredictionPaddy}
  />,
  <Route
    exact
    path="/water_consumption_prediction_paddy/:id"
    component={WaterConsumptionPredictionPaddy}
  />,
  <Route
    exact
    path="/reservoirs_select_domestic_water_consumption_prediction"
    component={ReservoirsSelectDomesticWaterConsumptionPrediction}
  />,
  <Route
    exact
    path="/reservoirs_select_domestic_water_consumption_prediction/:id"
    component={HouseSelectDomesticWaterConsumptionPrediction}
  />,
  <Route
    exact
    path="/domestic_water_consumption_prediction/:id"
    component={DomesticWaterConsumptionPrediction}
  />,
  <Route
    exact
    path="/reservoir_select_domestic_water_distribution_plan"
    component={ReservoirsSelectDomesticWaterDistributionPlan}
  />,
  <Route
    exact
    path="/domestic_water_distribution_plan/:id"
    component={DomesticWaterDistributionPlan}
  />,
  <Route
    exact
    path="/paddy_water_distribution_plan"
    component={PaddyWaterDistributionPlan}
  />,
  <Route
    exact
    path="/reservoirs_select_water_level"
    component={ReservoirsSelectWaterLevel}
  />,
  <Route
    exact
    path="/reservoirs_select_water_consumption_paddy"
    component={ReservoirsSelectWaterConsumptionPaddy}
  />,
  <Route
    exact
    path="/reservoirs_select_water_consumption_domestic"
    component={ReservoirsSelectWaterConsumptionDomestic}
  />,
];
