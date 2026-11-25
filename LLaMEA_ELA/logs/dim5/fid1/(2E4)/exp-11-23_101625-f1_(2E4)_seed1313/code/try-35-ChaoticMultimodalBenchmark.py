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
            freq1 = 3.2 * (i + 1) ** 1.55
            freq2 = 7.3 * (i + 1) ** 0.85
            amp1 = 0.65 * (i + 1) ** -0.55
            amp2 = 0.45 * (i + 1) ** -0.35
            result += amp1 * np.sin(freq1 * x[i]) * np.cos(freq2 * x[i] * 0.75)
            result += amp2 * np.sin(freq2 * x[i]**2) * np.cos(freq1 * x[i])
            
        # Adaptive polynomial interaction terms with dynamic coupling strength
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited range for complexity
                coupling = 0.25 * (i + j + 1) ** -0.75
                interaction = (x[i]**3 + x[j]**3) * np.exp(-0.25 * (x[i] - x[j])**2)
                result += coupling * interaction
                
        # Multi-scale dynamic saddle-point structure with varying depths
        for i in range(self.dim):
            result += 0.45 * (np.sin(3.2 * x[i]) * np.cos(4.2 * x[i]) + 
                           0.55 * np.sin(6.2 * x[i]) * np.cos(2.2 * x[i]) +
                           0.35 * np.sin(8.2 * x[i]) * np.cos(5.2 * x[i]))
            
        # Exponentially decaying high-frequency oscillations with chaotic modulation
        for i in range(self.dim):
            result += 0.22 * np.sin(15.5 * x[i]) * np.exp(-0.12 * x[i]**2) * np.cos(0.55 * np.sum(x**2))
            
        # Asymmetric penalty with irregular critical points and non-linear transformations
        critical_points = np.array([1.6, -2.1, 2.6, -3.1, 0.9, -1.3, 1.9, -2.3])
        penalties = []
        for i in range(min(8, self.dim)):
            diff = x[i] - critical_points[i]
            penalties.append(diff**6 * np.exp(-0.55 * diff**2))
        result += 0.16 * np.sum(penalties)
            
        # Additional chaotic modulation with dynamic phase shifts
        chaos_mod = 0.09 * np.sin(np.sum(x**3) * 0.45 + np.sum(np.sin(x)) * 0.25)
        result += chaos_mod
        
        # Gradient irregularity term with local field variations
        grad_irregularity = 0.06 * np.sum(np.sin(10.5 * x) * np.cos(8.5 * x))
        result += grad_irregularity
        
        return result