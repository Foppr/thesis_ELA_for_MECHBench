import numpy as np

class ChaoticOscillatorLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters
        self.omega = np.pi * (1.0 + np.random.rand(dim) * 2.0)
        self.gamma = 0.5 + np.random.rand(dim) * 1.5
        self.alpha = 0.1 + np.random.rand(dim) * 0.4
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic oscillator component
        chaotic = 0.0
        for i in range(self.dim):
            # Phase-coupled oscillators with chaotic modulation
            phase = self.omega[i] * x[i] + np.sin(x[(i+1) % self.dim]) * self.gamma[i]
            chaotic += np.sin(phase) * np.exp(-self.alpha[i] * np.abs(x[i]))
        
        # Recursive trigonometric fractal component
        fractal = 0.0
        for i in range(self.dim):
            # Build fractal-like structure through recursive sine/cosine
            val = x[i]
            for _ in range(3):
                val = np.sin(val) + np.cos(val * 0.5)
            fractal += val * np.exp(-0.1 * np.abs(x[i]))
        
        # Multi-scale interaction with varying coupling strengths
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Distance-based coupling with periodic modulation
                dist = np.abs(x[i] - x[j])
                coupling += np.sin(dist * 2.0) * np.exp(-0.05 * dist) * (i + j + 1)
        
        # Asymmetric basin landscape with polynomial and exponential mixing
        basin = 0.0
        for i in range(self.dim):
            # Asymmetric polynomial with exponential scaling
            if x[i] >= 0:
                basin += (x[i] ** 2.5) * np.exp(-0.2 * x[i])
            else:
                basin += (x[i] ** 3.5) * np.exp(0.1 * x[i])
        
        # Cross-dimensional resonance with harmonic coupling
        resonance = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Harmonic coupling with phase differences
                coupling_term = np.sin(x[i] * x[j] * 0.3) * np.cos(x[i] + x[j] * 0.7)
                resonance += coupling_term * np.exp(-0.02 * (x[i]**2 + x[j]**2))
        
        # Fractional dimensionality effect with logarithmic scaling
        fractional = 0.0
        for i in range(self.dim):
            fractional += np.log(np.abs(x[i]) + 1.0) * np.sin(x[i] * 0.5)
        
        # Combine all components with adaptive weights
        weights = np.array([0.8, 0.7, 0.6, 0.9, 0.5, 0.4])
        components = np.array([chaotic, fractal, coupling, basin, resonance, fractional])
        return np.sum(weights * components)