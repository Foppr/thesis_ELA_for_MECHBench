import numpy as np

class ChaoticRidgeMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponentially decaying correlation structure with modified decay rate
        corr = np.sum([
            np.exp(-i * 0.4) * x_norm[i] * x_norm[(i + 1) % self.dim]
            for i in range(self.dim)
        ])
        
        # Sine-wave modulated ridges with altered frequencies and amplitudes
        ridge = 0
        for i in range(self.dim):
            freq = 3**(i % 3 + 1)  # Changed from 2** to 3** for higher frequencies
            amp = 1.5 / (i + 1)    # Increased amplitude scaling
            ridge += amp * np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[(i + 1) % self.dim])
        
        # Asymmetric basin structure with modified chaotic behavior
        basin = 0
        for i in range(self.dim):
            basin += (np.sin(x_norm[i]**3) * np.exp(-x_norm[i]**2) + 
                     0.7 * np.cos(3 * x_norm[i]) * np.exp(-abs(x_norm[i])))  # Increased cosine weight
        
        # Multi-scale periodic modulation with altered phase shifts
        mod = 0
        for i in range(self.dim):
            mod += np.sin(12 * x_norm[i] + np.sin(8 * x_norm[i])) * np.cos(6 * x_norm[i])  # Changed frequencies
        
        # Combined chaotic landscape with modified conditioning
        r = np.sqrt(np.sum(x_norm**2))
        cond = 1.0 + 2.0 * (1.0 - np.exp(-r / 2.5))  # Increased conditioning strength
        
        # Final function value with modified scaling and interference
        return cond * (corr + ridge + basin + mod) * (1.0 + 0.5 * np.sin(2 * r) * np.cos(3 * r))