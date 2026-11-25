import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Adaptive conditioning based on dimension
        condition_factors = np.array([1.0 + 0.5 * np.sin(2.0 * i) for i in range(self.dim)])
        
        # Periodic trigonometric components with varying frequencies
        periodic_terms = 0.0
        for i in range(self.dim):
            freq = 2.0 * (i + 1)
            periodic_terms += np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i]) * condition_factors[i]
        
        # Cross-dimensional interference with varying coupling strengths
        interference_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 0.3 + 0.2 * np.sin(0.5 * (i + j))
                interference_terms += coupling_strength * np.sin(3.0 * x_scaled[i]) * np.cos(2.0 * x_scaled[j])
        
        # Radial exponential decay with sinusoidal modulation
        r = np.sqrt(np.sum(x_scaled**2))
        radial_term = np.exp(-r) * (1.0 + 0.3 * np.sin(5.0 * r))
        
        # Multi-modal component with chaotic frequency modulation
        modal_component = 0.0
        for i in range(self.dim):
            freq_mod = 1.0 + 0.4 * np.sin(7.0 * x_scaled[i])
            modal_component += np.sin(freq_mod * (4.0 * np.pi * x_scaled[i])) * np.cos(freq_mod * (2.0 * np.pi * x_scaled[i]))
        
        # Combine all terms with different weights and add noise
        result = 0.5 * periodic_terms + 0.3 * interference_terms + 0.2 * radial_term + 0.4 * modal_component
        
        # Add chaotic noise term
        noise = np.random.uniform(-0.05, 0.05)
        result += noise
        
        return result