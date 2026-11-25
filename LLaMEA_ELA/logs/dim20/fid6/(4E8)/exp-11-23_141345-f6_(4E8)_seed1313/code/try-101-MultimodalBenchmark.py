import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic oscillations with modified frequencies and amplitudes
        chaotic_term = np.sum(np.sin(2.7 * x + np.cos(1.3 * x)) * np.cos(1.9 * x + np.sin(0.8 * x)))
        
        # Modified radial symmetry with polynomial scaling and exponential decay
        r_squared = np.sum(x**2)
        radial_term = r_squared * np.exp(-0.12 * r_squared) * (1 + 0.1 * r_squared**1.5)
        
        # Increased cross-dimensional coupling with higher-order polynomial interactions
        cross_term = np.sum(x[:-2] * x[1:-1] * x[2:] * np.sin(0.3 * x[:-2]) * np.cos(0.2 * x[1:-1]) * np.sin(0.1 * x[2:]))
        
        # Enhanced trigonometric couplings with altered phase shifts and frequencies
        trig_term = np.sum(np.sin(1.2 * x) * np.cos(0.7 * x) * np.sin(0.5 * x) * np.cos(0.3 * x))
        
        # Additional high-frequency chaotic component for increased multimodality
        high_freq_term = np.sum(np.sin(5.2 * x + np.cos(2.8 * x)) * np.cos(4.1 * x + np.sin(1.9 * x)))
        
        # Modified exponential decay with logarithmic correction terms
        exp_term = np.sum(np.exp(-0.2 * x**2) * np.cos(0.5 * x) * np.log(1 + 0.05 * x**2))
        
        # Combined function with adjusted weights for enhanced multimodality and complexity
        return 0.30 * chaotic_term + 0.20 * radial_term + 0.15 * cross_term + 0.12 * trig_term + 0.08 * high_freq_term + 0.15 * exp_term