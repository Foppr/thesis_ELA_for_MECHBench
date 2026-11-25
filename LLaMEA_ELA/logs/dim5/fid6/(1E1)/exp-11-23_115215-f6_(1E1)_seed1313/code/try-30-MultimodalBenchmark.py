import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f_val = np.sum(x**2)
        
        # Add multiple local minima using sine waves with different frequencies and amplitudes
        for i in range(self.dim):
            f_val += 0.5 * np.sin(7 * x[i]) * np.cos(3 * x[i]) + 0.2 * np.sin(5 * x[i]) + 0.1 * np.sin(8 * x[i])
            
        # Add a global minimum at origin with additional penalty terms
        f_val += 0.02 * np.sum(np.abs(x)) + 0.01 * np.sum(x**4) + 0.005 * np.sum(x**6) + 0.001 * np.sum(x**8)
        
        # Introduce additional complexity with higher frequency components and modified amplitudes
        for i in range(self.dim):
            f_val += 0.25 * np.sin(13 * x[i]) + 0.2 * np.cos(10 * x[i]) + 0.15 * np.sin(16 * x[i])
            
        # Add interaction terms between dimensions to increase complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.06 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) + 0.04 * np.sin(2*x[i]) * np.cos(2*x[j])
                
        # Add cross-dimensional polynomial interactions
        for i in range(self.dim):
            f_val += 0.05 * (x[i]**3) * np.sum(x[:i] if i > 0 else [0]) + 0.03 * x[i]**5
                
        # Add a large number of local minima using a sum of high-frequency sinusoids
        for i in range(self.dim):
            for k in range(1, 7):
                f_val += 0.04 * np.sin(k * 11 * x[i]) * np.cos(k * 8 * x[i])
                
        # Additional cross-dimensional interactions with higher-order terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.02 * (x[i]**2) * (x[j]**3) + 0.01 * x[i] * (x[j]**4)
                
        # Add novel high-frequency coupled terms
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                f_val += 0.08 * np.sin(17 * x[i] + 12 * x[j]) * np.cos(9 * x[i] - 5 * x[j])
                
        # Add exponentially weighted polynomial coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.03 * np.exp(-0.5 * (x[i]**2 + x[j]**2)) * (x[i]**3 + x[j]**3)
                
        # Add a new set of interaction terms with trigonometric products
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.05 * np.sin(x[i] * x[j]) * np.cos(x[i] + x[j]) + 0.02 * np.tan(0.5 * x[i]) * np.sin(0.7 * x[j])
                
        # Add a complex non-linear transformation with multiple sinusoidal components
        for i in range(self.dim):
            f_val += 0.1 * np.sin(20 * x[i] + 3 * np.sin(7 * x[i])) + 0.05 * np.cos(15 * x[i] - 4 * np.cos(6 * x[i]))
                
        # Add a final layer of cross-dimensional coupling with exponential scaling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.04 * np.exp(-0.1 * np.abs(x[i] - x[j])) * (x[i]**2 + x[j]**2)
                
        # Introduce a small mutation to increase difficulty: slightly modify one interaction term
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.015 * np.sin(3*x[i]) * np.cos(4*x[j]) * np.exp(-0.2*(x[i]-x[j])**2)
                
        return f_val