import numpy as np

class MultimodalTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize frequency and amplitude parameters for trigonometric components
        self.freq_params = 1.5 + 2.0 * np.sin(np.arange(dim) * 0.8)
        self.amp_params = 0.8 + 0.7 * np.cos(np.arange(dim) * 1.1)
        # Asymmetric saddle point parameters with chaotic variation
        self.saddle_params = 0.3 + 0.6 * np.sin(np.arange(dim) * 0.4 + np.pi/4)
        # Chaotic coupling parameters
        self.chaos_params = 0.5 + 0.5 * np.sin(np.arange(dim) * 0.6 + np.pi/3)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis component with chaotic width variation
        radial_basis = 0.0
        for i in range(self.dim):
            width = 1.2 + 0.3 * np.sin(i * 0.4 + self.chaos_params[i])
            radial_basis += np.exp(-0.5 * (x[i] / width)**2)
        
        # Trigonometric oscillation component with chaotic frequencies and amplitudes
        trig_component = 0.0
        for i in range(self.dim):
            freq = self.freq_params[i]
            amp = self.amp_params[i]
            trig_component += amp * np.sin(freq * x[i] + 0.3 * np.cos(freq * x[i])) * np.cos(freq * x[i]**2 + 0.2 * np.sin(x[i]))
        
        # Asymmetric saddle point component with chaotic modification
        saddle_term = 0.0
        for i in range(self.dim):
            saddle_term += self.saddle_params[i] * (x[i]**3 - 3*x[i]) * np.exp(-0.15 * x[i]**2 + 0.1 * np.sin(x[i]))
        
        # Cross-dimensional interaction with chaotic coupling
        cross_interaction = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            coupling_strength = 0.8 + 0.4 * np.sin(i * 0.5 + self.chaos_params[i])
            cross_interaction += coupling_strength * np.sin(2.0 * x[i] + 0.5 * x[j] + 0.3 * np.cos(x[i])) * np.cos(1.5 * x[i] - x[j]**2 + 0.2 * np.sin(x[j]))
        
        # Non-separable mixed polynomial and exponential component with chaotic modification
        mixed_term = 0.0
        for i in range(self.dim):
            mixed_term += (x[i]**4 + 2*x[i]**3 - 5*x[i]**2 + x[i] + 0.5 * np.sin(x[i])) * np.exp(-0.07 * x[i]**2 + 0.1 * np.cos(x[i]))
        
        # Chaotic polynomial component for additional complexity
        chaotic_poly = 0.0
        for i in range(self.dim):
            chaotic_poly += (x[i]**5 + 0.5*x[i]**4 - 2*x[i]**3 + 0.8*x[i]**2 - x[i]) * np.sin(0.3 * x[i] + self.chaos_params[i])
        
        # Combine all components with different weights
        result = 0.15 * np.sum(x**2) + 0.35 * radial_basis + 0.2 * trig_component + \
                 0.18 * saddle_term + 0.08 * cross_interaction + 0.07 * mixed_term + 0.05 * chaotic_poly
        
        return result