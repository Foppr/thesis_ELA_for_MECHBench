import numpy as np

class PolynomialRBFStochasticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute random coefficients for stochastic perturbations
        np.random.seed(42)
        self.coeffs = np.random.uniform(-1.0, 1.0, (dim, 10))
        
    def f(self, x):
        x = np.array(x)
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Polynomial chaos expansion component with mixed terms
        for i in range(self.dim):
            xi = x[i]
            result += (xi**2 + xi**3 + 0.5 * xi**4) * (1.0 + 0.1 * i)
            
        # Radial basis function with varying widths and centers
        for i in range(min(5, self.dim)):
            center = np.random.uniform(-4.0, 4.0)
            width = np.random.uniform(0.5, 2.0)
            result += 0.5 * np.exp(-width * (x[i] - center)**2) * (1.0 + 0.2 * i)
            
        # Cross-dimensional coupling with trigonometric interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.3 * np.sin(x[i] * x[j]) * np.cos(0.5 * (x[i] + x[j]))
                
        # Stochastic perturbation using precomputed coefficients
        for i in range(self.dim):
            for k in range(10):
                result += self.coeffs[i, k] * np.sin((k+1) * x[i]) * np.cos((k+2) * x[i])
                
        # Dynamic radial component with time-like parameter
        if self.dim >= 2:
            r = np.sqrt(np.sum(x[:2]**2))
            result += 0.4 * np.sin(5.0 * r + 0.1 * r**3) * np.exp(-0.1 * r)
            
        # Asymmetric polynomial with varying exponents
        for i in range(self.dim):
            if x[i] >= 0:
                result += 0.2 * (x[i]**3 + 0.5 * x[i]**5)
            else:
                result += 0.25 * (abs(x[i])**2.5 + 0.3 * abs(x[i])**4)
                
        # High-frequency oscillatory term with varying amplitudes
        for i in range(self.dim):
            result += 0.15 * np.sin(20.0 * x[i] + 0.5 * np.sin(5.0 * x[i]))
            
        # Boundary attraction and repulsion terms
        for i in range(self.dim):
            if abs(x[i]) < 1.0:
                result += 0.3 * (1.0 - abs(x[i]))**2
            else:
                result += 0.2 * (abs(x[i]) - 4.0)**2
                
        # Interaction between every third dimension for added complexity
        for i in range(0, self.dim, 3):
            if i + 2 < self.dim:
                result += 0.1 * x[i] * x[i+1] * x[i+2] * np.exp(-0.1 * (x[i]**2 + x[i+1]**2 + x[i+2]**2))
                
        # Global scaling with dynamic factor
        global_factor = 1.0 + 0.1 * np.sin(np.sum(x**2) / 10.0)
        result *= global_factor
        
        return result