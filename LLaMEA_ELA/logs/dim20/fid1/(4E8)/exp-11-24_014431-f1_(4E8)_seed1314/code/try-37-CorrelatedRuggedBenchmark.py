import numpy as np

class CorrelatedRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize function value
        f_val = 0.0
        
        # Add quadratic term for conditioning
        f_val += 0.5 * np.sum(x**2)
        
        # Add exponentially decaying correlation structure
        # Correlation decreases with distance between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Stronger exponential decay
                corr = np.exp(-0.2 * (j - i))
                f_val += 0.4 * corr * x[i] * x[j]
        
        # Add ruggedness through high-frequency sinusoidal terms
        for i in range(self.dim):
            # Shifted and scaled frequencies
            f_val += 0.3 * np.sin(15 * x[i]) * np.cos(7 * x[i])
            
        # Add polynomial penalty to encourage convergence to origin
        f_val += 0.02 * np.sum(x**4) + 0.01 * np.sum(x**6)
        
        # Add cubic interaction terms for higher-order correlations
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    strength = 0.015 / (1.0 + np.exp(-0.3*(i+j+k)))
                    f_val += strength * x[i] * x[j] * x[k]
                
        # Add modified interaction terms with varying strengths based on dimension indices
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                strength = 0.03 / (1.0 + np.exp(-0.4*(i+j)))
                f_val += strength * np.sin(2*x[i]) * np.cos(3*x[j])
                
        return f_val