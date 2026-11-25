import numpy as np

class ChaoticRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.ridge_count = 3
        self.frequency_base = 1.0
        self.amplitude_base = 2.0
        self.decay_factor = 0.5
        self.coupling_strength = 0.3
        
    def f(self, x):
        # Handle dimension mismatch
        if len(x) < self.dim:
            raise ValueError("Dimension mismatch: input has fewer dimensions than expected")
        elif len(x) > self.dim:
            x = x[:self.dim]
        
        # Scale input to [-5, 5] range if needed
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize function value
        result = 0.0
        
        # Ridge structures with exponential decay and sinusoidal modulation
        for i in range(self.ridge_count):
            # Dynamic frequency and amplitude based on ridge index
            freq = self.frequency_base * (1 + 0.2 * np.sin(i))
            amp = self.amplitude_base * (1 + 0.1 * np.cos(i))
            
            # Ridge position with chaotic modulation
            ridge_pos = i * 1.5 + 0.3 * np.sin(x[0] if len(x) > 0 else 0)
            
            # Ridge function with exponential decay and sinusoidal components
            ridge_val = 0.0
            for j in range(self.dim):
                xi = x[j]
                # Exponential decay with chaotic modulation of decay rate
                decay_rate = self.decay_factor * (1 + 0.2 * np.sin(xi * 3.1))
                exp_term = np.exp(-decay_rate * np.abs(xi - ridge_pos))
                
                # Sinusoidal modulation
                sin_term = np.sin(freq * xi + i * np.pi / 4)
                cos_term = np.cos(freq * xi + i * np.pi / 3)
                
                ridge_val += amp * exp_term * sin_term * cos_term
            
            result += ridge_val**2
        
        # Cross-dimensional coupling with adaptive weights
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Adaptive coupling strength based on input values
                weight = self.coupling_strength * (1 + 0.2 * np.sin(x[i] * x[j]))
                coupling += weight * np.exp(-0.1 * (x[i] - x[j])**2) * np.sin(x[i] + x[j])
        
        # Asymmetric scaling with chaotic modulation
        scale_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Chaotic modulation of scaling factor
            scale_factor = 1.0 + 0.3 * np.sin(xi * 2.7)
            scale_term += scale_factor * (xi**2) * np.exp(-0.05 * xi**2)
        
        # Combine all components with proper weighting
        return 0.4 * result + 0.3 * coupling + 0.3 * scale_term