%% Model definition
N = 4;  % no of degrees of freedom (moving masses)
m = 1;  % mass [kg] OR [kg * m^2] for torsion
k = 1;  % stiffness [N/m] OR [Nm/rad]
c = 0.3;  % viscous damping [Ns/m] OR [Nms/rad]

%% Build system matrix
M = m * eye(N);
pairs = zeros(N);
for i=1:(N-1)
    pair = [1 -1;
            -1 1];
    pairs(i:i+1,i:i+1) = pairs(i:i+1,i:i+1) + pair;
end
K = k * pairs;
C = c * pairs;

% Fix the first mass in place by removing the degree of freedom
K = K(2:N, 2:N); C = C(2:N, 2:N); M = M(2:N, 2:N);
N = N-1;

global A;
A = [(-inv(M)*C) (-inv(M)*K);
     eye(N) zeros(N)];  % state matrix

%% Eigenvalues
[eigvec, eigval] = eig(K, M);   % undamped (generalised eigenvalue problem)
[complvec, complval] = eig(A);  % damped (complex solution)

%% Solve
modenum = 1;
z0 = zeros(2*N, 1); % x1'; x2'; x3'; x4'; x1; x2; x3; x4;
z0(1:N,:) = eigvec(:,modenum);  % initialise velocities from mode amplitude
angular_frequency = sqrt(eigval(modenum,modenum));
period = 2 * pi / angular_frequency;

sol = ode45(@model, [0 10], z0, odeset('MaxStep', 0.1));

%% Plot results
plot(sol.x, sol.y((N+1):(2*N),:))
title(['Mode number ', num2str(modenum), ', period ', num2str(period)])
xlabel('time [s]')
ylabel('mass position [m]')

%% Function definitions
% (have to be at the end of file)

function dz = model(~, z)
    global A;
    dz = A * z;
end