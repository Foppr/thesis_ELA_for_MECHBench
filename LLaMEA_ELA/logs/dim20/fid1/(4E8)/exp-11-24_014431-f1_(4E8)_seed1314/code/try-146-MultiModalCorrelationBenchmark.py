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
            f_val += 1.2 * np.sin(20 * np.pi * x[i]) + 0.9 * np.sin(40 * np.pi * x[i]) + \
                     0.6 * np.sin(80 * np.pi * x[i]) + 0.4 * np.sin(160 * np.pi * x[i])
        
        # Add radial basis components with chaotic centers and widths
        for i in range(self.dim):
            center = 3.0 * np.sin(0.9 * i) - 1.5
            width = 0.1 + 0.2 * np.cos(0.5 * i)
            f_val += np.exp(-width * (x[i] - center)**2)
        
        # Add cross-dimensional exponential penalties with chaotic coupling strengths
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.3 * (1 + np.sin(1.5 * (i + j)))
                f_val += coupling * np.exp(-0.9 * (x[i] - x[j])**2) * np.cos(7 * (x[i] + x[j]))
        
        # Add polynomial conditioning with chaotic exponents and adaptive coefficients
        for i in range(self.dim):
            f_val += 0.3 * (x[i]**4) * (1 + 0.4 * np.sin(8 * x[i])) + \
                     0.2 * (x[i]**6) * (1 + 0.3 * np.cos(6 * x[i])) + \
                     0.15 * (x[i]**8) * (1 + 0.2 * np.sin(4 * x[i]))
        
        # Add chaotic interaction terms with multi-scale harmonic modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.2 * np.sin(9 * x[i]) * np.cos(8 * x[j]) * \
                         np.exp(-0.3 * (x[i] - x[j])**2) * (1 + 0.5 * np.sin(4 * (x[i] + x[j])))
        
        # Add fractal-like self-similar components with recursive scaling
        for i in range(self.dim):
            f_val += 0.15 * np.sin(25 * x[i]) * np.cos(20 * x[i]) * \
                     np.exp(-0.1 * (x[i] - 0.6)**2) * (1 + 0.4 * np.sin(12 * x[i]))
        
        # Add global chaotic modulation with multiple sinusoidal components
        f_val += 0.4 * np.sin(4 * np.pi * np.sum(x)) + 0.35 * np.cos(5 * np.pi * np.sum(x)) + \
                 0.3 * np.sin(8 * np.pi * np.sum(x)**2) + 0.15 * np.cos(10 * np.pi * np.sum(x)**3) + \
                 0.08 * np.sin(12 * np.pi * np.sum(x)**4)
        
        # Add self-similar fractal structure at multiple scales
        scale_factor = 0.3
        for k in range(1, 11):
            for i in range(self.dim):
                f_val += scale_factor * np.sin(k * 40 * x[i]) * np.cos(k * 35 * x[i])
            scale_factor *= 0.6
        
        # Add sharp gradient penalties at boundary regions
        penalty = 0.0
        for i in range(self.dim):
            if abs(x[i]) > 4.7:
                penalty += 25 * (abs(x[i]) - 4.7)**2
        f_val += penalty
        
        # Add cubic coupling terms for enhanced complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.08 * (x[i]**3) * np.sin(4 * x[j]) + 0.07 * (x[j]**3) * np.cos(4 * x[i])
        
        # Add additional chaotic cubic coupling terms with variable interaction strengths
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                strength = 0.05 * (1 + np.sin(0.7 * i) * np.cos(0.7 * j))
                f_val += strength * (x[i]**3) * (x[j]**3) * np.sin(5 * (x[i] - x[j]))
        
        # Add adaptive harmonic components with dynamic frequencies
        for i in range(self.dim):
            freq = 30 + 20 * np.sin(0.6 * i)
            f_val += 0.06 * np.sin(freq * x[i]) * np.cos(freq * x[i] / 2) * (1 + 0.2 * np.sin(7 * x[i]))
        
        # Add higher-order coupling terms for increased complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    f_val += 0.03 * (x[i]**2) * (x[j]**2) * np.sin(3 * x[k]) + \
                             0.02 * (x[k]**2) * (x[i]**2) * np.cos(3 * x[j])
        
        # Add quartic and quintic interaction terms for even greater complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.015 * (x[i]**4) * np.sin(2 * x[j]) + 0.012 * (x[j]**4) * np.cos(2 * x[i])
        
        # Add additional multi-scale chaotic components
        for i in range(self.dim):
            f_val += 0.05 * np.sin(35 * x[i]) * np.cos(30 * x[i]) * \
                     np.exp(-0.05 * (x[i] - 0.7)**2) * (1 + 0.25 * np.sin(15 * x[i]))
        
        return f_val