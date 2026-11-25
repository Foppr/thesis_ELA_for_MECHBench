import numpy as np

class MultiModalCorrelationBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize function value
        f_val = 0.0
        
        # Add enhanced chaotic sine-wave components with increased frequency and amplitude variations
        for i in range(self.dim):
            f_val += 0.8 * np.sin(25 * np.pi * x[i]) + 0.6 * np.sin(50 * np.pi * x[i]) + \
                     0.4 * np.sin(100 * np.pi * x[i]) + 0.2 * np.sin(200 * np.pi * x[i]) + \
                     0.1 * np.sin(400 * np.pi * x[i])
        
        # Add enhanced radial basis components with more chaotic centers and wider variations
        for i in range(self.dim):
            center = 4.5 * np.sin(0.9 * i) - 2.5
            width = 0.01 + 0.25 * np.cos(0.6 * i)
            f_val += np.exp(-width * (x[i] - center)**2)
        
        # Add enhanced cross-dimensional exponential penalties with stronger chaotic coupling strengths
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.4 * (1 + np.sin(1.2 * (i + j)))
                f_val += coupling * np.exp(-0.5 * (x[i] - x[j])**2) * np.cos(8 * (x[i] + x[j]))
        
        # Add enhanced polynomial conditioning with more chaotic exponents and stronger coefficients
        for i in range(self.dim):
            f_val += 0.4 * (x[i]**6) * (1 + 0.5 * np.sin(9 * x[i])) + \
                     0.3 * (x[i]**8) * (1 + 0.4 * np.cos(7 * x[i])) + \
                     0.2 * (x[i]**10) * (1 + 0.3 * np.sin(5 * x[i]))
        
        # Add enhanced chaotic interaction terms with multi-scale harmonic modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.2 * np.sin(9 * x[i]) * np.cos(8 * x[j]) * \
                         np.exp(-0.3 * (x[i] - x[j])**2) * (1 + 0.6 * np.sin(5 * (x[i] + x[j])))
        
        # Add enhanced fractal-like self-similar components with recursive scaling
        for i in range(self.dim):
            f_val += 0.15 * np.sin(30 * x[i]) * np.cos(25 * x[i]) * \
                     np.exp(-0.15 * (x[i] - 0.9)**2) * (1 + 0.5 * np.sin(15 * x[i]))
        
        # Add enhanced global chaotic modulation with multiple sinusoidal components
        f_val += 0.5 * np.sin(5 * np.pi * np.sum(x)) + 0.4 * np.cos(6 * np.pi * np.sum(x)) + \
                 0.3 * np.sin(8 * np.pi * np.sum(x)**2) + 0.25 * np.cos(10 * np.pi * np.sum(x)**3) + \
                 0.2 * np.sin(12 * np.pi * np.sum(x)**4)
        
        # Add enhanced self-similar fractal structure at multiple scales
        scale_factor = 0.25
        for k in range(1, 12):
            for i in range(self.dim):
                f_val += scale_factor * np.sin(k * 35 * x[i]) * np.cos(k * 30 * x[i])
            scale_factor *= 0.35
        
        # Add enhanced sharp gradient penalties at boundary regions
        penalty = 0.0
        for i in range(self.dim):
            if abs(x[i]) > 4.7:
                penalty += 25 * (abs(x[i]) - 4.7)**2
        f_val += penalty
        
        # Add enhanced cubic coupling terms for even greater complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.08 * (x[i]**3) * np.sin(5 * x[j]) + 0.07 * (x[j]**3) * np.cos(5 * x[i]) + \
                         0.04 * (x[i]**5) * np.cos(4 * x[j]) + 0.03 * (x[j]**5) * np.sin(4 * x[i])
        
        # Add adaptive coupling terms that vary based on dimensionality
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                adaptive_coupling = 0.12 * (1 + 0.3 * np.sin(0.7 * i) * np.cos(0.7 * j))
                f_val += adaptive_coupling * np.exp(-0.25 * (x[i] - x[j])**2) * np.sin(5 * (x[i] + x[j]))
        
        return f_val