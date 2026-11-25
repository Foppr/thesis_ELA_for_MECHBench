import numpy as np

class GradientMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Radial symmetry term with adaptive curvature
        r = np.sqrt(np.sum(x**2))
        radial_term = 0.5 * r**2 * (1.0 + 0.3 * np.sin(5.0 * r))
        
        # Saddle-point dominance with multiple competing optima
        saddle_terms = 0.0
        for i in range(self.dim):
            saddle_terms += (0.8 * x[i]**2 * np.cos(3.0 * x[i]) + 
                           0.4 * x[i]**4 * np.sin(2.0 * x[i]) + 
                           0.2 * np.sin(7.0 * x[i]) * np.cos(5.0 * x[i]))
        
        # Adaptive curvature term with varying condition numbers
        curvature = 0.0
        for i in range(self.dim):
            # Varying curvature based on dimension index
            curv = 1.0 + 0.5 * np.sin(0.3 * i)
            curvature += curv * x[i]**2 * (1.0 + 0.2 * np.cos(4.0 * x[i]))
        
        # Cross-dimensional coupling with varying interaction strengths
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Interaction strength varies with dimension indices
                strength = 0.3 + 0.2 * np.sin(0.2 * (i + j))
                coupling += strength * x[i] * x[j] * np.sin(2.0 * (x[i] + x[j]))
        
        # Multi-modal component with multiple local minima
        modal_term = 0.0
        for i in range(self.dim):
            modal_term += (3.0 * np.sin(2.0 * x[i]) * np.cos(3.0 * x[i]) + 
                          2.0 * np.sin(5.0 * x[i])**2 + 
                          1.5 * np.cos(4.0 * x[i])**2)
        
        # Global scaling factor
        scale = 1.0 + 0.1 * np.sum(np.sin(x)**2)
        
        # Penalty for being far from origin to encourage convergence
        penalty = 0.05 * r**3
        
        return scale * (radial_term + saddle_terms + curvature + coupling + modal_term) + penalty