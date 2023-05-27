# Optimized-control-strategy-CCC-TU-Delft-
Control strategy for Venetian blinds in an event space with fully glazed facades using model-based optimization.
[Developed within a Master thesis in TU Delft, based on the case study of the Co-Creation Center, in The Green Village.]

The proposed control strategy of the blinds for indoor visual comfort is steered by an optimization process in Grasshopper. The optimization employed here is based on the Radial Basis Function Optimization (RBFOpt) algorithm, which can be performed by Grasshopper's component Opossum (OPtimizatiOn Solver with SUrrogate Models). 

The aim of the optimized control system is  the regulation of the amount of daylight entry, balanced by glare risks. The former is expressed by the average horizontal illuminance on the workplane (Ewp) calculated at a sensor grid 0.85 m above the floor, whereas the latter are evaluated by the maximum value of cylindrical illuminance (Ecyl) between nine viewpoints evenly distributed on the floorplan. The priority of the control system is occupants' visual comfort avoiding glare.

The variables of the optimization are 8; blinds' increments and angles for each of the four facades. At the beginning, the designer should select the appropriate mode / space usage (presentation, meeting, workshop), depending on the event that takes place in the building. The optimization process is constrained by the limits of Ewp and Ecyl. In particular, to ensure an adequate quantity of light in the space, Ewp should be more than 300 lx, 500 lx and 750 lx for presentation, meeting and workshop respectively. At the same time, only imperceptible glare is allowed by employing the upper threshold of 1400 lx for Ecyl.

For the case of meetings and workshops, the aim is to prevent noticeable or disturbing glare, while maximizing the amount of daylight so as to achieve low energy demands for electric lighting. Since visual comfort is prioritized and only imperceptible glare is allowed, the largest amount of daylight entry can be achieved only when Ecyl has a value very close to 1400 lx, but still lower than this threshold. In this manner, noticeable glare is prevented, while the maximum possible Ewp is accomplished, trying to minimize energy demands for electric lighting. 

On the contrary, for the presentation scenario, apart from preventing glare, the aim is to allow for small amounts of daylight entry, enough to meet the 300 lx requirement. This is because, during a presentation, the light levels should be low, but sufficient to write down notes. In this case, the two targets are non-competing. The aim now is to minimize daylight entry until Ewp has a value very close to 300 lx, but still higher than this limit. At the same time, a very low Ecyl value is accomplished (< 1400 lx), ensuring the occurrence of only imperceptible glare.

The optimization algorithm is basically described by a single objective function, where Ecyl is multiplied by a penalty factor. The calculation of the objective function is performed within the Python script given in this repo. The inputs of the python script are the activity mode (presentation, meeting, workshop), the lists with the values of the 8 variables (blinds' increments and angles for each facade) tested by the optimization algorithm in every iteration and the lists with the corresponding values of Ewp and Ecyl.

During workshops and meetings, the control system tries to maximize the objective function, whereas during presentations its minimization is targeted. The penalty is derived from the optimization constraints and is applied to enforce the algorithm to find values for Ewp and Ecyl within their limits. The objective function is harder penalized when Ecyl is above 1400 lx, as glare prevention is prioritized.

More details can be found in the Master thesis "Control strategy for Venetian blinds and electric lighting in an event space with fully glazed facades", available at http://repository.tudelft.nl/.
