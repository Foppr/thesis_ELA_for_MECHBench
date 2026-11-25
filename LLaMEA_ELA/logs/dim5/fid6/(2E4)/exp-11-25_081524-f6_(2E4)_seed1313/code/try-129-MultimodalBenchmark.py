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
            chaotic_term += np.sin(2.0 * np.pi * logistic) * np.cos(4.0 * x[i])
        
        # Multi-peak Gaussian with dynamic centers and variances
        gaussian_term = 0.0
        num_peaks = min(5, self.dim)
        for i in range(num_peaks):
            center = -4.0 + 2.0 * (i / (num_peaks - 1) if num_peaks > 1 else 0)
            variance = 0.5 + 0.5 * np.sin(0.5 * i)
            gaussian_term += np.exp(-0.5 * ((x[i] - center) ** 2) / variance)
        
        # Rugged saddle point structure with fractal-like behavior and fractional Brownian motion
        rugged_term = 0.0
        for i in range(self.dim-1):
            diff = x[i] - x[i+1]
            rugged_term += (diff**2 + 0.1 * np.sin(10.0 * diff)) * np.exp(-0.05 * np.abs(diff))
        
        # Dynamic coupling with time-delayed interactions and fractional Brownian motion
        delay_coupling = 0.0
        for i in range(self.dim-3):
            # Add fractional Brownian motion component for enhanced complexity
            fbm_component = np.sin(0.3 * x[i]) * np.cos(0.7 * x[i+1]) * np.sin(0.5 * x[i+2])
            delay_coupling += (x[i] * x[i+1] + 0.5 * x[i+2] + fbm_component) * np.cos(0.3 * x[i])
        
        # Global scaling with sinusoidal modulation based on dimensionality and noise injection
        scale_factor = 1.5 + 0.5 * np.sin(0.2 * self.dim)
        
        # Add a small random noise component to increase robustness
        noise = np.random.normal(0, 0.01)
        
        return (chaotic_term + gaussian_term + rugged_term + delay_coupling) * scale_factor + noise