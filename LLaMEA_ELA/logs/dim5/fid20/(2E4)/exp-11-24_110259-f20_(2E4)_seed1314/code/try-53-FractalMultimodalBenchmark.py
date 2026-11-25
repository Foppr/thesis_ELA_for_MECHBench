import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Base radial component with fractal-like behavior using fractional powers
        r_squared = np.sum(x_scaled**2)
        radial_term = np.exp(-r_squared / 2.0) + 0.3 * (r_squared ** 1.7)
        
        # Generate fractal-like correlations using nested trigonometric maps
        fractal_component = 0.0
        for i in range(self.dim):
            # Chaotic map with nested sine and cosine operations
            val = np.sin(2.0 * np.pi * (x_scaled[i] + 0.5))
            for _ in range(3):
                val = np.sin(10.0 * val + np.cos(7.0 * val))
            fractal_component += val ** 2
        
        # Fractional Brownian motion inspired correlation structure
        fbm_corr = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = abs(x_scaled[i] - x_scaled[j])
                fbm_corr += np.sin(5.0 * dist) * (dist ** 0.3)
        
        # Nested periodic interactions with varying frequencies and amplitudes
        nested_periodic = 0.0
        for i in range(self.dim):
            inner_sum = 0.0
            for k in range(1, 6):
                inner_sum += np.sin(k * x_scaled[i]) * np.cos(k * x_scaled[(i+1) % self.dim])
            nested_periodic += inner_sum ** 2
        
        # Add chaotic cross-dimensional coupling with exponential weighting (modified)
        chaos_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_val = np.sin(3.0 * (x_scaled[i] + x_scaled[j]))
                weight = np.exp(-abs(x_scaled[i] - x_scaled[j]) / 1.5)  # Modified weight
                chaos_coupling += coupling_val * weight
        
        # Combine all components with dynamic weighting based on position
        dynamic_weight = 1.0 + 0.5 * np.sin(3.0 * r_squared)
        
        result = (dynamic_weight * radial_term + 
                 0.4 * fractal_component + 
                 0.3 * fbm_corr + 
                 0.2 * nested_periodic + 
                 0.15 * chaos_coupling)  # Increased coupling weight
        
        return result