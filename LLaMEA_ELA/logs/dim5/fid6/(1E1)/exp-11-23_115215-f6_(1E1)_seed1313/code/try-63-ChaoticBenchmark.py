import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute logistic map parameters for chaos generation
        self.r_values = np.linspace(3.5, 4.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f_val = np.sum(x**2)
        
        # Add chaotic logistic map components
        for i in range(self.dim):
            # Logistic map with parameter r_i
            if i == 0:
                logistic_val = x[i]
            else:
                logistic_val = self.r_values[i] * x[i-1] * (1 - x[i-1])
            f_val += 0.3 * np.sin(logistic_val * 10) * np.cos(logistic_val * 7)
            
        # Add radial basis function components with varying widths
        for i in range(self.dim):
            # Radial basis with dynamic center and width
            center = np.sin(i * 0.5) * 3.0
            width = 0.5 + 0.5 * np.cos(i * 0.3)
            f_val += 0.2 * np.exp(-0.5 * ((x[i] - center) / width)**2)
            
        # Add asymmetric coupling terms
        for i in range(self.dim):
            if i > 0:
                # Asymmetric interaction: stronger influence from previous dimension
                f_val += 0.15 * (x[i] - x[i-1])**3 + 0.1 * np.abs(x[i] - x[i-1])**1.5
                
        # Add multi-scale sinusoidal modulations
        for i in range(self.dim):
            f_val += 0.25 * np.sin(2 * x[i]) * np.cos(3 * x[i]) + \
                     0.1 * np.sin(5 * x[i]) * np.cos(7 * x[i]) + \
                     0.05 * np.sin(11 * x[i])
                     
        # Add polynomial coupling with exponential weights
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = np.exp(-0.1 * (i + j))
                f_val += weight * (x[i]**2) * (x[j]**3) + 0.05 * x[i] * x[j]
                
        # Add chaotic phase coupling with time-delayed terms
        for i in range(self.dim):
            if i > 1:
                delayed_term = np.sin(x[i-2] + 0.5 * x[i-1])
                f_val += 0.1 * delayed_term * np.cos(x[i])
                
        # Add a final complex non-linear transformation
        f_val += 0.1 * np.sin(np.sum(x**3)) + 0.05 * np.cos(np.prod(x))
        
        return f_val