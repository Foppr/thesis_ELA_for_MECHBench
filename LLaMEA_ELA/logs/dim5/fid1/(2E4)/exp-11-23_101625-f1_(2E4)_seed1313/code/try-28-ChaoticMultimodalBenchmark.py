import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Enhanced chaotic sinusoidal terms with stronger frequency modulation and amplitude scaling
        for i in range(self.dim):
            freq = 6 * (i + 1) ** 1.8
            amp = 0.6 * (i + 1) ** -0.5
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7)
            
        # Higher-order polynomial interaction terms with non-linear coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = (x[i]**5 + x[j]**5) * np.exp(-0.2 * (x[i] - x[j])**2)
                result += 0.2 * interaction
                
        # Dynamic saddle-point structure with multi-scale competing minima
        for i in range(self.dim):
            result += 0.35 * (np.sin(2.8 * x[i]) * np.cos(3.2 * x[i]) + 
                           0.7 * np.sin(4.2 * x[i]) * np.cos(2.8 * x[i]))
            
        # Multi-scale oscillation with exponential decay and increased frequency
        for i in range(self.dim):
            result += 0.2 * np.sin(13 * x[i]) * np.exp(-0.08 * x[i]**2)
            
        # Asymmetric penalty with more complex critical point arrangement
        critical_points = np.array([1.3, -1.9, 2.1, -2.7, 0.6, -0.8])
        if self.dim >= 6:
            penalties = []
            for i in range(6):
                if i < self.dim:
                    penalties.append((x[i] - critical_points[i])**4)
            result += 0.15 * np.sum(penalties)
            
        # Additional chaotic modulation term to increase landscape irregularity
        chaos_mod = 0.06 * np.sin(np.sum(x**2) * 0.35)
        result += chaos_mod
        
        return result