import numpy as np

class ChaoticExponentialBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential radial basis components with varying scales and amplitudes
        result = 0.0
        for i in range(self.dim):
            result += 2.8 * np.exp(-0.4 * (x[i] - 2.0)**2) + 2.1 * np.exp(-0.2 * (x[i] + 3.0)**2) + 1.5 * np.exp(-0.6 * (x[i] - 1.0)**2)
        
        # Trigonometric coupling between dimensions with exponential decay and phase modulation
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                coupling = 1.8 * np.exp(-0.15 * (x[i] - x[j])**2)
                result += coupling * np.sin(9 * x[i] + 0.5 * np.sin(3 * x[i])) * np.cos(7 * x[j] + 0.3 * np.sin(2 * x[j]))
        
        # Chaotic sine-wave modulation with dynamic frequency and amplitude
        chaos_mod = 1.0
        for i in range(self.dim):
            chaos_mod *= np.sin(15 * x[i] + np.sin(8 * x[i])) + 1.3
        result += 2.2 * chaos_mod
        
        # Cross-dimensional polynomial interactions with exponential weights and higher-order terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.9 * (x[i]**4 + x[j]**4) * np.exp(-0.15 * (x[i] - x[j])**2)
        
        # Asymmetric exponential penalties near boundaries with enhanced boundary sensitivity
        for i in range(self.dim):
            if x[i] < 0:
                result += 2.0 * np.exp(-0.3 * (x[i] + 5.0)**2) * (1 + 0.6 * np.sin(18 * x[i]))
            else:
                result += 1.5 * np.exp(-0.25 * (x[i] - 5.0)**2) * (1 + 0.5 * np.cos(14 * x[i]))
        
        # High-frequency oscillatory terms with polynomial weights and increased complexity
        for i in range(self.dim):
            result += 1.3 * x[i]**5 * np.sin(30 * x[i]) * np.cos(25 * x[i])
        
        # Fractal-like structure using recursive cosine and exponential components with enhanced scaling
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += np.cos(35 * x[i]) * np.exp(-0.12 * x[i]**2)
        result += 1.6 * fractal_term**2
        
        # Dynamic conditioning with multi-scale sine waves and enhanced coupling
        condition_factor = 1.0
        for i in range(self.dim):
            condition_factor *= (1 + 0.4 * np.sin(12 * x[i]) * np.cos(9 * x[i]))
        result += 1.8 * condition_factor
        
        # Additional cross-dimensional exponential coupling with cosine modulation and phase shifts
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                result += 1.1 * np.exp(-0.15 * (x[i] - x[j])**2) * np.cos(6 * (x[i] + x[j]) + 0.2 * np.sin(4 * x[i]))
        
        # Global harmonic structure with weighted polynomial components and enhanced complexity
        harmonic_sum = 0.0
        for i in range(self.dim):
            harmonic_sum += np.sin(7 * x[i]) * np.cos(6 * x[i]) * np.exp(-0.2 * x[i]**2)
        result += 1.5 * harmonic_sum**2
        
        # Noise injection with chaotic sine-wave components and increased variability
        noise = 0.0
        for i in range(self.dim):
            noise += 0.5 * np.sin(45 * x[i]) * np.cos(40 * x[i])
        result += noise
        
        return result