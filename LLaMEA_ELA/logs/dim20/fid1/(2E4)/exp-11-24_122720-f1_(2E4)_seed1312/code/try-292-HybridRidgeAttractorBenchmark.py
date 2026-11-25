import numpy as np

class HybridRidgeAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize adaptive ridge parameters
        self.ridge_strength = [1.5 + 0.5 * np.sin(i * np.pi / (dim + 1)) for i in range(dim)]
        self.coupling_factor = 0.3 + 0.2 * np.cos(dim * np.pi / 6)
        self.frequency_mod = [1.0 + 0.3 * np.sin(i * np.pi / (dim + 2)) for i in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Periodic trigonometric potential component
        trig_potential = 0
        for i in range(self.dim):
            freq = self.frequency_mod[i]
            # Multi-frequency trigonometric combination
            trig_potential += (np.sin(freq * x[i]) + 
                              0.5 * np.sin(2 * freq * x[i]) + 
                              0.3 * np.sin(3 * freq * x[i]))
        
        # Adaptive ridge structure with cross-dimensional coupling
        ridge_structure = 0
        for i in range(self.dim):
            strength = self.ridge_strength[i]
            # Ridge with adaptive curvature
            ridge = strength * (x[i]**2) * (1 + 0.2 * np.cos(x[i]))
            # Cross-dimensional interaction term
            coupling = 0
            for j in range(self.dim):
                if i != j:
                    coupling += np.sin((x[i] - x[j]) * (i + j + 1))
            ridge_structure += ridge + self.coupling_factor * coupling
            
        # Cross-dimensional interaction potentials
        cross_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Non-separable interaction between dimensions
                cross_interaction += np.sin((x[i] + x[j]) * (i + j + 1)) * np.cos((x[i] - x[j]) * (i + j + 1))
        
        # Combine all components with dimensionality scaling
        result = 2.0 * trig_potential + 1.5 * ridge_structure + 0.8 * cross_interaction
        
        # Add dimensionality-dependent scaling factor
        dim_factor = 1.0 + 0.1 * np.log(self.dim + 1) + 0.05 * np.sin(self.dim * np.pi / 3)
        result *= dim_factor
        
        return result