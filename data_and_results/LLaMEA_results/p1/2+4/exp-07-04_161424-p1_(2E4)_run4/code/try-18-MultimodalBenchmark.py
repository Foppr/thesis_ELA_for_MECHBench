import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quadratic base term with slight noise
        quadratic = np.sum(x_norm**2) + 0.01 * np.random.rand()
        
        # Chaotic sinusoidal terms using logistic map dynamics
        logistic_map = np.sin(10 * np.pi * x_norm) * np.exp(-0.5 * x_norm**2)
        chaotic = np.sum(logistic_map**2 + 0.3 * np.sin(15 * x_norm) * np.cos(7 * x_norm))
        
        # Radial basis function components with varying widths
        rbf = np.sum(np.exp(-2 * (x_norm - 0.5)**2) + np.exp(-3 * (x_norm + 0.3)**2) + np.exp(-1.5 * x_norm**2))
        
        # Polynomial interaction terms with asymmetric coefficients
        polynomial = np.sum((x_norm**5 + 0.7 * x_norm**4 + 0.3 * x_norm**3 + 0.1 * x_norm**2) * np.sin(5 * np.pi * x_norm))
        
        # Cross-dimensional interaction using chaotic exponential decay
        cross_term = np.exp(-np.sum(np.abs(x_norm)**1.5)) * np.prod(np.sin(3 * np.pi * x_norm) + 0.2 * np.cos(2 * np.pi * x_norm))
        
        # Asymmetric noise perturbation
        noise = 0.02 * np.sum(np.sin(20 * x_norm)**3 + 0.5 * np.cos(12 * x_norm)**2)
        
        # Add a complex global minimum structure
        global_structure = 0.05 * np.sum(np.sin(25 * x_norm)**4 + np.cos(18 * x_norm)**3)
        
        # Combine all terms with varying weights
        return 1.5 * quadratic + 0.8 * chaotic + 0.3 * rbf + 0.25 * polynomial + 0.1 * cross_term + noise + global_structure