import numpy as np

class MultimodalTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with adaptive scaling
        r = np.sqrt(np.sum(x**2))
        radial_term = 0.1 * r * np.sin(5.0 * r) * np.exp(-0.1 * r**2)
        
        # Trigonometric oscillations in each dimension
        trig_term = np.sum(np.sin(10.0 * x) * np.cos(7.0 * x) * np.sin(3.0 * x)) / self.dim
        
        # Multimodal component with multiple peaks
        multi_peak = 0
        for i in range(self.dim):
            multi_peak += np.sin(2.0 * np.pi * x[i]) * np.cos(3.0 * np.pi * x[i]) * np.sin(5.0 * np.pi * x[i])
        
        # Adaptive conditioning based on dimension
        condition_factor = 1.0 + 0.5 * np.sin(self.dim * 0.5)
        
        # Cross-dimensional interaction terms
        cross_term = 0
        if self.dim > 1:
            for i in range(self.dim - 1):
                cross_term += (x[i]**2 + x[i+1]**2) * np.sin(2.0 * np.pi * (x[i] - x[i+1]))
        
        # Gaussian noise component
        noise = 0.01 * np.random.normal(0, 1)
        
        # Combine all terms
        result = condition_factor * (radial_term + trig_term + multi_peak + cross_term) + noise
        
        return result