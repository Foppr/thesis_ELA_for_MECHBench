import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Intensified chaotic oscillations with higher frequencies and amplitudes
        chaotic_term = np.sum(np.sin(4.2 * x + np.cos(2.1 * x)) * np.cos(3.7 * x + np.sin(1.9 * x)))
        
        # Augmented radial symmetry breaking with polynomial scaling and exponential decay
        r_squared = np.sum(x**2)
        radial_term = r_squared * np.exp(-0.25 * r_squared) * (1 + 0.25 * r_squared**1.5)
        
        # Stronger cross-dimensional coupling with higher-order polynomial interactions
        cross_term = np.sum(x[:-3] * x[1:-2] * x[2:-1] * x[3:] * np.sin(0.5 * x[:-3]) * np.cos(0.4 * x[1:-2]) * np.sin(0.3 * x[2:-1]) * np.cos(0.2 * x[3:]))
        
        # Enhanced trigonometric couplings with altered phase shifts and frequencies
        trig_term = np.sum(np.sin(2.0 * x) * np.cos(1.2 * x) * np.sin(0.8 * x) * np.cos(0.5 * x))
        
        # Additional high-frequency chaotic component for increased multimodality
        high_freq_term = np.sum(np.sin(7.5 * x + np.cos(4.2 * x)) * np.cos(6.8 * x + np.sin(3.1 * x)))
        
        # Augmented exponential decay with logarithmic correction terms
        exp_term = np.sum(np.exp(-0.35 * x**2) * np.cos(0.8 * x) * np.log(1 + 0.12 * x**2))
        
        # Novel hybrid interaction terms to improve fitness scores
        hybrid_term = np.sum((x**4) * np.sin(0.6 * x) * np.cos(0.3 * x) * np.exp(-0.15 * x**2))
        
        # Combined function with adjusted weights for enhanced multimodality and complexity
        return 0.42 * chaotic_term + 0.28 * radial_term + 0.22 * cross_term + 0.16 * trig_term + 0.13 * high_freq_term + 0.15 * exp_term + 0.08 * hybrid_term