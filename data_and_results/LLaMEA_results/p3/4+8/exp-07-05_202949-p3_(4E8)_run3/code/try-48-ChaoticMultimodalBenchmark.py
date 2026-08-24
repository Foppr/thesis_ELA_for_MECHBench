import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with asymmetric scaling
        result = 0.0
        for i in range(self.dim):
            if x[i] >= 0:
                result += 0.5 * (x[i] - 2.0)**2
            else:
                result += 0.3 * (x[i] + 2.0)**2
        
        # Nested oscillatory components with varying frequencies
        for i in range(self.dim):
            result += 0.1 * np.sin(10.0 * x[i]) * np.cos(7.0 * x[i]) + 0.05 * np.sin(15.0 * x[i])
        
        # Asymmetric interaction terms with dynamic scaling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic scaling based on dimension indices
                scale = (i + 1) * (j + 1) * 0.01
                diff = x[i] - x[j]
                result += scale * (diff**2 + 0.1 * diff**4)
        
        # Chaotic basin structure with exponential modulation
        chaos_term = 0.0
        for i in range(self.dim):
            chaos_term += np.exp(-0.5 * x[i]**2) * np.sin(2.0 * np.pi * x[i])
        result += 0.2 * chaos_term
        
        # Multi-scale periodicity with non-uniform frequency distribution
        periodicity = 0.0
        freqs = [1.0, 2.5, 4.0, 6.0, 8.5]
        for i in range(self.dim):
            for k, freq in enumerate(freqs):
                if k % 2 == 0:
                    periodicity += 0.03 * np.sin(freq * x[i])
                else:
                    periodicity += 0.02 * np.cos(freq * x[i])
        result += periodicity
        
        # Asymmetric polynomial terms to create skewed local minima
        for i in range(self.dim):
            if x[i] >= 0:
                result += 0.005 * x[i]**5 + 0.001 * x[i]**7
            else:
                result += 0.003 * x[i]**5 + 0.002 * x[i]**7
        
        # Add a global distortion term to shift the optimal region
        distortion = 0.0
        for i in range(self.dim):
            distortion += 0.01 * (x[i] - 1.0)**3
        result += distortion
        
        return result