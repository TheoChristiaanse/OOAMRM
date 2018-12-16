# OOAMRM

An object orientated version of a 1D AMR simulation.


## Class structure

- Material class
> - Specific Heat
> - Magnetization  
> - Density
> - Conduction

- Regenerator class 
> Take several materials
> - Structure of the regenerator
> - Closure relationships
> - Geometry of the regenerator

- Device class
> Regenerator lives in a device
> - Magnetic Field
> - Flow Wave Form
> - Casing leaks

- Simulation class
> Simulation class takes a device and resolves the device performance from the features