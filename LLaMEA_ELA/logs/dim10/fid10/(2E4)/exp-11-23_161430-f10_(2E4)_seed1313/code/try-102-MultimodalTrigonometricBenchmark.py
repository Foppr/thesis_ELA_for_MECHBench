import numpy as np

class MultimodalTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic frequency parameters
        self.freq_params = 3.0 + 2.0 * np.sin(np.arange(dim) * 0.8 + 1.0)
        self.amp_params = 1.5 + 0.8 * np.cos(np.arange(dim) * 1.1 + 0.5)
        # Modified saddle point parameters with chaotic variation
        self.saddle_params = 0.7 + 0.4 * np.sin(np.arange(dim) * 0.6 + 0.3)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced radial basis with chaotic widths
        radial_basis = 0.0
        for i in range(self.dim):
            width = 1.2 + 0.6 * np.sin(i * 0.4 + 0.7)
            radial_basis += np.exp(-0.3 * (x[i] / width)**2) + 0.1 * np.sin(x[i])
        
        # Modified trigonometric component with chaotic coupling
        trig_component = 0.0
        for i in range(self.dim):
            freq = self.freq_params[i]
            amp = self.amp_params[i]
            trig_component += amp * np.sin(freq * x[i] + 0.3 * np.cos(x[i])) * np.cos(freq * x[i]**1.5)
        
        # Novel asymmetric saddle with chaotic modulation
        saddle_term = 0.0
        for i in range(self.dim):
            saddle_term += self.saddle_params[i] * (x[i]**4 - 4*x[i]**2) * np.exp(-0.15 * x[i]**2) + 0.2 * np.sin(x[i]**3)
        
        # Chaotic cross-dimensional interaction
        cross_interaction = 0.0
        for i in range(self.dim):
            j = (i + 2) % self.dim  # Changed coupling pattern
            cross_interaction += np.sin(1.5 * x[i] + 0.7 * x[j] + 0.3 * np.cos(x[i])) * np.cos(2.0 * x[i] - x[j]**1.8)
        
        # Enhanced mixed polynomial and exponential component with chaotic modulation
        mixed_term = 0.0
        for i in range(self.dim):
            mixed_term += (x[i]**5 + 3*x[i]**4 - 6*x[i]**3 + 2*x[i]**2 - x[i]) * np.exp(-0.07 * x[i]**2) + 0.15 * np.sin(x[i]**2)
        
        # Combine all components with updated weights for better balance
        result = 0.15 * np.sum(x**2) + 0.35 * radial_basis + 0.2 * trig_component + \
                 0.18 * saddle_term + 0.12 * cross_interaction + 0.05 * mixed_term
        
        return result