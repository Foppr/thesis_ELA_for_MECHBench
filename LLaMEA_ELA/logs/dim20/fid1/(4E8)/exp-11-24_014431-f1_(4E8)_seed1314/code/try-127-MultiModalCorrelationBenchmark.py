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
            f_val += 0.6 * np.sin(12 * np.pi * x[i]) + 0.3 * np.sin(24 * np.pi * x[i]) + \
                     0.2 * np.sin(48 * np.pi * x[i]) + 0.1 * np.sin(96 * np.pi * x[i]) + \
                     0.05 * np.sin(192 * np.pi * x[i])
        
        # Add radial basis components with chaotic centers and widths
        for i in range(self.dim):
            center = 2.5 * np.sin(0.5 * i) - 1.2
            width = 0.02 + 0.10 * np.cos(0.3 * i)
            f_val += np.exp(-width * (x[i] - center)**2)
        
        # Add cross-dimensional exponential penalties with chaotic coupling strengths
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.12 * (1 + np.sin(0.7 * (i + j)))
                f_val += coupling * np.exp(-0.25 * (x[i] - x[j])**2) * np.cos(3.5 * (x[i] + x[j]))
        
        # Add polynomial conditioning with chaotic exponents and adaptive coefficients
        for i in range(self.dim):
            f_val += 0.12 * (x[i]**3) * (1 + 0.25 * np.sin(5 * x[i])) + \
                     0.06 * (x[i]**5) * (1 + 0.15 * np.cos(3 * x[i])) + \
                     0.02 * (x[i]**7) * (1 + 0.08 * np.sin(6 * x[i]))
        
        # Add chaotic interaction terms with multi-scale harmonic modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.1 * np.sin(5 * x[i]) * np.cos(4 * x[j]) * \
                         np.exp(-0.12 * (x[i] - x[j])**2) * (1 + 0.3 * np.sin(2.5 * (x[i] + x[j])))
        
        # Add fractal-like self-similar components with multiple scales
        for scale in range(1, 7):
            for i in range(self.dim):
                f_val += 0.025 * np.sin(scale * 18 * x[i]) * np.cos(scale * 8 * x[i]) * \
                         np.exp(-0.06 * (scale * x[i])**2) * (1 + 0.12 * np.sin(scale * 3 * x[i]))
        
        # Add global chaotic modulation with multiple sinusoidal components
        f_val += 0.25 * np.sin(2.5 * np.pi * np.sum(x)) + 0.18 * np.cos(3.5 * np.pi * np.sum(x)) + \
                 0.13 * np.sin(5 * np.pi * np.sum(x)**2) + 0.09 * np.cos(7 * np.pi * np.sum(x)**3) + \
                 0.04 * np.sin(9 * np.pi * np.sum(x)**4)
        
        # Add fractal-like multi-scale interaction terms
        for scale in range(1, 5):
            for i in range(self.dim):
                for j in range(i+1, self.dim):
                    f_val += 0.018 * scale * np.sin(scale * 2.5 * x[i]) * np.cos(scale * 3.5 * x[j]) * \
                             np.exp(-0.04 * (x[i] - x[j])**2) * (1 + 0.2 * np.sin(scale * (x[i] + x[j])))
        
        # Add sharp gradient penalties at boundary regions
        penalty = 0.0
        for i in range(self.dim):
            if abs(x[i]) > 4.6:
                penalty += 12 * (abs(x[i]) - 4.6)**2
        f_val += penalty
        
        # Add fractal dimensionality scaling factor
        fractal_factor = 1.0 + 0.18 * np.sin(0.5 * np.sum(x))
        f_val *= fractal_factor
        
        # Add cubic coupling terms for enhanced complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.04 * (x[i]**3) * (x[j]**3) * np.exp(-0.025 * (x[i] - x[j])**2)
        
        # Add high-frequency noise components
        for i in range(self.dim):
            f_val += 0.018 * np.sin(90 * x[i]) + 0.009 * np.cos(130 * x[i])
        
        return f_val