import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Exponential potential wells with varying depths and positions
        well_term = 0.0
        for i in range(self.dim):
            position = 0.5 * np.sin(i * 0.7) + 0.3 * np.cos(i * 0.4)
            depth = 2.0 + 1.5 * np.sin(i * 0.9)
            well_term += depth * np.exp(-np.abs(x_normalized[i] - position)**2.5)
        
        # Logarithmic barrier terms creating complex gradient landscapes
        barrier_term = 0.0
        for i in range(self.dim):
            barrier_term -= np.log(1e-6 + np.abs(x_normalized[i])**0.7) * (1 + 0.3 * np.sin(i * 0.5))
        
        # Chaotic saddle-point interactions with multi-scale coupling
        saddle_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling
                coupling_strength = 1.0 / (1.0 + 0.5 * np.exp(-0.3 * (i + j)))
                distance = np.abs(x_normalized[i] - x_normalized[j])
                saddle_term += coupling_strength * np.sin(10 * distance) * np.cos(7 * distance)
        
        # Multi-frequency oscillatory component with dynamic amplitude modulation
        oscillation_term = 0.0
        for i in range(self.dim):
            freq = 3.0 + 2.0 * np.sin(i * 0.6)
            amp = 1.0 + 0.5 * np.cos(i * 0.8)
            oscillation_term += amp * np.sin(freq * x_normalized[i]) * np.cos(freq * x_normalized[i] * 0.7)
        
        # Fractional dimensionality scaling with non-linear transformation
        frac_dim_term = 0.0
        for i in range(self.dim):
            frac_dim_term += (x_normalized[i]**3.2) * (1 + 0.4 * np.sin(i * 1.2))
        
        # Combined function with adaptive weighting based on dimensionality
        weight_sum = 0.8 + 0.2 * np.sin(self.dim * 0.3)
        return (0.4 * well_term + 
                0.3 * barrier_term + 
                0.2 * saddle_term +  
                0.15 * oscillation_term +  
                0.1 * frac_dim_term)