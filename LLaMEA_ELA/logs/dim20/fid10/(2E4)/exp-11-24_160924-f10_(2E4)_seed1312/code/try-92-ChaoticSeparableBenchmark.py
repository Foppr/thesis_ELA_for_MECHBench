import numpy as np

class ChaoticSeparableBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Separable chaotic trigonometric components with varying frequencies and amplitudes
        for i in range(self.dim):
            xi = x[i]
            # Use chaotic sine and cosine combinations with dynamic amplitudes
            amplitude = 1.0 + 0.5 * np.sin(0.3 * i)
            result += amplitude * (np.sin(2.5 * xi) + 0.7 * np.cos(3.2 * xi)) * np.exp(-0.1 * xi**2)
            
        # Add non-separable coupling with exponential decay and chaotic interaction
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic coupling strength based on dimension indices
                coupling = 1.2 + 0.8 * np.sin(0.5 * (i + j))
                distance = np.sqrt((x[i] - x[j])**2 + 0.01)
                result += coupling * np.exp(-0.3 * distance) * np.sin(5 * (x[i] + x[j]))
                
        # Add high-order polynomial terms with chaotic coefficients
        for i in range(self.dim):
            xi = x[i]
            # Use chaotic polynomial coefficients that vary with dimension index
            coeff = 1.0 + 0.3 * np.cos(0.4 * i)
            result += coeff * (xi**7 - 3 * xi**5 + 2 * xi**3 - xi) * np.exp(-0.2 * xi**2)
            
        # Add adaptive scaling based on global statistics
        mean_x = np.mean(x)
        std_x = np.std(x)
        result += 0.5 * (std_x**2 + mean_x**2) * np.sin(1.5 * np.sum(x))
        
        # Add chaotic interaction terms involving multiple dimensions
        if self.dim >= 3:
            for i in range(self.dim - 2):
                # Triple-wise interactions with chaotic coupling
                result += 0.8 * np.sin(x[i] + x[i+1] + x[i+2]) * np.cos(0.7 * (x[i] - x[i+1]))
                
        # Add exponential conditioning term that increases difficulty with dimensionality
        result += 0.3 * np.sum(np.exp(0.5 * x**2) * np.sin(2 * x))
        
        # Add chaotic penalty near the global optimum to increase convergence difficulty
        result += 0.4 * np.sum((x - 1.0)**6) + 0.2 * np.sum(np.abs(x - 1.0))
        
        return result