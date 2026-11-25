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
            amplitude = 2.0 + 1.2 * np.sin(0.5 * i)
            result += amplitude * (np.sin(4.0 * xi) + 0.8 * np.cos(5.0 * xi)) * np.exp(-0.2 * xi**2)
            
        # Add non-separable coupling with exponential decay and chaotic interaction
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic coupling strength based on dimension indices
                coupling = 2.0 + 1.5 * np.sin(0.7 * (i + j))
                distance = np.sqrt((x[i] - x[j])**2 + 0.03)
                result += coupling * np.exp(-0.5 * distance) * np.sin(8 * (x[i] + x[j]))
                
        # Add high-order polynomial terms with chaotic coefficients
        for i in range(self.dim):
            xi = x[i]
            # Use chaotic polynomial coefficients that vary with dimension index
            coeff = 1.5 + 0.6 * np.cos(0.6 * i)
            result += coeff * (xi**9 - 4.0 * xi**7 + 3.0 * xi**5 - 1.5 * xi**3 + 0.5 * xi) * np.exp(-0.3 * xi**2)
            
        # Add adaptive scaling based on global statistics
        mean_x = np.mean(x)
        std_x = np.std(x)
        result += 1.0 * (std_x**2 + mean_x**2) * np.sin(3.0 * np.sum(x))
        
        # Add chaotic interaction terms involving multiple dimensions
        if self.dim >= 4:
            for i in range(self.dim - 3):
                # Quadruple-wise interactions with chaotic coupling
                result += 1.5 * np.sin(x[i] + x[i+1] + x[i+2] + x[i+3]) * np.cos(0.9 * (x[i] - x[i+1]))
                
        # Add exponential conditioning term that increases difficulty with dimensionality
        result += 0.6 * np.sum(np.exp(0.7 * x**2) * np.sin(3.0 * x))
        
        # Add chaotic penalty near the global optimum to increase convergence difficulty
        result += 0.8 * np.sum((x - 1.5)**9) + 0.5 * np.sum(np.abs(x - 1.5))
        
        # Add additional chaotic cross-dimensional interactions with higher frequency components
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.8 * np.sin(10 * (x[i] * x[j])) * np.cos(0.4 * (x[i]**2 + x[j]**2))
                
        # Add a new chaotic oscillation component that scales with dimension
        if self.dim > 1:
            oscillation = 0.0
            for i in range(self.dim):
                oscillation += np.sin(9 * x[i]) * np.cos(1.1 * i)
            result += 1.2 * oscillation * np.exp(-0.4 * np.sum(x**2))
            
        # Add a new chaotic term with fractal-like behavior
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += np.sin(2.5 * x[i]) * np.cos(1.3 * x[i]) * np.exp(-0.1 * (x[i] - 2.0)**2)
        result += 0.9 * fractal_term
        
        return result