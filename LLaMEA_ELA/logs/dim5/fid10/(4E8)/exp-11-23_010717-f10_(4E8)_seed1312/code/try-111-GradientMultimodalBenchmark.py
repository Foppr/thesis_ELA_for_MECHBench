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
        
        # Saddle-point dominance with multiple competing optima (modified)
        saddle_terms = 0.0
        for i in range(self.dim):
            saddle_terms += (0.9 * x[i]**2 * np.cos(3.5 * x[i]) + 
                           0.45 * x[i]**4 * np.sin(2.5 * x[i]) + 
                           0.25 * np.sin(7.5 * x[i]) * np.cos(5.5 * x[i]))
        
        # Adaptive curvature term with varying condition numbers
        curvature = 0.0
        for i in range(self.dim):
            # Varying curvature based on dimension index (modified)
            curv = 1.0 + 0.6 * np.sin(0.35 * i)
            curvature += curv * x[i]**2 * (1.0 + 0.25 * np.cos(4.5 * x[i]))
        
        # Cross-dimensional coupling with varying interaction strengths (modified)
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Interaction strength varies with dimension indices (modified)
                strength = 0.35 + 0.25 * np.sin(0.25 * (i + j))
                coupling += strength * x[i] * x[j] * np.sin(2.5 * (x[i] + x[j]))
        
        # Multi-modal component with multiple local minima (modified)
        modal_term = 0.0
        for i in range(self.dim):
            modal_term += (3.5 * np.sin(2.5 * x[i]) * np.cos(3.5 * x[i]) + 
                          2.5 * np.sin(5.5 * x[i])**2 + 
                          1.8 * np.cos(4.5 * x[i])**2)
        
        # Global scaling factor (modified)
        scale = 1.0 + 0.15 * np.sum(np.sin(x)**2)
        
        # Penalty for being far from origin to encourage convergence
        penalty = 0.06 * r**3
        
        return scale * (radial_term + saddle_terms + curvature + coupling + modal_term) + penalty