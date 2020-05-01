%--------------------------------------------------------------------------
% Evaluates the Cauchy stress tensor for material type 1.
%--------------------------------------------------------------------------
function Cauchy = stress9(kinematics,properties,cons)
mu              = properties(2);
lambda          = properties(3);
J               = kinematics.J;
b               = kinematics.b;
K = lambda + 2* mu/3;
K/mu;
E = 1/2*(kinematics.F'*kinematics.F - cons.I);
S = lambda * trace(E) * cons.I + 2 * mu * E;
Cauchy          = 1/J*kinematics.F*S*kinematics.F';
end