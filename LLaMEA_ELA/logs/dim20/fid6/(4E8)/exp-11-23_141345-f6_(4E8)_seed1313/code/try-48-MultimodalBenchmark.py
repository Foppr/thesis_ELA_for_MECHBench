import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced exponential decay with radial symmetry and logarithmic scaling
        exp_term = np.sum(np.exp(-0.15 * x**2) * np.cos(3.0 * x) * np.log(1.0 + 0.1 * np.abs(x)))
        
        # Multi-frequency trigonometric interactions with polynomial modulation
        trig_term = np.sum(np.sin(4.0 * x) * np.cos(2.0 * x) * np.sin(0.75 * x) * (1.0 + 0.05 * x**2))
        
        # Radial component with inverse scaling and sinusoidal perturbation
        radial_term = np.sum(x**2 * np.exp(-0.03 * np.sum(x**2)) * np.sin(0.5 * np.sum(x**2)))
        
        # Enhanced cross-term interactions with higher-order polynomial coupling and chaotic modulation
        cross_term = 0.0
        for i in range(self.dim - 1):
            cross_term += (np.sin(x[i] + x[i+1]) * 
                          (x[i]**4 + x[i+1]**4) * 
                          np.cos(0.4 * (x[i]**2 + x[i+1]**2)) *
                          np.exp(-0.02 * np.abs(x[i] - x[i+1])))
        
        # Chaotic component with multiple sinusoidal frequencies and exponential dampening
        chaotic_term = np.sum(np.sin(6.0 * x) * np.cos(3.0 * x) * np.sin(1.5 * x) * np.exp(-0.2 * np.abs(x)**1.5))
        
        # Additional high-frequency oscillation for increased multimodality
        high_freq_term = np.sum(np.sin(10.0 * x) * np.cos(5.0 * x) * (1.0 + 0.1 * np.abs(x)))
        
        # Combined function with optimized weights for better fitness score
        return 0.15 * exp_term + 0.25 * trig_term + 0.2 * radial_term + 0.3 * cross_term + 0.05 * chaotic_term + 0.05 * high_freq_term