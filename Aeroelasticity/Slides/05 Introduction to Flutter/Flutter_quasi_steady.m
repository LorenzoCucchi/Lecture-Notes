% 05738 -- STRUCTURAL DYNAMICS AND AEROELASTICITY
%   Prof. Giuseppe Quaranta
%   Flutter of the typical section using quasi steady approximation and 
%   state-space form
%   the basic equation for the TS are the adimensional equation
%   V is the flutter index spped, i.e. 2U/(c w_t)

clc
clear all
close all

mu = 10;
xt = 0.05;
rt = 0.5;

e = 0.5;
R = 0.5;
cla   = 2*pi;

M = [1  xt;  
     xt rt^2];

Ks = [R^2  0;
      0    rt^2];

Ca = cla/(mu*pi)*[1  0;
                  -e  0];
              
Ka = cla/(mu*pi)* [0   1;
                   0  -e];
               
V = 0:0.01:1.8;

e2   = zeros(4,length(V));
ev  = zeros(4,4,length(V));


for i = 1:length(V)
    A = [zeros(2,2),          eye(2);
        -M\(Ks+V(i)^2*Ka),  -M\(V(i)*Ca)  ];
    [ev1, e1] = eig(A);
    ep(:,i) = diag(e1);
    ev(:,:,i) = ev1;
    
end


figure(1);
plot(real(ep(1,:)), imag(ep(1,:)), 'bx');
hold on;
plot(real(ep(1,1)), imag(ep(1,1)), 'rx','MarkerSize', 10);
plot(real(ep(2,:)), imag(ep(2,:)), 'bx');
plot(real(ep(2,1)), imag(ep(2,1)), 'rx','MarkerSize', 10);
plot(real(ep(3,:)), imag(ep(3,:)), 'bx');
plot(real(ep(3,1)), imag(ep(3,1)), 'rx','MarkerSize', 10);
plot(real(ep(4,:)), imag(ep(4,:)), 'bx');
plot(real(ep(4,1)), imag(ep(4,1)), 'rx','MarkerSize', 10);
grid on;
xlabel('Real');
ylabel('Imaginary');


figure(2);
plot(V, imag(ep(1,:)), 'bx');
hold on;
plot(V, imag(ep(2,:)), 'bx');
plot(V, imag(ep(3,:)), 'bx');
plot(V, imag(ep(4,:)), 'bx');
grid on;
xlabel('V');
ylabel('\omega');


figure(3);
plot(V, -real(ep(1,:))./abs(ep(1,:)), 'bx');
hold on;
plot(V, -real(ep(2,:))./abs(ep(2,:)), 'bx');
plot(V, -real(ep(3,:))./abs(ep(3,:)), 'bx');
plot(V, -real(ep(4,:))./abs(ep(4,:)), 'bx');
grid on;
xlabel('V');
ylabel('\xi');

% figure (4);
% plot(V, abs(squeeze(ev(1,1,:)./ev(2,1,:))), 'bx');
% hold on;
% plot(V, abs(squeeze(ev(1,2,:)./ev(2,2,:))), 'rx');
% xlabel('V');
% ylabel('|(h/b)/\theta|');
% 
% figure (5);
% plot(V, phase(squeeze(ev(1,1,:)./ev(2,1,:)))/pi*180, 'bx');
% hold on;
% plot(V, phase(squeeze(ev(1,2,:)./ev(2,2,:)))/pi*180, 'rx');
% xlabel('V');
% ylabel('arg((h/b)/\theta), deg.');
