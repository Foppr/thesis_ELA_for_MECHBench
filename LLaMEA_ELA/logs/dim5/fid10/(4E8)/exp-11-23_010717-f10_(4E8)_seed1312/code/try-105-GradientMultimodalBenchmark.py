import numpy as np

class GradientMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Radial symmetry term with adaptive curvature
        r = np.sqrt(np.sum(x**2))
        radial_term = 0.5 * r**2 + 0.3 * np.sin(3.0 * r) + 0.2 * np.cos(2.0 * r)
        
        # Saddle-point dominant terms with varying condition numbers
        saddle_terms = 0.0
        for i in range(self.dim):
            # Adaptive curvature based on dimension
            curvature = 1.0 + 0.5 * np.sin(0.5 * i)
            saddle_terms += curvature * x[i]**2 * np.cos(x[i])
            
        # Multiple competing optima with different scaling factors
        optima_terms = 0.0
        for i in range(self.dim):
            # Different frequency components for each dimension
            freq = 1.0 + 0.3 * np.sin(0.7 * i)
            optima_terms += 0.8 * np.sin(freq * x[i]) * np.cos(freq * x[i])**2
            
        # Cross-dimensional coupling with varying interaction strengths
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Interaction strength varies with dimension indices
                strength = 0.5 + 0.3 * np.sin(0.3 * (i + j))
                cross_terms += strength * x[i] * x[j] * np.sin(x[i] + x[j])
                
        # Add noise component for additional challenge
        noise = 0.1 * np.sum(np.random.normal(0, 1, self.dim) * x)
        
        # Global scaling factor to adjust difficulty
        global_scale = 1.0 + 0.2 * np.sin(r)
        
        return global_scale * (radial_term + saddle_terms + optima_terms + cross_terms) + noise