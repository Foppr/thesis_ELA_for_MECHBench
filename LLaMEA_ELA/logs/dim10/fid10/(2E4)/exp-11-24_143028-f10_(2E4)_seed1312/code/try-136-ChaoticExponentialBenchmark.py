import numpy as np

class ChaoticExponentialBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential radial basis components with varying scales
        result = 0.0
        for i in range(self.dim):
            result += 2.7 * np.exp(-0.5 * (x[i] - 1.8)**2) + 2.0 * np.exp(-0.3 * (x[i] + 2.8)**2) + 1.4 * np.exp(-0.7 * (x[i] - 1.2)**2)
        
        # Trigonometric coupling between dimensions with exponential decay
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                coupling = 1.6 * np.exp(-0.2 * (x[i] - x[j])**2)
                result += coupling * np.sin(8.5 * x[i]) * np.cos(6.5 * x[j])
        
        # Chaotic sine-wave modulation with dynamic frequency
        chaos_mod = 1.0
        for i in range(self.dim):
            chaos_mod *= np.sin(14.5 * x[i] + np.sin(7.5 * x[i])) + 1.25
        result += 2.2 * chaos_mod
        
        # Cross-dimensional polynomial interactions with exponential weights
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.9 * (x[i]**3 + x[j]**3) * np.exp(-0.1 * (x[i] - x[j])**2)
        
        # Asymmetric exponential penalties near boundaries
        for i in range(self.dim):
            if x[i] < 0:
                result += 1.8 * np.exp(-0.4 * (x[i] + 5.0)**2) * (1 + 0.5 * np.sin(15.5 * x[i]))
            else:
                result += 1.4 * np.exp(-0.3 * (x[i] - 5.0)**2) * (1 + 0.4 * np.cos(12.5 * x[i]))
        
        # High-frequency oscillatory terms with polynomial weights
        for i in range(self.dim):
            result += 1.2 * x[i]**4 * np.sin(25.5 * x[i]) * np.cos(20.5 * x[i])
        
        # Fractal-like structure using recursive cosine and exponential components
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += np.cos(30.5 * x[i]) * np.exp(-0.1 * x[i]**2)
        result += 1.5 * fractal_term**2
        
        # Dynamic conditioning with multi-scale sine waves
        condition_factor = 1.0
        for i in range(self.dim):
            condition_factor *= (1 + 0.35 * np.sin(10.5 * x[i]) * np.cos(8.5 * x[i]))
        result += 1.7 * condition_factor
        
        # Additional cross-dimensional exponential coupling with cosine modulation
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                result += 0.95 * np.exp(-0.2 * (x[i] - x[j])**2) * np.cos(5.5 * (x[i] + x[j]))
        
        # Global harmonic structure with weighted polynomial components
        harmonic_sum = 0.0
        for i in range(self.dim):
            harmonic_sum += np.sin(6.5 * x[i]) * np.cos(5.5 * x[i]) * np.exp(-0.15 * x[i]**2)
        result += 1.35 * harmonic_sum**2
        
        # Noise injection with chaotic sine-wave components
        noise = 0.0
        for i in range(self.dim):
            noise += 0.45 * np.sin(40.5 * x[i]) * np.cos(35.5 * x[i])
        result += noise
        
        return result