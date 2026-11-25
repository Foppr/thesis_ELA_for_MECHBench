import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Add chaotic sine-cosine coupling with varying frequencies and amplitudes
        for i in range(self.dim):
            freq1 = 6 + (i % 8) * 2
            freq2 = 4 + (i % 6) * 3
            coupling = np.sin(freq1 * x[i]) * np.cos(freq2 * x[i])
            result += 0.6 * coupling * np.exp(-0.15 * np.abs(x[i]))
            
        # Add nested exponential decay with sinusoidal modulation
        for i in range(self.dim):
            exp_decay = np.exp(-0.3 * (x[i] - 1.2)**2)
            sin_mod = np.sin(12 * x[i]) + 0.6 * np.sin(28 * x[i])
            result += 0.35 * exp_decay * sin_mod
            
        # Add multi-scale frequency components with asymmetric peaks
        for i in range(self.dim):
            freqs = [9, 13, 19, 26]
            asym_peak = 0.45 * np.sin(16 * x[i]) * np.exp(-0.35 * (x[i] - 0.6)**2)
            result += asym_peak
            
        # Add cross-dimensional interactions with exponential scaling
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                dist = np.abs(x[i] - x[j])
                interaction = np.exp(-0.6 * dist) * np.sin(22 * (x[i] + x[j]))
                result += 0.2 * interaction
                
        # Add irregular multi-modal structure with varying amplitudes
        for i in range(self.dim):
            result += 0.3 * np.sin(32 * x[i]) * np.cos(16 * x[i]) * np.exp(-0.12 * (x[i] + 2.2)**2)
            
        # Add high-frequency chaotic component
        for i in range(self.dim):
            result += 0.2 * np.sin(75 * x[i]) * np.cos(50 * x[i])
            
        # Add asymmetric ridge coupling with exponential weighting
        for i in range(self.dim):
            ridge = np.exp(-0.25 * (x[i] - 1.3)**2) * np.sin(27 * x[i])
            result += 0.14 * ridge
            
        # Add irregular global minimum structure
        for i in range(self.dim):
            result += 0.35 * np.exp(-0.35 * (x[i] + 1.9)**2) * np.cos(42 * x[i])
            
        return result