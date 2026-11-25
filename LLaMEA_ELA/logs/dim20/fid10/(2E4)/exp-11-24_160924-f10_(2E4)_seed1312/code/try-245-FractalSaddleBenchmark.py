import numpy as np

class FractalSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize fractal parameters
        self.fractal_dims = np.random.uniform(0.5, 2.0, dim)
        self.saddle_strengths = np.random.uniform(1.0, 3.0, dim)
        self.coupling_strengths = np.random.uniform(0.1, 0.5, dim)
        self.frequency_modulators = np.random.uniform(0.8, 1.5, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Add fractal-like self-similarity components
        for i in range(self.dim):
            xi = x[i]
            fractal_dim = self.fractal_dims[i]
            
            # Fractal-like term with power-law scaling
            fractal_term = np.abs(xi)**(1.0 + 0.5 * np.sin(fractal_dim * xi))
            
            # Add gradient-based saddle-point dominance
            saddle_strength = self.saddle_strengths[i]
            saddle_term = saddle_strength * (xi**2 - 1.0)**2
            
            # Combine fractal and saddle components
            result += fractal_term + saddle_term
            
        # Add dynamic cross-dimensional coupling with varying strength
        for i in range(self.dim):
            xi = x[i]
            for j in range(i+1, self.dim):
                xj = x[j]
                
                # Dynamic coupling based on dimension indices and frequencies
                coupling_strength = self.coupling_strengths[i] * self.coupling_strengths[j]
                freq_mod_i = self.frequency_modulators[i]
                freq_mod_j = self.frequency_modulators[j]
                
                # Cross-dimensional interaction with fractal-like modulation
                cross_term = coupling_strength * np.sin(freq_mod_i * xi) * np.cos(freq_mod_j * xj)
                result += cross_term
                
        # Add multi-scale oscillatory components for complexity
        scale_factors = [1.0, 2.0, 3.0]
        for scale in scale_factors:
            osc_sum = 0.0
            for i in range(self.dim):
                xi = x[i]
                osc_sum += np.sin(scale * xi) * np.cos(scale * xi)
            result += 0.1 * osc_sum**2
            
        # Add dimensionally varying global scaling
        global_scale = 1.0 + 0.2 * np.sum(np.sin(0.5 * x))
        result *= global_scale
        
        return result