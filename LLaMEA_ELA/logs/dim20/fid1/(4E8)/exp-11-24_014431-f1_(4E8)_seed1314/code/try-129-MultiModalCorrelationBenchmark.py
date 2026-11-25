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
            f_val += 0.7 * np.sin(14 * np.pi * x[i]) + 0.5 * np.sin(28 * np.pi * x[i]) + \
                     0.4 * np.sin(56 * np.pi * x[i]) + 0.3 * np.sin(112 * np.pi * x[i])
        
        # Add radial basis components with chaotic centers and widths
        for i in range(self.dim):
            center = 2.5 * np.sin(0.7 * i) - 1.25
            width = 0.07 + 0.14 * np.cos(0.4 * i)
            f_val += np.exp(-width * (x[i] - center)**2)
        
        # Add cross-dimensional exponential penalties with chaotic coupling strengths
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.2 * (1 + np.sin(0.9 * (i + j)))
                f_val += coupling * np.exp(-0.7 * (x[i] - x[j])**2) * np.cos(5 * (x[i] + x[j]))
        
        # Add polynomial conditioning with chaotic exponents and adaptive coefficients
        for i in range(self.dim):
            f_val += 0.2 * (x[i]**3) * (1 + 0.3 * np.sin(7 * x[i])) + \
                     0.1 * (x[i]**5) * (1 + 0.2 * np.cos(5 * x[i]))
        
        # Add chaotic interaction terms with multi-scale harmonic modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.12 * np.sin(7 * x[i]) * np.cos(6 * x[j]) * \
                         np.exp(-0.2 * (x[i] - x[j])**2) * (1 + 0.4 * np.sin(3 * (x[i] + x[j])))
        
        # Add fractal-like self-similar components with recursive scaling
        for i in range(self.dim):
            f_val += 0.08 * np.sin(20 * x[i]) * np.cos(16 * x[i]) * \
                     np.exp(-0.07 * (x[i] - 0.5)**2) * (1 + 0.3 * np.sin(10 * x[i]))
        
        # Add global chaotic modulation with multiple sinusoidal components
        f_val += 0.3 * np.sin(3 * np.pi * np.sum(x)) + 0.25 * np.cos(4 * np.pi * np.sum(x)) + \
                 0.2 * np.sin(6 * np.pi * np.sum(x)**2) + 0.1 * np.cos(8 * np.pi * np.sum(x)**3)
        
        # Add self-similar fractal structure at multiple scales
        scale_factor = 0.2
        for k in range(1, 8):
            for i in range(self.dim):
                f_val += scale_factor * np.sin(k * 30 * x[i]) * np.cos(k * 25 * x[i])
            scale_factor *= 0.65
        
        # Add sharp gradient penalties at boundary regions
        penalty = 0.0
        for i in range(self.dim):
            if abs(x[i]) > 4.5:
                penalty += 20 * (abs(x[i]) - 4.5)**2
        f_val += penalty
        
        # Add cubic coupling terms for enhanced complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.05 * (x[i]**3) * np.sin(3 * x[j]) + 0.04 * (x[j]**3) * np.cos(3 * x[i])
        
        # Add additional chaotic cubic coupling terms with variable interaction strengths
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                strength = 0.025 * (1 + np.sin(0.6 * i) * np.cos(0.6 * j))
                f_val += strength * (x[i]**3) * (x[j]**3) * np.sin(4 * (x[i] - x[j]))
        
        # Add adaptive harmonic components with dynamic frequencies
        for i in range(self.dim):
            freq = 25 + 12 * np.sin(0.5 * i)
            f_val += 0.04 * np.sin(freq * x[i]) * np.cos(freq * x[i] / 2) * (1 + 0.15 * np.sin(6 * x[i]))
        
        return f_val