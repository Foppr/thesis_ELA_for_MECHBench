import numpy as np

class HybridChaoticRBF:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic logistic map sequence for dimensionality
        self.logistic_seq = np.array([0.5])
        for i in range(dim * 10):
            self.logistic_seq = np.append(self.logistic_seq, 4.0 * self.logistic_seq[-1] * (1 - self.logistic_seq[-1]))
        self.logistic_seq = self.logistic_seq[:dim]
        
    def f(self, x):
        # Normalize input to [-1, 1] for logistic map
        x_norm = x / 5.0
        
        # Radial Basis Function component with chaotic center placement
        result = 0.0
        for i in range(self.dim):
            # Use logistic sequence for dynamic centers
            center = 2.0 * self.logistic_seq[i] - 1.0
            # Multiquadric RBF with varying shape parameter
            rbf_val = np.sqrt((x_norm[i] - center)**2 + 0.1)
            result += np.exp(-rbf_val**2) * (i + 1)
            
        # Add chaotic logistic map component
        for i in range(self.dim):
            logistic_val = 4.0 * x_norm[i] * (1 - x_norm[i])
            result += 0.5 * np.sin(logistic_val * np.pi) * (i + 1)
            
        # Thin-plate spline component with cross-dimensional interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Use exponential weighting based on dimension
                weight = np.exp(-0.1 * (i + j))
                # Multiquadric thin plate spline interaction
                dist = np.sqrt((x_norm[i] - x_norm[j])**2 + 0.01)
                result += weight * dist**2 * np.log(dist + 1e-10)
                
        # Add a global conditioning term with polynomial scaling
        poly_term = np.sum(x_norm**4) + 0.5 * np.sum(x_norm**3)
        result += 0.3 * poly_term
        
        # Introduce a fractal-like self-similarity through recursive application of logistic map
        logistic_sum = 0.0
        for i in range(self.dim):
            logistic_sum += np.sin(2.0 * self.logistic_seq[i] * np.pi) * (i + 1)
        result += 0.2 * logistic_sum
        
        # Add a small penalty term to avoid exact zero at global minimum
        result += 0.1 * np.sum(x**2) / (self.dim + 1)
        
        return result