import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic sine wave component with modified logistic map and harmonic interference
        chaotic_term = 0.0
        r = 3.98
        for i in range(self.dim):
            logistic = r * x[i] * (1 - x[i] / 5.0)
            chaotic_term += np.sin(4.5 * np.pi * logistic) * np.cos(3.1 * x[i]) + \
                           0.4 * np.sin(8.2 * x[i]) * np.exp(-0.15 * x[i]**2) + \
                           0.2 * np.sin(2.7 * x[i]) * np.cos(1.9 * x[i]**2)
        
        # Irregular multi-peak Gaussian with randomized centers, variances, and amplitude modulations
        gaussian_term = 0.0
        num_peaks = min(9, self.dim)
        for i in range(num_peaks):
            center = -4.5 + 2.0 * np.sin(0.6 * i) * (i / (num_peaks - 1) if num_peaks > 1 else 0)
            variance = 0.1 + 0.7 * np.cos(0.5 * i) * np.random.rand()
            amplitude = 1.2 + 0.3 * np.sin(0.8 * i)
            gaussian_term += amplitude * np.exp(-0.5 * ((x[i] - center) ** 2) / variance) * \
                            (1 + 0.3 * np.sin(4.0 * x[i]) + 0.1 * np.cos(2.5 * x[i]))
        
        # Fractal-like rugged saddle point structure with variable exponents and harmonic coupling
        rugged_term = 0.0
        for i in range(self.dim-3):
            diff = x[i] - x[i+1]
            rugged_term += (diff**4 + 0.4 * np.sin(7.0 * diff) + 0.2 * diff**3) * \
                          np.exp(-0.08 * np.abs(diff)) * np.cos(0.3 * x[i]) + \
                          0.15 * np.sin(3.0 * x[i+2]) * np.cos(1.5 * x[i])
        
        # Multi-scale coupling with non-linear interaction terms and dynamic coupling strength
        multi_coupling = 0.0
        for i in range(self.dim-5):
            coupling_strength = 0.8 + 0.4 * np.sin(0.3 * i)
            multi_coupling += coupling_strength * (x[i] * x[i+1]**2 + 0.5 * x[i+2] * np.sin(0.6 * x[i])) * \
                             np.cos(0.4 * x[i]) * np.exp(-0.03 * i) + \
                             0.2 * np.cos(2.0 * x[i+3]) * np.sin(1.2 * x[i+4])
        
        # Fractional Brownian motion with dynamic Hurst parameter and harmonic modulation
        fbm_term = 0.0
        hurst = 0.65 + 0.15 * np.sin(0.15 * self.dim)
        for i in range(self.dim):
            fbm_term += (np.sin(0.9 * x[i]) * np.cos(0.6 * x[i]**2) + \
                       0.3 * np.cos(1.1 * x[i])) * (np.random.rand() - 0.5) * np.exp(-0.015 * i)
        
        # Global scaling with dynamic modulation based on dimensionality, chaos, and harmonic interference
        scale_factor = 2.0 + 0.8 * np.sin(0.5 * self.dim) * np.cos(0.3 * np.sum(x**2)) + \
                      0.4 * np.sin(1.2 * np.sum(x)) * np.cos(0.7 * np.mean(x))
        
        return (chaotic_term + gaussian_term + rugged_term + multi_coupling + fbm_term) * scale_factor