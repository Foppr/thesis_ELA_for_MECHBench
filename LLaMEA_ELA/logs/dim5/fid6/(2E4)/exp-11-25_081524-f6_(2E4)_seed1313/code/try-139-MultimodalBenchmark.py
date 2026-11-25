import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine wave component with logistic map modulation
        chaotic_term = 0.0
        r = 3.9
        for i in range(self.dim):
            logistic = r * x[i] * (1 - x[i] / 5.0)
            chaotic_term += np.sin(4.0 * np.pi * logistic) * np.cos(2.5 * x[i])
        
        # Multi-peak Gaussian with dynamic centers and variances
        gaussian_term = 0.0
        num_peaks = min(5, self.dim)
        for i in range(num_peaks):
            center = -4.8 + 1.2 * (i / (num_peaks - 1) if num_peaks > 1 else 0)
            variance = 0.2 + 0.8 * np.sin(0.4 * i)
            gaussian_term += np.exp(-0.5 * ((x[i] - center) ** 2) / variance)
        
        # Rugged saddle point structure with fractal-like behavior
        rugged_term = 0.0
        for i in range(self.dim-1):
            diff = x[i] - x[i+1]
            rugged_term += (diff**2 + 0.3 * np.sin(7.0 * diff)) * np.exp(-0.04 * np.abs(diff))
        
        # Dynamic coupling with time-delayed interactions
        delay_coupling = 0.0
        for i in range(self.dim-3):
            delay_coupling += (x[i] * x[i+1] + 0.4 * x[i+2]) * np.cos(0.5 * x[i])
        
        # Add fractional Brownian motion component for increased complexity
        fbm_term = 0.0
        hurst = 0.7
        for i in range(self.dim):
            fbm_term += np.sin(0.8 * x[i]) * np.cos(0.5 * x[i]**2) * (np.random.rand() - 0.5)
        
        # Global scaling with sinusoidal modulation based on dimensionality
        scale_factor = 1.3 + 0.7 * np.sin(0.4 * self.dim)
        
        return (chaotic_term + gaussian_term + rugged_term + delay_coupling + fbm_term) * scale_factor