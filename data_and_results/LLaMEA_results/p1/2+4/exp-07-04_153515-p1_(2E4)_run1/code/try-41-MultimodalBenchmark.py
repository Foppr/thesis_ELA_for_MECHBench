import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic function
        f_val = np.sum(x**2)
        
        # Add multiple periodic components with varying frequencies and amplitudes
        for i in range(self.dim):
            f_val += 0.3 * np.sin(7 * x[i]) * np.cos(4 * x[i]) + 0.2 * np.sin(3 * x[i])**2 + 0.1 * np.cos(5 * x[i])
        
        # Introduce complex exponential interactions between variables to create rugged landscape
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.1 * np.exp(-0.3 * (x[i] - x[j])**2) * np.sin(6 * (x[i] + x[j])) + 0.05 * np.exp(-0.2 * (x[i] + x[j])**2) * np.cos(3 * (x[i] - x[j]))
        
        # Add higher-order polynomial terms with sinusoidal modulation
        for i in range(self.dim):
            f_val += 0.05 * (x[i]**6) * np.cos(3 * x[i]) + 0.03 * (x[i]**4) * np.sin(4 * x[i]) + 0.02 * (x[i]**3) * np.cos(2 * x[i])
        
        # Incorporate multiple shifted exponential terms to generate numerous local minima
        for i in range(self.dim):
            f_val += 0.15 * np.exp(-0.4 * (x[i] - 2.5)**2) * np.sin(5 * (x[i] - 2.5)) + 0.1 * np.exp(-0.2 * (x[i] + 2.0)**2) * np.cos(4 * (x[i] + 2.0))
        
        # Add cross-terms with sine and cosine products to increase complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.08 * np.sin(2 * x[i]) * np.cos(3 * x[j]) + 0.06 * np.cos(4 * x[i]) * np.sin(2 * x[j])
        
        return f_val