import numpy as np

class AdaptiveRidgeAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize chaotic and fractal parameters
        self.fractal_dims = np.random.uniform(0.3, 2.5, dim)
        self.saddle_strengths = np.random.uniform(0.8, 3.5, dim)
        self.ridge_strengths = np.random.uniform(1.0, 4.0, dim)
        self.coupling_strengths = np.random.uniform(0.05, 0.6, dim)
        self.frequency_modulators = np.random.uniform(0.5, 2.0, dim)
        self.chaos_factors = np.random.uniform(0.1, 0.8, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Add chaotic fractal-like self-similarity components
        for i in range(self.dim):
            xi = x[i]
            fractal_dim = self.fractal_dims[i]
            
            # Fractal term with chaotic modulation
            chaos_mod = np.sin(self.chaos_factors[i] * xi)
            fractal_term = np.abs(xi)**(1.0 + 0.3 * np.sin(fractal_dim * xi) * chaos_mod)
            
            # Add gradient-based saddle-point dominance
            saddle_strength = self.saddle_strengths[i]
            saddle_term = saddle_strength * (xi**2 - 1.0)**2
            
            # Add ridge attraction component
            ridge_strength = self.ridge_strengths[i]
            ridge_term = ridge_strength * np.exp(-0.5 * xi**2) * np.cos(xi)
            
            # Combine all components
            result += fractal_term + saddle_term + ridge_term
            
        # Add dynamic cross-dimensional coupling with chaotic modulation
        for i in range(self.dim):
            xi = x[i]
            for j in range(i+1, self.dim):
                xj = x[j]
                
                # Dynamic coupling with chaos factor
                coupling_strength = self.coupling_strengths[i] * self.coupling_strengths[j]
                freq_mod_i = self.frequency_modulators[i]
                freq_mod_j = self.frequency_modulators[j]
                
                # Cross-dimensional interaction with chaotic modulation
                chaos_i = np.sin(self.chaos_factors[i] * xi)
                chaos_j = np.sin(self.chaos_factors[j] * xj)
                cross_term = coupling_strength * np.sin(freq_mod_i * xi + chaos_i) * np.cos(freq_mod_j * xj + chaos_j)
                result += cross_term
                
        # Add multi-scale oscillatory components with dynamic amplitude
        scale_factors = [1.0, 2.0, 3.0, 4.0]
        for scale in scale_factors:
            osc_sum = 0.0
            for i in range(self.dim):
                xi = x[i]
                # Dynamic amplitude modulation based on dimension index
                amp_mod = 1.0 + 0.2 * np.sin(0.5 * i)
                osc_sum += amp_mod * np.sin(scale * xi) * np.cos(scale * xi)
            result += 0.15 * osc_sum**2
            
        # Add adaptive global scaling with chaotic modulation
        global_scale = 1.0 + 0.3 * np.sum(np.sin(0.5 * x)) * np.prod(np.cos(0.3 * x))
        result *= global_scale
        
        # Add noise component to increase robustness testing
        noise = np.random.normal(0, 0.01, self.dim)
        for i in range(self.dim):
            result += noise[i] * np.sin(x[i])
            
        return result