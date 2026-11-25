import numpy as np

class MultiModalCorrelationBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize function value
        f_val = 0.0
        
        # Add chaotic sine-wave components with varying frequencies and amplitudes
        for i in range(self.dim):
            f_val += 0.7 * np.sin(30 * np.pi * x[i]) + 0.5 * np.sin(60 * np.pi * x[i]) + \
                     0.3 * np.sin(120 * np.pi * x[i]) + 0.1 * np.sin(240 * np.pi * x[i])
        
        # Add radial basis components with chaotic centers and varying widths
        for i in range(self.dim):
            center = 2.5 * np.sin(0.7 * i) - 2.0
            width = 0.03 + 0.12 * np.cos(0.5 * i)
            f_val += np.exp(-width * (x[i] - center)**2)
        
        # Add cross-dimensional exponential penalties with adaptive coupling strengths
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.35 * (1 + np.sin(1.5 * (i + j)))
                f_val += coupling * np.exp(-0.4 * (x[i] - x[j])**2) * np.cos(6 * (x[i] + x[j]))
        
        # Add polynomial conditioning with chaotic exponents and coefficients
        for i in range(self.dim):
            f_val += 0.3 * (x[i]**6) * (1 + 0.35 * np.sin(8 * x[i])) + \
                     0.2 * (x[i]**8) * (1 + 0.3 * np.cos(6 * x[i])) + \
                     0.15 * (x[i]**10) * (1 + 0.25 * np.sin(4 * x[i]))
        
        # Add chaotic interaction terms with multi-scale harmonic modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.18 * np.sin(8 * x[i]) * np.cos(7 * x[j]) * \
                         np.exp(-0.25 * (x[i] - x[j])**2) * (1 + 0.5 * np.sin(4 * (x[i] + x[j])))
        
        # Add fractal-like self-similar components with recursive scaling
        for i in range(self.dim):
            f_val += 0.1 * np.sin(25 * x[i]) * np.cos(20 * x[i]) * \
                     np.exp(-0.1 * (x[i] - 0.6)**2) * (1 + 0.4 * np.sin(12 * x[i]))
        
        # Add global chaotic modulation with multiple sinusoidal components
        f_val += 0.4 * np.sin(4 * np.pi * np.sum(x)) + 0.3 * np.cos(5 * np.pi * np.sum(x)) + \
                 0.2 * np.sin(7 * np.pi * np.sum(x)**2) + 0.15 * np.cos(9 * np.pi * np.sum(x)**3) + \
                 0.1 * np.sin(11 * np.pi * np.sum(x)**4)
        
        # Add self-similar fractal structure at multiple scales
        scale_factor = 0.2
        for k in range(1, 10):
            for i in range(self.dim):
                f_val += scale_factor * np.sin(k * 30 * x[i]) * np.cos(k * 25 * x[i])
            scale_factor *= 0.2
        
        # Add sharp gradient penalties at boundary regions
        penalty = 0.0
        for i in range(self.dim):
            if abs(x[i]) > 4.6:
                penalty += 20 * (abs(x[i]) - 4.6)**2
        f_val += penalty
        
        # Add cubic coupling terms for increased complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.07 * (x[i]**3) * np.sin(4 * x[j]) + 0.06 * (x[j]**3) * np.cos(4 * x[i]) + \
                         0.035 * (x[i]**4) * np.cos(3 * x[j]) + 0.025 * (x[j]**4) * np.sin(3 * x[i])
        
        # Add adaptive coupling terms based on dimensionality
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                adaptive_coupling = 0.1 * (1 + 0.2 * np.sin(0.6 * i) * np.cos(0.6 * j))
                f_val += adaptive_coupling * np.exp(-0.2 * (x[i] - x[j])**2) * np.sin(4 * (x[i] + x[j]))
        
        return f_val