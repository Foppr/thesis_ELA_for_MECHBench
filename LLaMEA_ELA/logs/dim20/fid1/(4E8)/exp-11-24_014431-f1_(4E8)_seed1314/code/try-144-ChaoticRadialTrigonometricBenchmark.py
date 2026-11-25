import numpy as np

class ChaoticRadialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize function value
        f_val = 0.0
        
        # Add chaotic radial basis components with varying centers and widths
        for i in range(self.dim):
            center = 3.5 * np.sin(0.7 * i) - 1.5
            width = 0.02 + 0.18 * np.cos(0.4 * i)
            f_val += 0.8 * np.exp(-width * (x[i] - center)**2)
        
        # Add trigonometric coupling terms with varying frequencies and amplitudes
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq = 3 + 2 * np.sin(0.5 * i) * np.cos(0.5 * j)
                amp = 0.6 + 0.4 * np.sin(0.3 * (i + j))
                f_val += amp * np.sin(freq * (x[i] - x[j])) * np.cos(freq * (x[i] + x[j]))
        
        # Add adaptive polynomial conditioning with chaotic exponents
        for i in range(self.dim):
            exp = 3 + 2 * np.sin(0.6 * i)
            f_val += 0.5 * (x[i]**exp) * (1 + 0.3 * np.cos(5 * x[i]))
        
        # Add chaotic harmonic components with multi-scale modulation
        for k in range(1, 8):
            scale = 0.25 * (0.8 ** k)
            for i in range(self.dim):
                f_val += scale * np.sin(k * 15 * x[i]) * np.cos(k * 12 * x[i])
        
        # Add boundary penalty with chaotic scaling
        penalty = 0.0
        for i in range(self.dim):
            if abs(x[i]) > 4.7:
                penalty += 18 * (abs(x[i]) - 4.7)**3
        f_val += penalty
        
        # Add cross-dimensional exponential interactions with adaptive coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.25 + 0.15 * np.sin(0.4 * i) * np.cos(0.4 * j)
                f_val += coupling * np.exp(-0.3 * (x[i] - x[j])**2) * np.sin(5 * (x[i] + x[j]))
        
        # Add chaotic phase-shifted sine components
        for i in range(self.dim):
            f_val += 0.4 * np.sin(10 * x[i] + 0.5 * np.sin(3 * x[i])) + \
                     0.3 * np.cos(8 * x[i] + 0.4 * np.cos(2 * x[i]))
        
        # Add fractal-like self-similar structure with recursive scaling
        scale_factor = 0.18
        for k in range(1, 6):
            for i in range(self.dim):
                f_val += scale_factor * np.sin(k * 20 * x[i]) * np.cos(k * 18 * x[i])
            scale_factor *= 0.4
        
        return f_val