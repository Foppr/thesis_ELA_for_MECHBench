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
            for _ in range(5):  # Increased nesting depth
                val = np.sin(15.0 * val + np.cos(11.0 * val))  # Increased frequencies
            fractal_component += val ** 2
        
        # Fractional Brownian motion inspired correlation structure with enhanced complexity
        fbm_corr = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = abs(x_scaled[i] - x_scaled[j])
                fbm_corr += np.sin(8.0 * dist) * (dist ** 0.4)  # Increased frequency and roughness
        
        # Nested periodic interactions with varying frequencies and amplitudes
        nested_periodic = 0.0
        for i in range(self.dim):
            inner_sum = 0.0
            for k in range(1, 8):  # Increased frequency range
                inner_sum += np.sin(k * x_scaled[i]) * np.cos(k * x_scaled[(i+1) % self.dim])
            nested_periodic += inner_sum ** 2
        
        # Add chaotic cross-dimensional coupling with exponential weighting and additional terms
        chaos_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_val = np.sin(5.0 * (x_scaled[i] + x_scaled[j]))
                weight = np.exp(-abs(x_scaled[i] - x_scaled[j]) / 3.0)
                chaos_coupling += coupling_val * weight
        
        # Add saddle point structures with additional quadratic terms
        saddle_term = 0.0
        for i in range(self.dim):
            saddle_term += 0.2 * (x_scaled[i] ** 2) * np.cos(10.0 * x_scaled[i])
        
        # Add higher-order interaction terms for increased complexity
        high_order_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    high_order_interaction += np.sin(2.0 * (x_scaled[i] + x_scaled[j] + x_scaled[k]))
        
        # Combine all components with dynamic weighting based on position
        dynamic_weight = 1.0 + 0.7 * np.sin(5.0 * r_squared)  # Increased modulation
        
        result = (dynamic_weight * radial_term + 
                 0.5 * fractal_component + 
                 0.4 * fbm_corr + 
                 0.3 * nested_periodic + 
                 0.2 * chaos_coupling + 
                 0.1 * saddle_term + 
                 0.15 * high_order_interaction)
        
        return result