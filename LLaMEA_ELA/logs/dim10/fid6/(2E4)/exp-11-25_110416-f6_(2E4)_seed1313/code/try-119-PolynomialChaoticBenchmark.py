import numpy as np

class PolynomialChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequence for polynomial chaos
        self.chaos_seq = np.array([0.5])
        for _ in range(dim * 20):
            self.chaos_seq = np.append(self.chaos_seq, 4 * self.chaos_seq[-1] * (1 - self.chaos_seq[-1]))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial term with adaptive conditioning
        result = np.sum(x**4) * 0.05
        
        # Add polynomial chaos components with varying exponents
        for i in range(self.dim):
            exp_factor = 2 + 3 * np.sin(self.chaos_seq[i % len(self.chaos_seq)] * 10)
            result += 0.8 * (x[i]**exp_factor) * np.cos(3 * x[i] * self.chaos_seq[(i+1) % len(self.chaos_seq)])
            
        # Add trigonometric coupling with adaptive frequencies
        for i in range(self.dim):
            freq = 1 + 2 * np.abs(np.sin(self.chaos_seq[i % len(self.chaos_seq)] * 5))
            result += 0.6 * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5)
            
        # Add multi-scale harmonic interactions
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                coupling = 0.5 + 0.5 * np.sin(self.chaos_seq[(i+j) % len(self.chaos_seq)])
                result += 0.4 * np.sin(2 * x[i] + x[j]) * np.cos(x[i] - 2 * x[j]) * coupling
                
        # Add adaptive conditioning with chaotic scaling
        for i in range(self.dim):
            scale = 1 + 0.5 * np.sin(self.chaos_seq[i % len(self.chaos_seq)] * 15)
            result += 0.3 * (x[i]**2) * scale
            
        # Add fractal-like polynomial terms with chaotic coefficients
        for i in range(self.dim):
            coeff = 1 + 0.8 * np.cos(self.chaos_seq[(i*3) % len(self.chaos_seq)] * 7)
            result += coeff * x[i]**(3 + np.abs(np.sin(self.chaos_seq[(i*2) % len(self.chaos_seq)] * 4)))
            
        # Add asymmetric polynomial interactions
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                asym_factor = 1 + 0.3 * np.sin(self.chaos_seq[(i*j) % len(self.chaos_seq)])
                result += 0.25 * (x[i]**2) * (x[j]**3) * asym_factor
                
        # Add chaotic noise with polynomial modulation
        for i in range(self.dim):
            noise = np.sin(self.chaos_seq[i % len(self.chaos_seq)] * 100) * 0.1
            result += noise * x[i]**2
            
        return result