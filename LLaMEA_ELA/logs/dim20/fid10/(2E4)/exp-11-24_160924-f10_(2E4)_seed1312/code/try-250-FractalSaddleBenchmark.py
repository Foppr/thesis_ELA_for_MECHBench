import numpy as np

class FractalSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize fractal parameters with slight modifications
        self.fractal_dims = np.random.uniform(0.3, 1.8, dim)
        self.saddle_strengths = np.random.uniform(1.2, 2.8, dim)
        self.coupling_strengths = np.random.uniform(0.05, 0.4, dim)
        self.frequency_modulators = np.random.uniform(0.6, 1.7, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Add fractal-like self-similarity components with modified exponents
        for i in range(self.dim):
            xi = x[i]
            fractal_dim = self.fractal_dims[i]
            
            # Modified fractal-like term with altered power-law scaling
            fractal_term = np.abs(xi)**(1.2 + 0.3 * np.sin(fractal_dim * xi))
            
            # Add gradient-based saddle-point dominance with modified strength
            saddle_strength = self.saddle_strengths[i]
            saddle_term = saddle_strength * (xi**2 - 1.0)**2.5
            
            # Combine fractal and saddle components
            result += fractal_term + saddle_term
            
        # Add dynamic cross-dimensional coupling with modified interaction
        for i in range(self.dim):
            xi = x[i]
            for j in range(i+1, self.dim):
                xj = x[j]
                
                # Modified coupling based on dimension indices and frequencies
                coupling_strength = self.coupling_strengths[i] * self.coupling_strengths[j]
                freq_mod_i = self.frequency_modulators[i]
                freq_mod_j = self.frequency_modulators[j]
                
                # Cross-dimensional interaction with modified modulation
                cross_term = coupling_strength * np.sin(freq_mod_i * xi + 0.5) * np.cos(freq_mod_j * xj + 0.3)
                result += cross_term
                
        # Add multi-scale oscillatory components for complexity with altered scaling
        scale_factors = [1.2, 2.5, 3.5]
        for scale in scale_factors:
            osc_sum = 0.0
            for i in range(self.dim):
                xi = x[i]
                osc_sum += np.sin(scale * xi) * np.cos(scale * xi)
            result += 0.15 * osc_sum**2
            
        # Add dimensionally varying global scaling with modified factor
        global_scale = 1.0 + 0.15 * np.sum(np.sin(0.6 * x))
        result *= global_scale
        
        return result