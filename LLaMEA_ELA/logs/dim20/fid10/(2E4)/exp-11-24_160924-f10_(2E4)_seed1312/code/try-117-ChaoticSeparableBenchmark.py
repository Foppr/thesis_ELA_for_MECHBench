import numpy as np

class ChaoticSeparableBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Enhanced chaotic sinusoidal components with varying frequencies and amplitudes
        for i in range(self.dim):
            xi = x[i]
            # Use chaotic logistic map modulation for sinusoidal terms with enhanced chaos
            chaotic_factor = 1.0 + 0.5 * np.sin(7.0 * xi) * np.cos(3.0 * xi) * np.tan(1.5 * xi)
            result += chaotic_factor * (np.sin(5.0 * xi) + 0.6 * np.cos(4.0 * xi) + 0.3 * np.sin(2.0 * xi))
            
        # Add adaptive coupling strengths based on dimension index with enhanced non-linearity
        for i in range(self.dim):
            xi = x[i]
            # Adaptive coupling strength with exponential decay and chaotic modulation
            coupling_strength = 1.0 + 0.7 * np.exp(-0.15 * i) * np.sin(0.4 * i)
            result += coupling_strength * (xi**4 - 3 * xi**3 + 2 * xi**2 - xi) * np.cos(3.0 * xi)
            
        # Add non-separable coupling using enhanced chaotic trigonometric ratios
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Enhanced chaotic coupling strength with dynamic modulation
                coupling = 2.0 + 0.8 * np.sin(0.4 * (i + j)) * np.cos(0.3 * (i - j)) * np.tan(0.2 * (i + j))
                # Enhanced chaotic ratio coupling with exponential decay and additional trigonometric terms
                if abs(x[i] - x[j]) > 1e-8:
                    ratio = np.tan(x[i]) / np.tan(x[j]) + 0.3 * np.sin(x[i] * x[j])
                    result += coupling * ratio * np.exp(-0.07 * (x[i]**2 + x[j]**2))
                    
        # Add enhanced high-order polynomial terms with chaotic coefficients
        for i in range(self.dim):
            xi = x[i]
            # Enhanced chaotic coefficient based on dimension index and sinusoidal modulation
            coeff = 1.0 + 0.6 * np.sin(0.7 * i) * np.cos(0.4 * xi) * np.tan(0.3 * xi)
            result += coeff * (xi**8 - 4 * xi**6 + 6 * xi**4 - 4 * xi**2 + 1)
            
        # Add enhanced gradient complexity through chaotic rational functions
        if self.dim >= 2:
            for i in range(self.dim - 1):
                # Enhanced gradient-inducing rational coupling with multiple chaotic terms
                numerator = np.tan(x[i]) + np.sin(x[i+1]) + 0.5 * np.cos(x[i] * x[i+1])
                denominator = np.cos(x[i]) + np.tan(x[i+1]) + 0.3 * np.sin(x[i] + x[i+1]) + 0.2
                result += 0.6 * (numerator / denominator)
                
        # Add enhanced chaotic penalty near global optimum to increase convergence difficulty
        result += 0.8 * np.sum(np.exp(-0.4 * (x - 1.0)**2)) + 0.5 * np.sum(np.abs(x - 1.0)**5)
        
        # Add enhanced multi-modal structure with chaotic polynomial peaks
        for i in range(self.dim):
            xi = x[i]
            # Peaks at multiple locations using enhanced chaotic polynomial ratios
            peak1 = 1.0 / (1.0 + (xi - 2.5)**2 + 0.2 * np.sin(6.0 * xi))
            peak2 = 1.0 / (1.0 + (xi + 2.5)**2 + 0.2 * np.cos(4.0 * xi))
            peak3 = 1.0 / (1.0 + (xi - 1.0)**2 + 0.15 * np.tan(3.0 * xi))
            result += 0.6 * (peak1 + peak2 + peak3)
            
        # Add enhanced chaotic saddle points with rational polynomial modulation
        for i in range(self.dim):
            xi = x[i]
            # Enhanced saddle point inducing term with chaotic modulation
            saddle_term = (xi**5 - 3 * xi**3 + 2 * xi) / (xi**2 + 0.7 + 0.3 * np.sin(5.0 * xi))
            result += 0.4 * saddle_term
            
        return result