import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine-wave interaction terms with frequency modulation
        chaotic_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 0.001)
                freq_mod = 1.0 + 0.3 * np.sin(0.5 * (x[i] + x[j]))
                chaotic_interaction += np.sin(freq_mod * dist) * np.cos(3.0 * (x[i] - x[j])) * np.exp(-0.1 * dist)
        
        # Adaptive elliptic conditioning with position-dependent scaling
        elliptic_condition = 0.0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.5 * np.cos(0.3 * x[i]) + 0.2 * np.sin(0.7 * x[i])
            elliptic_condition += scale_factor * (x[i] ** 2) * np.exp(-0.05 * np.abs(x[i]))
        
        # Dynamic gradient reversal with hyperbolic tangent modulation
        grad_reversal = 0.0
        for i in range(self.dim):
            mod = 1.0 + 0.4 * np.tanh(0.8 * x[i])
            grad_reversal += mod * np.sinh(2.0 * x[i]) * np.cos(1.5 * x[i])
        
        # Multi-scale fractal-like structure with recursive polynomial terms
        fractal_structure = 0.0
        for i in range(self.dim):
            term = x[i] ** 3
            for k in range(1, 4):
                term += 0.1 * np.sin(k * x[i]) * (x[i] ** (2 + k % 2))
            fractal_structure += term
        
        # Asymmetric basin with piecewise exponential and polynomial components
        asymmetric_basin = 0.0
        for i in range(self.dim):
            if x[i] < 0:
                asymmetric_basin += 0.4 * np.exp(0.5 * x[i]) + 0.1 * x[i]**3
            else:
                asymmetric_basin += 0.3 * x[i]**4 - 0.2 * np.exp(-0.3 * x[i])
        
        # Cross-term coupling with dynamic weight adjustment based on local curvature
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                curvature_i = np.cos(x[i]) + 0.5
                curvature_j = np.sin(x[j]) + 0.5
                weight = curvature_i * curvature_j
                cross_coupling += weight * (x[i]**2 + x[j]**2) * np.exp(-0.1 * np.abs(x[i] - x[j]))
        
        # Combined fitness value with dynamic weighting
        total = 0.3 * chaotic_interaction + 0.25 * elliptic_condition + 0.2 * grad_reversal + 0.15 * fractal_structure + 0.05 * asymmetric_basin + 0.05 * cross_coupling
        
        return total