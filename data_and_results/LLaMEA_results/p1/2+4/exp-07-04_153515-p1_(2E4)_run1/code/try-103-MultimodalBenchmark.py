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
            f_val += 0.2 * np.sin(5 * x[i]) * np.cos(3 * np.sin(x[i])) * np.exp(-0.1 * x[i]**2)
        
        # Add radial basis function components with random centers and widths
        centers = np.random.uniform(-5, 5, (7, self.dim))
        widths = np.random.uniform(0.3, 1.5, 7)
        for i in range(7):
            dist = np.sum((x - centers[i])**2)
            f_val += 0.15 * np.exp(-widths[i] * dist) * np.cos(2 * np.sum(x - centers[i]))
        
        # Add asymmetric polynomial terms with logistic modulation
        for i in range(self.dim):
            if x[i] >= 0:
                f_val += 0.08 * (x[i]**3) * np.cos(1.5 * x[i]) + 0.04 * (x[i]**5) * np.sin(0.7 * x[i])
            else:
                f_val += 0.06 * (x[i]**4) * np.sin(2 * x[i]) + 0.05 * (x[i]**6) * np.cos(0.4 * x[i])
        
        # Add a complex interaction term between all pairs of variables with logistic coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.12 * np.cos(3 * x[i]) * np.sin(2 * x[j]) * np.exp(-0.15 * (x[i] - x[j])**2) * (1 + 0.2 * np.tanh(x[i] + x[j]))
        
        # Add a global logistic modulation based on the norm of x
        norm = np.sqrt(np.sum(x**2))
        f_val += 0.15 * np.tanh(0.4 * norm) * np.cos(0.6 * norm)
        
        return f_val