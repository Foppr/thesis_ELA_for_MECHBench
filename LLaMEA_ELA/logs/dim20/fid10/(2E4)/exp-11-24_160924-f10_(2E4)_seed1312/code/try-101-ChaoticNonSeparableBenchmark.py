import numpy as np

class ChaoticNonSeparableBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Chaotic sine-cosine components with varying parameters
        for i in range(self.dim):
            xi = x[i]
            # Chaos-inducing term using sine-cosine map
            chaos_factor = np.sin(xi) * np.cos(2.0 * xi) + 0.5 * np.sin(3.0 * xi)
            result += 0.8 * chaos_factor
            
        # Non-separable coupling with adaptive conditioning
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Adaptive coupling strength based on dimension indices and input values
                coupling = 1.0 + 0.3 * np.sin(0.5 * (i + j)) * np.cos(0.3 * (x[i] + x[j]))
                # Polynomial coupling with chaotic modulation
                poly_term = (x[i]**2 + x[j]**2) * (1.0 + 0.1 * np.sin(x[i] * x[j]))
                result += coupling * poly_term
                
        # Multi-modal structure with chaotic peaks
        for i in range(self.dim):
            xi = x[i]
            # Multiple chaotic peak locations
            peak_locations = [np.sin(i), np.cos(i), np.tan(i)]
            peak_sum = 0.0
            for loc in peak_locations:
                if not np.isnan(loc):
                    peak_sum += 1.0 / (1.0 + (xi - loc)**2)
            result += 0.5 * peak_sum
            
        # Adaptive conditioning with polynomial terms
        for i in range(self.dim):
            xi = x[i]
            # Dimension-dependent conditioning factor
            cond_factor = 1.0 + 0.2 * np.sin(0.7 * i) + 0.1 * np.cos(0.4 * i)
            result += cond_factor * (xi**4 - 2 * xi**2 + 0.5 * xi)
            
        # Gradient complexity through chaotic rational functions
        if self.dim >= 2:
            for i in range(self.dim - 1):
                # Chaotic gradient-inducing ratio
                numerator = np.sin(x[i]) + np.cos(x[i+1]) + 0.3 * np.sin(x[i] * x[i+1])
                denominator = np.cos(x[i]) + np.sin(x[i+1]) + 0.2 * np.cos(x[i] * x[i+1]) + 0.1
                result += 0.4 * (numerator / denominator)
                
        # Sharp gradient regions with chaotic penalty terms
        sharp_penalty = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Chaotic penalty that increases near critical points
            penalty = np.exp(-0.5 * (xi - np.sin(i))**2) + 0.3 * np.abs(xi - np.cos(i))
            sharp_penalty += penalty
            
        result += 0.6 * sharp_penalty
        
        # Add high-order polynomial with chaotic coefficients
        for i in range(self.dim):
            xi = x[i]
            # Chaotic coefficient modulation
            coeff_mod = 1.0 + 0.2 * np.sin(0.8 * xi) * np.cos(0.6 * xi)
            result += coeff_mod * (xi**5 - 3 * xi**3 + 2 * xi)
            
        return result