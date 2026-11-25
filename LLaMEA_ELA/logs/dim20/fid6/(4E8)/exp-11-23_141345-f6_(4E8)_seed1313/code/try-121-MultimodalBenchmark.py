import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic oscillations with modified frequencies and amplitudes
        chaotic_term = np.sum(np.sin(3.1 * x + np.cos(1.7 * x)) * np.cos(2.3 * x + np.sin(1.1 * x)))
        
        # Modified radial symmetry with polynomial scaling and exponential decay
        r_squared = np.sum(x**2)
        radial_term = r_squared * np.exp(-0.18 * r_squared) * (1 + 0.15 * r_squared**1.3)
        
        # Increased cross-dimensional coupling with higher-order polynomial interactions
        cross_term = np.sum(x[:-2] * x[1:-1] * x[2:] * np.sin(0.4 * x[:-2]) * np.cos(0.3 * x[1:-1]) * np.sin(0.2 * x[2:]))
        
        # Enhanced trigonometric couplings with altered phase shifts and frequencies
        trig_term = np.sum(np.sin(1.5 * x) * np.cos(0.8 * x) * np.sin(0.6 * x) * np.cos(0.4 * x))
        
        # Additional high-frequency chaotic component for increased multimodality
        high_freq_term = np.sum(np.sin(6.0 * x + np.cos(3.5 * x)) * np.cos(5.0 * x + np.sin(2.5 * x)))
        
        # Modified exponential decay with logarithmic correction terms
        exp_term = np.sum(np.exp(-0.25 * x**2) * np.cos(0.6 * x) * np.log(1 + 0.08 * x**2))
        
        # Novel hybrid interaction terms to improve fitness scores
        hybrid_term = np.sum((x**3) * np.sin(0.5 * x) * np.cos(0.2 * x) * np.exp(-0.1 * x**2))
        
        # Combined function with adjusted weights for enhanced multimodality and complexity
        return 0.35 * chaotic_term + 0.25 * radial_term + 0.18 * cross_term + 0.14 * trig_term + 0.10 * high_freq_term + 0.12 * exp_term + 0.06 * hybrid_term