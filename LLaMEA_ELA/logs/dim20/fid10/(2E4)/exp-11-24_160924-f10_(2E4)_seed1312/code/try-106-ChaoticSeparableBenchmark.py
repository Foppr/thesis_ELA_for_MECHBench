import numpy as np

class ChaoticSeparableBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Separable chaotic components with sinusoidal modulation
        for i in range(self.dim):
            xi = x[i]
            # Chaotic sinusoidal term with varying frequency
            chaos_term = np.sin(13.0 * xi) * np.cos(7.0 * xi)
            result += 0.5 * chaos_term * (1.0 + 0.1 * np.sin(2.0 * xi))
            
        # Add adaptive coupling terms with dimension-dependent strengths
        for i in range(self.dim):
            xi = x[i]
            # Adaptive coupling strength based on dimension index
            coupling_strength = 1.0 + 0.3 * np.sin(0.5 * i)
            # High-order polynomial with chaotic modulation
            result += coupling_strength * (xi**5 - 2*xi**3 + xi) * np.exp(-0.1 * xi**2)
            
        # Add non-separable coupling using chaotic rational functions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic coupling with dimension-dependent weights
                weight = 0.5 + 0.2 * np.sin(0.3 * (i - j))
                # Rational function with chaotic numerator and denominator
                numerator = np.sin(xi) * np.cos(xj) + 0.1 * xi**3
                denominator = np.cos(xi) * np.sin(xj) + 0.1 * xj**3 + 0.01
                result += weight * (numerator / denominator)
                
        # Add multi-modal structure with chaotic peaks
        for i in range(self.dim):
            xi = x[i]
            # Multiple chaotic peak locations
            peak1 = 2.0 * np.exp(-0.5 * (xi - 1.0)**2) * np.sin(3.0 * xi)
            peak2 = 1.5 * np.exp(-0.5 * (xi + 1.0)**2) * np.cos(2.0 * xi)
            peak3 = 1.0 * np.exp(-0.5 * (xi - 2.0)**2) * np.sin(4.0 * xi)
            result += peak1 + peak2 + peak3
            
        # Add gradient complexity through chaotic rational derivatives
        if self.dim >= 2:
            for i in range(self.dim - 1):
                # Chaotic gradient-inducing term
                numerator = np.sin(xi) * np.cos(x[i+1]) + np.cos(xi) * np.sin(x[i+1])
                denominator = np.cos(xi) * np.cos(x[i+1]) + np.sin(xi) * np.sin(x[i+1]) + 0.1
                result += 0.4 * (numerator / denominator)
                
        # Add chaotic penalty near global optimum
        global_optimum = np.ones(self.dim) * 1.5
        dist = np.sum((x - global_optimum)**2)
        result += 0.3 * np.exp(-dist/2.0) + 0.2 * np.sum(np.abs(x - 1.5)**4)
        
        # Add high-order polynomial terms with chaotic coefficients
        for i in range(self.dim):
            xi = x[i]
            # Chaotic coefficient based on dimension and input value
            coeff = 1.0 + 0.2 * np.sin(3.0 * i) * np.cos(xi)
            result += coeff * (xi**7 - 3*xi**5 + 3*xi**3 - xi)
            
        return result