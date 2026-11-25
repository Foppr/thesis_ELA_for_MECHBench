import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic sine wave component with modified logistic map
        chaotic_term = 0.0
        r = 3.92
        for i in range(self.dim):
            logistic = r * x[i] * (1 - x[i] / 5.0)
            chaotic_term += np.sin(4.5 * np.pi * logistic) * np.cos(2.8 * x[i]) + \
                           0.35 * np.sin(7.5 * x[i]) * np.exp(-0.12 * x[i]**2)
        
        # Irregular multi-peak Gaussian with randomized centers and variances
        gaussian_term = 0.0
        num_peaks = min(8, self.dim)
        for i in range(num_peaks):
            center = -4.9 + 1.9 * np.sin(0.6 * i) * (i / (num_peaks - 1) if num_peaks > 1 else 0)
            variance = 0.25 + 0.55 * np.cos(0.3 * i) * np.random.rand()
            gaussian_term += np.exp(-0.5 * ((x[i] - center) ** 2) / variance) * \
                            (1 + 0.25 * np.sin(3.5 * x[i]))
        
        # Fractal-like rugged saddle point structure with variable exponents
        rugged_term = 0.0
        for i in range(self.dim-2):
            diff = x[i] - x[i+1]
            rugged_term += (diff**3 + 0.35 * np.sin(6.5 * diff) + 0.12 * diff**2) * \
                          np.exp(-0.06 * np.abs(diff)) * np.cos(0.25 * x[i])
        
        # Multi-scale coupling with non-linear interaction terms
        multi_coupling = 0.0
        for i in range(self.dim-4):
            multi_coupling += (x[i] * x[i+1]**2 + 0.45 * x[i+2] * np.sin(0.55 * x[i])) * \
                             np.cos(0.35 * x[i]) * np.exp(-0.025 * i)
        
        # Sinusoidal coupling between dimensions
        coupling_term = 0.0
        for i in range(self.dim-1):
            coupling_term += 0.25 * np.sin(3.5 * (x[i] + x[i+1])) * np.cos(0.55 * x[i]) * np.exp(-0.015 * i)
        
        # Fractional Brownian motion with dynamic Hurst parameter
        fbm_term = 0.0
        hurst = 0.72 + 0.12 * np.sin(0.12 * self.dim)
        for i in range(self.dim):
            fbm_term += np.sin(0.85 * x[i]) * np.cos(0.55 * x[i]**2) * \
                       (np.random.rand() - 0.5) * np.exp(-0.015 * i)
        
        # Global scaling with dynamic modulation based on dimensionality and chaos
        scale_factor = 1.6 + 0.4 * np.sin(0.45 * self.dim) * np.cos(0.25 * np.sum(x**2))
        
        return (chaotic_term + gaussian_term + rugged_term + multi_coupling + coupling_term + fbm_term) * scale_factor