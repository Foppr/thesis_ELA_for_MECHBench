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
            f_val += 0.7 * np.sin(15 * np.pi * x[i]) + 0.4 * np.sin(30 * np.pi * x[i]) + \
                     0.3 * np.sin(60 * np.pi * x[i]) + 0.2 * np.sin(120 * np.pi * x[i]) + \
                     0.1 * np.sin(240 * np.pi * x[i])
        
        # Add radial basis components with chaotic centers and widths
        for i in range(self.dim):
            center = 3.0 * np.sin(0.6 * i) - 1.5
            width = 0.03 + 0.12 * np.cos(0.4 * i)
            f_val += np.exp(-width * (x[i] - center)**2)
        
        # Add cross-dimensional exponential penalties with chaotic coupling strengths
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.15 * (1 + np.sin(0.8 * (i + j)))
                f_val += coupling * np.exp(-0.3 * (x[i] - x[j])**2) * np.cos(4 * (x[i] + x[j]))
        
        # Add polynomial conditioning with chaotic exponents and adaptive coefficients
        for i in range(self.dim):
            f_val += 0.15 * (x[i]**3) * (1 + 0.3 * np.sin(6 * x[i])) + \
                     0.08 * (x[i]**5) * (1 + 0.2 * np.cos(4 * x[i])) + \
                     0.03 * (x[i]**7) * (1 + 0.1 * np.sin(7 * x[i]))
        
        # Add chaotic interaction terms with multi-scale harmonic modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.12 * np.sin(6 * x[i]) * np.cos(5 * x[j]) * \
                         np.exp(-0.15 * (x[i] - x[j])**2) * (1 + 0.4 * np.sin(3 * (x[i] + x[j])))
        
        # Add fractal-like self-similar components with multiple scales
        for scale in range(1, 8):
            for i in range(self.dim):
                f_val += 0.03 * np.sin(scale * 20 * x[i]) * np.cos(scale * 9 * x[i]) * \
                         np.exp(-0.07 * (scale * x[i])**2) * (1 + 0.15 * np.sin(scale * 4 * x[i]))
        
        # Add global chaotic modulation with multiple sinusoidal components
        f_val += 0.3 * np.sin(3 * np.pi * np.sum(x)) + 0.2 * np.cos(4 * np.pi * np.sum(x)) + \
                 0.15 * np.sin(6 * np.pi * np.sum(x)**2) + 0.1 * np.cos(8 * np.pi * np.sum(x)**3) + \
                 0.05 * np.sin(10 * np.pi * np.sum(x)**4)
        
        # Add fractal-like multi-scale interaction terms
        for scale in range(1, 6):
            for i in range(self.dim):
                for j in range(i+1, self.dim):
                    f_val += 0.02 * scale * np.sin(scale * 3 * x[i]) * np.cos(scale * 4 * x[j]) * \
                             np.exp(-0.05 * (x[i] - x[j])**2) * (1 + 0.25 * np.sin(scale * (x[i] + x[j])))
        
        # Add sharp gradient penalties at boundary regions
        penalty = 0.0
        for i in range(self.dim):
            if abs(x[i]) > 4.7:
                penalty += 15 * (abs(x[i]) - 4.7)**2
        f_val += penalty
        
        # Add fractal dimensionality scaling factor
        fractal_factor = 1.0 + 0.2 * np.sin(0.6 * np.sum(x))
        f_val *= fractal_factor
        
        # Add cubic coupling terms for enhanced complexity (slightly modified)
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.06 * (x[i]**3) * (x[j]**3) * np.exp(-0.03 * (x[i] - x[j])**2)  # Increased coupling strength
        
        # Add high-frequency noise components
        for i in range(self.dim):
            f_val += 0.02 * np.sin(100 * x[i]) + 0.01 * np.cos(150 * x[i])
        
        return f_val