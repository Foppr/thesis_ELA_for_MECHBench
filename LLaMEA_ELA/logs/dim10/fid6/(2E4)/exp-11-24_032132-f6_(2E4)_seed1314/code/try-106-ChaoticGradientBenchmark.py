import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.peak_count = 5
        self.frequency_base = 2.0
        self.amplitude_scale = 1.5
        self.phase_shift = np.pi / 4
        
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
        
        # Multiple interacting peaks with chaotic phase shifts
        for i in range(self.peak_count):
            # Dynamic frequency and amplitude based on peak index
            freq = self.frequency_base * (1 + 0.3 * np.sin(i))
            amp = self.amplitude_scale * (1 + 0.2 * np.cos(i))
            
            # Phase shift with chaotic component
            phase = i * self.phase_shift + 0.1 * np.sin(x[0] if len(x) > 0 else 0)
            
            # Peak function with non-linear transformation
            peak_val = 0.0
            for j in range(self.dim):
                xi = x[j]
                # Chaotic interaction term between dimensions
                interaction = np.sin(freq * xi + phase) * np.cos(freq * xi + phase * 1.5)
                peak_val += amp * np.exp(-0.1 * (xi - i)**2) * interaction
            
            result += peak_val**2
        
        # Cross-dimensional interference with dynamic coupling
        interference = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic coupling strength based on dimension indices
                coupling_strength = 0.5 * (1 + np.sin(0.3 * (i + j)))
                interference += coupling_strength * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
        
        # Asymmetric exponential decay with chaotic modulation
        decay_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Chaotic modulation of decay rate
            decay_rate = 0.2 + 0.1 * np.sin(xi * 2.3)
            decay_term += np.exp(-decay_rate * np.abs(xi)) * np.sin(xi * 4.1)
        
        # Combine all components with proper scaling
        return 0.3 * result + 0.4 * interference + 0.3 * decay_term