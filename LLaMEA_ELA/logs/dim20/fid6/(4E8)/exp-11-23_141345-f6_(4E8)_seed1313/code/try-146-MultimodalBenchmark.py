import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic oscillations with modified frequencies and amplitudes
        chaotic_term = np.sum(np.sin(3.2 * x + np.cos(1.8 * x)) * np.cos(2.4 * x + np.sin(1.2 * x)))
        
        # Modified radial symmetry with polynomial scaling and exponential decay
        r_squared = np.sum(x**2)
        radial_term = r_squared * np.exp(-0.2 * r_squared) * (1 + 0.18 * r_squared**1.4)
        
        # Increased cross-dimensional coupling with higher-order polynomial interactions
        cross_term = np.sum(x[:-2] * x[1:-1] * x[2:] * np.sin(0.45 * x[:-2]) * np.cos(0.35 * x[1:-1]) * np.sin(0.25 * x[2:]))
        
        # Enhanced trigonometric couplings with altered phase shifts and frequencies
        trig_term = np.sum(np.sin(1.6 * x) * np.cos(0.85 * x) * np.sin(0.65 * x) * np.cos(0.45 * x))
        
        # Additional high-frequency chaotic component for increased multimodality
        high_freq_term = np.sum(np.sin(6.2 * x + np.cos(3.7 * x)) * np.cos(5.2 * x + np.sin(2.7 * x)))
        
        # Modified exponential decay with logarithmic correction terms
        exp_term = np.sum(np.exp(-0.28 * x**2) * np.cos(0.65 * x) * np.log(1 + 0.09 * x**2))
        
        # Novel hybrid interaction terms to improve fitness scores
        hybrid_term = np.sum((x**3) * np.sin(0.55 * x) * np.cos(0.25 * x) * np.exp(-0.12 * x**2))
        
        # Combined function with adjusted weights for enhanced multimodality and complexity
        return 0.36 * chaotic_term + 0.24 * radial_term + 0.19 * cross_term + 0.13 * trig_term + 0.09 * high_freq_term + 0.11 * exp_term + 0.07 * hybrid_term