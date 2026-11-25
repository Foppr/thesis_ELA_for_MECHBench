import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Base quadratic term for conditioning
        quadratic = 0.1 * np.sum(x**2)
        
        # Sinusoidal waves with varying frequencies and amplitudes
        sinusoidal = 0.0
        for i in range(self.dim):
            freq = (i + 1) * 2.0
            amp = 1.0 / (i + 1)
            sinusoidal += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Polynomial penalty terms to create complex landscape
        polynomial = 0.0
        for i in range(self.dim):
            polynomial += (x[i]**4 - 2*x[i]**2 + 1) * (i + 1) * 0.1
            
        # Chaotic component using logistic map-like behavior
        chaotic = 0.0
        for i in range(self.dim):
            if i > 0:
                chaotic += np.sin(x[i-1] * x[i]) * 0.5
                
        # Add noise and scaling
        noise = np.sum(np.random.randn(self.dim) * 0.01)
        
        return quadratic + sinusoidal + polynomial + chaotic + noise