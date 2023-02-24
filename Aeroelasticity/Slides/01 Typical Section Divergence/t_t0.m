    % 05738 -- STRUCTURAL DYNAMICS AND AEROELASTICITY
%   Prof. Giuseppe Quaranta
%   Static Aeroelasticity of Typical Section
%   Plot of the ratio of between the rigid torsion and the aeroelastic
%   torsion

% ratio of dynamic pressure on diveregence dynamic pressure [0,1]
 q_qD = 0:0.01:1;

 y = 1*(1./(1-q_qD));
 semilogy(q_qD,y, '-b','LineWidth', 1.5);
 hold on;
 grid on;
 U_UD = 0:0.01:1;
 y = 1*(1./(1-(U_UD).^2));
 semilogy(U_UD,y, '-r','LineWidth', 1.5); 
 xlabel('q/q_D U/U_D');
 ylabel('\theta/\theta_0');
 legend('f(q/q_D)', 'f(U/U_D)');