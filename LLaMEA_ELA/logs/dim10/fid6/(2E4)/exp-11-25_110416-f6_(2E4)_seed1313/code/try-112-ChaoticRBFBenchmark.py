import numpy as np

class ChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute logistic map sequence for chaotic behavior
        self.logistic_seq = np.array([0.5])
        for _ in range(dim * 10):
            self.logistic_seq = np.append(self.logistic_seq, 4 * self.logistic_seq[-1] * (1 - self.logistic_seq[-1]))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2) * 0.1
        
        # Add chaotic logistic map based modulation
        for i in range(self.dim):
            chaos_factor = self.logistic_seq[i % len(self.logistic_seq)]
            result += 0.5 * np.sin(10 * x[i] * chaos_factor) * np.cos(7 * x[i] * chaos_factor)
            
        # Add radial basis function components with chaotic centers
        for i in range(min(20, self.dim)):
            center = 5.0 * (i % 3 - 1) + 2.0 * np.sin(self.logistic_seq[i % len(self.logistic_seq)])
            sigma = 0.5 + 0.3 * np.cos(self.logistic_seq[(i+5) % len(self.logistic_seq)])
            result += 0.3 * np.exp(-0.5 * ((x[i] - center) / sigma)**2)
            
        # Add asymmetric cosine interactions with chaotic coupling
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                coupling = self.logistic_seq[(i+j) % len(self.logistic_seq)]
                asym_cos = np.cos(5 * x[i]) * np.sin(3 * x[j]) * (1 + 0.2 * coupling)
                result += 0.2 * asym_cos
                
        # Add multi-scale fractal-like oscillations
        for i in range(self.dim):
            freq = 2**((i % 5) + 1)
            result += 0.4 * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7) * np.exp(-0.1 * x[i]**2)
            
        # Add piecewise linear chaotic regions
        for i in range(self.dim):
            if x[i] < 0:
                result += 0.3 * (x[i] + 5) * np.sin(20 * x[i])
            else:
                result += 0.3 * (5 - x[i]) * np.cos(15 * x[i])
                
        # Add irregular high-frequency noise with chaotic amplitude
        for i in range(self.dim):
            noise_amp = 0.1 + 0.05 * np.sin(self.logistic_seq[i % len(self.logistic_seq)] * 100)
            result += noise_amp * np.sin(50 * x[i])
            
        # Add cross-dimensional fractal coupling
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                fractal_coupling = np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) * (x[i]**2 + x[j]**2)
                result += 0.15 * fractal_coupling
                
        return result