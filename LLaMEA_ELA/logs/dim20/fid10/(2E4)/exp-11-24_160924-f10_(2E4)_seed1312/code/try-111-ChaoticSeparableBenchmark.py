import numpy as np

class ChaoticSeparableBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Chaotic sinusoidal components with varying frequencies and amplitudes
        for i in range(self.dim):
            xi = x[i]
            # Use chaotic logistic map modulation for sinusoidal terms
            chaotic_factor = 1.0 + 0.3 * np.sin(5.0 * xi) * np.cos(2.0 * xi)
            result += chaotic_factor * (np.sin(4.0 * xi) + 0.5 * np.cos(3.0 * xi))
            
        # Add adaptive coupling strengths based on dimension index
        for i in range(self.dim):
            xi = x[i]
            # Adaptive coupling strength with exponential decay
            coupling_strength = 1.0 + 0.5 * np.exp(-0.1 * i)
            result += coupling_strength * (xi**3 - 2 * xi**2 + xi) * np.sin(2.0 * xi)
            
        # Add non-separable coupling using chaotic trigonometric ratios
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic coupling strength with dynamic modulation
                coupling = 1.5 + 0.5 * np.sin(0.3 * (i + j)) * np.cos(0.2 * (i - j))
                # Chaotic ratio coupling with exponential decay - modified interaction
                if abs(x[i] - x[j]) > 1e-8:
                    ratio = np.tan(x[i]) / (np.tan(x[j]) + 0.1)
                    result += coupling * ratio * np.exp(-0.03 * (x[i]**2 + x[j]**2))
                    
        # Add high-order polynomial terms with chaotic coefficients
        for i in range(self.dim):
            xi = x[i]
            # Chaotic coefficient based on dimension index and sinusoidal modulation
            coeff = 1.0 + 0.4 * np.sin(0.5 * i) * np.cos(0.3 * xi)
            result += coeff * (xi**7 - 3 * xi**5 + 3 * xi**3 - xi)
            
        # Add gradient complexity through chaotic rational functions
        if self.dim >= 2:
            for i in range(self.dim - 1):
                # Chaotic gradient-inducing rational coupling - modified denominator
                numerator = np.tan(x[i]) + np.sin(x[i+1])
                denominator = np.cos(x[i]) + np.tan(x[i+1]) + 0.3 * np.sin(0.5 * x[i])
                result += 0.4 * (numerator / denominator)
                
        # Add chaotic penalty near global optimum to increase convergence difficulty
        result += 0.6 * np.sum(np.exp(-0.3 * (x - 1.0)**2)) + 0.4 * np.sum(np.abs(x - 1.0)**4)
        
        # Add multi-modal structure with chaotic polynomial peaks
        for i in range(self.dim):
            xi = x[i]
            # Peaks at multiple locations using chaotic polynomial ratios
            peak1 = 1.0 / (1.0 + (xi - 2.0)**2 + 0.1 * np.sin(5.0 * xi))
            peak2 = 1.0 / (1.0 + (xi + 2.0)**2 + 0.1 * np.cos(3.0 * xi))
            result += 0.5 * (peak1 + peak2)
            
        # Add chaotic saddle points with rational polynomial modulation - enhanced structure
        for i in range(self.dim):
            xi = x[i]
            # Saddle point inducing term with chaotic modulation - modified denominator
            saddle_term = (xi**4 - 2 * xi**2) / (xi**2 + 0.5 + 0.3 * np.sin(4.0 * xi) + 0.1 * xi**2)
            result += 0.3 * saddle_term
            
        return result