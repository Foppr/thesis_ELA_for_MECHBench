import numpy as np

class ChaoticOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
        
        # Scale input to [-1, 1] for computation
        x_scaled = x / 5.0
        
        # Base quadratic term creating a central attraction
        quadratic = np.sum(x_scaled ** 2)
        
        # Chaotic exponential terms with varying decay rates
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.exp(-10 * np.abs(x_scaled[i])) * np.sin(5 * x_scaled[i]) * (i + 1)
            
        # Trigonometric oscillations creating complex interference patterns
        trig = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                trig += np.cos(x_scaled[i] * x_scaled[j]) * np.sin(2 * (x_scaled[i] + x_scaled[j]))
                
        # Add a global sinusoidal modulation
        modulation = np.sin(np.sum(x_scaled) * 3) * 0.5
        
        return quadratic + chaotic + trig + modulation