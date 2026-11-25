import numpy as np

class ChaoticPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial base with dynamic conditioning
        f1 = np.sum(x**4) + 0.5 * np.sum(x**3) + 0.2 * np.sum(x**2)
        
        # Dynamic sine-cosine interactions with adaptive coupling
        f2 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 1.0 + 0.3 * np.sin(0.5 * (i - j) + 0.2 * np.sum(x))
                interaction = np.sin(x[i]) * np.cos(x[j]) + np.cos(x[i]) * np.sin(x[j])
                f2 += coupling * interaction * np.exp(-0.1 * (x[i]**2 + x[j]**2))
                
        # Adaptive radial conditioning with chaotic modulation
        r = np.sqrt(np.sum(x**2) + 1e-8)
        radial_factor = 1.0 + 0.5 * np.sin(0.3 * r) * np.cos(0.2 * r) * np.exp(-0.02 * r)
        
        # Multi-scale boundary penalties
        f3 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                penalty = 2.0 * (5.0 - np.abs(x[i]))**3
                f3 += penalty * np.exp(-0.1 * x[i]**2)
                
        # Chaotic cross-dimensional terms with time-varying coefficients
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                time_coeff = 0.8 + 0.4 * np.sin(0.1 * (i + j) + 0.3 * r)
                f4 += time_coeff * x[i]**2 * x[j] * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                
        # Enhanced harmonic interactions with exponential weights
        f5 = 0.0
        for i in range(self.dim):
            freq1 = 2.0 + 3.0 * np.sin(0.2 * i + 0.1 * r)
            freq2 = 1.5 + 2.5 * np.cos(0.15 * i + 0.2 * r)
            f5 += (np.sin(freq1 * x[i]) + np.cos(freq2 * x[i])) * np.exp(-0.03 * x[i]**2)
            
        # Multi-scale cubic terms with dynamic coefficients
        f6 = 0.0
        for i in range(self.dim):
            coeff = 1.2 + 0.8 * np.sin(0.4 * i + 0.2 * r)
            f6 += coeff * x[i]**3 * np.exp(-0.04 * x[i]**2)
            
        # Fractal-like cross-terms with varying interaction strengths
        f7 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                strength = 0.5 + 0.5 * np.sin(0.3 * (i - j) + 0.2 * r)
                f7 += strength * np.sin(x[i] * x[j]) * np.exp(-0.06 * (x[i]**2 + x[j]**2))
                
        # Additional chaotic sine-wave interactions
        f8 = 0.0
        for i in range(self.dim):
            wave_freq = 3.0 + 4.0 * np.sin(0.1 * i + 0.15 * r)
            f8 += np.sin(wave_freq * x[i]) * np.exp(-0.08 * x[i]**2)
            
        # Complex exponential interactions with adaptive weights
        f9 = 0.0
        for i in range(self.dim):
            weight = 1.0 + 0.6 * np.cos(0.2 * i + 0.1 * r)
            f9 += weight * np.exp(-0.5 * x[i]**2) * np.sin(x[i])
            
        # Combined chaotic polynomial and trigonometric terms
        result = (f1 * radial_factor + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9)
        
        return result