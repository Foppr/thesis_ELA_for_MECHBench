import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Chaotic gradient components with time-varying frequencies
        for i in range(self.dim):
            xi = x[i]
            
            # Base chaotic gradient component
            base = np.sin(xi) * np.cos(xi) + 0.3 * np.sin(2 * xi)
            
            # Time-varying harmonic oscillations (modified frequencies and amplitudes)
            oscillation = 0.0
            for k in range(1, 6):
                freq = 1.5 + 0.5 * np.sin(0.2 * i + k)  # Time-varying frequency
                amp = 0.4 + 0.2 * np.cos(0.3 * i + k)   # Time-varying amplitude
                oscillation += amp * np.sin(freq * xi)
            
            # Adaptive conditioning based on dimension and chaotic modulation
            condition = 1.0 + 0.5 * np.sin(0.4 * i + np.cos(xi)) * np.abs(xi)
            
            # Asymmetric basin with chaotic perturbations
            asymmetry = 0.25 * np.sin(xi**3) * np.cos(0.5 * xi) + 0.1 * np.sin(3 * xi)
            
            result += condition * (base + oscillation) + asymmetry
            
        # Cross-dimensional coupling with chaotic interaction strengths
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic coupling strength (time-varying based on indices)
                coupling_strength = 0.4 * (1 + np.sin(0.3 * i + 0.2 * j))
                diff = x[i] - x[j]
                coupling += coupling_strength * np.exp(-0.1 * diff**2) * np.sin(diff)
                
        # Add chaotic periodicity component
        periodicity = 0.0
        for i in range(self.dim):
            xi = x[i]
            term = 0.0
            for k in range(1, 7):  # Increased to 6 terms
                freq = 2.0 + 0.3 * np.sin(0.1 * i + k)
                term += np.sin(freq * xi) / (k**1.2)
            periodicity += term
            
        # Combine all components with modified weights
        result = 0.7 * result + 0.25 * coupling + 0.2 * periodicity
        
        # Chaotic penalty term with varying exponents
        penalty = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Chaotic penalty with non-uniform exponents
            if xi >= 0:
                exponent = 2.5 + 0.4 * np.sin(0.3 * i)
                penalty += 0.1 * xi**exponent
            else:
                exponent = 3.0 + 0.3 * np.cos(0.2 * i)
                penalty += 0.15 * np.abs(xi)**exponent
                
        result += penalty
        
        # Final scaling factor for good fitness range
        result *= 1.6
        
        return result