import numpy as np

class SinusoidalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        # Precompute frequency parameters for each dimension
        self.frequencies = 2.0 + 1.5 * np.sin(np.arange(dim) * 0.8)
        # Precompute amplitude parameters
        self.amplitudes = 1.0 + 0.5 * np.cos(np.arange(dim) * 0.6)
        
    def f(self, x):
        if len(x) != self.dim:
            if len(x) < self.dim:
                x = np.pad(x, (0, self.dim - len(x)), mode='constant', constant_values=0.0)
            else:
                x = x[:self.dim]
        
        # Clip to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial term with sinusoidal modulation
        r = np.sqrt(np.sum(x**2))
        radial_term = 0.5 * r**2 + 0.3 * np.sin(3.0 * r) * np.cos(2.0 * r)
        
        # Multi-modal sinusoidal term
        modal_term = 0.0
        for i in range(self.dim):
            # Dimensional sinusoidal component with varying frequency and amplitude
            modal_term += self.amplitudes[i] * np.sin(self.frequencies[i] * x[i]) * np.cos(self.frequencies[i] * x[i])
        
        # Cross-dimensional coupling term
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Coupling strength based on dimension indices and variable values
                coupling_strength = 0.2 + 0.1 * np.sin(i * 0.5 + j * 0.3)
                coupling_term += coupling_strength * np.sin(x[i] - x[j])**2
        
        # Radial symmetry breaking term
        symmetry_break = 0.0
        for i in range(self.dim):
            symmetry_break += 0.1 * (x[i]**4 - 2.0 * x[i]**2)
        
        # Add a global scaling factor and return final function value
        return 1.0 * radial_term + 0.8 * modal_term + 0.6 * coupling_term + 0.4 * symmetry_break