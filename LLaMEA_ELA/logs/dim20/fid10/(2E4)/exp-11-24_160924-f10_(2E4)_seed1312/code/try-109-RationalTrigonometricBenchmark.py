import numpy as np

class RationalTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Periodic components with varying frequencies and amplitudes
        for i in range(self.dim):
            xi = x[i]
            # Use rational polynomial terms combined with trigonometric functions
            numerator = xi**4 + 2 * xi**2 + 1
            denominator = xi**2 + 1
            result += np.sin(3.0 * xi) * (numerator / denominator)
            
        # Add saddle point inducing terms with rational couplings
        for i in range(self.dim):
            xi = x[i]
            # Rational polynomial with sinusoidal modulation
            ratio_term = (xi**3 + xi) / (xi**2 + 0.5)
            result += 0.5 * np.cos(2.0 * xi) * ratio_term
            
        # Add non-separable coupling using trigonometric ratios
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Coupling strength varies with dimension indices
                coupling = 1.0 + 0.3 * np.cos(0.2 * (i + j))
                # Trigonometric ratio coupling with enhanced chaos
                if abs(x[i] - x[j]) > 1e-8:
                    ratio = np.sin(x[i]) / (np.sin(x[j]) + 0.1)
                    result += coupling * ratio * np.exp(-0.1 * (x[i]**2 + x[j]**2))
                    
        # Add high-order polynomial terms with rational coefficients
        for i in range(self.dim):
            xi = x[i]
            # Rational coefficient based on dimension index with chaotic modulation
            coeff = 1.0 + 0.2 / (1.0 + np.abs(xi)) * np.sin(0.5 * xi)
            result += coeff * (xi**6 - 4 * xi**4 + 4 * xi**2)
            
        # Add gradient complexity through ratio of trigonometric functions
        if self.dim >= 2:
            for i in range(self.dim - 1):
                # Gradient-inducing rational coupling with adaptive scaling
                numerator = np.sin(x[i]) + np.cos(x[i+1])
                denominator = np.cos(x[i]) + np.sin(x[i+1]) + 0.1 + 0.05 * np.sin(0.3 * x[i])
                result += 0.3 * (numerator / denominator)
                
        # Add chaotic penalty near global optimum to increase convergence difficulty
        result += 0.5 * np.sum(np.exp(-0.5 * (x - 2.0)**2)) + 0.3 * np.sum(np.abs(x - 2.0)**3)
        
        # Add multi-modal structure with rational polynomial peaks
        for i in range(self.dim):
            xi = x[i]
            # Peaks at multiple locations using rational polynomial ratios with chaotic modulation
            peak1 = 1.0 / (1.0 + (xi - 1.5)**2) * np.sin(0.7 * xi)
            peak2 = 1.0 / (1.0 + (xi + 1.5)**2) * np.cos(0.7 * xi)
            result += 0.4 * (peak1 + peak2)
            
        # Add enhanced chaotic component for better benchmarking
        chaotic_component = 0.0
        for i in range(self.dim):
            chaotic_component += np.sin(5.0 * x[i]) * np.cos(3.0 * x[i])
        result += 0.2 * chaotic_component
        
        return result