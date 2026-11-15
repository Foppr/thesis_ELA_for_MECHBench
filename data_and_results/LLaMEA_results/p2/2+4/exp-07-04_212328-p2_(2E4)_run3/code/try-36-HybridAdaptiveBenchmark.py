import numpy as np

class HybridAdaptiveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension mismatch")
        
        # Base polynomial term with adaptive scaling
        f = np.sum(x**4) * 0.5
        
        # Add trigonometric components with varying frequencies and amplitudes
        for i in range(self.dim):
            f += 0.3 * np.sin(2 * np.pi * x[i]) * np.cos(3 * np.pi * x[i]) * np.sin(5 * np.pi * x[i])
            
        # Add radial basis function components with adaptive centers and widths
        centers = np.linspace(-4.0, 4.0, min(5, self.dim))
        for i in range(min(5, self.dim)):
            if i < len(centers):
                f += 0.2 * np.exp(-0.5 * ((x[i] - centers[i]) / (0.5 + 0.1 * i))**2)
                
        # Add asymmetric valley structure with directional bias
        for i in range(self.dim):
            f += 0.1 * (x[i] - 1.0)**2 * (x[i] + 2.0)**2 * np.sin(0.5 * x[i])
            
        # Add coupled oscillatory terms with varying coupling strengths
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                coupling = 0.05 * (i + 1) * (j + 1) / (self.dim + 1)
                f += coupling * np.sin(2 * x[i] + x[j]) * np.cos(x[i] - 2 * x[j])
                
        # Add multi-modal structure with varying local minima
        local_minima = np.array([[-2.0, 2.0], [2.0, -2.0], [0.0, 0.0], [-1.0, -1.0], [1.0, 1.0]])
        minima_term = 0
        for min_point in local_minima:
            if self.dim >= len(min_point):
                diff = x[:len(min_point)] - min_point
                minima_term += np.exp(-0.3 * np.sum(diff**2))
        f += 0.4 * minima_term
        
        # Add noise component with non-uniform distribution
        noise = np.random.normal(0, 0.01, self.dim)
        f += 0.02 * np.sum(noise * np.sin(10 * x))
        
        # Add directional scaling and rotation effects
        rotation_matrix = np.random.rand(self.dim, self.dim) * 2 - 1
        rotated_x = np.dot(rotation_matrix, x)
        f += 0.05 * np.sum(rotated_x**3)
        
        # Add adaptive difficulty parameter based on dimensionality
        adaptive_factor = 1.0 + 0.1 * np.log(self.dim + 1)
        f *= adaptive_factor
        
        return f