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
            freq1 = 5 + (i % 7) * 2
            freq2 = 3 + (i % 5) * 3
            coupling = np.sin(freq1 * x[i]) * np.cos(freq2 * x[i])
            result += 0.5 * coupling * np.exp(-0.1 * np.abs(x[i]))
            
        # Add nested exponential decay with sinusoidal modulation
        for i in range(self.dim):
            exp_decay = np.exp(-0.2 * (x[i] - 1.0)**2)
            sin_mod = np.sin(10 * x[i]) + 0.5 * np.sin(25 * x[i])
            result += 0.3 * exp_decay * sin_mod
            
        # Add multi-scale frequency components with asymmetric peaks
        for i in range(self.dim):
            freqs = [8, 12, 18, 25]
            asym_peak = 0.4 * np.sin(15 * x[i]) * np.exp(-0.3 * (x[i] - 0.5)**2)
            result += asym_peak
            
        # Add cross-dimensional interactions with exponential scaling
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                dist = np.abs(x[i] - x[j])
                interaction = np.exp(-0.5 * dist) * np.sin(20 * (x[i] + x[j]))
                result += 0.15 * interaction
                
        # Add irregular multi-modal structure with varying amplitudes
        for i in range(self.dim):
            result += 0.25 * np.sin(30 * x[i]) * np.cos(15 * x[i]) * np.exp(-0.1 * (x[i] + 2.0)**2)
            
        # Add high-frequency chaotic component
        for i in range(self.dim):
            result += 0.18 * np.sin(70 * x[i]) * np.cos(45 * x[i])
            
        # Add asymmetric ridge coupling with exponential weighting
        for i in range(self.dim):
            ridge = np.exp(-0.2 * (x[i] - 1.2)**2) * np.sin(25 * x[i])
            result += 0.12 * ridge
            
        # Add irregular global minimum structure
        for i in range(self.dim):
            result += 0.3 * np.exp(-0.3 * (x[i] + 1.8)**2) * np.cos(40 * x[i])
            
        return result