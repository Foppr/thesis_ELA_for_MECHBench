import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Chaotic sinusoidal terms with varying frequencies and amplitudes
        for i in range(self.dim):
            freq = 3 * (i + 1) ** 1.5
            amp = 0.3 * (i + 1) ** -0.5
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7)
            
        # Polynomial interaction terms with cross-dimensional coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = (x[i]**3 + x[j]**3) * np.exp(-0.1 * (x[i] - x[j])**2)
                result += 0.1 * interaction
                
        # Saddle-point structure with multiple competing minima
        for i in range(self.dim):
            result += 0.2 * (np.sin(2 * x[i]) * np.cos(3 * x[i]) + 
                           0.5 * np.sin(4 * x[i]) * np.cos(2 * x[i]))
            
        # Multi-scale oscillation with varying amplitudes
        for i in range(self.dim):
            result += 0.1 * np.sin(10 * x[i]) * np.exp(-0.05 * x[i]**2)
            
        # Asymmetric penalty for deviation from critical points
        critical_points = np.array([1.0, -1.5, 2.0, -2.5])
        if self.dim >= 4:
            penalties = []
            for i in range(4):
                if i < self.dim:
                    penalties.append((x[i] - critical_points[i])**4)
            result += 0.08 * np.sum(penalties)
            
        return result