import numpy as np

class ChaoticRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f_val = np.sum(x**2)
        
        # Add logarithmic barrier terms to create ruggedness
        for i in range(self.dim):
            f_val += 10.0 * np.log(1.0 + np.abs(x[i])) + 5.0 * np.log(1.0 + x[i]**2)
            
        # Add chaotic trigonometric interactions with varying frequencies
        for i in range(self.dim):
            f_val += 3.0 * np.sin(np.exp(x[i])) + 2.0 * np.cos(np.pi * np.exp(x[i]))
            
        # Add power-law coupled terms with varying exponents
        for i in range(self.dim):
            f_val += 0.5 * np.abs(x[i])**1.7 + 0.3 * np.abs(x[i])**2.3
            
        # Cross-dimensional power-law interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.1 * (np.abs(x[i])**(1.5 + 0.1*j)) * (np.abs(x[j])**(1.2 + 0.05*i))
                
        # Add a complex multi-scale sinusoidal landscape
        for i in range(self.dim):
            f_val += 2.0 * np.sin(10 * x[i] + np.sin(3 * x[i])) + 1.5 * np.cos(7 * x[i] + np.cos(5 * x[i]))
            
        # Add exponentially increasing frequency components
        for k in range(1, 6):
            for i in range(self.dim):
                f_val += 0.2 * np.sin(k**2 * x[i]) * np.cos(k * x[i]**2)
                
        # Add chaotic coupling terms with exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.05 * np.exp(-np.abs(x[i] - x[j])) * np.sin(10 * (x[i]**2 + x[j]**2))
                
        # Add a final layer of logarithmic penalty with cross-dimensional terms
        for i in range(self.dim):
            f_val += 0.8 * np.log(1.0 + np.abs(x[i] - 1.0)) + 0.4 * np.log(1.0 + np.abs(x[i] + 1.0))
            
        # Add a highly non-linear transformation
        for i in range(self.dim):
            f_val += 1.2 * np.sin(np.tan(x[i] / 2.0)) + 0.8 * np.cos(np.log(np.abs(x[i]) + 1.0))
            
        return f_val