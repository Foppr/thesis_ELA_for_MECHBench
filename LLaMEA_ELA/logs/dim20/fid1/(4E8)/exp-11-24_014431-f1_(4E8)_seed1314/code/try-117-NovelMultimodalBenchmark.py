import numpy as np

class NovelMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize function value
        f_val = 0.0
        
        # Add enhanced periodic components with chaotic modulation and higher frequency terms
        for i in range(self.dim):
            f_val += 0.5 * np.sin(2.0 * np.pi * x[i]) + 0.4 * np.cos(3.0 * np.pi * x[i]) + \
                     0.3 * np.sin(5.0 * np.pi * x[i]) + 0.25 * np.cos(7.0 * np.pi * x[i]) + \
                     0.2 * np.sin(9.0 * np.pi * x[i]) + 0.15 * np.cos(11.0 * np.pi * x[i]) + \
                     0.1 * np.sin(13.0 * np.pi * x[i]) * (1.0 + 0.4 * np.sin(5.0 * x[i]))
        
        # Add modified radial basis function components with adaptive widths and additional terms
        centers = np.linspace(-4.5, 4.5, self.dim)
        widths = np.logspace(-1.5, 1.5, self.dim)
        for i in range(self.dim):
            f_val += 0.7 * np.exp(-0.5 * ((x[i] - centers[i]) / widths[i])**2) + \
                     0.3 * np.exp(-0.3 * ((x[i] - centers[i]) / (widths[i] * 0.5))**4) + \
                     0.15 * np.exp(-0.2 * ((x[i] - centers[i]) / (widths[i] * 0.7))**6)
        
        # Add enhanced cross-dimensional polynomial interactions with chaotic coupling and additional terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.12 * (x[i]**2 + x[j]**2) * np.sin(0.5 * (x[i] - x[j])**2) * \
                         (1.0 + 0.3 * np.sin(3.0 * x[i]) * np.cos(2.0 * x[j])) + \
                         0.08 * x[i]**3 * x[j]**2 * np.cos(0.3 * (x[i] + x[j])) * \
                         (1.0 + 0.2 * np.sin(4.0 * x[i]))
        
        # Add multi-scale harmonic interaction with exponential coupling and additional complex terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.08 * np.sin(4.0 * x[i]) * np.cos(3.0 * x[j]) * \
                         np.exp(-0.1 * (x[i] - x[j])**2) * (1 + 0.4 * np.sin(2.0 * (x[i] + x[j]))) + \
                         0.05 * np.cos(5.0 * x[i]) * np.sin(6.0 * x[j]) * \
                         np.exp(-0.05 * (x[i] + x[j])**2) * (1 + 0.3 * np.cos(3.0 * (x[i] - x[j])))
        
        # Add global sine modulation with chaotic frequency variation and additional terms
        sum_x = np.sum(x)
        f_val += 0.4 * np.sin(0.3 * sum_x**2) + 0.3 * np.cos(0.4 * sum_x**3) + \
                 0.2 * np.sin(0.5 * sum_x**4) * (1.0 + 0.3 * np.sin(0.2 * sum_x)) + \
                 0.15 * np.cos(0.6 * sum_x**5) * (1.0 + 0.2 * np.cos(0.3 * sum_x))
        
        # Add enhanced boundary penalty terms with exponential scaling and additional terms
        for i in range(self.dim):
            f_val += 0.5 * np.exp(-0.4 * (x[i] - 4.0)**2) + 0.4 * np.exp(-0.3 * (x[i] + 4.0)**2) + \
                     0.25 * np.exp(-0.2 * (x[i] - 5.0)**2) + 0.2 * np.exp(-0.1 * (x[i] + 5.0)**2) + \
                     0.1 * np.exp(-0.3 * (x[i] - 4.5)**2) + 0.08 * np.exp(-0.2 * (x[i] + 4.5)**2)
        
        # Add enhanced conditioning term with fractional powers and additional polynomial terms
        f_val += 0.2 * np.sum(x**4) + 0.15 * np.sum(x**6) + 0.1 * np.sum(x**8) + \
                 0.08 * np.sum(np.abs(x)**3.5) + 0.05 * np.sum(x**10)
        
        # Add novel fractal-like self-similar structure with recursive scaling
        for i in range(self.dim):
            f_val += 0.08 * np.sin(10.0 * x[i]) * np.cos(8.0 * x[i]) * \
                     (1.0 + 0.2 * np.sin(6.0 * x[i])) + \
                     0.05 * np.cos(12.0 * x[i]) * np.sin(9.0 * x[i]) * \
                     (1.0 + 0.15 * np.cos(7.0 * x[i]))
        
        # Add recursive self-similar structure with adaptive coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.03 * np.sin(8.0 * x[i]) * np.cos(7.0 * x[j]) * \
                         (1.0 + 0.25 * np.sin(4.0 * (x[i] + x[j]))) * \
                         np.exp(-0.1 * (x[i] - x[j])**2) + \
                         0.02 * np.cos(9.0 * x[i]) * np.sin(8.0 * x[j]) * \
                         (1.0 + 0.2 * np.cos(5.0 * (x[i] - x[j]))) * \
                         np.exp(-0.05 * (x[i] + x[j])**2)
        
        return f_val