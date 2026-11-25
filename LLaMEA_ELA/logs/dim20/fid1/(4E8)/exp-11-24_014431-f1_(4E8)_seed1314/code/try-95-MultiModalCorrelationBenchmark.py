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
            f_val += 0.5 * np.sin(10 * np.pi * x[i]) + 0.3 * np.sin(20 * np.pi * x[i]) + \
                     0.2 * np.sin(40 * np.pi * x[i]) + 0.1 * np.sin(80 * np.pi * x[i])
        
        # Add radial basis components with chaotic centers and widths
        for i in range(self.dim):
            center = 2.5 * np.sin(0.5 * i) - 1.25
            width = 0.05 + 0.1 * np.cos(0.3 * i)
            f_val += np.exp(-width * (x[i] - center)**2)
        
        # Add cross-dimensional exponential penalties with chaotic coupling strengths
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.1 * (1 + np.sin(0.7 * (i + j)))
                f_val += coupling * np.exp(-0.5 * (x[i] - x[j])**2) * np.cos(3 * (x[i] + x[j]))
        
        # Add polynomial conditioning with chaotic exponents and adaptive coefficients
        for i in range(self.dim):
            f_val += 0.1 * (x[i]**3) * (1 + 0.2 * np.sin(5 * x[i])) + \
                     0.05 * (x[i]**5) * (1 + 0.1 * np.cos(3 * x[i])) + \
                     0.02 * (x[i]**2.5) * (1 + 0.15 * np.sin(7 * x[i]))
        
        # Add chaotic interaction terms with multi-scale harmonic modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.08 * np.sin(5 * x[i]) * np.cos(4 * x[j]) * \
                         np.exp(-0.1 * (x[i] - x[j])**2) * (1 + 0.3 * np.sin(2 * (x[i] + x[j])))
        
        # Add fractal-like self-similar components with multiple scales
        for scale in range(1, 6):
            for i in range(self.dim):
                f_val += 0.02 * np.sin(scale * 15 * x[i]) * np.cos(scale * 7 * x[i]) * \
                         np.exp(-0.05 * (scale * x[i])**2) * (1 + 0.1 * np.sin(scale * 3 * x[i]))
        
        # Add global chaotic modulation with multiple sinusoidal components
        f_val += 0.2 * np.sin(2 * np.pi * np.sum(x)) + 0.15 * np.cos(3 * np.pi * np.sum(x)) + \
                 0.1 * np.sin(5 * np.pi * np.sum(x)**2) + 0.05 * np.cos(7 * np.pi * np.sum(x)**3)
        
        # Add fractal-like multi-scale interaction terms
        for scale in range(1, 4):
            for i in range(self.dim):
                for j in range(i+1, self.dim):
                    f_val += 0.01 * scale * np.sin(scale * 2 * x[i]) * np.cos(scale * 3 * x[j]) * \
                             np.exp(-0.03 * (x[i] - x[j])**2) * (1 + 0.2 * np.sin(scale * (x[i] + x[j])))
        
        # Add sharp gradient penalties at boundary regions
        penalty = 0.0
        for i in range(self.dim):
            if abs(x[i]) > 4.5:
                penalty += 10 * (abs(x[i]) - 4.5)**2
        f_val += penalty
        
        # Add fractal dimensionality scaling factor
        fractal_factor = 1.0 + 0.1 * np.sin(0.5 * np.sum(x))
        f_val *= fractal_factor
        
        return f_val