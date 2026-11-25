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
            # Modified decay rate with different modulation
            decay_rate = 0.7 + 0.4 * np.cos(i * np.pi / (self.dim + 1))
            exp_potential += np.exp(-decay_rate * abs(x[i])) * np.sin(x[i])
        
        # Sine-wave harmonic component with altered frequencies
        sine_harmonic = 0
        for i in range(self.dim):
            # Changed frequency pattern for more complexity
            freq = 2.0 + 1.5 * np.cos(i * np.pi / (self.dim + 2))
            sine_harmonic += np.cos(freq * x[i]) * np.sin(0.3 * x[i])
        
        # Dynamic ridge structure with modified parameters
        ridge_structure = 0
        for i in range(self.dim):
            # Changed ridge height and width modulation
            height = 0.8 + 0.6 * np.cos(i * np.pi / (self.dim + 3))
            width = 0.3 + 0.4 * np.sin(i * np.pi / (self.dim + 4))
            # Modified Gaussian ridge with new parameters
            ridge_structure += height * np.exp(-0.5 * ((x[i] + 1.5) / width)**2)
        
        # Cross-term interaction with new coupling weights
        cross_terms = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Altered coupling strength pattern
                coupling = 0.4 + 0.3 * np.cos((i + j) * np.pi / (self.dim + 5))
                cross_terms += coupling * x[i] * x[j]
        
        # Global scaling factor with different modulation
        scale_factor = 1.2 + 0.3 * np.sin(self.dim * np.pi / 10)
        
        # Combine all components with new weighted contributions
        weight1 = 0.25 + 0.15 * np.cos(self.dim * np.pi / 8)
        weight2 = 0.35 + 0.15 * np.sin(self.dim * np.pi / 9)
        weight3 = 0.25 + 0.1 * np.cos(self.dim * np.pi / 7)
        weight4 = 0.15 + 0.1 * np.sin(self.dim * np.pi / 6)
        
        return (weight1 * exp_potential + 
                weight2 * sine_harmonic + 
                weight3 * ridge_structure + 
                weight4 * cross_terms) * scale_factor