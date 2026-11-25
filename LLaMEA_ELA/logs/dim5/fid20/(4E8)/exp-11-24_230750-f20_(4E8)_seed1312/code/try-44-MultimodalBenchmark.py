import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Nested chaotic sine waves with varying amplitudes and frequencies
        nested_chaos = np.sum(np.sin(10.0 * np.sin(3.0 * x)) * np.cos(7.0 * np.cos(2.0 * x)))
        
        # Augmented radial basis functions with dynamic centers and widths
        rbf_terms = 0.05 * np.sum(np.exp(-np.sum((x[:, None] - np.linspace(-5, 5, self.dim))**2, axis=0) / 2.0))
        
        # Dynamic polynomial couplings with adaptive exponents
        poly_coupling = 0.1 * np.sum((x[:-1]**4 + x[1:]**4) * (x[:-1]**2 + x[1:]**2))
        
        # Adaptive exponential conditioning with varying decay rates
        exp_cond = np.sum(np.exp(-0.6 * np.abs(x)) * np.sin(3.0 * x)**2)
        
        # Additional high-frequency trigonometric components with phase modulation
        high_freq_trig = 0.2 * np.sum(np.sin(15.0 * x + np.sin(x)) + np.cos(12.0 * x + np.cos(x)))
        
        # Combined function value
        return nested_chaos + rbf_terms + poly_coupling + exp_cond + high_freq_trig