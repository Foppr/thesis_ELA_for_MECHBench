import numpy as np

class ChaoticSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute key parameters for the chaotic landscape
        self.coefficients = np.random.uniform(-1.0, 1.0, size=(dim, 5))
        self.frequencies = np.random.uniform(1.0, 5.0, size=dim)
        self.amplitudes = np.random.uniform(0.5, 2.0, size=dim)
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
        
        # Apply polynomial basin term
        basin = np.sum((x / 5.0)**4)
        
        # Add chaotic sinusoidal components
        chaotic = 0.0
        for i in range(self.dim):
            # Multiple sinusoidal waves with different frequencies and amplitudes
            wave = 0.0
            for j in range(3):
                freq = self.frequencies[i] * (j + 1)
                amp = self.amplitudes[i] * (j + 1)
                wave += amp * np.sin(freq * x[i])
            
            # Add chaotic modulation using neighboring dimensions
            if i > 0:
                modulator = np.sin(x[i-1] * 0.5) * 0.3
                wave *= (1.0 + modulator)
                
            chaotic += wave
        
        # Add noise term for additional complexity
        noise = np.random.normal(0, 0.05)
        
        return basin + chaotic + noise