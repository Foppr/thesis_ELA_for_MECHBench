import numpy as np

class MultimodalSymmetricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Radial symmetric component with multiple local minima
        radial = np.sum(x_scaled**2)
        radial_term = np.exp(-radial) * np.cos(2.0 * np.pi * np.sqrt(radial))
        
        # Trigonometric oscillations in all dimensions
        trig_sum = 0.0
        for i in range(self.dim):
            trig_sum += np.sin(3.0 * x_scaled[i]) + np.cos(2.0 * x_scaled[i])
            
        # Exponential barrier terms near boundaries
        barrier = 0.0
        for i in range(self.dim):
            barrier += np.exp(1.0 / (1.0 - x_scaled[i]**2)) if np.abs(x_scaled[i]) < 1.0 else 0.0
            
        # Cross-term interactions creating complex valleys
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(x_scaled[i] * x_scaled[j]) * np.cos(x_scaled[i] + x_scaled[j])
                
        # Multi-frequency harmonic component
        harmonic = 0.0
        frequencies = [1.0, 2.0, 3.0, 4.0]
        for freq in frequencies:
            harmonic += np.sin(freq * np.sum(x_scaled)) * np.cos(freq * np.sqrt(np.sum(x_scaled**2)))
            
        # Combined function with carefully balanced weights
        return 0.8 * radial_term + 1.2 * trig_sum + 0.6 * barrier + 0.4 * cross_term + 0.3 * harmonic