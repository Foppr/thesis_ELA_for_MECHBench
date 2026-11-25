import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters for each dimension
        self.chaos_params = np.random.uniform(0.1, 0.9, dim)
        self.fractal_dims = np.random.uniform(0.5, 2.0, dim)
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic saddle-point component
        chaotic_term = 0.0
        for i in range(self.dim):
            param = self.chaos_params[i]
            chaotic_term += np.sin(param * x[i]) * np.cos(param * x[i]) * (1 + 0.1 * np.sin(3 * x[i]))
        
        # Fractal attractor embedding
        fractal_term = 0.0
        for i in range(self.dim):
            dim_frac = self.fractal_dims[i]
            fractal_term += np.sin(x[i] ** dim_frac) * np.cos(x[i] ** (dim_frac + 0.5)) * (1 + 0.2 * np.cos(2 * x[i]))
        
        # Dynamic gradient modulation
        grad_mod = 0.0
        for i in range(self.dim-1):
            grad_mod += (x[i+1] - x[i])**2 * np.exp(-0.5 * (x[i] + x[i+1])**2)
        
        # Embedded saddle-point structure with varying curvature
        saddle_term = 0.0
        for i in range(self.dim):
            saddle_term += (x[i]**4 - 6*x[i]**2) * np.sin(0.5 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Coupling between dimensions via dynamic phase shifts
        coupling_term = 0.0
        for i in range(self.dim-2):
            phase_shift = np.sin(0.3 * x[i]) * np.cos(0.4 * x[i+1])
            coupling_term += x[i] * x[i+2] * phase_shift
        
        # Final scaling with dimensionality-dependent factor
        dim_factor = 1.0 + 0.5 * (self.dim / 10.0)
        
        return (chaotic_term + fractal_term + grad_mod + saddle_term + coupling_term) * dim_factor