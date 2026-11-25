import numpy as np

class ChaoticInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.num_waves = 6
        self.noise_std = 0.1
        self.time_factor = 0.05
        
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
        
        # Generate time-varying wave parameters
        for i in range(self.num_waves):
            # Chaotic frequency and phase modulation
            freq = 1.0 + 0.5 * np.sin(i * 2.3 + self.time_factor * np.sum(x))
            phase = 0.5 * np.cos(i * 1.7 + self.time_factor * np.sum(x**2))
            
            # Wave interference pattern
            wave_contrib = np.sin(freq * np.sum(x) + phase)
            
            # Adaptive amplitude based on position
            amp = 1.0 + 0.3 * np.sin(i * 0.8 + np.mean(x)**2)
            
            # Add to result with dynamic weighting
            result += amp * wave_contrib
            
        # Spectral decomposition component
        spectral_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Frequency-dependent spectral weights
            weight = 1.0 + 0.2 * np.cos(i * 1.5)
            spectral_term += weight * (np.sin(xi * 3.0) + np.cos(xi * 2.0))
            
        # Adaptive noise modulation
        noise = self.noise_std * np.random.randn() * (1.0 + 0.1 * np.sum(x**2))
        
        # Condition number varying component
        cond_factor = 1.0 + 0.5 * np.sin(np.sum(x)**2)
        
        # Combine all components
        return cond_factor * (0.3 * result + 0.5 * spectral_term) + noise