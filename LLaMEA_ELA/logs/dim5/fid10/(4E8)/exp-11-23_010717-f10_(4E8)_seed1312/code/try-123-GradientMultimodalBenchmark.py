import numpy as np

class GradientMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Radial symmetry term with enhanced adaptive curvature
        r = np.sqrt(np.sum(x**2))
        radial_term = 0.5 * r**2 * (1.0 + 0.4 * np.sin(6.0 * r) + 0.2 * np.cos(3.0 * r))
        
        # Enhanced saddle-point dominance with multiple competing optima
        saddle_terms = 0.0
        for i in range(self.dim):
            saddle_terms += (1.2 * x[i]**2 * np.cos(4.0 * x[i]) + 
                           0.7 * x[i]**4 * np.sin(3.0 * x[i]) + 
                           0.35 * np.sin(8.0 * x[i]) * np.cos(6.0 * x[i]) +
                           0.12 * x[i]**6 * np.cos(2.0 * x[i]))
        
        # Improved adaptive curvature term with stronger condition number variation
        curvature = 0.0
        for i in range(self.dim):
            # Stronger varying curvature based on dimension index
            curv = 1.6 + 0.9 * np.sin(0.4 * i) * np.cos(0.3 * i)
            curvature += curv * x[i]**2 * (1.0 + 0.35 * np.cos(5.0 * x[i]) + 0.12 * np.sin(7.0 * x[i]))
        
        # Enhanced cross-dimensional coupling with non-uniform interaction strengths
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Non-uniform interaction strength with dimension-dependent variation
                strength = 0.45 + 0.35 * np.sin(0.25 * (i + j)) * np.cos(0.1 * (i - j))
                coupling += strength * x[i] * x[j] * np.sin(3.5 * (x[i] + x[j]) + 0.55 * np.cos(x[i] - x[j]))
        
        # Enhanced multi-modal component with increased local minima density
        modal_term = 0.0
        for i in range(self.dim):
            modal_term += (4.2 * np.sin(2.0 * x[i]) * np.cos(3.0 * x[i]) + 
                          3.2 * np.sin(6.0 * x[i])**2 + 
                          2.7 * np.cos(5.0 * x[i])**2 +
                          1.2 * np.sin(9.0 * x[i]) * np.cos(4.0 * x[i]))
        
        # Global scaling factor with enhanced non-linearity
        scale = 1.0 + 0.22 * np.sum(np.sin(x)**3) + 0.11 * np.sum(np.cos(x)**2)
        
        # Improved penalty for being far from origin
        penalty = 0.11 * r**3 + 0.06 * r**4
        
        return scale * (radial_term + saddle_terms + curvature + coupling + modal_term) + penalty