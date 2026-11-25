import numpy as np

class ChaoticRidgeMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced exponentially decaying correlation structure with modified decay rate
        corr = np.sum([
            np.exp(-i * 0.3) * x_norm[i] * x_norm[(i + 1) % self.dim]
            for i in range(self.dim)
        ])
        
        # Sine-wave modulated ridges with altered frequencies and amplitudes
        ridge = 0
        for i in range(self.dim):
            freq = 4**(i % 4 + 1)  # Changed from 3** to 4** for even higher frequencies
            amp = 2.0 / (i + 1)    # Increased amplitude scaling
            ridge += amp * np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[(i + 1) % self.dim])
        
        # Asymmetric basin structure with modified chaotic behavior and increased complexity
        basin = 0
        for i in range(self.dim):
            basin += (np.sin(x_norm[i]**3) * np.exp(-x_norm[i]**2) + 
                     0.8 * np.cos(3 * x_norm[i]) * np.exp(-abs(x_norm[i])) +
                     0.3 * np.sin(5 * x_norm[i]) * np.exp(-x_norm[i]**4))  # Added higher-order sinusoidal component
        
        # Multi-scale periodic modulation with altered phase shifts and increased complexity
        mod = 0
        for i in range(self.dim):
            mod += np.sin(15 * x_norm[i] + np.sin(10 * x_norm[i])) * np.cos(7 * x_norm[i])  # Changed frequencies
        
        # Combined chaotic landscape with modified conditioning and enhanced difficulty
        r = np.sqrt(np.sum(x_norm**2))
        cond = 1.0 + 3.0 * (1.0 - np.exp(-r / 2.0))  # Increased conditioning strength
        
        # Final function value with modified scaling and interference
        return cond * (corr + ridge + basin + mod) * (1.0 + 0.6 * np.sin(2 * r) * np.cos(3 * r))