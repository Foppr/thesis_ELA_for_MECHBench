import numpy as np

class ChaoticSpiralFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize function value
        f_val = 0.0
        
        # Add chaotic logarithmic spiral components
        for i in range(self.dim):
            r = np.sqrt(x[i]**2 + 0.1)
            theta = np.arctan2(x[i], 0.1) + 3 * np.log(r + 1)
            f_val += 0.5 * np.sin(10 * theta) * np.exp(-0.1 * r)
        
        # Add adaptive radial basis functions with dynamic centers and widths
        for i in range(self.dim):
            center = 3.0 * np.sin(0.3 * i) - 1.5
            width = 0.05 + 0.1 * np.cos(0.2 * i)
            f_val += 0.8 * np.exp(-width * (x[i] - center)**2) * (1 + 0.3 * np.sin(5 * x[i]))
        
        # Add dynamic polynomial coupling with varying exponents
        for i in range(self.dim):
            exponent = 2 + 3 * np.sin(0.4 * i)
            f_val += 0.3 * (x[i]**exponent) * (1 + 0.2 * np.cos(7 * x[i]))
        
        # Add self-similar fractal components with recursive scaling
        scale_factor = 0.3
        for k in range(1, 6):
            for i in range(self.dim):
                f_val += scale_factor * np.sin(k * 20 * x[i]) * np.cos(k * 15 * x[i]) * (1 + 0.2 * np.sin(k * 10 * x[i]))
            scale_factor *= 0.6
        
        # Add harmonic boundary penalties with adaptive strength
        for i in range(self.dim):
            if abs(x[i]) > 4.0:
                strength = 5.0 + 3.0 * np.sin(0.5 * i)
                f_val += strength * (abs(x[i]) - 4.0)**3
        
        # Add cross-dimensional coupling with dynamic interaction strengths
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                strength = 0.2 + 0.1 * np.sin(0.3 * (i + j))
                f_val += strength * np.sin(5 * x[i]) * np.cos(4 * x[j]) * np.exp(-0.5 * (x[i] - x[j])**2)
        
        # Add multi-scale chaotic modulation with varying frequencies
        freqs = [1, 3, 7, 11, 19]
        for k, freq in enumerate(freqs):
            f_val += 0.15 * np.sin(freq * np.sum(x)) * np.cos(freq * np.sum(x) / 2) * (1 + 0.2 * np.sin(freq * np.sum(x)**2))
        
        # Add chaotic cubic coupling with variable interaction coefficients
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coeff = 0.1 + 0.05 * np.cos(0.4 * i) * np.sin(0.4 * j)
                f_val += coeff * (x[i]**3) * (x[j]**2) * np.sin(3 * x[i] + x[j])
        
        # Add fractal-like radial components with recursive scaling
        for i in range(self.dim):
            r = np.sqrt(x[i]**2 + 0.01)
            f_val += 0.2 * np.sin(15 * r) * np.cos(12 * r) * (1 + 0.25 * np.sin(8 * r))
        
        # Add harmonic polynomial terms with dynamic coefficients
        for i in range(self.dim):
            f_val += 0.1 * x[i]**4 * np.sin(3 * x[i]) + 0.08 * x[i]**6 * np.cos(2 * x[i])
        
        return f_val