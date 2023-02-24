### Notes 23rd of February 
Aersapce control systems design problems are intrinsically multivariable, nonlinear, often associated with large model uncertainity and unstable dynamics.
The course aims at the following goals:
* to present classical results on nonlinear analysis;
* to provide a sound background on modern methods and tools for the
stability and performance analysis of linear and nonlinear systems;
* to cover robust analysis and design of SISO and MIMO linear time-
invariant (LTI) feedback control systems;
* to discuss basic ideas on gain-scheduled, adaptive, nonlinear
control systems design;
* to illustrate the above methods using detailed case studies.

### Basic control courses deal with
* SISO plants and controllers
* Analysis and design for:
    * nominal stability
    * nominal performance
* Restrictive settings in aerospace prolems
    * uncertainty matters, so robustness of stability and performance is an issue
    * the plant is MIMO, so methods for SISO analysis and design break down.

### Why is robust control harder?

* the response of uncertain plants is harder to characterise
*predicting stability and performance is more complicated

Why is it relevant?

* variation of dynamics over envelope
* modelling of aerodynamics and structural dynamics
* actuator/sensor dynamics
* delays due to implementation

### Why is robust control harder?

* MIMO plants exhibit more complex behaviour
* Performance requirements harder to formulate
* Design less intuitive than SISO case
Why is MIMO control relevant?
* Besides single-axis autopilots (such as the 1912 Sperry),
all FCS design problems are multivariable!


## Course programme 

### Intrduction
* Recap on linear systems and SISO analysis/design problems
* Motivation for advanced analysis and design methods;
* Introductory examples.

### 1. Systems theory - stability:
* Equilibria of nonlinear systems;
* Lyapunov stability for equilibria of nonlinear systems: definition
and examples;
* Stability for LTI systems: Lyapunov inequalities and equations.

Question addressed: for a nonlinear system, how do you define stability
of equilibria and how does this relate to stability of LTI systems? Are
there simple computational tests for LTI stability analysis?

### 1. Systems theory - performance:
* $H_2$ performance for linear systems;
* $H_∞$ performance for linear systems.

Question addressed: for a generic feedback system, how do you
formalize performance requirements in a way that is
* compatible with handling qualities requirements
* scalable from SISO to MIMO problems
* suitable for automated solution of design problems?

### 2. Linear SISO feedback systems - nominal design:
* Frequency-domain loop-shaping and sensitivity shaping;
* Time-domain state feedback and observer-based output-feedback
using classical methods:
    * eigenvalue assignment;
    * LQ control.

Question addressed: for a generic feedback system, how do
you formulate a control law design problem so that
* Nominal stability
* Nominal performance

### 3. Linear SISO feedback systems - robust analysis design:

* Uncertainty modelling in SISO systems;
* Robust stability analysis of SISO feedback systems;
* Nominal and robust performance analysis;
* Requirement specification;
* Robust design: unstructured and structured mixed sensitivity
synthesis.

Question addressed: for a generic feedback system, how do
you formulate a control law design problem so that
* Nominal and robust stability
* Nominal and robust performance
* Control law structure

### 4. Linear MIMO robust analysis and design:
* Introduction to MIMO linear systems;
* Nominal stability and performance in the MIMO case;
* Robust stability and performance in the MIMO case;
* MIMO robust design.

Question addressed: aerospace control problems are almost
always multivariable in nature. How can we scale up results for
SISO systems to the MIMO case?

### 5. Implementation issues:
* Modern anti-windup methods for MIMO control systems subject to
saturations;
* Implementation of gain-scheduled controllers.

Questions addressed:
* for a typical FCS, actuator saturations are a key issue; is it possible
to predict their role in the operation of the system?
* How can we take into account the dependence of the dynamics on
the flight condition in the implementation?

### 6. Aircraft flight control

* Introduction to flight control architectures (classical SAS+CAS; dynamic inversion, model following);
* Aircraft SAS and CAS design (longitudinal and lateral-directional).

### 7. Rotorcraft altitude control
* Modelling for attitude control;
* Rotorcraft SAS;
* Rotor state feedback.

### 8. Multirotor UAV attitude and position control
* PID cascade architecture;
* Inversion-based architectures (dynamic inversion and model following)

### 9. Structural control
* Active vibration control systems.


## Recap on LTI SISO systems
### Time domain:
* LTI systems in state space form: definitions and notation
* SISO first order systems: solutions of state and output equations, free and forced response
* SISO higher order systems: solutions of state and output
equations, free and forced response in formal analogy
* Matrix exponential and the response of higher order
systems
* Coordinate changes in state space and equivalent
representations
* Superposition principle
* Stability of LTI systems: definition via free motion and eigenvalues.

### Frequency domain:
* Transfer function definition and connection with impulse
response
* Definition of poles, zeros, gain and response type
* Poles and eigenvalues: cancellations
* Definition of frequency response operator and sinusoidal
response
* Minimum phase and nonminimum phase zeros.