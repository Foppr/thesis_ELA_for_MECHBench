import numpy as np

class ChaoticSpiralBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic Gaussian potentials with adaptive variance and spiral modulation
        r = np.sqrt(np.sum(x**2))
        f1 = 0.0
        for i in range(self.dim):
            sigma = 1.0 + 0.5 * np.sin(0.3 * i + 0.1 * r)
            mu = 0.5 * np.cos(0.4 * i + 0.2 * r)
            f1 += np.exp(-0.5 * ((x[i] - mu) / sigma)**2) * (1.0 + 0.3 * np.sin(0.5 * i + 0.2 * r))
            
        # Adaptive spiral couplings with dynamic angles and radial scaling
        f2 = 0.0
        for i in range(self.dim):
            angle = 0.5 * np.pi * (i / self.dim) + 0.3 * r
            radius = 1.0 + 0.4 * np.cos(0.2 * i + 0.1 * r)
            f2 += radius * np.sin(angle + x[i]) * np.exp(-0.02 * x[i]**2)
            
        # Fractal-like cross-dimensional interaction terms with recursive coupling
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.4 + 0.6 * np.sin(0.3 * (i + j) + 0.2 * r)
                f3 += coupling * np.cos(x[i] * x[j]) * np.exp(-0.01 * (x[i]**2 + x[j]**2))
                
        # Dynamic harmonic oscillations with time-varying frequencies and multi-scale modulation
        f4 = 0.0
        for i in range(self.dim):
            freq = 1.5 + 3.0 * np.sin(0.2 * i)
            amp = 1.0 + 0.7 * np.cos(0.3 * i + 0.1 * r)
            phase = 0.3 * np.sin(0.1 * i + 0.2 * r)
            f4 += amp * np.cos(freq * x[i] + phase) * np.exp(-0.04 * np.abs(x[i]))
            
        # Enhanced boundary penalty with exponential and logarithmic scaling
        f5 = 0.0
        for i in range(self.dim):
            if x[i] < 0:
                penalty = 2.0 * np.exp(-x[i]**2 / 10.0) + 0.5 * np.log(1.0 - x[i]/5.0)**2
            else:
                penalty = 2.0 * np.exp(-x[i]**2 / 10.0) + 0.5 * np.log(1.0 + x[i]/5.0)**2
            f5 += penalty
            
        # Stochastic phase-coupled cross-terms with dynamic interaction strengths
        f6 = 0.0
        for i in range(self.dim):
            phase = np.random.uniform(0, 2*np.pi) + 0.2 * r
            for j in range(i+1, self.dim):
                strength = 0.5 + 0.5 * np.cos(0.4 * (i - j) + 0.3 * r)
                f6 += strength * np.sin(x[i] + phase) * np.cos(x[j]) * np.exp(-0.03 * (x[i]**2 + x[j]**2))
                
        # Global irregularity through nested polynomial terms with chaotic coefficients
        f7 = 0.0
        for i in range(self.dim):
            coeff1 = 0.2 + 0.4 * np.cos(0.3 * i)
            coeff2 = 0.6 + 0.4 * np.sin(0.2 * i)
            coeff3 = 0.3 + 0.5 * np.cos(0.4 * i)
            f7 += coeff1 * x[i]**4 + coeff2 * x[i]**3 + coeff3 * x[i]**2
            
        # Additional chaotic cubic terms for increased multimodality
        f8 = 0.0
        for i in range(self.dim):
            coeff = 0.9 + 0.3 * np.cos(0.6 * i + 0.1 * r)
            f8 += coeff * x[i]**3 * np.exp(-0.03 * x[i]**2)
            
        # Cross-dimensional chaotic coupling with cosine modulation
        f9 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                mod = 1.0 + 0.5 * np.cos(0.2 * (i * j) + 0.3 * r)
                f9 += mod * np.cos(x[i] + x[j]) * np.exp(-0.04 * (x[i]**2 + x[j]**2))
                
        # Novel nested trigonometric chaos for enhanced multimodality
        f10 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                term = np.sin(0.5 * (x[i]**2 + x[j]**2)) * np.cos(0.3 * (x[i] - x[j]))
                f10 += term * np.exp(-0.02 * (x[i]**2 + x[j]**2))
                
        # Additional chaotic sine-cosine cross-terms with varying frequencies
        f11 = 0.0
        for i in range(self.dim):
            freq_i = 2.0 + 1.5 * np.sin(0.4 * i)
            for j in range(i+1, self.dim):
                freq_j = 1.8 + 1.2 * np.cos(0.3 * j)
                f11 += np.sin(freq_i * x[i]) * np.cos(freq_j * x[j]) * np.exp(-0.01 * (x[i]**2 + x[j]**2))
                
        # Multi-scale chaotic modulation with nested exponential components
        f12 = 0.0
        for i in range(self.dim):
            scale_factor = 0.5 + 0.5 * np.sin(0.6 * i + 0.3 * r)
            f12 += scale_factor * np.exp(-0.1 * x[i]**2) * np.sin(0.8 * x[i]) * np.cos(0.4 * x[i])
                
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12