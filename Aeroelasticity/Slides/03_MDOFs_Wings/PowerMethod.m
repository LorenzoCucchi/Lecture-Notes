% 05738 -- STRUCTURAL DYNAMICS AND AEROELASTICITY
%   Prof. Giuseppe Quaranta
%   power method to compute eigenvalues
%   and eigenvectors

format long e
kmax = 20;
A = 10*rand(1)*rand(5);
z0 = rand(5,1);
z0 = z0/norm(z0);
disp(A);
disp(eig(A));
disp(z0);

for k = 1: kmax
    z = A*z0;
    lambda = (z'*A*z)/norm(z)^2;
    disp(['Step: ', num2str(k), ' Eig: ', num2str(lambda, '%14.10f\n')]);
    z0 = z;
end
    
