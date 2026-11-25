import numpy as np

class ExponentialRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay potential component
        exp_potential = 0
        for i in range(self.dim):
            # Dynamic decay rate based on dimension and position
            decay_rate = 0.5 + 0.3 * np.sin(i * np.pi / (self.dim + 1))
            exp_potential += np.exp(-decay_rate * abs(x[i])) * np.cos(x[i])
        
        # Sine-wave harmonic component with varying frequencies
        sine_harmonic = 0
        for i in range(self.dim):
            freq = 1.0 + 2.0 * np.sin(i * np.pi / (self.dim + 2))
            sine_harmonic += np.sin(freq * x[i]) * np.cos(0.5 * x[i])
        
        # Dynamic ridge structure with varying heights and widths
        ridge_structure = 0
        for i in range(self.dim):
            # Ridge height modulated by dimension and position
            height = 1.0 + 0.5 * np.sin(i * np.pi / (self.dim + 3))
            width = 0.5 + 0.3 * np.cos(i * np.pi / (self.dim + 4))
            # Gaussian ridge with dynamic parameters
            ridge_structure += height * np.exp(-0.5 * ((x[i] - 1.0) / width)**2)
        
        # Cross-term interaction with dynamic coupling weights
        cross_terms = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic coupling strength based on indices and dimensionality
                coupling = 0.3 + 0.2 * np.sin((i + j) * np.pi / (self.dim + 5))
                cross_terms += coupling * x[i] * x[j]
        
        # Global scaling factor with dimension-dependent modulation
        scale_factor = 1.0 + 0.2 * np.cos(self.dim * np.pi / 10)
        
        # Combine all components with weighted contributions
        weight1 = 0.3 + 0.1 * np.sin(self.dim * np.pi / 8)
        weight2 = 0.4 + 0.1 * np.cos(self.dim * np.pi / 9)
        weight3 = 0.2 + 0.05 * np.sin(self.dim * np.pi / 7)
        weight4 = 0.1 + 0.05 * np.cos(self.dim * np.pi / 6)
        
        return (weight1 * exp_potential + 
                weight2 * sine_harmonic + 
                weight3 * ridge_structure + 
                weight4 * cross_terms) * scale_factor