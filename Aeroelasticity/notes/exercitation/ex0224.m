close all
clear all
clc

N = 4;
m = 1;
k = 1;
c = 0.3;

M = m*eye(N);
pairs = zeros(N);

for i = 1:N-1
    pair = [1,-1;-1,1];
    pairs(i:(i+1),i:(i+1))=pairs(i:i+1,i:i+1)+pair;
end

K =k*pairs;

[eigevec, eigeval]=eig(K,M);

global A;

A=[zeros(N) -inv(M)*K;
    eye(N) zeros(N)];

z0 = zeros(2*N,1);
z0(1)=1.0;
z0(N) = -1.0;
%z0(1:N)=eigevec;

sol = ode45(@model, [0 10], z0, odeset('MaxStep',0.1));

plot(sol.x, sol.y(N+1:N*2,:))

function dz = model(t,z)
    global A;
    dz = A*z;
end
