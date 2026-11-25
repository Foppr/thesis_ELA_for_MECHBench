import numpy as np

class ChaoticPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Scale input to [-5, 5] domain if needed
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Polynomial terms with varying degrees and dynamic coefficients
        for i in range(self.dim):
            coeff = 0.5 + 0.3 * np.sin(0.5 * i)
            result += coeff * (x[i] ** (3 + i % 3)) * (1.0 + 0.1 * i)
        
        # Radial components with chaotic modulation and varying frequencies
        if self.dim >= 2:
            r = np.sqrt(np.sum(x[:2]**2))
            freq_mod = 1.0 + 0.2 * np.sin(r)
            result += 0.8 * np.sin(freq_mod * 6.0 * r) * np.cos(freq_mod * 4.0 * r) * np.exp(-0.2 * r)
        
        # Asymmetric chaotic terms with exponential decay and dynamic scaling
        for i in range(self.dim):
            if x[i] > 0:
                result += 0.4 * np.exp(-0.5 * x[i]) * np.sin(10.0 * x[i]) * (1.0 + 0.2 * x[i]**2)
            else:
                result += 0.3 * np.exp(-0.7 * abs(x[i])) * np.cos(8.0 * x[i]) * (1.0 + 0.15 * x[i]**2)
        
        # Dynamic frequency modulation with chaotic phase shifts
        for i in range(self.dim):
            freq = 2.0 + 0.5 * np.sin(x[i] * 0.3) + 0.3 * np.cos(x[i] * 0.7)
            result += 0.25 * np.sin(freq * x[i]) * np.exp(-0.1 * abs(x[i]))
        
        # Cross-dimensional coupling with chaotic interaction terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
                result += 0.15 * interaction * np.exp(-0.05 * (x[i]**2 + x[j]**2))
        
        # Multi-scale radial components with varying amplitudes and frequencies
        if self.dim >= 3:
            r = np.sqrt(np.sum(x[:3]**2))
            result += 0.6 * np.sin(12.0 * r) * np.exp(-0.3 * r) * (1.0 + 0.1 * r**2)
        
        # Boundary attraction with chaotic penalty function
        for i in range(self.dim):
            boundary_penalty = 0.5 * (5.0 - abs(x[i]))**4
            result += boundary_penalty
        
        # Chaotic sine-cosine products with dynamic amplitude modulation
        for i in range(self.dim):
            amp_mod = 1.0 + 0.3 * np.sin(2.0 * x[i])
            result += 0.3 * amp_mod * np.sin(5.0 * x[i]) * np.cos(7.0 * x[i]) * np.exp(-0.1 * abs(x[i]))
        
        # High-order polynomial interactions with chaotic coefficients
        for i in range(min(self.dim, 4)):
            for j in range(i+1, min(self.dim, i+3)):
                coeff = 0.2 + 0.1 * np.sin(0.5 * (i + j))
                result += coeff * (x[i]**3) * (x[j]**2) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Global chaotic modulation based on sum of variables
        sum_x = np.sum(x)
        result += 0.4 * np.sin(8.0 * sum_x) * np.cos(6.0 * sum_x) * np.exp(-0.1 * abs(sum_x))
        
        return result