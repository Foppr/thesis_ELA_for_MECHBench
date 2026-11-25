import numpy as np

class ChaoticGaussianCorrelationBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize function value
        f_val = 0.0
        
        # Add chaotic Gaussian peak components with dynamic centers and widths
        for i in range(self.dim):
            center = 3.0 * np.sin(0.5 * i) - 1.5
            width = 0.1 + 0.2 * np.cos(0.4 * i)
            f_val += 2.0 * np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Add trigonometric correlation terms with adaptive coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.3 * (1 + 0.5 * np.sin(0.7 * (i - j)))
                f_val += coupling * np.sin(3 * x[i]) * np.cos(2 * x[j]) * \
                         np.exp(-0.3 * (x[i] - x[j])**2)
        
        # Add polynomial conditioning with chaotic exponents
        for i in range(self.dim):
            exponent = 2 + 1.5 * np.sin(0.6 * i)
            f_val += 0.2 * (x[i]**exponent) * (1 + 0.3 * np.cos(4 * x[i]))
        
        # Add dynamic coupling terms with time-varying strengths
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                strength = 0.25 * (1 + np.sin(0.8 * i) * np.cos(0.6 * j))
                f_val += strength * np.exp(-0.5 * (x[i] - x[j])**2) * \
                         np.sin(5 * (x[i] + x[j]))
        
        # Add fractal-like harmonic components with recursive scaling
        scale_factor = 0.1
        for k in range(1, 6):
            for i in range(self.dim):
                f_val += scale_factor * np.sin(k * 8 * x[i]) * np.cos(k * 6 * x[i])
            scale_factor *= 0.7
        
        # Add chaotic sine-wave interactions with varying frequencies
        for i in range(self.dim):
            freq = 5 + 3 * np.sin(0.3 * i)
            f_val += 0.15 * np.sin(freq * x[i]) * (1 + 0.2 * np.cos(2 * freq * x[i]))
        
        # Add boundary penalties with exponential growth
        penalty = 0.0
        for i in range(self.dim):
            if abs(x[i]) > 4.7:
                penalty += 10 * np.exp(2 * (abs(x[i]) - 4.7))
        f_val += penalty
        
        # Add cubic coupling with dynamic interaction coefficients
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coeff = 0.1 * (1 + 0.5 * np.sin(0.4 * i) * np.cos(0.3 * j))
                f_val += coeff * x[i]**3 * x[j]**2 * np.sin(2 * (x[i] - x[j]))
        
        # Add adaptive harmonic modulation with multi-scale components
        for i in range(self.dim):
            mod_freq = 15 + 8 * np.sin(0.5 * i)
            f_val += 0.08 * np.sin(mod_freq * x[i]) * np.cos(mod_freq * x[i] / 3) * \
                     (1 + 0.15 * np.sin(3 * x[i]))
        
        return f_val