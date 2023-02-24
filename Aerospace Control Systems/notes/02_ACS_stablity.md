# Aerospace Control Systems

## Theory – stability

Lyapunov theory: autonomous systems
* Equilibria and stability
* Lyapunov’s stability theorem
* LaSalle invariance principle
* Stability of linear time-invariant systems

### Equilibria and their stability

For the autonomous system
$$
\begin{equation}
\dot x = f(x)
\end{equation}
$$

for which an equilibrium is known

$$
\begin{equation}
\bar x: \ 0=f(\bar x)
\end{equation}
$$

we first want to recall the definition of stability of the equilibrium and then characterise and study such property.

Assume for semplicity that $\bar x=0$\
Then  the equilibrium is:
* Stable, if for all $\epsilon>0$ there exists $\delta = \delta(\epsilon)>0$ such that
$||x(0)||<\delta\Rightarrow||x(t)||<\epsilon, \ \forall t>0$
* Unstable, if is not stable
* Asymptotically stable(AS), if it is stable and if $\delta$ can be chose such that\
$||x(0)||<\delta \Rightarrow \lim_{t \to \infty}x(t)=0$

### Stability and derivation

Let $x=0$ an equilibrium for the nonlinear system\
$$
\begin{equation}
\dot x = f(x)
\end{equation}
$$

and consider

$$
\begin{equation}
A=\frac{\partial f(x)}{\partial x}\Big|_{x=0}
\end{equation}
$$

We have that:
* $x=0$ is an AS equilibrium if $Re\ \lambda_i<0$ for all the eigenvalues of A
* $x=0$ is an unstable equilibrium if $Re\ \lambda_i>0$ for at least one of the eigenvalues of A.

## Example: the pendulum
State equations for a pendulum (mass m, length l) with friction 

$$
\begin{equation}
\begin{cases}
\dot x_1 = x_2\\ 
\dot x_2 = -\frac{g}{l}\sin{x_1} - \frac{k}{m}x_2
\end{cases}
\end{equation}
$$


Linearisation in $x=0$

$$
\begin{equation}
\begin{cases}
\dot\delta x_1 = \delta x_2\\ 
\dot\delta x_2 = -\frac{g}{l}\delta x_1 - \frac{k}{m}\delta x_2
\end{cases}
\end{equation}
$$

In this case the eigenvalues have negative real part so $x=0$ is AS.

### Without friction
State equations for a pendulum without friction

$$
\begin{equation}
\begin{cases}
\dot x_1 = x_2\\ 
\dot x_2 = -\frac{g}{l}\sin{x_1}
\end{cases}
\end{equation}
$$

Linearisation in $x=0$

$$
\begin{equation}
\begin{cases}
\dot\delta x_1 = \delta x_2\\ 
\dot\delta x_2 = -\frac{g}{l}\delta x_1
\end{cases}
\end{equation}
$$

The eigenvalues are imaginary, so the linearisation criterion does not allow us to conclude about the stability of the equilibrium.

 **Energy base analysis of the system:**

 the total mechanical energy of the pendulum is give by
 $$
 \begin{equation}
 E(x)=\frac{g}{l}(1-\cos(x_1))+\frac{1}{2}x_2^2
 \end{equation}
 $$

 (reference for the potential energy chosen such that $E(0)=0$).

<br />

### **Total mechanical energy** 
<br />
<image src="images/pendulum1.png">
<image src="images/pendulum_contour.png">

<br />

#### **Without friction:**

the system is conservative, so E(x)=c, c function of the initial condition (and dE/dt=0)

E(x)=c is a closed curve enclosing x=0

Therefore, for sufficiently small c x remains arbitrarily close to zero.

Hence, x=0 is a stable equilibrium.

#### **With friction:**

the system dissipates energy, so E decreases and
dE(t)/dt<0.

E keeps decreasing as long as the pendulum is moving.

So x tends to zero.

Hence x=0 is an AS equilibrium.

### **Lyapunov functions**

* The stability of the pendulum’s x=0 equilibrium can be
studied using an energy-based approach.
* Lyapunov proved that more general functions can be
used to this purpose.
* Consider an energy-like continuously differentiable
function V(x) and compute its derivative along the
trajectories of the system:

$$\begin{equation}
\dot V(x) = \sum_{i=1}^n\frac{\partial V}{\partial x_i}\dot x_i=\sum_{i=1}^n\frac{\partial V}{\partial x_i}f_i(x)
\end{equation}
$$

Key observation:
if $ \dot V(x)$ is negative along the soluton of the state equation, then $V(x)$ is decreasing.

Therefore, if we can construct a function V(x) with this property, we have a tool to carry out a stability analysis.

### **Lyapunov's stability theorem**
**Theorem:** let $x=0$ an equilibrium of the sistem and D a domain which includes $x=0$. Then given a smoot function $V:D\rightarrow R$ such that:

$$
\begin{equation}
\begin{cases}
V(0)=0, \ V(x)>0\ in \ D, \quad x \neq 0\\ 
\dot V(x) \le 0 \quad in \; D
\end{cases}
\end{equation}
$$

then the equilibrium is stable.\
If in addition

$$
\begin{equation}
\dot V(x) <0 \quad in \; D, \quad x \neq 0
\end{equation}
$$

then the equilibrium is asymptotically stable.


#### **Proof: stability**

Given $\epsilon >0$, choose $r \in (0,\epsilon]$:

$$
\begin{equation}
B_r=\{ x\in \R^n:||x|| \le r\} \in \ D\end{equation}
$$

Let

$$
\begin{equation}
\alpha=\min_{||x||=r}V(x), \quad (\alpha>0)
\end{equation}
$$

choose $\beta \in (0,\alpha)$ and define

$$
\begin{equation}
\Omega_{\beta}=\{x\in B_r: V(x)\le \beta \}
\end{equation}
$$

NOTE: $\Omega_{\beta}$ is a closed and bounded set, hence it is a compact set.

Note that since $\dot V(x(t))\le 0$\
then

$$
\begin{equation}
\dot V(x(t))\le V(x(0)) \quad \forall t\geq 0
\end{equation} 
$$
and if $ x(0)\in\Omega_{\beta} $ then we have $x(t)\in\Omega_{beta} \quad \forall t\geq 0$.

Furthemore, V(x) is continuous and $V(0)=0$ so

$$
\begin{equation}
\exists\delta:\quad ||x||\leq\delta\Rightarrow V(x)<\beta
\end{equation}
$$

and therefore

$$
\begin{equation}
B_{\delta}\subset\Omega_{\beta}\subset B_r
\end{equation}
$$

Then we have 

$$
\begin{equation}
x(0)\in B_{\delta}\Rightarrow x(0)\in \Omega_{\beta} \Rightarrow x(t)\in \Omega_{\beta}\Rightarrow x(t)\in B_r
\end{equation}
$$

and this implies that

$$
\begin{equation}
||x(0)||\leq\delta\Rightarrow||x(t)||<r\leq\epsilon \quad \forall t \geq 0
\end{equation}
$$

and so the equilibrium is stable.

#### **Proof: asymptotic stability**
We need to show that $x(t)\rightarrow 0,t\rightarrow \infty$, or equivalently

$$
\begin{equation}
\forall a>0 \quad \exists\Tau>0:||x(t)||<a \quad \forall t>\Tau
\end{equation}
$$

To this purpose it's sufficient to show that

$V(x(t))\rightarrow0,t\rightarrow\infty$.\
$V(x(t))$ monotonically decreasing, bounded from below, so\
$V(x(t))\rightarrow c,\ c\geq0, \ t\rightarrow\infty$.

Assume that $c>0.$\
Then there exists $d>0$ such that $B_d\subset\Omega_c$\
and so $x(t)$ remains outside $B_d$ for all $t\geq 0.$

Note now that

$$
\begin{equation}
V(x(t))=V(x(0))+\int_0^t\dot V(x(\tau))d\tau\leq V(x(0))-\gamma t
\end{equation}
$$

where

$$
\begin{equation}
-\gamma = \max_{d\leq||x||\leq r}\dot V(x)
\end{equation}
$$
Since the right hand side becomes negative for suff. large t, then c cannot be positive.

$ $

#### **Quadratic Lyapunov Functions**

Quadratic functions are often chosen as candidate
Lyapunov functions:
$$
\begin{equation}
V(x) = x^TPx=\sum_{i=1}^n\sum_{j=1}^np_{ij}x_ix_j, \quad P=P^T
\end{equation}
$$
The function is positive (semi)definite iff matrix P is, and this condition is easy to check.

$ $

#### **Pros and Cons of Lyapunov Theorem**
* Enables stability analysis without the need to solve the
state equation
* Does not provide criteria for the choice of V(x) (though
physics usually help);
* The stability condition is only sufficient.


