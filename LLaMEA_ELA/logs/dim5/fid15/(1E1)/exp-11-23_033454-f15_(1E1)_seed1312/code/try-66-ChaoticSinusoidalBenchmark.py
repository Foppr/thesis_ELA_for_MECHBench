import numpy as np

class ChaoticSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for chaotic behavior
        self.freq_factors = np.random.uniform(1.0, 3.0, dim)
        self.ampl_factors = np.random.uniform(0.5, 2.0, dim)
        self.phase_shifts = np.random.uniform(0, 2*np.pi, dim)
        
    def f(self, x):
        if len(x) != self.dim:
            if len(x) < self.dim:
                x = np.pad(x, (0, self.dim - len(x)), mode='constant', constant_values=0.0)
            else:
                x = x[:self.dim]
        
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        quadratic = 0.1 * np.sum(x**2)
        
        # Chaotic sinusoidal modulations with nested frequencies
        sinusoidal = 0.0
        for i in range(self.dim):
            freq = self.freq_factors[i]
            ampl = self.ampl_factors[i]
            phase = self.phase_shifts[i]
            # Nested modulation: higher frequency on top of lower frequency
            sinusoidal += ampl * np.sin(freq * x[i] + phase) * np.cos(0.5 * freq * x[i] + phase)
        
        # Add saddle-point structure through cross-dimensional interactions
        saddle = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Create saddle points with interaction terms
                saddle += 0.3 * np.sin(0.5 * (x[i] + x[j])) * np.cos(0.3 * (x[i] - x[j]))
        
        # Introduce chaotic behavior through exponential scaling of gradients
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.exp(-0.1 * abs(x[i])) * np.sin(2.0 * x[i])
        
        return quadratic + sinusoidal + saddle + chaotic