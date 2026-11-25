import numpy as np

class ChaoticRidgeMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponentially decaying correlation structure across dimensions
        corr = np.sum([
            np.exp(-i * 0.3) * x_norm[i] * x_norm[(i + 1) % self.dim]
            for i in range(self.dim)
        ])
        
        # Sine-wave modulated ridges with varying frequencies and amplitudes
        ridge = 0
        for i in range(self.dim):
            freq = 2**(i % 4 + 1)
            amp = 1.0 / (i + 1)
            ridge += amp * np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[(i + 1) % self.dim])
        
        # Asymmetric basin structure with chaotic attractor-like behavior
        basin = 0
        for i in range(self.dim):
            basin += (np.sin(x_norm[i]**3) * np.exp(-x_norm[i]**2) + 
                     0.5 * np.cos(3 * x_norm[i]) * np.exp(-abs(x_norm[i])))
        
        # Multi-scale periodic modulation with chaotic phase shifts
        mod = 0
        for i in range(self.dim):
            mod += np.sin(10 * x_norm[i] + np.sin(7 * x_norm[i])) * np.cos(5 * x_norm[i])
        
        # Combined chaotic landscape with adaptive conditioning
        r = np.sqrt(np.sum(x_norm**2))
        cond = 1.0 + 1.5 * (1.0 - np.exp(-r / 3.0))
        
        # Final function value with asymmetric scaling and chaotic interference
        return cond * (corr + ridge + basin + mod) * (1.0 + 0.4 * np.sin(2 * r) * np.cos(3 * r))