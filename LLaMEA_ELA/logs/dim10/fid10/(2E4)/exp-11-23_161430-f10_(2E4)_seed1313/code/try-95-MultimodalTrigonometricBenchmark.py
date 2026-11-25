import numpy as np

class MultimodalTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize frequency and amplitude parameters for trigonometric components
        self.freq_params = 2.0 + 1.5 * np.sin(np.arange(dim) * 0.7)
        self.amp_params = 1.0 + 0.5 * np.cos(np.arange(dim) * 0.9)
        # Asymmetric saddle point parameters
        self.saddle_params = 0.5 + 0.3 * np.sin(np.arange(dim) * 0.5)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis component with varying widths
        radial_basis = 0.0
        for i in range(self.dim):
            width = 1.0 + 0.4 * np.sin(i * 0.3)
            radial_basis += np.exp(-0.5 * (x[i] / width)**2)
        
        # Trigonometric oscillation component with varying frequencies and amplitudes
        trig_component = 0.0
        for i in range(self.dim):
            freq = self.freq_params[i]
            amp = self.amp_params[i]
            trig_component += amp * np.sin(freq * x[i]) * np.cos(freq * x[i]**2)
        
        # Asymmetric saddle point component
        saddle_term = 0.0
        for i in range(self.dim):
            saddle_term += self.saddle_params[i] * (x[i]**3 - 3*x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Cross-dimensional interaction with sine coupling
        cross_interaction = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            cross_interaction += np.sin(2.0 * x[i] + 0.5 * x[j]) * np.cos(1.5 * x[i] - x[j]**2)
        
        # Non-separable mixed polynomial and exponential component
        mixed_term = 0.0
        for i in range(self.dim):
            mixed_term += (x[i]**4 + 2*x[i]**3 - 5*x[i]**2 + x[i]) * np.exp(-0.05 * x[i]**2)
        
        # Combine all components with different weights
        result = 0.2 * np.sum(x**2) + 0.3 * radial_basis + 0.25 * trig_component + \
                 0.15 * saddle_term + 0.1 * cross_interaction + 0.05 * mixed_term
        
        return result