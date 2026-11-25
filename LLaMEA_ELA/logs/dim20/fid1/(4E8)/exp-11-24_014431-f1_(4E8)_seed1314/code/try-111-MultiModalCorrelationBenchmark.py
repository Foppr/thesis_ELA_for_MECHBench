import numpy as np

class MultiModalCorrelationBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize function value
        f_val = 0.0
        
        # Add enhanced chaotic sine-wave components with fractional frequencies
        for i in range(self.dim):
            f_val += 0.6 * np.sin(12 * np.pi * x[i]**1.3) + 0.4 * np.sin(25 * np.pi * x[i]**1.7) + \
                     0.3 * np.sin(50 * np.pi * x[i]**1.2) + 0.2 * np.sin(100 * np.pi * x[i]**1.5)
        
        # Add radial basis components with fractional centers and widths
        for i in range(self.dim):
            center = 2.8 * np.sin(0.6 * i)**1.4 - 1.4
            width = 0.03 + 0.12 * np.cos(0.4 * i)**1.3
            f_val += np.exp(-width * (x[i] - center)**2)
        
        # Add cross-dimensional exponential penalties with quaternion-like coupling strengths
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.15 * (1 + np.sin(0.8 * (i + j)) * np.cos(0.6 * (i - j)))
                f_val += coupling * np.exp(-0.4 * (x[i] - x[j])**2) * np.cos(4 * (x[i] + x[j]))
        
        # Add fractional polynomial conditioning with chaotic exponents
        for i in range(self.dim):
            f_val += 0.15 * (x[i]**3.5) * (1 + 0.25 * np.sin(6 * x[i])) + \
                     0.08 * (x[i]**6.2) * (1 + 0.15 * np.cos(4 * x[i]))
        
        # Add enhanced chaotic interaction terms with multi-scale harmonic modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.12 * np.sin(6 * x[i]) * np.cos(5 * x[j]) * \
                         np.exp(-0.15 * (x[i] - x[j])**2) * (1 + 0.4 * np.sin(3 * (x[i] + x[j])))
        
        # Add enhanced fractal-like self-similar components with recursive scaling
        for i in range(self.dim):
            f_val += 0.08 * np.sin(20 * x[i]) * np.cos(16 * x[i]) * \
                     np.exp(-0.08 * (x[i] - 0.6)**2) * (1 + 0.3 * np.sin(10 * x[i]))
        
        # Add global chaotic modulation with multiple sinusoidal components
        f_val += 0.25 * np.sin(2.5 * np.pi * np.sum(x)) + 0.2 * np.cos(3.5 * np.pi * np.sum(x)) + \
                 0.15 * np.sin(5.5 * np.pi * np.sum(x)**2) + 0.1 * np.cos(7.5 * np.pi * np.sum(x)**3)
        
        # Add enhanced self-similar fractal structure at multiple scales
        scale_factor = 0.15
        for k in range(1, 8):
            for i in range(self.dim):
                f_val += scale_factor * np.sin(k * 25 * x[i]) * np.cos(k * 20 * x[i])
            scale_factor *= 0.4
        
        # Add sharp gradient penalties at boundary regions
        penalty = 0.0
        for i in range(self.dim):
            if abs(x[i]) > 4.6:
                penalty += 15 * (abs(x[i]) - 4.6)**2
        f_val += penalty
        
        # Add enhanced cubic coupling terms with fractional powers
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.05 * (x[i]**3.7) * np.sin(2.5 * x[j]) + 0.04 * (x[j]**3.8) * np.cos(2.2 * x[i])
        
        # Add quaternion-like coupling terms for increased complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    f_val += 0.02 * (x[i]**2) * np.sin(3 * x[j]) * np.cos(2 * x[k]) + \
                             0.015 * (x[j]**2) * np.cos(3 * x[i]) * np.sin(2 * x[k])
        
        # Add fractional polynomial conditioning with multi-scale exponents
        for i in range(self.dim):
            f_val += 0.03 * (x[i]**4.1) * (1 + 0.18 * np.sin(7 * x[i])) + \
                     0.025 * (x[i]**7.3) * (1 + 0.12 * np.cos(5 * x[i]))
        
        return f_val