import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with fractal scaling
        r = np.sqrt(np.sum(x**2))
        radial = r * (1.0 + 0.1 * np.sin(10 * r))
        
        # Trigonometric coupling with multiple frequencies
        trig_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.abs(x[i] - x[j])
                trig_coupling += np.cos(5 * distance) * np.sin(3 * distance) * np.exp(-0.1 * distance**2)
        
        # Power-law decay modulations with fractal dimensionality
        power_decay = 0
        for i in range(self.dim):
            power_decay += (1.0 + 0.5 * np.cos(2 * np.pi * x[i])) * np.exp(-0.05 * np.abs(x[i])**1.5)
        
        # Radial symmetry with multiple peaks
        symmetry = 0
        for i in range(self.dim):
            symmetry += np.sin(4 * x[i]) * np.cos(2 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Cross-dimensional fractal interactions
        fractal_interaction = 0
        for i in range(self.dim):
            interaction_sum = 0
            for j in range(self.dim):
                if i != j:
                    interaction_sum += np.sin(3 * (x[i] - x[j])) * np.exp(-0.2 * (x[i] - x[j])**2)
            fractal_interaction += interaction_sum**2
        
        # Global scaling factor based on dimensionality
        scale = 1.0 + 0.05 * np.log(self.dim + 1)
        
        # Combine all components
        return scale * (radial + 0.3 * trig_coupling + 0.2 * power_decay + 0.1 * symmetry + 0.05 * fractal_interaction)