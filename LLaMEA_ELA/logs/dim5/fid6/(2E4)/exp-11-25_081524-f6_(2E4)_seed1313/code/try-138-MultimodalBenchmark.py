import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine wave component with logistic map modulation
        chaotic_term = 0.0
        r = 3.8
        for i in range(self.dim):
            logistic = r * x[i] * (1 - x[i] / 5.0)
            chaotic_term += np.sin(3.0 * np.pi * logistic) * np.cos(3.0 * x[i])
        
        # Multi-peak Gaussian with dynamic centers and variances
        gaussian_term = 0.0
        num_peaks = min(6, self.dim)
        for i in range(num_peaks):
            center = -4.5 + 1.5 * (i / (num_peaks - 1) if num_peaks > 1 else 0)
            variance = 0.3 + 0.7 * np.sin(0.7 * i)
            gaussian_term += np.exp(-0.5 * ((x[i] - center) ** 2) / variance)
        
        # Rugged saddle point structure with fractal-like behavior and fractional Brownian motion
        rugged_term = 0.0
        for i in range(self.dim-1):
            diff = x[i] - x[i+1]
            rugged_term += (diff**2 + 0.15 * np.sin(12.0 * diff)) * np.exp(-0.07 * np.abs(diff))
        
        # Dynamic coupling with time-delayed interactions and fractional Brownian motion
        delay_coupling = 0.0
        for i in range(self.dim-3):
            # Add fractional Brownian motion component for enhanced complexity
            fbm_component = np.sin(0.4 * x[i]) * np.cos(0.8 * x[i+1]) * np.sin(0.6 * x[i+2])
            delay_coupling += (x[i] * x[i+1] + 0.6 * x[i+2] + fbm_component) * np.cos(0.4 * x[i])
        
        # Global scaling with sinusoidal modulation based on dimensionality and noise injection
        scale_factor = 1.3 + 0.7 * np.sin(0.3 * self.dim)
        
        # Add a small random noise component to increase robustness
        noise = np.random.normal(0, 0.015)
        
        # Introduce additional complexity through polynomial interactions and enhanced coupling
        poly_interaction = 0.0
        for i in range(self.dim):
            poly_interaction += x[i]**4 + 0.4 * x[i]**3 - 0.2 * x[i]**2
        
        # Combine all components with modified weights to improve fitness
        return (chaotic_term * 0.8 + gaussian_term * 0.9 + rugged_term * 0.7 + 
                delay_coupling * 0.6 + poly_interaction * 0.5) * scale_factor + noise