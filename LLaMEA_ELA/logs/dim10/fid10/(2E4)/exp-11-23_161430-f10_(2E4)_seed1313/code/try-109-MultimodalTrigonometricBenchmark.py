import numpy as np

class MultimodalTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize frequency and amplitude parameters for trigonometric components
        self.freq_params = 1.2 + 1.8 * np.sin(np.arange(dim) * 0.7)
        self.amp_params = 0.6 + 0.9 * np.cos(np.arange(dim) * 1.3)
        # Asymmetric saddle point parameters with chaotic variation
        self.saddle_params = 0.4 + 0.5 * np.sin(np.arange(dim) * 0.5 + np.pi/5)
        # Chaotic coupling parameters
        self.chaos_params = 0.6 + 0.4 * np.sin(np.arange(dim) * 0.7 + np.pi/4)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis component with chaotic width variation
        radial_basis = 0.0
        for i in range(self.dim):
            width = 1.0 + 0.4 * np.sin(i * 0.3 + self.chaos_params[i])
            radial_basis += np.exp(-0.5 * (x[i] / width)**2)
        
        # Trigonometric oscillation component with chaotic frequencies and amplitudes
        trig_component = 0.0
        for i in range(self.dim):
            freq = self.freq_params[i]
            amp = self.amp_params[i]
            trig_component += amp * np.sin(freq * x[i] + 0.4 * np.cos(freq * x[i])) * np.cos(freq * x[i]**2 + 0.3 * np.sin(x[i]))
        
        # Asymmetric saddle point component with chaotic modification
        saddle_term = 0.0
        for i in range(self.dim):
            saddle_term += self.saddle_params[i] * (x[i]**3 - 3*x[i]) * np.exp(-0.2 * x[i]**2 + 0.15 * np.sin(x[i]))
        
        # Cross-dimensional interaction with chaotic coupling
        cross_interaction = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            coupling_strength = 0.7 + 0.5 * np.sin(i * 0.6 + self.chaos_params[i])
            cross_interaction += coupling_strength * np.sin(2.5 * x[i] + 0.4 * x[j] + 0.2 * np.cos(x[i])) * np.cos(1.8 * x[i] - x[j]**2 + 0.15 * np.sin(x[j]))
        
        # Non-separable mixed polynomial and exponential component with chaotic modification
        mixed_term = 0.0
        for i in range(self.dim):
            mixed_term += (x[i]**4 + 1.5*x[i]**3 - 4*x[i]**2 + 1.5*x[i] + 0.6 * np.sin(x[i])) * np.exp(-0.08 * x[i]**2 + 0.12 * np.cos(x[i]))
        
        # Chaotic polynomial component for additional complexity
        chaotic_poly = 0.0
        for i in range(self.dim):
            chaotic_poly += (x[i]**5 + 0.6*x[i]**4 - 1.8*x[i]**3 + 0.9*x[i]**2 - 0.8*x[i]) * np.sin(0.4 * x[i] + self.chaos_params[i])
        
        # Combine all components with different weights
        result = 0.2 * np.sum(x**2) + 0.3 * radial_basis + 0.25 * trig_component + \
                 0.15 * saddle_term + 0.09 * cross_interaction + 0.06 * mixed_term + 0.05 * chaotic_poly
        
        return result