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
            f_val += 0.4 * np.sin(8 * np.pi * x[i]) + 0.25 * np.sin(16 * np.pi * x[i]) + \
                     0.15 * np.sin(32 * np.pi * x[i]) + 0.1 * np.sin(64 * np.pi * x[i])
        
        # Add radial basis components with chaotic centers and widths
        for i in range(self.dim):
            center = 2.0 * np.sin(0.4 * i) - 1.0
            width = 0.03 + 0.08 * np.cos(0.25 * i)
            f_val += np.exp(-width * (x[i] - center)**2)
        
        # Add cross-dimensional exponential penalties with chaotic coupling strengths
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.08 * (1 + np.sin(0.6 * (i + j)))
                f_val += coupling * np.exp(-0.4 * (x[i] - x[j])**2) * np.cos(2.5 * (x[i] + x[j]))
        
        # Add polynomial conditioning with chaotic exponents and adaptive coefficients
        for i in range(self.dim):
            f_val += 0.12 * (x[i]**3) * (1 + 0.15 * np.sin(4 * x[i])) + \
                     0.06 * (x[i]**5) * (1 + 0.08 * np.cos(2.5 * x[i]))
        
        # Add chaotic interaction terms with multi-scale harmonic modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.06 * np.sin(4 * x[i]) * np.cos(3 * x[j]) * \
                         np.exp(-0.15 * (x[i] - x[j])**2) * (1 + 0.2 * np.sin(1.5 * (x[i] + x[j])))
        
        # Add fractal-like self-similar components with recursive scaling
        for i in range(self.dim):
            f_val += 0.04 * np.sin(12 * x[i]) * np.cos(9 * x[i]) * \
                     np.exp(-0.03 * (x[i] - 0.4)**2) * (1 + 0.15 * np.sin(6 * x[i]))
        
        # Add global chaotic modulation with multiple sinusoidal components
        f_val += 0.18 * np.sin(1.5 * np.pi * np.sum(x)) + 0.13 * np.cos(2.5 * np.pi * np.sum(x)) + \
                 0.08 * np.sin(4 * np.pi * np.sum(x)**2) + 0.04 * np.cos(6 * np.pi * np.sum(x)**3)
        
        # Add self-similar fractal structure at multiple scales
        scale_factor = 0.08
        for k in range(1, 5):
            for i in range(self.dim):
                f_val += scale_factor * np.sin(k * 16 * x[i]) * np.cos(k * 12 * x[i])
            scale_factor *= 0.4
        
        # Add sharp gradient penalties at boundary regions
        penalty = 0.0
        for i in range(self.dim):
            if abs(x[i]) > 4.5:
                penalty += 8 * (abs(x[i]) - 4.5)**2
        f_val += penalty
        
        return f_val