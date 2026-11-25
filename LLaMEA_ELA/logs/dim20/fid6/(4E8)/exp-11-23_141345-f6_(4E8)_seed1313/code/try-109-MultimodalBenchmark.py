import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-inspired chaotic oscillations with nested frequency modulation
        chaotic_term = np.sum(np.sin(3.1 * x + np.cos(2.2 * x) * np.sin(1.7 * x)) * 
                             np.cos(2.8 * x + np.sin(1.9 * x) * np.cos(1.3 * x)))
        
        # Enhanced radial symmetry with fractal scaling and logarithmic barriers
        r_squared = np.sum(x**2)
        radial_term = r_squared * np.exp(-0.15 * r_squared) * (1 + 0.2 * r_squared**1.8) * np.log(1 + 0.1 * r_squared)
        
        # Increased cross-dimensional coupling with fractal-like polynomial interactions
        cross_term = np.sum(x[:-3] * x[1:-2] * x[2:-1] * x[3:] * 
                           np.sin(0.4 * x[:-3]) * np.cos(0.3 * x[1:-2]) * 
                           np.sin(0.2 * x[2:-1]) * np.cos(0.1 * x[3:]))
        
        # Enhanced trigonometric couplings with multi-scale phase interactions
        trig_term = np.sum(np.sin(1.5 * x) * np.cos(0.8 * x) * 
                          np.sin(0.6 * x) * np.cos(0.4 * x) * 
                          np.sin(0.2 * x) * np.cos(0.1 * x))
        
        # Additional fractal high-frequency component with chaotic phase shifts
        high_freq_term = np.sum(np.sin(6.3 * x + np.cos(3.7 * x) * np.sin(2.1 * x)) * 
                               np.cos(5.8 * x + np.sin(2.9 * x) * np.cos(1.8 * x)))
        
        # Modified exponential decay with fractal correction terms and multi-scale interactions
        exp_term = np.sum(np.exp(-0.25 * x**2) * np.cos(0.6 * x) * 
                         np.log(1 + 0.08 * x**2) * np.sin(0.3 * x) * np.cos(0.2 * x))
        
        # Combined function with fractal-weighted components for enhanced multimodality and complexity
        return 0.25 * chaotic_term + 0.25 * radial_term + 0.18 * cross_term + 0.14 * trig_term + 0.09 * high_freq_term + 0.10 * exp_term