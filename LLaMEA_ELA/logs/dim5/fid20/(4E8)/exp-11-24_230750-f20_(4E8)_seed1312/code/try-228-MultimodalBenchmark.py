import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like recursive tangent interactions with self-similar structures
        fractal_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited cross-dimensionality
                fractal_interaction += np.tan(x[i] * x[j]) * np.exp(-0.1 * np.abs(x[i] - x[j]))
        
        # Enhanced polynomial coupling with chaotic modulation and dynamic scaling
        poly_coupling = 0.0
        for i in range(self.dim):
            poly_coupling += (x[i]**6 - 3*x[i]**4 + 3*x[i]**2 - 1) * np.sin(5 * x[i]) * np.cos(3 * x[i])
        
        # Dynamic sinusoidal modulation with fractal-like self-similarity and modified frequencies
        sin_modulation = 0.0
        for scale in [0.2, 0.5, 1.0, 1.5]:
            sin_modulation += np.sum(np.sin(scale * x) * np.cos(scale * x) * 
                                   np.exp(-0.15 * np.abs(x)) * np.sin(0.3 * np.pi * x))
        
        # Adaptive penalty corridors with logarithmic scaling and multi-scale penalties
        penalty_corridors = 0.0
        for i in range(self.dim):
            dist_from_center = np.abs(x[i])
            penalty_corridors += (dist_from_center - 4.0)**2 * np.log(1 + 0.5 * dist_from_center)
        
        # Chaotic component using modified logistic map with time-varying parameter and memory effects
        chaotic = 0.0
        r_values = [3.8 + 0.2 * np.sin(i * 0.7) for i in range(self.dim)]
        for i in range(self.dim):
            if i == 0:
                chaotic += x[i] * (r_values[i] * (1 - x[i]))
            else:
                chaotic += x[i] * (r_values[i] * (1 - 0.5 * x[i-1] - 0.5 * x[i]))
        
        # Radial basis function with adaptive widths, multi-scale interactions and phase modulation
        rbf = 0.0
        centers = np.linspace(-4.5, 4.5, 9)
        for center in centers:
            dist = np.sum((x - center) ** 2)
            width = 0.3 + 0.7 * np.sin(center * 0.5)
            rbf += np.exp(-0.3 * dist / (width**2)) * np.cos(3 * np.pi * dist) * np.sin(0.2 * dist)
        
        # Cross-dimensional interaction term with nested complexity and dynamic coupling
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interaction += np.sin(x[i] * x[j]) * np.exp(-0.2 * (x[i] - x[j])**2) * np.cos(0.5 * x[i])
        
        # Basin structure with logarithmic barrier and multi-scale attraction
        basin_structure = 0.0
        for i in range(self.dim):
            dist_to_zero = np.abs(x[i])
            basin_structure += np.log(1 + 0.2 * dist_to_zero) * np.sin(2 * x[i])
        
        # Combined fitness with adjusted weights for enhanced discrimination and complexity
        return 0.25 * fractal_interaction + 0.2 * poly_coupling + 0.18 * sin_modulation + 0.15 * penalty_corridors + 0.12 * chaotic + 0.08 * rbf + 0.07 * cross_interaction + 0.05 * basin_structure