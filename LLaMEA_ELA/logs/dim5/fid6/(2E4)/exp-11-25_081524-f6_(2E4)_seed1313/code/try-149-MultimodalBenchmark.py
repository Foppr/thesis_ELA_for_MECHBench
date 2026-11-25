import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Highly chaotic time-varying logistic map with dynamic r parameter
        chaotic_term = 0.0
        for i in range(self.dim):
            r = 3.9 + 0.1 * np.sin(0.3 * self.dim + 0.7 * x[i])
            logistic = r * x[i] * (1 - x[i] / 5.0)
            chaotic_term += np.sin(6.0 * np.pi * logistic) * np.cos(3.0 * x[i]) + \
                           0.4 * np.sin(9.0 * x[i]) * np.exp(-0.15 * x[i]**2) + \
                           0.2 * np.cos(4.0 * logistic) * np.sin(0.5 * x[i])
        
        # Multi-scale fractal Gaussian field with dynamic centers and variances
        gaussian_term = 0.0
        num_peaks = min(9, self.dim)
        for i in range(num_peaks):
            center = -4.5 + 2.0 * np.sin(0.6 * i + 0.3 * self.dim) * (i / (num_peaks - 1) if num_peaks > 1 else 0)
            variance = 0.1 + 0.7 * np.cos(0.5 * i + 0.2 * self.dim) * np.random.rand()
            gaussian_term += np.exp(-0.5 * ((x[i] - center) ** 2) / variance) * \
                            (1 + 0.3 * np.sin(4.0 * x[i]) + 0.1 * np.cos(2.0 * x[i]))
        
        # Dynamic rugged saddle point structure with adaptive exponents
        rugged_term = 0.0
        for i in range(self.dim-3):
            diff = x[i] - x[i+1]
            exponent = 2.5 + 0.8 * np.sin(0.4 * i + 0.2 * self.dim)
            rugged_term += (diff**exponent + 0.4 * np.sin(7.0 * diff) + 0.15 * diff**(exponent-0.5)) * \
                          np.exp(-0.08 * np.abs(diff)) * np.cos(0.3 * x[i])
        
        # Adaptive multi-scale coupling with dimensionality-dependent weights
        multi_coupling = 0.0
        for i in range(self.dim-5):
            weight = 0.5 + 0.3 * np.sin(0.2 * i + 0.1 * self.dim)
            multi_coupling += (x[i] * x[i+1]**2 + 0.5 * x[i+2] * np.sin(0.6 * x[i])) * \
                             np.cos(0.4 * x[i]) * np.exp(-0.03 * i) * weight
        
        # Dynamic sinusoidal coupling with varying frequencies
        coupling_term = 0.0
        for i in range(self.dim-2):
            freq1 = 2.5 + 0.5 * np.sin(0.3 * i)
            freq2 = 1.5 + 0.4 * np.cos(0.2 * self.dim)
            coupling_term += 0.3 * np.sin(freq1 * (x[i] + x[i+1])) * np.cos(freq2 * x[i]) * np.exp(-0.02 * i)
        
        # Fractional Brownian motion with dynamic Hurst parameter and time-varying amplitude
        fbm_term = 0.0
        hurst = 0.65 + 0.15 * np.sin(0.15 * self.dim)
        for i in range(self.dim):
            amplitude = 0.8 + 0.2 * np.cos(0.2 * i + 0.1 * self.dim)
            fbm_term += amplitude * np.sin(0.9 * x[i]) * np.cos(0.6 * x[i]**2) * \
                       (np.random.rand() - 0.5) * np.exp(-0.015 * i)
        
        # Global scaling with dynamic modulation based on dimensionality, chaos, and landscape complexity
        scale_factor = 2.0 + 0.8 * np.sin(0.5 * self.dim) * np.cos(0.3 * np.sum(x**2)) * \
                      (1 + 0.2 * np.sin(0.4 * np.sum(np.abs(x))))
        
        return (chaotic_term + gaussian_term + rugged_term + multi_coupling + coupling_term + fbm_term) * scale_factor