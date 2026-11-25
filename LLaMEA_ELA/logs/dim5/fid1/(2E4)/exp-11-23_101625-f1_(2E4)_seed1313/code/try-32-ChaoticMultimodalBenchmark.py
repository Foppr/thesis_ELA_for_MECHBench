import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with adaptive scaling
        result = 0.8 * np.sum(x**2)
        
        # Nested chaotic sinusoidal terms with varying frequencies and modulations
        for i in range(self.dim):
            freq1 = 3 * (i + 1) ** 1.5
            freq2 = 7 * (i + 1) ** 0.8
            amp1 = 0.6 * (i + 1) ** -0.5
            amp2 = 0.4 * (i + 1) ** -0.3
            result += amp1 * np.sin(freq1 * x[i]) * np.cos(freq2 * x[i] * 0.7)
            result += amp2 * np.sin(freq2 * x[i]**2) * np.cos(freq1 * x[i])
            
        # Adaptive polynomial interaction terms with dynamic coupling strength
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited range for complexity
                coupling = 0.2 * (i + j + 1) ** -0.7
                interaction = (x[i]**3 + x[j]**3) * np.exp(-0.2 * (x[i] - x[j])**2)
                result += coupling * interaction
                
        # Multi-scale dynamic saddle-point structure with varying depths
        for i in range(self.dim):
            result += 0.4 * (np.sin(3.0 * x[i]) * np.cos(4.0 * x[i]) + 
                           0.5 * np.sin(6.0 * x[i]) * np.cos(2.0 * x[i]) +
                           0.3 * np.sin(8.0 * x[i]) * np.cos(5.0 * x[i]))
            
        # Exponentially decaying high-frequency oscillations with chaotic modulation
        for i in range(self.dim):
            result += 0.2 * np.sin(15 * x[i]) * np.exp(-0.1 * x[i]**2) * np.cos(0.5 * np.sum(x**2))
            
        # Asymmetric penalty with irregular critical points and non-linear transformations
        critical_points = np.array([1.5, -2.0, 2.5, -3.0, 0.8, -1.2, 1.8, -2.2])
        penalties = []
        for i in range(min(8, self.dim)):
            diff = x[i] - critical_points[i]
            penalties.append(diff**6 * np.exp(-0.5 * diff**2))
        result += 0.15 * np.sum(penalties)
            
        # Additional chaotic modulation with dynamic phase shifts
        chaos_mod = 0.08 * np.sin(np.sum(x**3) * 0.4 + np.sum(np.sin(x)) * 0.2)
        result += chaos_mod
        
        # Gradient irregularity term with local field variations
        grad_irregularity = 0.05 * np.sum(np.sin(10 * x) * np.cos(8 * x))
        result += grad_irregularity
        
        return result