import numpy as np

class SinusoidalRadialSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Radial component with multiple peaks and valleys
        r = np.sqrt(np.sum(x_scaled**2))
        radial_term = np.sin(5 * np.pi * r) * np.exp(-r**2)
        
        # Sinusoidal oscillations in each dimension
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += np.sin(3 * np.pi * x_scaled[i]) * np.cos(4 * np.pi * x_scaled[i])
        
        # Cross-dimensional interaction creating saddle points
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += (x_scaled[i]**2 + x_scaled[j]**2) * np.sin(np.pi * x_scaled[i] * x_scaled[j])
        
        # Additional multimodal component with varying frequency
        multi_term = 0.0
        for i in range(self.dim):
            multi_term += np.sin(7 * np.pi * x_scaled[i]) * np.cos(2 * np.pi * x_scaled[i]) * np.exp(-x_scaled[i]**2)
        
        # Combine all terms with different weights
        return 0.5 * radial_term + 0.3 * sin_term + 0.2 * cross_term + 0.4 * multi_term + 1.0