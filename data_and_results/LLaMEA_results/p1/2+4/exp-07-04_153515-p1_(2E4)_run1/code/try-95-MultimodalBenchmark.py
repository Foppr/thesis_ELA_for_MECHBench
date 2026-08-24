import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f_val = np.sum(x**2)
        
        # Add chaotic logistic map interactions
        for i in range(self.dim):
            f_val += 0.2 * np.sin(5 * np.log(4 * np.abs(x[i]) + 1)) * np.cos(3 * x[i])
        
        # Add radial basis function components with random centers and widths
        centers = np.random.uniform(-5, 5, (5, self.dim))
        widths = np.random.uniform(0.5, 2.0, 5)
        for i in range(5):
            dist = np.sum((x - centers[i])**2)
            f_val += 0.15 * np.exp(-widths[i] * dist) * np.cos(2 * np.sum(x - centers[i]))
        
        # Add asymmetric polynomial terms with logistic modulation
        for i in range(self.dim):
            if x[i] >= 0:
                f_val += 0.08 * (x[i]**3) * np.sin(3 * x[i]) + 0.03 * (x[i]**5) * np.cos(0.7 * x[i])
            else:
                f_val += 0.06 * (x[i]**4) * np.cos(2 * x[i]) + 0.04 * (x[i]**6) * np.sin(0.4 * x[i])
        
        # Add a complex interaction term between all pairs of variables using logistic functions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.12 * np.sin(3 * x[i]) * np.cos(2 * x[j]) * np.exp(-0.1 * (x[i] - x[j])**2)
        
        # Add a global logistic modulation based on the norm of x
        norm = np.sqrt(np.sum(x**2))
        f_val += 0.15 * np.log(3 * norm + 1) * np.sin(0.4 * norm)
        
        return f_val