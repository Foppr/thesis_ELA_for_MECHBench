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
            f_val += 0.7 * np.sin(15 * np.pi * x[i]) + 0.5 * np.sin(30 * np.pi * x[i]) + \
                     0.3 * np.sin(60 * np.pi * x[i]) + 0.15 * np.sin(120 * np.pi * x[i]) + \
                     0.1 * np.sin(240 * np.pi * x[i])
        
        # Add enhanced radial basis components with more chaotic centers and wider variations
        for i in range(self.dim):
            center = 3.0 * np.sin(0.7 * i) - 1.5
            width = 0.02 + 0.15 * np.cos(0.4 * i)
            f_val += np.exp(-width * (x[i] - center)**2)
        
        # Add enhanced cross-dimensional exponential penalties with stronger chaotic coupling strengths
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.2 * (1 + np.sin(0.9 * (i + j)))
                f_val += coupling * np.exp(-0.3 * (x[i] - x[j])**2) * np.cos(5 * (x[i] + x[j]))
        
        # Add enhanced polynomial conditioning with more chaotic exponents and stronger coefficients
        for i in range(self.dim):
            f_val += 0.2 * (x[i]**4) * (1 + 0.3 * np.sin(7 * x[i])) + \
                     0.15 * (x[i]**6) * (1 + 0.2 * np.cos(5 * x[i])) + \
                     0.1 * (x[i]**8) * (1 + 0.1 * np.sin(3 * x[i]))
        
        # Add enhanced chaotic interaction terms with multi-scale harmonic modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.12 * np.sin(7 * x[i]) * np.cos(6 * x[j]) * \
                         np.exp(-0.2 * (x[i] - x[j])**2) * (1 + 0.4 * np.sin(3 * (x[i] + x[j])))
        
        # Add enhanced fractal-like self-similar components with recursive scaling
        for i in range(self.dim):
            f_val += 0.08 * np.sin(20 * x[i]) * np.cos(16 * x[i]) * \
                     np.exp(-0.08 * (x[i] - 0.7)**2) * (1 + 0.3 * np.sin(10 * x[i]))
        
        # Add enhanced global chaotic modulation with multiple sinusoidal components
        f_val += 0.3 * np.sin(3 * np.pi * np.sum(x)) + 0.2 * np.cos(4 * np.pi * np.sum(x)) + \
                 0.15 * np.sin(6 * np.pi * np.sum(x)**2) + 0.1 * np.cos(8 * np.pi * np.sum(x)**3) + \
                 0.05 * np.sin(10 * np.pi * np.sum(x)**4)
        
        # Add enhanced self-similar fractal structure at multiple scales
        scale_factor = 0.15
        for k in range(1, 8):
            for i in range(self.dim):
                f_val += scale_factor * np.sin(k * 25 * x[i]) * np.cos(k * 20 * x[i])
            scale_factor *= 0.4
        
        # Add enhanced sharp gradient penalties at boundary regions
        penalty = 0.0
        for i in range(self.dim):
            if abs(x[i]) > 4.7:
                penalty += 15 * (abs(x[i]) - 4.7)**2
        f_val += penalty
        
        # Add enhanced cubic coupling terms for even greater complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.05 * (x[i]**3) * np.sin(3 * x[j]) + 0.04 * (x[j]**3) * np.cos(3 * x[i]) + \
                         0.02 * (x[i]**4) * np.cos(2 * x[j]) + 0.01 * (x[j]**4) * np.sin(2 * x[i])
        
        return f_val