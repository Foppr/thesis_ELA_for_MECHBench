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
            f_val += 0.8 * np.sin(20 * np.pi * x[i]) + 0.6 * np.sin(40 * np.pi * x[i]) + \
                     0.4 * np.sin(80 * np.pi * x[i]) + 0.2 * np.sin(160 * np.pi * x[i]) + \
                     0.1 * np.sin(320 * np.pi * x[i])
        
        # Add enhanced radial basis components with more chaotic centers and wider variations
        for i in range(self.dim):
            center = 4.0 * np.sin(0.8 * i) - 2.0
            width = 0.01 + 0.2 * np.cos(0.5 * i)
            f_val += np.exp(-width * (x[i] - center)**2)
        
        # Add enhanced cross-dimensional exponential penalties with stronger chaotic coupling strengths
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.3 * (1 + np.sin(1.1 * (i + j)))
                f_val += coupling * np.exp(-0.4 * (x[i] - x[j])**2) * np.cos(6 * (x[i] + x[j]))
        
        # Add enhanced polynomial conditioning with more chaotic exponents and stronger coefficients
        for i in range(self.dim):
            f_val += 0.3 * (x[i]**5) * (1 + 0.4 * np.sin(8 * x[i])) + \
                     0.2 * (x[i]**7) * (1 + 0.3 * np.cos(6 * x[i])) + \
                     0.15 * (x[i]**9) * (1 + 0.2 * np.sin(4 * x[i]))
        
        # Add enhanced chaotic interaction terms with multi-scale harmonic modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.15 * np.sin(8 * x[i]) * np.cos(7 * x[j]) * \
                         np.exp(-0.25 * (x[i] - x[j])**2) * (1 + 0.5 * np.sin(4 * (x[i] + x[j])))
        
        # Add enhanced fractal-like self-similar components with recursive scaling
        for i in range(self.dim):
            f_val += 0.1 * np.sin(25 * x[i]) * np.cos(20 * x[i]) * \
                     np.exp(-0.1 * (x[i] - 0.8)**2) * (1 + 0.4 * np.sin(12 * x[i]))
        
        # Add enhanced global chaotic modulation with multiple sinusoidal components
        f_val += 0.4 * np.sin(4 * np.pi * np.sum(x)) + 0.3 * np.cos(5 * np.pi * np.sum(x)) + \
                 0.2 * np.sin(7 * np.pi * np.sum(x)**2) + 0.15 * np.cos(9 * np.pi * np.sum(x)**3) + \
                 0.1 * np.sin(11 * np.pi * np.sum(x)**4)
        
        # Add enhanced self-similar fractal structure at multiple scales
        scale_factor = 0.2
        for k in range(1, 10):
            for i in range(self.dim):
                f_val += scale_factor * np.sin(k * 30 * x[i]) * np.cos(k * 25 * x[i])
            scale_factor *= 0.3
        
        # Add enhanced sharp gradient penalties at boundary regions
        penalty = 0.0
        for i in range(self.dim):
            if abs(x[i]) > 4.8:
                penalty += 20 * (abs(x[i]) - 4.8)**2
        f_val += penalty
        
        # Add enhanced cubic coupling terms for even greater complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.07 * (x[i]**3) * np.sin(4 * x[j]) + 0.06 * (x[j]**3) * np.cos(4 * x[i]) + \
                         0.03 * (x[i]**5) * np.cos(3 * x[j]) + 0.02 * (x[j]**5) * np.sin(3 * x[i])
        
        # Add adaptive coupling terms that vary based on dimensionality
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                adaptive_coupling = 0.1 * (1 + 0.2 * np.sin(0.6 * i) * np.cos(0.6 * j))
                f_val += adaptive_coupling * np.exp(-0.2 * (x[i] - x[j])**2) * np.sin(4 * (x[i] + x[j]))
        
        return f_val