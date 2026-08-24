import numpy as np

class ChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequence for spatial variation
        self.chaos_seq = np.array([np.sin(2**i * np.pi * 0.12345) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f_value = np.sum(x**2)
        
        # Add chaotic radial basis functions with varying widths
        for i in range(self.dim):
            # Use chaotic sequence for center placement
            center = 5.0 * self.chaos_seq[i]
            width = 0.5 + 0.5 * np.sin(i * 0.789)
            f_value += 2.0 * np.exp(-0.5 * ((x[i] - center) / width)**2)
            
        # Introduce asymmetric sine-wave modulations with chaotic frequencies
        for i in range(self.dim):
            freq = 2.0 + 3.0 * self.chaos_seq[i]
            amp = 1.0 + 0.5 * np.cos(i * 0.456)
            phase = np.pi * self.chaos_seq[i]
            f_value += amp * np.sin(freq * x[i] + phase) * np.abs(np.sin(freq * x[i]))
            
        # Add a multi-scale chaotic landscape component
        for i in range(self.dim):
            scale = 1.0 + 2.0 * np.abs(np.sin(self.chaos_seq[i] * 10))
            f_value += 0.5 * scale * np.sin(5 * x[i]) * np.cos(3 * x[i]) * np.tanh(x[i])
            
        # Cross-variable chaotic interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Use chaotic coupling strength
                coupling = 0.3 * (1 + self.chaos_seq[i] * self.chaos_seq[j])
                f_value += coupling * np.sin(2 * x[i]) * np.cos(3 * x[j]) * np.exp(-0.1 * (x[i] - x[j])**2)
                
        # Add a logistic map inspired component
        logistic_base = 3.8 * (x % 1.0)  # Normalize to [0,1]
        f_value += 0.4 * np.sum(logistic_base * (1 - logistic_base))
        
        # Add a final chaotic modulation with varying amplitude
        final_mod = np.sum(np.sin(self.chaos_seq * x) * np.cos(self.chaos_seq * x))
        f_value += 0.3 * final_mod
        
        return f_value